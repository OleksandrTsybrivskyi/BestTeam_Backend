from rest_framework import serializers
from .models import User, Location, Review, Proposal

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
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'location', 'user', 'rating', 'comment', 'created_at']


class ProposalSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    location_name = serializers.SerializerMethodField()

    class Meta:
        model = Proposal
        fields = [
            'id',
            'user',
            'username',
            'location',
            'location_name',
            'comment',
            'ramps',
            'tactile_elements',
            'adapted_toilets',
            'wide_entrance',
            'visual_impairment_friendly',
            'wheelchair_accessible',
            'created_at'
        ]
        read_only_fields = ['user', 'username', 'location_name', 'created_at']

    def get_username(self, obj):
        return obj.user.username

    def get_location_name(self, obj):
        return obj.location.name
