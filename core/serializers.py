from rest_framework import serializers
from .models import User, Location, Review

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'join_date', 'is_accessibility_user']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'location', 'user', 'username', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'username', 'created_at']

    def get_username(self, obj):
        return obj.user.username
