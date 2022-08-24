from colorama import Fore
from prettytable import PrettyTable

from validation import Validators


class PlayerView:
    def sort_players_by_classement_or_first_name():
        sort_key = ""
        sort_with = int(
            input(
                " 1 : Pour trier par l'ordre alphabétique\n 2 : pour trier par classement\n "
            )
        )
        if sort_with == 1:
            sort_key = "first_name"
        elif sort_with == 2:
            sort_key = "classement"
        return sort_key

    def showAllView(list, sort_key):
        """
        Customizing sort key to display french equivalent in the message
        """
        custom_key = "Prénom" if sort_key == "first_name" else sort_key
        print(
            f"\n{Fore.LIGHTBLUE_EX} Il y a {len(list)} joueurs triés par {custom_key}\n"
        )

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
                    f"{Fore.LIGHTBLUE_EX}------",
                    f"{Fore.LIGHTBLUE_EX}------",
                    f"{Fore.LIGHTBLUE_EX}------",
                    f"{Fore.LIGHTBLUE_EX}------",
                    f"{Fore.LIGHTBLUE_EX}------",
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

    def updateOnePlayer():
        player_id = input("Entrez l'id de joueur à modifier : ")
        return player_id

    def player_new_data():
        classement = int(input("Entrez le Classemnt ? "))
        while Validators.is_valide_classement(classement) is False:
            classement = int(input(f"{Fore.CYAN} Entrez le Classemnt ? "))
        return classement
