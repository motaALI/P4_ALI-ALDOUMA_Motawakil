from tinydb import TinyDB, Query
from models.player import Player
# from models.round import Round
player_db = TinyDB("DB/players.json")
player_db_query = Query()

tournament_db = TinyDB("DB/tournaments.json")
# tournament_db  = tournament_db.table("tournaments")
TournamentQuery = Query()

class Round:
    def __init__(self, matches):
        self.matches = matches

class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_at: str,
        end_at: str,
        time_control: str,
        round: int,
        players: list,
        rounds: list, # Matche pas forcement des obj => j1, j2
        round_total: 4,
        description: str,
    ):
        self.name = name
        self.location = location
        self.start_at = start_at
        self.end_at = end_at
        self.time_control = time_control
        self.round = round
        self.players = players
        self.rounds = rounds
        self.round_total = round_total
        self.description = description


    def tournament_serializer(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_at": self.start_at,
            "end_at": self.end_at,
            "time_control": self.time_control,
            "round": self.round,
            "players": self.players,
            "rounds": self.rounds,
            "round_total": self.round_total,
            "description": self.description,
        }

    def getAll():
        result = tournament_db.all()
        return result

    def make_pair(self):
        """Combine two players randomly to play a chess game"""

        pairs_of_players = [] 
        for p1 in self.players:
            for p2 in self.players:
                pairs_of_players.append((p1,p2))
        pairs = list(set(pairs_of_players))
        print(f'YOUR tournament players pairs : {pairs}')
        return pairs
    
    def get_tournament_players(id):
        tournament_players = []
        players_details = []
        tournament_db = TinyDB("DB/tournaments.json")
        res = tournament_db.get(doc_id=id)
        if res is not None:
            
            players = res["players"]
            for p in players.split(','):
                r = player_db.get(doc_id=p)
                players_details.append(r)
                print(f'YOUR Player : {p}')
                print(f'YOUR Player Type : {type(p)}')
                print(f'YOUR Players details : {players_details}')

                if p:
                    tournament_players.append(p)
            round = Round(tournament_players, (players_details))
            print(f'YOUR tournament players : {round.matches}')

        # CHESS_PLAYERS = [players_details(last_name, classement) for last_name, classement in zip(Round.players_details)]
        print()
        return tournament_players

    def create_first_round(tournament):
        players = tournament.players
        sorted_players = sorted(players, key=lambda player: player["score_tournament"])
        print(f"sorted players : {sorted_players}")
        player_round = [(players[i], players[i + 4], [0, 0]) for i in range(0, len(players),2)]
        round.matches = [[players[i], players[i+4]] for i in range(0, len(players), 2)]
        round = Round(player_round)
        print(f'Your first round {round}')
        return round

    def next_round(tournament):
        players = tournament.players
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
    

    def create_tournament(self):
        players_per_tournament = []
        # res = tournament_db.get(doc_id=id)
        # if res is not None:
        players = self.players
        print(f'YOUR DATA : {self.players}')
        for p in players.split(','):
            r = player_db.get(doc_id=p)
            players_per_tournament.append(r)
        # print(f'YOUR Players per tournament are : {players_per_tournament}')
        # self.create_first_round(players)
        return tournament_db.insert(self.tournament_serializer())

    def get_one_tournament(id):
        tournament_db = TinyDB("DB/tournaments.json")
        res = tournament_db.get(doc_id=id)
        if res is not None:
            print(f'YOUR TOURNAMENT IS : {res}')
            return res
        else:
            # print(f"IL N'A Y PAS UN TOURNOI POUR L'ID {id}")
            return False

    def insert_multi_players(**players):
        for p in players:
            player = Player(p["first_name"], p["last_name"], p["gender"], p["date_of_birth"], p["classement"])
            print(f"YOUR PLAYERS FOR A TOURNAMENT ARE : {player}")
            return player.create_player(p)

    
    def addPlayersToTournaments(id):
        res = tournament_db.search(TournamentQuery.doc_id == id)


        r = res['players']
        print(f'YOUR TOURNAMENT IS : { r }')

    def load_tournaments_db():
        tournament_db = TinyDB("DB/tournaments.json")
        tournament_db.all()
        tournaments = []
        for item in tournament_db:
            tournaments.append(item)
        return tournaments

    

    def rounds_of_tournament(self):
        tournament = self.get_one_tournament()
        self.create_first_round(tournament)
        self.next_round(tournament)