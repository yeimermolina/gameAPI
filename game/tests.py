from django.test import TestCase, Client
from django.urls import  reverse
from game.models import Player, Game, Round, Move
import logging
class GameTestCase(TestCase):
    def setUp(self):
        paper = Move.objects.create(name='Paper')
        rock = Move.objects.create(name='Rock')
        scissors = Move.objects.create(name='Scissors')
        self.set_strong_weakness_moves(paper, rock, scissors)
        self.set_strong_weakness_moves(rock, scissors, paper)
        self.set_strong_weakness_moves(scissors, paper, rock)

        player_1 = Player.objects.create(nickname="player1")
        player_2 = Player.objects.create(nickname="player2")
        game = Game.objects.create(player_1=player_1, player_2=player_2)

        first_round = Round.objects.create(game=game, move_player_1=paper, move_player_2=rock)
        second_round = Round.objects.create(game=game, move_player_1=paper, move_player_2=rock)
        third_round = Round.objects.create(game=game, move_player_1=paper, move_player_2=rock)
    
    def set_strong_weakness_moves(self, instance, strong_against, weak_against):
        instance.strong_against = strong_against
        instance.weak_against = weak_against
        return instance.save()

    def test_move_strong_against(self):
        paper = Move.objects.get(name="Paper")
        rock = Move.objects.get(name="Rock")
        scissors = Move.objects.get(name="Scissors")
        self.assertEqual(paper.strong_against, rock)
        self.assertEqual(rock.strong_against, scissors)
        self.assertEqual(scissors.strong_against, paper)
    
    def test_move_weak_against(self):
        paper = Move.objects.get(name="Paper")
        rock = Move.objects.get(name="Rock")
        scissors = Move.objects.get(name="Scissors")
        self.assertEqual(paper.weak_against, scissors)
        self.assertEqual(rock.weak_against, paper)
        self.assertEqual(scissors.weak_against, rock)
    
    def test_game_winner(self):
        player1 = Player.objects.get(nickname="player1")
        game = Game.objects.get(id=1)
        self.assertEqual(game.winner.nickname, player1.nickname)

    def test_number_of_rounds_won_by_player(self):
        player1 = Player.objects.get(nickname="player1")  
        player2= Player.objects.get(nickname="player2")  
        game = Game.objects.get(id=1)
        wons_round_player_1 = Round.objects.filter(game=game, winner=player1).count()
        wons_round_player_2 = Round.objects.filter(game=game, winner=player2).count()
        self.assertEqual(wons_round_player_1, 3)
        self.assertEqual(wons_round_player_2, 0)

    def test_view_get_moves(self):
        paper = Move.objects.get(name="Paper")
        rock = Move.objects.get(name="Rock")
        scissors = Move.objects.get(name="Scissors")
        
        request = Client()
        move_url = reverse('games:move-list')
        response = request.get(move_url)
        
        # logger = logging.getLogger('django')
        # logger.info(response.data)
        self.assertEqual(paper.name, response.data[0]['name'])
        self.assertEqual(rock.name, response.data[1]['name'])
        self.assertEqual(scissors.name, response.data[2]['name'])
    
    def test_view_get_players(self):
        player1 = Player.objects.get(nickname="player1")  
        player2= Player.objects.get(nickname="player2")
        wins_player_1 = Game.objects.filter(winner=player1).count() 
        wins_player_2 = Game.objects.filter(winner=player2).count() 
        request = Client()
        player_url = reverse('games:player-list')
        response = request.get(player_url)

        self.assertEqual(wins_player_1, response.data['results'][0]['won_games'])
        self.assertEqual(player1.nickname, response.data['results'][0]['nickname'])
        self.assertEqual(wins_player_2, response.data['results'][1]['won_games'])
        self.assertEqual(player2.nickname, response.data['results'][1]['nickname'])
        
