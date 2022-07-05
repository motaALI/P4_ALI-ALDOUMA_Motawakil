from models.player import Player
from views.player import PlayerView
from view import Display


class Controller_player:
    def __init__(self):
        self.display = Display
        self.plyer_v = PlayerView

    def showAll():
        players = Player.load_player_db()
        return PlayerView.showAllView(players)

    def create_player():
        (
            first_name,
            last_name,
            gender,
            date_of_birth,
            classement,
        ) = PlayerView.create_player()
        player = Player(first_name, last_name, gender, date_of_birth, classement)
        return player.create_player()

    def endView():
        print("Goodbye!")

    def manage_players():
        menu = {
            "1": "Créer un joueur",
            "2": "Lister les joueurs",
            "3": "Modifier un joueur",
            "R": "Reveneir à l'accueil",
        }

        Display.render_menu(menu)
        response = Display.get_user_input(menu)
        if response == "1":
            print("Créer un joueur")
            Controller_player.create_player()
        elif response == "2":
            print("Liste des joueurs")
            Controller_player.showAll()
        elif response == "3":
            print("Modifier un joueur")
        elif response == "R":
            print("Reveneir à l'accueil")
        else:
            print("Error")
