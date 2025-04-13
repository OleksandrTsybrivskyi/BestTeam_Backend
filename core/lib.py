from .models import Location
from .serializers import LocationSerializer


def location_process_get(request):
    '''
    Видати список локацій з бази даних, що відповідають
    заданим фільтрам

    :param parameters: словник, що містить критерії фільтрації,
    а саме:
    ramps
    tactile_elements
    adapted_toilets
    wide_entrance
    visual_impairment_friendly
    wheelchair_accessible
    якщо якогось значення немає в словнику, вважати, що воно
    дорівнює False

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
    parameters = request.GET.dict()


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