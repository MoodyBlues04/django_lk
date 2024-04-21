from rest_framework import serializers
from base.models import Tariff


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class UpdateTariffSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField(min_value=0)
    duration = serializers.IntegerField(min_value=0)
    adverts_count = serializers.IntegerField(min_value=0)

    def update(self, instance: Tariff, validated_data: dict) -> None:
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.duration = validated_data['duration']
        instance.adverts_count = validated_data['adverts_count']
        instance.save()
