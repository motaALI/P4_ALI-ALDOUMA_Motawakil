from models.tournament import Tournament
from views.tournament import TournamentView
from views.player import PlayerView
from view import Display

class Round:
    def __init__(self, matches):
        self.matches = matches

class Controller_tournament:
    def __init__(self):
        self.display = Display

    def create_first_round(tournament):
        players = tournament["players"]
        sorted(players, key=lambda player: player["score_tournament"])
        player_round = [(players[i], players[i+4], [0,0]) for i in range(0, len(players), 2)]
        tournament.matches = [[players[i], players[i+4]] for i in range(0, len(players), 2)]
        round = Round(player_round)
        print("ROUNDDDD : ",round)
    

    def next_round(tournament):
        players = tournament["players"]
        sorted(players, key=lambda player: player["score_tournament"])
        matches = []
        for index, player in enumerate(players):
            if not [player, players[index +1]] in tournament.matches:
                matches[player, players[index +1]]
                tournament.matches = [player, players[index+1]]
                continue

    def set_results(round):
        for index, match in enumerate(round):
            print("match", index+1)
            print(match[0], "VS", match[1])
        tournament = Tournament
        tournament.next_round()
        tournament.save()

    def showAllTournaments():
        tournaments = Tournament.load_tournaments_db()
        return TournamentView.showAllView(tournaments)
        # print('SHOW ALL TOURNAMENTS ')

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
            description
        ) = TournamentView.create_tournament()
        tournament = Tournament(name, location, start_at, end_at, time_control, round, players, rounds, round_total, description)
        tournament.create_first_round()
        return tournament.create_tournament()
    
    def update_tournament():
        print('TOURNAMENT UPDATED !')

    def addPlayersToTournaments():
        print("Players ADDED To Tournaments")
        id =  TournamentView.insert_multi_players()
        return Tournament.get_one_tournament(id)

    def get_tournament_players():
        id =  TournamentView.get_tournament_players()
        tournament = Tournament
        return Tournament.get_tournament_players(id)


    def manage_tournaments():
        menu = {
            "1": "Créer un nouveau tournoi",
            "2": "Ajouter huit joueurs",
            "7": "Lister les joueurs de tornoi",
            "3": "Liste des tournois",
            "4": "Modifier un tournoi",
            "R": "Reveneir à l'accueil",
        }

        Display.render_menu(menu)
        response = Display.get_user_input(menu)
        if response == "1":
            print("Créer un tournoi")
            Controller_tournament.create_tournament()
        elif response == "7":
            print("Lister les joueurs de tornoi")
            Controller_tournament.get_tournament_players()
        elif response == "2":
            for i in range(8):
                print(f"Veuillez ajouter votre {i} jour")
                Controller_tournament.addPlayersToTournaments()
        elif response == "3":
            print("Liste des tournois")
            Controller_tournament.showAllTournaments()
        elif response == "4":
            Controller_tournament.update_tournament()
        elif response == "R":
            print("Reveneir à l'accueil")
        else:
            print("Error")