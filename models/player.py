from tinydb import TinyDB
from datetime import datetime

player_db = TinyDB("players.json")
from colorama import Fore


"""


●	Nom de famille
●	Prénom
●	Date de naissance
●	Sexe
●	Classement
○	Il s'agit d'un chiffre positif.

"""
"""
TODO => VALIDATION 
SEND APP CODE TO GIT P1
"""


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

        self.player_db = TinyDB("players.json")

    def player_serializer(self):
        """Return serialized player info"""
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "classement": self.classement,
        }

    # String méthode pour renvoyer le nom + prènom de joueur
    def full_name(self):
        print(f"{Fore.RED}  {self.last_name}")

    def __str__(self):
        return f"Nom : {self.first_name} Prènom : {self.last_name}"

    def plyer_full_infos(self):
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
        player_db = TinyDB("players.json")
        player_db.all()
        players = []
        for item in player_db:
            players.append(item)

        return players
