from rest_framework import serializers
from . models import Perros

class PerrosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perros
        fields = '__all__'