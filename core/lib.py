from .models import Location
from .serializers import LocationSerializer


def location_process_post(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        location = serializer.save()
        return serializer.data


def location_process_get(request):
    locations = Location.objects.filter(has_ramp=True)
    serialized = LocationSerializer(locations, many=True)
    return serialized.data
