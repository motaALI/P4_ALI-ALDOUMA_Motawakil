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
            "3": "Rapports",
            "q": "Quitter",
        }

        Display.render_menu(menu)
        response = Display.get_user_input(menu)

        if response == "1":
            Controller_player.manage_players()
        elif response == "2":
            Controller_tournament.manage_tournaments()
        elif response == "3":
            # self.matche_controller()
            print("Choix 3")
        elif response in ["q", "Q"]:
            Display.endView()
            return False
        else:
            Display.ShowError()
