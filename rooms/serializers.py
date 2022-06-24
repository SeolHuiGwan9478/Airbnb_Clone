from dataclasses import field
from email.policy import default
from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room
class ReadRoomSerializer(serializers.ModelSerializer):
    user = RelatedUserSerializer()
    class Meta:
        model = Room
        exclude = (
            "modified",
        )

class WriteRoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    address = serializers.CharField(max_length=140)
    price = serializers.IntegerField()
    beds = serializers.IntegerField(default=1)
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = serializers.IntegerField(default=1)
    bathrooms = serializers.IntegerField(default=1)
    check_in = serializers.TimeField(default="00:00:00")
    check_out = serializers.TimeField(default="00:00:00")
    instant_book = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)
    
    # def validate_beds(self, beds):
    #     if beds < 5:
    #         raise serializers.ValidationError("Your house is too small")
    #     else:
    #         return beds

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", default = instance.name)
        instance.address = validated_data.get("address", default = instance.address)
        instance.price = validated_data.get("price", default = instance.price)
        instance.beds = validated_data.get("beds", default = instance.beds)
        instance.lat = validated_data.get("lat", default = instance.lat)
        instance.lng = validated_data.get("lng", default = instance.lng)
        instance.bedrooms = validated_data.get("bedrooms", default = instance.bedrooms)
        instance.bathrooms = validated_data.get("bathrooms", default = instance.bathrooms)
        instance.check_in = validated_data.get("check_in", default = instance.check_in)
        instance.check_out = validated_data.get("check_out", default = instance.check_out)
        instance.instant_book = validated_data.get("instant_book", default = instance.instant_book)

        instance.save()
        return instance

    def validate(self, data):
        if self.instance:
            check_in = data.get("check_in", default=self.instance.check_in)
            check_out = data.get("check_out", default=self.instance.check_out)
        else:
            check_in = data.get("check_in")
            check_out = data.get("check_out")
        if check_in == check_out:
            raise serializers.ValidationError("Not enough time between changes")
        return data