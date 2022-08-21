from models.tournament import Tournament
from view import Display
from views.tournament import TournamentView


class Round:
    def __init__(self, matches):
        self.matches = matches


class Controller_tournament:
    def __init__(self):
        self.display = Display

    # def create_first_round(tournament):
    #     players = tournament["players"]
    #     sorted(players, key=lambda player: player["score_tournament"])
    #     player_round = [
    #         (players[i], players[i + 4], [0, 0]) for i in range(0, len(players), 2)
    #     ]
    #     tournament.matches = [
    #         [players[i], players[i + 4]] for i in range(0, len(players), 2)
    #     ]
    #     round = Round(player_round)
    #     print("ROUNDDDD :", round)

    # def next_round(tournament):
    #     players = tournament["players"]
    #     sorted(players, key=lambda player: player["score_tournament"])
    #     matches = []
    #     for index, player in enumerate(players):
    #         if not [player, players[index + 1]] in tournament.matches:
    #             matches[player, players[index + 1]]
    #             tournament.matches = [player, players[index + 1]]
    #             continue

    def set_results(round):
        for index, match in enumerate(round):
            print("match", index + 1)
            print(match[0], "VS", match[1])
        tournament = Tournament
        tournament.next_round()
        tournament.save()

    def showAllTournaments():
        id = TournamentView.get_tournament_players()
        tournaments = Tournament.load_tournaments_db(id)
        return TournamentView.showAllView(tournaments)
        # print('SHOW ALL TOURNAMENTS ')
    
    def show_tournament_players():
        id = TournamentView.enter_id()
        ps = Tournament.showAllTournamentPlayers(id)
        return TournamentView.showAllTournamentPlayers(ps)

    def create_tournament():
        (
            name,
            location,
            start_at,
            end_at,
            time_control,
            round,
            players,
            rounds,
            round_total,
            description,
        ) = TournamentView.create_tournament()
        tournament = Tournament(
            name,
            location,
            start_at,
            end_at,
            time_control,
            round,
            players,
            rounds,
            round_total,
            description,
        )
        return tournament.create_tournament()

    def update_tournament():
        print("TOURNAMENT UPDATED !")

    def add_players_to_tournament():
        print("Players ADDED To Tournaments")
        id = TournamentView.insert_multi_players()
        return Tournament.get_one_tournament(id)

    """
    Display rounds in the tournament
    """

    def get_rounds_in_tournaments():
        id = TournamentView.get_rounds_in_tournament()
        return Tournament.get_one_tournament(id)

    def get_tournament_players():
        id = TournamentView.get_tournament_players()
        return Tournament.get_tournament_players(id)
    
    def insert_tournament_result():
        id = TournamentView.get_tournament_players()
        return Tournament.insert_tournament_result(id)
    
    def players_filter():
        menu_display = {
            "1": "Afficher tous les acteurs par ordre alphabétique",
            "2": "Afficher tous les acteurs par classement",
        }
        
    def manage_tournaments():
        menu = {
            "1": "Créer un nouveau tournoi",
            "2": "Lister les joueurs de tournoi",
            "3": "Saisir les resultats d'un tournoi",
            "4": "Liste des tournois",
            "5": "Modifier un tournoi",
            "6": "Afficher les round d'un tournoi",
            "R": "Reveneir à l'accueil",
        }
        
    

        Display.render_menu(menu)
        response = Display.get_user_input(menu)
        if response == "1":
            print("Créer un tournoi")
            Controller_tournament.create_tournament()
        elif response == "2":
            print("Lister les joueurs de tornoi")
            Controller_tournament.show_tournament_players()
        # elif response == "3":
        #     for i in range(8):
        #         print(f"Veuillez ajouter votre {i} jour")
        #         Controller_tournament.add_players_to_tournaments()
        elif response == "3":
            for i in range(8):
                print(f"Veuillez ajouter votre {i} jour")
                Controller_tournament.add_players_to_tournaments()
        elif response == "4":
            print("Liste des tournois")
            Controller_tournament.showAllTournaments()
        elif response == "5":
            Controller_tournament.update_tournament()
        elif response == "6":
            Controller_tournament.get_rounds_in_tournaments()
        elif response == "R":
            print("Reveneir à l'accueil")
        else:
            print("Error")
