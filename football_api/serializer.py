from rest_framework import serializers
from football_api.models import Country, Player


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class PlayerSerializerWithCountry(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
        depth = 1





"""
from rest_framework import serializers

from football_api.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    number_of_pages = serializers.IntegerField()
    published_date = serializers.DateField()
    quantity = serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
        instance.published_date = data.get('pubblished_date', instance.published_date)
        instance.quantity = data.get('quantity', instance.quantity)

        instance.save()
        return instance

class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "Diet Coke":
            raise ValidationError("no pls")
        return value

    def validate(self, data):
        if data["number_of_pages"] > 400 or data["quantity"] > 200:
            raise ValidationError("Too heavy")
        return data

    def get_description(self, data):
        return "This is called " + str(data.title) + " and it is long"
"""
