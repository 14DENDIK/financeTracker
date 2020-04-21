from rest_framework import serializers

from .models import ExpanseType, Expanse


class ExpanseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpanseType
        fields = '__all__'


class ExpanseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expanse
        fields = '__all__'
