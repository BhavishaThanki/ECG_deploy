from rest_framework import serializers

class MyDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()