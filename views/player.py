from controllers.player import Player
# from controllers.player import Controller_player
# from colorama import Fore, Back, Style
from colorama import Fore, Back, Style


class PlayerView:

    def showAllView(list):
        print(f"Il y a {len(list)} jours")
        for player in list:
            print(f"Prènom : {player['first_name']} Nom: {player['last_name']}  Genre :{player['gender']} Date de naissance :{player['date_of_birth']} classement :{player['classement']}")
        # Player.getAll()


    def create_player():
        first_name = input("Entrez le prènom ? ")
        last_name = input("Entrez le nom ? ")
        gender = input("Entrez genre ?")
        date_of_birth = input("Entrez la date de nai ? ")
        classement = input("Entrez le Classemnt ? ")
        # print(Player.create_player(first_name, last_name,gender, date_of_birth, classement ))
        return first_name, last_name,gender, date_of_birth, classement


    def startView():
        print("Binevenu sur l'application Chess tournament")
        # print(Fore.GREEN +'Do you want to see everyone in my db?[y/n]')

