from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import status, request, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from football_api.models import Country, Player
from football_api.serializer import  CountrySerializer, PlayerSerializer, PlayerSerializerWithCountry


### COUNTRY ###

class CountryList(APIView):
    def get(self, request):
        countries = Country.objects.all()  # Complex Data
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class CountryCreate(APIView):
    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryDetail(APIView):
    def get_country_by_pk(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Country doesnt exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        country = self.get_country_by_pk(pk)
        if type(country) == Country:
            serializer = CountrySerializer(country)
            return Response(serializer.data)
        return country # will be Response if doestn't exist

    def put(self, request, pk):
        country = self.get_country_by_pk(pk)
        if type(country) != Country:
            return country
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        country = self.get_country_by_pk(pk)
        if type(country) != Country:
            return country
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### PLAYER ###


class PlayerList(APIView):
    def get(self, request):
        players = Player.objects.all()  # Complex Data
        serializer = PlayerSerializerWithCountry(players, many=True)
        return Response(serializer.data)


class PlayerCreate(APIView):
    def post(self, request):
        player_data = request.data
        serializer = PlayerSerializer(data=player_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayerDetail(APIView):
    def get_player_by_pk(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Player doesnt exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        player = self.get_player_by_pk(pk)
        if type(player) == Player:
            serializer = PlayerSerializerWithCountry(player)
            return Response(serializer.data)
        return player

    def put(self, request, pk):
        player = self.get_player_by_pk(pk)
        if type(player) != Player:
            return player
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        player = self.get_player_by_pk(pk)
        if type(player) != Player:
            return player
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlayersOfCountry(APIView):
    def get(self, request, pk):
        players = Player.objects.filter(country=pk)  # Complex Data
        serializer = PlayerSerializerWithCountry(players, many=True)
        return Response(serializer.data)


class Documentation(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get(self, request):
        return render(request, 'docs.html')

"""

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()  # Complex Data
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Book doesnt exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
"""
from django.shortcuts import render
from football_api.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from football_api.serializer import BookSerializer
from rest_framework import status

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()  # Complex Data
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
      serializer = BookSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except:
        return Response({
            'error': 'Book doesnt exist'
        }, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""