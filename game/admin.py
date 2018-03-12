from django.contrib import admin
from .models import (
    Player,
    Move,
    Game,
    Round,
)


class PlayerAdmin(admin.ModelAdmin):
    pass

class GameAdmin(admin.ModelAdmin):
    pass

class MoveAdmin(admin.ModelAdmin):
    pass

class RoundAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Move, MoveAdmin)
admin.site.register(Round, RoundAdmin)
