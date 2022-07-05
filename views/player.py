class PlayerView:
    def showAllView(list):
        print(f"Il y a {len(list)} jours")
        print(
            "|{:<15}|{:<15}|{:<18}|{:<10}|{:<15}|".format(
                "Prènom", "Nom", "Date de naissance", "Genre", "Classement"
            )
        )
        print(
            "----------------------------------------------------------------------------"
        )
        for player in list:
            print(
                "|{:<15}|{:<15}|{:<18}|{:<10}|{:<15}|".format(
                    player["first_name"],
                    player["last_name"],
                    player["date_of_birth"],
                    player["gender"],
                    player["classement"],
                )
            )
            print(
                "----------------------------------------------------------------------------"
            )

    def create_player():
        first_name = input("Entrez le prènom ? ")
        last_name = input("Entrez le nom ? ")
        date_of_birth = input("Entrez la date de naissance ? ")
        gender = input("Entrez genre ?")
        classement = input("Entrez le Classemnt ? ")
        return first_name, last_name, date_of_birth, gender, classement

    def startView():
        print("Binevenu sur l'application Chess tournament")
