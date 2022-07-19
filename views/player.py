from prettytable import PrettyTable

class PlayerView:
    def showAllView(list):
        print(f"Il y a {len(list)} jours")
        players_table = PrettyTable()
        players_table.field_names = ["Prènom", "Nom", "Date de naissance", "Genre", "Classement"]
        for player in list:
            players_table.add_row([
                player["first_name"],
                player["last_name"],
                player["date_of_birth"],
                player["gender"],
                player["classement"],
            ])
            players_table.add_row(['------', '------', '------', '------', '------'])
        print(players_table)

    def create_player():
        first_name = input("Entrez le prènom ? ")
        last_name = input("Entrez le nom ? ")
        date_of_birth = input("Entrez la date de naissance ? ")
        gender = input("Entrez genre ?")
        classement = input("Entrez le Classemnt ? ")
        return first_name, last_name, date_of_birth, gender, classement

    def startView():
        print("Binevenu sur l'application Chess tournament")
