from django.db import models
from rest_framework import serializers
from first_app.models import CarSpecs

class CarSpecSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarSpecs
        fields = ['car_brand', 'car_model', 'production_year', 'car_body',]
