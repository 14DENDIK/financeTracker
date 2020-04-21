from rest_framework import serializers

from .models import IncomeType, Income


class IncomeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeType
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = '__all__'
