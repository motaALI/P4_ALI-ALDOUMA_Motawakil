from controllers.player import Controller_player
from controllers.tournament import Controller_tournament
from view import Display


class Controller:
    def __init__(self):
        self.display = Display()

    def accueil(self):
        menu = {
            "1": "Gestion des joueurs",
            "2": "Gestion des tournois",
            "3": "Gestion des matches",
            "q": "Quitter",
        }

        Display.render_menu(menu)
        response = Display.get_user_input(menu)

        if response == "1":
            Controller_player.manage_players()
            print("Choix 1")
        elif response == "2":
            Controller_tournament.manage_tournaments()
            print("Choix 2")
        elif response == "3":
            # self.matche_controller()
            print("Choix 3")
        else:
            Display.endView()
            print("Quitter")
