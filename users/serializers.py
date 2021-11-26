from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'email', 'username', 'first_name',
                  'last_name', 'id_num', 'password', 'profile_picture')

    def create(self, validated_data):
        user = super(ProfileSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
