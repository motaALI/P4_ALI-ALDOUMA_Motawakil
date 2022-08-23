from models.player import Player
from view import Display
from views.player import PlayerView


class Controller_player:
    def __init__(self):
        self.display = Display
        self.plyer_v = PlayerView

    def showAll():
        players = Player.load_player_db()
        return PlayerView.showAllView(players)

    def show_filtered_players():
        filter_key = PlayerView.filter_players_by_classement_or_first_name()
        players_list = Player.show_filtered_players(filter_key)
        return PlayerView.showAllView(players_list)

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

    def updateOnePlayer():
        id = PlayerView.updateOnePlayer()
        return Player.updateOnePlayer(id)

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
            Controller_player.create_player()
        elif response == "2":
            Controller_player.show_filtered_players()
        elif response == "3":
            Controller_player.updateOnePlayer()
        elif response == "R":
            Display.render_menu(menu)
        else:
            print("Error")
