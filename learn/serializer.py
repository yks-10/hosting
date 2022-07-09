from .models import *
from rest_framework import serializers

class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = "__all__"