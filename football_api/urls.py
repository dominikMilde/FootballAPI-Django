from django.urls import path
from football_api.views import PlayerCreate, CountryCreate, CountryList, CountryDetail, PlayerDetail, PlayerList, PlayersOfCountry

urlpatterns = [

    path("country/", CountryCreate.as_view()),
    path("country/list/", CountryList.as_view()),
    path("country/<int:pk>/", CountryDetail.as_view()),


    path("player/", PlayerCreate.as_view(), name="player"),
    path("player/list/", PlayerList.as_view()),
    path("player/<int:pk>/", PlayerDetail.as_view()),

    path("country/<int:pk>/player/", PlayersOfCountry.as_view())
]
