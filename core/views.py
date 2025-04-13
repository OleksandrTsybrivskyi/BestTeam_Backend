from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Location, Review, User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import LocationSerializer
from .lib import location_process_post, location_process_get, review_process_get, review_process_post


class LocationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response, status = location_process_get(request)
        return Response(response, status=status)

    # def post(self, request):
    #     response = location_process_post(request)
    #     return Response(response)


class ReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response, status = review_process_get(request)
        return Response(response, status=status)

    def post(self, request):
        response, status = review_process_post(request)
        return Response(response, status=status)


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        email = data['email']
        password = data['password']
        if not username or not email or not password:
            return Response({'error': 'Missing fields'}, status=400)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'User with such username exists'}, status=400)
        if User.objects.filter(email=email).exists():
            return Response({'error': 'User with such email exists'}, status=400)
        user = User.objects.create(username=username, email=email, password=password)
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=201)
