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

    return response, 200


def location_process_post(request): # не використовується
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
    Отримати відгуки на локацію з певним id

    :param parameters: словник, містить параметри, що вказані
    в url адресі. В ключі 'location_id' зберігається id
    локації, для якої потрібно отримати відгуки
    :return: повернути список відгуків на локацію у
    форматі словника
    формат:
    {
        id:int,
        location:int, #тут просто айді локації 
        user:int, # тут айді юзера
        rating:int,
        comment:str,
        created_at:str
    }
    '''
    parameters = request.GET.dict()
    location_id = parameters.get('location_id')

    try:
        location_id = int(location_id)
    except (TypeError, ValueError):
        return {"message": "Неправильний айді локації"}, 400
    if not location_id:
        return [], 200
    try:
        location = Location.objects.get(id=location_id)
    except Location.DoesNotExist:
        return {'message': 'Помилка: локацію не знайдено'}, 404
    reviews = Review.objects.filter(location=location)

    serializer = ReviewSerializer(reviews, many=True)
    return serializer.data, 200


def review_process_post(request):
    '''
    Надіслати відгук на локацію

    :param data: словник із JSON запитом, формат:
    {
        'location_id':int,
        'rating':int,
        'comment':str
    }
    :param user: об`єкт класу User. За допомогою нього
    отримується імя користувача
    :return: якщо все добре, повертається повідомлення
    {
        message:'ok'
    }
    status = 201

    інакше повернути 
    {
        message:'опис помилки'
    }
    status = код помилки
    '''
    data = request.data
    user = request.user

    try:
        location = Location.objects.get(id=data['location_id'])
    except Location.DoesNotExist:
        return {'message':'Помилка: локацію не знайдено'}, 404

    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user, location=location)
        return {'message': 'ok'}, 201
    return {'message': 'Помилка: дані не дійсні'}, 400
