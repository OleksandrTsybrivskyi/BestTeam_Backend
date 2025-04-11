from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Location
from .serializers import LocationSerializer


class LocationGetView(APIView):
    def get(self, request):
        locations = Location.objects.filter(has_ramp=True)
        print(locations)
        serialized = LocationSerializer(locations, many=True)
        return Response(serialized.data)

class LocationPostView(APIView):
    def post(self, request):
        print(request.data)
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            location = serializer.save()
            print(location.name)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
