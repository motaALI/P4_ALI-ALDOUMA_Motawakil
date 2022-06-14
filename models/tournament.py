from tinydb import TinyDB, Query
from datetime import datetime
import random
import time
player_db = TinyDB("players.json")
player_db_query = Query()

tournament_db = TinyDB("tournaments.json")
# tournament_db  = tournament_db.table("tournaments")
TournamentQuery = Query()

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
        rounds: list,
        round_total: 4,
        description: str
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
        tournament_db = TinyDB("tournaments.json")
        res = tournament_db.get(doc_id=id)
        if res is not None:
            
            players = res['players']
            for p in players:
                r = player_db.get(doc_id=p)
                print(f'YOUR Player : {r}')
                tournament_players.append(r)
        print(f'YOUR tournament players : {tournament_players}')
        
        return tournament_players

    def create_tournament(self):
        return tournament_db.insert(self.tournament_serializer())

    def get_one_tournament(id):
        tournament_db = TinyDB("tournaments.json")
        res = tournament_db.get(doc_id=id)
        if res is not None:
            print(f'YOUR TOURNAMENT IS : {res}')
            return res
        else:
            # print(f"IL N'A Y PAS UN TOURNOI POUR L'ID {id}")
            return False
    
    def addPlayersToTournaments(id):
        # tournament_db = TinyDB("tournaments.json")
        res = tournament_db.search(TournamentQuery.doc_id == id)
        r = res['players']
        print(f'YOUR TOURNAMENT IS : { r }')

    def load_tournaments_db():
        tournament_db = TinyDB("tournaments.json")
        tournament_db.all()
        tournaments = []
        for item in tournament_db:
            tournaments.append(item)
        return tournaments

    
