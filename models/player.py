from datetime import datetime
from colorama import Fore
from tinydb import TinyDB

player_db = TinyDB("DB/players.json")


def valid_d_of_b(date):
    try:
        datetime.strftime(date, "%d/%m/%Y")
    except Exception:
        return False
    return True


class Player:
    def __init__(self, first_name, last_name, date_of_birth, gender, classement):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.classement = classement
        self.score_tournament = 0
        self.player_db = TinyDB("DB/players.json")

    def player_serializer(self):
        """Return serialized player info"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "classement": self.classement,
        }

    # String méthode pour renvoyer le nom + prènom de joueur
    def full_name(self):
        print(f"{self.last_name}")

    def __str__(self):
        return f"Nom : {self.first_name} Prènom : {self.last_name}"

    def player_full_infos(self):
        return f"last_name:{self.last_name} \
                first_name:{self.first_name} \
                date_of_birth:{self.date_of_birth}\
                gender:{self.gender} \
                classement:{self.classement}"

    @classmethod
    def getAll():
        # result = []
        result = player_db.all()
        return result

    def create_player(self):
        return player_db.insert(self.player_serializer())

    @staticmethod
    def load_player_db():
        """Load player database
        @return: list of players
        """
        player_db = TinyDB("DB/players.json")
        player_db.all()
        players = []
        for item in player_db:
            players.append(item)

        return players

    def updateOnePlayer(self):
        id = int(self.get("id"))
        player = player_db.get(doc_id=id)
        if player is None:
            print(f"Il n'a y aucun joueur avec l'id {id}")
        else:
            print(f"Player à Modifier : {player}")
            classement = int(self.get("classement"))
            updated_player = player_db.update({"classement": classement}, doc_ids=[id])
            print(f"updated_player : {updated_player}")

    def showPlayerName(id):
        player = player_db.get(doc_id=id)
        return player.get("last_name")

    def show_sorted_players(self):
        sort_keys = ["classement", "first_name"]
        if self in sort_keys:
            is_reverse = True if self == "classement" else False
            res = player_db.all()
            players_list = sorted(res, key=lambda p: p[self], reverse=is_reverse)
            return players_list
        else:
            players_list = []
            print(
                f"{Fore.RED} Tri possible uniquement par classement ou l'ordre alphabétique"
            )
