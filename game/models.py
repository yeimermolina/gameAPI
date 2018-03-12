from django.db import models


class Player(models.Model):
    nickname = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nickname


class Game(models.Model):
    player_1 = models.ForeignKey(
        Player,
        related_name='player_1',
        on_delete=models.CASCADE
    )

    player_2 = models.ForeignKey(
        Player,
        related_name='player_2',
        on_delete=models.CASCADE
    )  

    winner = models.ForeignKey(
        Player,
        blank=True, 
        null=True, 
        related_name='winner',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} vs {1}".format(self.player_1.nickname, self.player_2.nickname)


class Move(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    strong_against = models.OneToOneField(
        'self', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='beat'
    )

    weak_against = models.OneToOneField(
        'self', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='beaten_by'
    )

    def __str__(self):
        return self.name
        

class Round(models.Model):
    game = models.ForeignKey(
        Game,
        related_name='rounds',
        on_delete=models.CASCADE
    )    

    winner = models.ForeignKey(
        Player,
        blank=True,
        null=True,
        related_name='round_winner',
        on_delete=models.CASCADE
    )

    move_player_1 = models.ForeignKey(
        Move,
        related_name='movel_player_1',
        on_delete=models.CASCADE
    ) 

    move_player_2 = models.ForeignKey(
        Move,
        related_name='movel_player_2',
        on_delete=models.CASCADE
    ) 

    def __str__(self):
        return str(self.id)                                                                                             
