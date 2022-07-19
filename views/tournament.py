from prettytable import PrettyTable


class TournamentView:
    def showAllView(list):
        print(f"Il y a {len(list)} tournois")
        # print("|{:<20}|{:<15}|{:<15}|{:<15}|{:<25}|{:<20}|".format(
        #     "Nom", "location", "Commance le :", "Fin", "Joueurs", "description")
        # )
        # print("------------------------------------------------------------------------------------------")
        # for tournament in list:
        #     print("|{:<20}|{:<15}|{:<15}|{:<15}|{:<25}|{:<20}|".format(
        #         tournament['name'],
        #         tournament['location'],
        #         tournament['start_at'],
        #         tournament['end_at'],
        #         tournament['players'],
        #         tournament['description']

        #     ))
        #     print("-----------------------------------------------------------------------------------------")
        # for tournament in list:
        #     print(f"{tournament.doc_id}", end="- ")
        #     print(f"{tournament['name']}", end=" | ")
        #     print(f"{tournament['location']}", end=" | ")
        #     print(f"{tournament['start_at']}", end=" | ")
        #     print(f"{tournament['end_at']}", end=" | ")
        #     print(f"{tournament['players']}", end=" | ")
        #     print(f"{tournament['description']}")
        my_table = PrettyTable()
        my_table.field_names = ["Nom", "location", "Commance le ", "Fin", "Joueurs", "Description"]
        
        for tournament in list:
            my_table.add_row([tournament['name'],
                tournament['location'],
                tournament['start_at'],
                tournament['end_at'],
                tournament['players'],
                tournament['description']])
        print(my_table)
        
    def create_tournament():
        # name = input("Entrez le nom de tournois : ")
        # location = input("Entrez le lieu de tournois : ")
        # start_at = input("Entrez la date début de tournois : ")
        # end_at = input("Entrez la le date fin de tournois : ")
        # time_control = input("Entrez le contrôle du temps : ")
        name = "Test 06"
        location = "Nantes"
        start_at = "30/06/2022"
        end_at = "30/06/2022"
        time_control = 10
        round = 0
        players_str = input(
            "Entrez les players utiliser un virgul pour separer ex [1, 2]: "
        )
        players = players_str.split(",")
        players_int = [int(p) for p in players]
        rounds = []
        round_total = 4
        # description = input("Entrez la description : ")
        description = "la description"
        return (
            name,
            location,
            start_at,
            end_at,
            time_control,
            round,
            players_int,
            rounds,
            round_total,
            description,
        )

    def addPlayersToTournaments():
        tournament_id = input(
            "Entrez le id de tornois sur lequel vous voulez ajouter des jours : "
        )
        return tournament_id

    def get_tournament_players():
        tournament_id = input(
            "Entrez le id de tornois sur lequel vous voulez voir ses jours : "
        )
        return tournament_id

    def get_rounds_in_tournament():
        tournament_id = input(
            "Entrez le id de tournoi sur lequel vous voulez affichier les matche : "
        )
        return tournament_id

    def insert_multi_players():
        tournament_id = input(
            "Entrez le id de tornois sur lequel vous voulez ajouter des jours : "
        )
        print(tournament_id)
        en = 0
        players = []
        while en < 8:
            player = input(
                "Veuillez entrer le jour \n Prènom, Nom, Date , Genre, Classenemt ?"
            )
            print("Prènom, Nom, Date , Genre, Classenemt ?")
            players.append(player)
            print(player)
            print(players)
            return players
