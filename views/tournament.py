class TournamentView:

    def showAllView(list):
        print(f"Il y a {len(list)} tournois")
        print("|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}|{:<20}|".format(
            "Nom", "location", "Commance le :", "Fin", "Joueurs", "description")
        )
        print("------------------------------------------------------------------------------------------")
        for tournament in list:
            print("|{:<15}|{:<15}|{:<15}|{:<15}|{:<15}|{:<20}|".format(
                tournament['name'],
                tournament['location'],
                tournament['start_at'],
                tournament['end_at'],
                tournament['players'],
                tournament['description']

            ))
            print("-----------------------------------------------------------------------------------------")
            # print(f"{tournament.doc_id}", end='-')
            # print(f"{tournament['name']} {tournament['location']}", end=' | ')
            # print(f"{tournament['start_at']} {tournament['end_at']}", end=' | ')
            # print(f"{tournament['rounds']} {tournament['players']}", end=' | ')
            # print(f"{tournament['time_control']} {tournament['description']}")

    def create_tournament():
        name = input("Entrez le nom de tornois : ")
        location = input("Entrez le lieu de tournois : ")
        start_at = input("Entrez la date début de tournois : ")
        end_at = input("Entrez la le date fin de tournois : ")
        time_control = input("Entrez le contrôle du temps : ")
        round = input("Entrez le round ? ")
        players = input("Entrez les players utiliser un virgul pour separer ex [1, 2]: ")
        rounds = input("Entrez les Tournées : ")
        round_total = input("Entrez le Tournées total : ")
        description = input("Entrez la description : ")
        return name, location, start_at, end_at, time_control, round, players, rounds, round_total, description

    def addPlayersToTournaments():
        tournament_id = input("Entrez le id de tornois sur lequel vous voulez ajouter des jours : ")
        return tournament_id

    def get_tournament_players():
        tournament_id = input("Entrez le id de tornois sur lequel vous voulez voir ses jours : ")
        return tournament_id
