from .models import Location, Review
from .serializers import LocationSerializer, ReviewSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


def location_process_get(request):
    '''
    Видати список всіх локацій з бази даних

    :return: список локацій у вигляді словників.
    формат словника є таким:
    {
        id: number;
        name: string;
        position: [number, number];
        accessibility: {
            ramps: boolean;
            tactileElements: boolean;
            adaptedToilets: boolean;
            wideEntrance: boolean;
            visualImpairmentFriendly: boolean;
            wheelchairAccessible: boolean;
        };
    };
    '''
    locations = Location.objects.all()

    response = []
    for loc in locations:
        response.append({
            'id': loc.id,
            'name': loc.name,
            'position': [loc.latitude, loc.longitude],
            'accessibility': {
                'ramps': loc.ramps,
                'tactileElements': loc.tactile_elements,
                'adaptedToilets': loc.adapted_toilets,
                'wideEntrance': loc.wide_entrance,
                'visualImpairmentFriendly': loc.visual_impairment_friendly,
                'wheelchairAccessible': loc.wheelchair_accessible,
            }
        })

    return response


def location_process_post(request):
    '''
    Змінити параметри доступності певної локації

    :param data: словник з даними про локацію
    Формат словника
    {
        id: number;
        name: string;
        position: [number, number];
        accessibility: {
            ramps: boolean;
            tactileElements: boolean;
            adaptedToilets: boolean;
            wideEntrance: boolean;
            visualImpairmentFriendly: boolean;
            wheelchairAccessible: boolean;
        };
    };
    :param user: обєкт класу User, якщо is_accessibility_user == False
    він не може змінити параметри доступності локації

    :return: словник з локацією
    якщо виникла помилка, повернути повідомлення про помилку
    '''

    data = request.data
    user = request.user


    if not user.is_accessibility_user:
        return "Відмовлено в доступі: користувач не залогінився"

    try:
        location = Location.objects.get(id=data['id'])
    except Location.DoesNotExist:
        return "Помилка: локацію не знайдено"


    accessibility = data.get('accessibility', {})
    location.ramps = accessibility.get('ramps', location.ramps)
    location.tactile_elements = accessibility.get('tactileElements', location.tactile_elements)
    location.adapted_toilets = accessibility.get('adaptedToilets', location.adapted_toilets)
    location.wide_entrance = accessibility.get('wideEntrance', location.wide_entrance)
    location.visual_impairment_friendly = accessibility.get('visualImpairmentFriendly',
                                                            location.visual_impairment_friendly)
    location.wheelchair_accessible = accessibility.get('wheelchairAccessible', location.wheelchair_accessible)
    location.save()

    response = {
        'id': location.id,
        'name': location.name,
        'position': [location.latitude, location.longitude],
        'accessibility': {
            'ramps': location.ramps,
            'tactileElements': location.tactile_elements,
            'adaptedToilets': location.adapted_toilets,
            'wideEntrance': location.wide_entrance,
            'visualImpairmentFriendly': location.visual_impairment_friendly,
            'wheelchairAccessible': location.wheelchair_accessible,
        }
    }

    return response


def review_process_get(request):
    '''
    Ти отримуєш parameters - це словник
    якщо в ньому є ключ 'location_name'
    то витягуєш з бази всі відгуки, що належать цій локації з іменем 'location_name'
    потрібно повернути список цих відгуків
    У вигляді словників (типу словник в такому форматі, як ти його витягуєш з бази даних, тобто дата надсилання локація юзер і т д)
    Якщо ключа location_name немає в словнику, то поверни пустий список
    '''

    parameters = request.GET.dict()
    location_name = parameters.get('location_name')

    if not location_name:
        return []

    reviews = Review.objects.filter(location__name=location_name)

    serializer = ReviewSerializer(reviews, many=True)
    return serializer.data


def review_process_post(request):
    '''
    data - це словник
    потрібно дістати з нього всі потрібні дані щоб створити
    новий відгук, на основі того, що є в базі даних
    '''
    data = request.data
    user = request.user

    try:
        location = Location.objects.get(id=data['location'])
    except Location.DoesNotExist:
        return "Помилка: локацію не знайдено"

    review = Review.objects.create(
        location=location,
        user=user,
        rating=data.get('rating', 0),
        comment=data.get('comment', '')
    )

    serializer = ReviewSerializer(review)
    return serializer.data

