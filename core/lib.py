from .models import Location, Review, Proposal
from .serializers import LocationSerializer, ReviewSerializer, ProposalSerializer
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
        description: string;
        image_url: string;
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
            'description': loc.description,
            'image_url': loc.image_url,
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
        username:str, #тут нік юзера
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

    data = request.data.copy()
    data.pop('location_id', None)

    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user, location=location)
        return {'message': 'ok'}, 201
    else:
        return {'message': 'Помилка: дані не дійсні', 'errors': serializer.errors}, 400



def proposal_process_get(request):
    '''
    отримати список пропозицій зі зміни рівнів доступності
    локацій, якщо користувач є is_accessibility_user 

    :param user: обєкт класу користувача
    :return: повертає список словників пропозицій
    у такому форматі:
    {
        location_id:int,
        location_name:str,
        user:int, #тут айді юзера
        username:str, #тут нік користувача
        comment:str,
        ramps: boolean;
        tactileElements: boolean;
        adaptedToilets: boolean;
        wideEntrance: boolean;
        visualImpairmentFriendly: boolean;
        wheelchairAccessible: boolean;
    }
    Якщо is_accessibility_user == False то повертає
    повідомлення про заборону доступу
    {
        message:'Помилка: недостатньо прав'
    }
    status = 403
    '''
    user = request.user

    if not user.is_accessibility_user:
        return {'message': 'Помилка: недостатньо прав'}, 403

    proposals = Proposal.objects.all().order_by('-created_at')
    serializer = ProposalSerializer(proposals, many=True)
    return serializer.data, 200


def proposal_process_post(request):
    '''
    Подати пропозицію на розгляд, якщо is_accessibility_user == True
    тоді змінити параметри доступності без додавання до списку
    пропозицій

    :param data: пропозиція у вигляді словника
    формат
    {
        location_id:int,
        comment:str,
        ramps: boolean;
        tactile_elements: boolean;
        adapted_toilets: boolean;
        wide_entrance: boolean;
        visual_impairment_friendly: boolean;
        wheelchair_accessible: boolean;
    }
    :param user: обєкт класу User
    :return: додати пропозицію до бази даних
    якщо немає помилок то повернути
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


    location_id = data.get('location_id')
    if not location_id:
        return {'message': 'Не вказано локацію'}, 400

    try:
        location = Location.objects.get(id=location_id)
        data['location'] = location.id
    except Location.DoesNotExist:
        return {'message': 'Локацію не знайдено'}, 404
    
    if user.is_accessibility_user:
        location.ramps = data.get('ramps', location.ramps)
        location.tactile_elements = data.get('tactile_elements', location.tactile_elements)
        location.adapted_toilets = data.get('adapted_toilets', location.adapted_toilets)
        location.wide_entrance = data.get('wide_entrance', location.wide_entrance)
        location.visual_impairment_friendly = data.get('visual_impairment_friendly', location.visual_impairment_friendly)
        location.wheelchair_accessible = data.get('wheelchair_accessible', location.wheelchair_accessible)
        location.save()

        return {'message': 'ok'}, 200

    serializer = ProposalSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user)
        return {'message': 'ok'}, 201
    else:
        return {'message': 'Невірні дані', 'errors': serializer.errors}, 400
    