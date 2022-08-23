from colorama import Fore
from prettytable import PrettyTable

from validation import Validators


class PlayerView:
    def showAllView(list):
        print()
        print(f"Il y a {len(list)} jours")
        print()
        players_table = PrettyTable()
        players_table.field_names = [
            "Prènom",
            "Nom",
            "Date de naissance",
            "Genre",
            "Classement",
        ]
        for player in list:
            players_table.add_row(
                [
                    player["first_name"],
                    player["last_name"],
                    player["date_of_birth"],
                    player["gender"],
                    player["classement"],
                ]
            )
            players_table.add_row(
                [
                    f"{Fore.CYAN}------",
                    f"{Fore.CYAN}------",
                    f"{Fore.CYAN}------",
                    f"{Fore.CYAN}------",
                    f"{Fore.CYAN}------",
                ]
            )
        print(players_table)

    def create_player():
        first_name = input(f"{Fore.CYAN} Entrez le prènom : ")
        while Validators.is_valide_input_string(first_name) is False:
            first_name = input(f"{Fore.CYAN} Entrez le prènom : ")
        last_name = input("Entrez le nom ? ")
        while Validators.is_valide_input_string(last_name) is False:
            last_name = input("Entrez le nom ? ")
        date_of_birth = input(f"{Fore.CYAN}Entrez la date de naissance : ")
        while Validators.is_dob_valide(date_of_birth) is False:
            date_of_birth = input("Entrez la date de naissance ? ")
        gender = input(
            f"{Fore.CYAN} Entrez genre choiser dans cette liste 'M' Masculain, 'F' Femme, 'O' Autre ?"
        )
        while Validators.is_valide_input_gender(gender) is False:
            gender = input("Entrez genre ?")
        classement = int(input("Entrez le Classemnt ? "))
        while Validators.is_valide_classement(classement) is False:
            classement = int(input(f"{Fore.CYAN} Entrez le Classemnt ? "))
        return first_name, last_name, date_of_birth, gender, classement

    def startView():
        print("Binevenu sur l'application Chess tournament")
