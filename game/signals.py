from django.db.models.signals import pre_save, post_save
from game.models import Round


def save_round_winner(sender, instance, **kwargs):
    """Before saving round data, check who is the winner of the round depending
    of the selected moves
    """

    current_round = instance
    if current_round.move_player_1 == current_round.move_player_2:
        pass
    elif current_round.move_player_1.strong_against == current_round.move_player_2:
        current_round.winner = current_round.game.player_1
    else:
        current_round.winner = current_round.game.player_2


def save_game_winner(sender, instance, **kwargs):
    """This is called after the round is saved, 
    it determines if the game is over or not
    """
    current_round = instance
    wins_player_1 = Round.objects.filter(game=current_round.game, winner=current_round.game.player_1).count()
    wins_player_2 = Round.objects.filter(game=current_round.game, winner=current_round.game.player_2).count()

    if wins_player_1 >= 3:
        current_round.game.winner = current_round.game.player_1
    elif wins_player_2 >= 3:
        current_round.game.winner = current_round.game.player_2
    else:
        pass

    current_round.game.save()


pre_save.connect(save_round_winner, sender=Round)
post_save.connect(save_game_winner, sender=Round)
