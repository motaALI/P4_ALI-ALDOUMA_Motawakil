class PlayerView:
    def showAllView(list):
        print(f"Il y a {len(list)} jours")
        print("{:<18} {:<15} {:<15} {:<10} {:<15}".format(
            "Prènom", "Nom", "Date de naissance", "Genre", "Classement")
        )
        for player in list:
            print("{:<18} {:<15} {:<15} {:<10} {:<15}".format(
                    player['first_name'],
                    player['last_name'],
                    player['date_of_birth'], 
                    player['gender'], 
                    player['classement']
                ))

    def create_player():
        first_name = input("Entrez le prènom ? ")
        last_name = input("Entrez le nom ? ")
        gender = input("Entrez genre ?")
        date_of_birth = input("Entrez la date de nai ? ")
        classement = input("Entrez le Classemnt ? ")
        return first_name, last_name, gender, date_of_birth, classement

    def startView():
        print("Binevenu sur l'application Chess tournament")
