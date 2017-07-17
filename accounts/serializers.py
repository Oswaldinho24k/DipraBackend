from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer(many=False, read_only=True)
	class Meta:
		model = User
		fields = "__all__"

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user

