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

    def show_sorted_players():
        sort_key = PlayerView.sort_players_by_classement_or_first_name()
        players_list = Player.show_sorted_players(sort_key)
        if players_list:
            return PlayerView.showAllView(players_list, sort_key)

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
        player_new_data_update = {}
        id = PlayerView.updateOnePlayer()
        classement = PlayerView.player_new_data()
        player_new_data_update.update({"id": id, "classement": classement})
        return Player.updateOnePlayer(player_new_data_update)

    # def endView():
    #     print("Goodbye!")

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
            Controller_player.show_sorted_players()
        elif response == "3":
            Controller_player.updateOnePlayer()
        elif response == "R":
            Display.render_menu(menu)
        else:
            print("-")
