from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'id_num', 'profile_picture')
