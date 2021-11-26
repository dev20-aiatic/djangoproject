from rest_framework import serializers
from .models import Board, Ideas


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class IdeasSerializer(serializers.ModelSerializer):

    # Se hace uso de PrimaryKeyRelatedField junto al metodo perform_create para hacer el campo usuario
    # sólo leible con el fin de prevenir que sea requerido al momento de crear la idea.
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Ideas
        fields = '__all__'


