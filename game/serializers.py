from rest_framework import serializers
from game.models import (
    Player,
    Move,
    Game,
    Round,
)


class PlayerSerializer(serializers.ModelSerializer):
    won_games = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ('id', 'nickname', 'won_games',)

    def get_won_games(self, obj):
        return Game.objects.filter(winner=obj).count()


class RoundSerializer(serializers.ModelSerializer):
    game_status = serializers.SerializerMethodField()
    round_winner = serializers.SerializerMethodField()

    class Meta:
        model = Round
        fields = (
            'game', 'move_player_1', 'move_player_2',
            'game_status', 'round_winner',
        )
    
    def get_game_status(self, obj):
        status = {'game_over': False, 'winner': 'Noone'}

        if obj.game.winner:
            status['game_over'] = True
            status['winner'] = obj.game.winner.nickname
        return status
    
    def get_round_winner(self, obj):
        return obj.winner.nickname if obj.winner else 'It is a tie'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'player_1', 'player_2',)
        read_only_fields = ('id',)
    

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ('id', 'name', )