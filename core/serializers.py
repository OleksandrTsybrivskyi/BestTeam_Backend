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
    user = UserSerializer(read_only=True)

    class Meta:
        model = Proposal
        fields = ['id', 'location', 'user', 'comment', 'created_at', \
                  'ramps', 'tactile_elements', 'adapted_toilets', 'wide_entrance', \
                    'visual_impairment_friendly', 'wheelchair_accessible']
