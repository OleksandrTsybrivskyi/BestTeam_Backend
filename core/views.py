from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Location
from .serializers import LocationSerializer


class LocationView(APIView):
    def get(self, request):
        locations = Location.objects.filter(has_ramp=True)
        serialized = LocationSerializer(locations, many=True)
        return Response(serialized.data)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            location = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
