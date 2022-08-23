from prettytable import PrettyTable


class TournamentView:
    def showAllView(list):
        print(f"Il y a {len(list)} tournois")
        my_table = PrettyTable()
        my_table.field_names = [
            "Nom",
            "location",
            "Date début ",
            "Date fin",
            "Joueurs",
            "Description",
        ]

        for tournament in list:
            my_table.add_row(
                [
                    tournament["name"],
                    tournament["location"],
                    tournament["start_at"],
                    tournament["end_at"],
                    tournament["players"],
                    tournament["description"],
                ]
            )
        print(my_table)

    def showAllTournamentPlayers(players_l):
        print(f"Il y a {players_l} jours")
        players_table = PrettyTable()
        players_table.field_names = [
            "Prènom",
            "Nom",
            "Date de naissance",
            "Genre",
            "Classement",
        ]
        for player in players_l:
            players_table.add_row(
                [
                    player["first_name"],
                    player["last_name"],
                    player["date_of_birth"],
                    player["gender"],
                    player["classement"],
                ]
            )
            players_table.add_row(["------", "------", "------", "------", "------"])
        print(players_table)

    def showRoundsInTournament(rounds_in_tournament):
        # print(f"Il y a {rounds_in_tournament} jours")
        # print(f"TYYYYYYYYYYYYYYYYOOOOOOOOOOOPEEEEEEEE {type(rounds_in_tournament)}")
        rounds_table = PrettyTable()
        rounds_table.field_names = ["Lieu", "Date debut", "Joueur"]
        # for round in rounds_in_tournament[0]:
        #     # print(f"ROUND ROUND {round}")
        #     # print(f"ROUND type {type(round)}")
        #     print(f"ROUND ROUND {round}")
        #     rounds_table.add_row([
        #         # round["score"],
        #         # round["histo_score"],
        #         # round["rank"],
        #     ])
        #     rounds_table.add_row(["------","------", "------", "------", "------"])
        # print(rounds_table)

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
            "Entrez l'id de tornois sur lequel vous voulez voir ses jours : "
        )
        return tournament_id

    def enter_id():
        filter_data_as_dict = {}
        filter_with = int(
            input(" 1 :Pour trier par l'ordre alphabétique\n 2 : trier par classement ")
        )
        if filter_with == 1:
            filter_data_as_dict.update({"filter_with": "first_name"})
        elif filter_with == 2:
            filter_data_as_dict.update({"filter_with": "classement"})
        else:
            print("Error !!!!!")
        tournament_id = input(
            "Entrez l'id de tornois sur lequel vous voulez ajouter des jours : "
        )
        filter_data_as_dict.update({"tournament_id": tournament_id})

        return filter_data_as_dict

    def insert_tournament_result():
        tournament_id = int(
            input("Entrez le id de tornois sur lequel vous voulez voir ses jours : ")
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
