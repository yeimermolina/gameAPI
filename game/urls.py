from django.urls import path
from game.views import GameList, RoundList, MoveList, PlayerList

app_name = 'game'

urlpatterns = [
    path('', GameList.as_view(), name='game-list' ),
    path('rounds', RoundList.as_view(), name='round-list' ),
    path('moves/', MoveList.as_view(), name='move-list' ),
    path('players/', PlayerList.as_view(), name='player-list' ),
]
