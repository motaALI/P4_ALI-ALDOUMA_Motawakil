from colorama import Fore, Style
from prettytable import PrettyTable
from models.player import Player


class TournamentView:
    def __init__(self) -> None:
        return self

    def showAllView(list):
        print(f"{Fore.BLUE}Il y a {Fore.GREEN}{len(list)} {Fore.BLUE}tournois")
        my_table = PrettyTable()
        my_table.field_names = [
            f"{Fore.MAGENTA}Nom",
            f"{Fore.MAGENTA}location",
            f"{Fore.MAGENTA}Date début ",
            f"{Fore.MAGENTA}Date fin",
            f"{Fore.MAGENTA}Joueurs",
            f"{Fore.MAGENTA}Description",
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
            my_table.add_row(
                [
                    f"{Fore.MAGENTA}---------------",
                    f"{Fore.MAGENTA}---------------",
                    f"{Fore.MAGENTA}---------------",
                    f"{Fore.MAGENTA}---------------",
                    f"{Fore.MAGENTA}---------------",
                    f"{Fore.MAGENTA}---------------",
                ]
            )
        print(my_table)

    def showAllTournamentPlayers(players_l):
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
        for index, round in enumerate(rounds_in_tournament):
            rounds_table = PrettyTable()
            rounds_table.field_names = ["Joueur UN", "Contre", "Joueur DEUX", "GANANT"]
            print(f"\n{Fore.CYAN} ROUND N° :  ({index + 1})")
            for match in round:
                winner = (
                    match[0]["player"]
                    if match[0]["histo_score"][index] == 1
                    else match[1]["player"]
                )
                # print(f"Joueur {Player.showPlayerName(int(match[0]['player']))}")
                rounds_table.add_row(
                    [
                        Player.showPlayerName(int(match[0]["player"])),
                        " X ",
                        Player.showPlayerName(int(match[1]["player"])),
                        Player.showPlayerName(int((winner))),
                    ]
                ),

                rounds_table.add_row(["------", "------", "------", "------"])
            print(rounds_table)
            print(Style.RESET_ALL, end="")
            """
            Clear the board to prepare it for displaying the next round
            """
            rounds_table.clear()

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
            "Entrez l'id de tornois sur lequel vous voulez ajouter des jours : "
        )
        return tournament_id

    def get_tournament_players():
        tournament_id = input(
            "Entrez l'id de tornois sur lequel vous voulez voir ses jours : "
        )
        return tournament_id

    def get_data_to_sort_with():
        sort_data_as_dict = {}
        sort_with = int(
            input(
                " 1 :Pour trier par l'ordre alphabétique\n 2 : trier par classement\n "
            )
        )
        if sort_with == 1:
            sort_data_as_dict.update({"sort_with": "first_name"})
        elif sort_with == 2:
            sort_data_as_dict.update({"sort_with": "classement"})
        else:
            print("Error !!!!!")
        tournament_id = input(
            "Entrez l'id de tornois sur lequel vous voulez ajouter des jours : \n"
        )
        sort_data_as_dict.update({"tournament_id": tournament_id})

        return sort_data_as_dict

    def updateOneTournamen():
        tournament_id = input("Entrez l'id de tournoi à modifier : ")
        return tournament_id

    """
    Get data to update tournamnt
    """

    def tournament_new_data():
        tournament_new_data_update = {}
        name = input("Entrez le nom de tournois : ")
        location = input("Entrez le lieu de tournois : ")
        description = input("Entrez la description : ")
        tournament_new_data_update.update(
            {"name": name, "location": location, "description": description}
        )

        return tournament_new_data_update

    def insert_tournament_result():
        tournament_id = int(
            input("Entrez l'id de tornois sur lequel vous voulez voir ses jours : ")
        )
        return tournament_id

    def get_rounds_in_tournament():
        tournament_id = input(
            "Entrez l'id 'un tournoi pour affichier tous les rounds : "
        )
        return tournament_id

    def insert_multi_players():
        tournament_id = input(
            "Entrez l'id de tornois sur lequel vous voulez ajouter des jours : "
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
