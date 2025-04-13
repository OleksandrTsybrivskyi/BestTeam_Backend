from .models import Location
from .serializers import LocationSerializer


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
    локацій

    :param parameters: список параметрів в URL адресі.
    Для даної функції не використовується
    :param user: обєкт класу користувача
    :return: повертає список словників пропозицій
    у такому форматі, як в базі даних.
    Якщо is_accessibility_user == False то повертає
    повідомлення про заборону доступу
    '''
    # parameters = request.GET.dict()
    user = request.user


def proposal_process_post(request):
    '''
    Подати пропозицію на розгляд

    :param data: пропозиція у вигляді словника
    формат
    {
        comment:str,
        ramps:bool,
        tactile_elements:bool,
        adapted_toilets:bool,
        wide_entrance:bool,
        visual_impairment_friendly:bool,
        wheelchair_accessible:bool
    }
    :param user: обєкт класу User
    :param parameters: словник параметрів в url адресі
    містить ключ 'location_id'
    :return: додати пропозицію до бази даних
    якщо немає помилок то повернути пропозицію
    у формі словника, інакше повернути повідомлення про помилку
    '''
    data = request.data
    user = request.user
    parameters = request.GET.dict()
    