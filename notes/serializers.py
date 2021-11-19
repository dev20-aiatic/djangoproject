from rest_framework import serializers
from .models import Board, Ideas


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'user', 'status')


class IdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ('id', 'title', 'content', 'user', 'board')


class IdeaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ('id', 'title', 'user', 'board')
