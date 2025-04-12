from .models import Location
from .serializers import LocationSerializer, ReviewSerializer
from .models import User, Review


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

    location_name = parameters.get('location_name')

    if not location_name:
        return []

    try:
        location = Location.objects.get(name=location_name)
    except Location.DoesNotExist:
        return []

    reviews = Review.objects.filter(location=location)
    serialized_reviews = ReviewSerializer(reviews, many=True)

    return serialized_reviews.data


def review_process_post(request):
    '''
    data - це словник
    потрібно дістати з нього всі потрібні дані щоб створити
    новий відгук, на основі того, що є в базі даних
    '''

    data = request.data

    location_id = data.get('location')
    user_id = data.get('user')
    rating = data.get('rating')
    comment = data.get('comment', '')

    if not all([location_id, user_id, rating]):
        return {"Помилка": "Нема даних полів."}

    try:
        location = Location.objects.get(id=location_id)
        user = User.objects.get(id=user_id)
    except (Location.DoesNotExist, User.DoesNotExist):
        return {"Помилка": "Нечітка локація юзера або ID."}

    review = Review.objects.create(
        location=location,
        user=user,
        rating=rating,
        comment=comment
    )

    return ReviewSerializer(review).data
