from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from game.serializers import (
    GameSerializer, 
    RoundSerializer, 
    MoveSerializer, 
    PlayerSerializer
)
from game.models import Game, Round, Player, Move
from game.utils import StandardResultsSetPagination


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def post(self, request, *args, **kwargs):
        """
            If player name exists, return data, otherwise create new player,
            and create new game
        """

        player_1, created = Player.objects.get_or_create(nickname=request.data.get('player_1'))
        player_2, created = Player.objects.get_or_create(nickname=request.data.get('player_2'))
        game = Game.objects.create(player_1=player_1, player_2=player_2)
        serializer = GameSerializer(game)
        return Response(serializer.data)


class RoundList(generics.ListCreateAPIView):
    """
        get request: List all records
        post request: Create new round
    """
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class MoveList(generics.ListAPIView):
    """
        get request: List all moves
    """
    queryset = Move.objects.all()
    serializer_class = MoveSerializer


class PlayerList(generics.ListAPIView):
    """
        get request: List all records
        post request: Create new player
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = StandardResultsSetPagination