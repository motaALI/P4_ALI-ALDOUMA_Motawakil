from view import Display
from controllers.player import Controller_player

class Controller:
    def __init__(self):
        self.display = Display()

    def accueil(self):
        menu = {
            '1': 'Gestion des joueurs',
            '2': 'Gestion des tournois',
            '3': 'Gestion des matches',
            'q': 'Quitter',
        }

        Display.render_menu(menu)
        response = Display.get_user_input(menu)

        if response == '1':
            Controller_player.manage_players()
            print("Choix 1")
        elif response == '2':
            # self.tournament_controller()
            print("Choix 2")
        elif response == '3':
            # self.matche_controller()
            print("Choix 3")
        else:
            # self.display.good_bay()
            print("Quitter")

    # def player_controller():
    #     menu = {
    #     '1': 'Créer un joueur',
    #     '2': 'Modifier un joueur',
    #     'R': 'Reveneir à l\'accueil',
    # }