from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Location
from .serializers import LocationSerializer
from .lib import location_process_post, location_process_get


class LocationView(APIView):
    def get(self, request):
        response = location_process_get(request)
        return Response(response)

    def post(self, request):
        response = location_process_post(request)
        return Response(response)
