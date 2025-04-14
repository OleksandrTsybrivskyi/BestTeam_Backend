from .models import Location, Proposal
from .serializers import LocationSerializer, ProposalSerializer


def location_process_post(request):
    parameters = request.GET.dict()


def location_process_get(request):
    data = request.data


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


def review_process_post(request):
    '''
    data - це словник
    потрібно дістати з нього всі потрібні дані щоб створити
    новий відгук, на основі того, що є в базі даних
    '''
    data = request.data


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
    