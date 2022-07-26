from tinydb import Query, TinyDB

# from tinydb.operations import set
from models.player import Player

player_db = TinyDB("DB/players.json")
player_db_query = Query()

tournament_db = TinyDB("DB/tournaments.json")
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
        rounds: list,
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

    def getAll(self):
        result = tournament_db.all()
        return result

    def sort_players_by_rank(self):
        """Sort players by rank (ascending)"""
        self.players = sorted(self.players, key=lambda x: x.get("classement"))

    def get_tournament_players(self):
        tournament_players = []
        players_details = []
        tournament_db = TinyDB("DB/tournaments.json")
        res = tournament_db.get(doc_id=self)
        if res is not None:

            players = res["players"]
            for p in players:
                r = player_db.get(doc_id=p)
                players_details.append(r)
                print(f"YOUR Player : {p}")
                print(f"YOUR Player Type : {type(p)}")
                print(f"YOUR Players details : {players_details}")

                if p:
                    tournament_players.append(p)
            round = Round(players_details)
            print(f"YOUR tournament players : {round.matches}")
        return tournament_players
    
    def insert_tournament_result(self):
        print("Hello from ")
    def get_rounds_in_tournament(self):
        tournament_db = TinyDB("DB/tournaments.json")
        res = tournament_db.get(doc_id=self)
        if res is not None:
            rounds = res["rounds"]
            matches = [r for r in rounds]
        return matches

    def create_first_round(self):
        players = self.players
        matches = []
        player_dat = []
        # player_data = [player_db.get(doc_id=p) for p in players]
        for p in players:
            test = player_db.get(doc_id=p)
            test.update({"id": p})
            player_dat.append(test)
        print(f"TOTTOTOT {player_dat}")
        sorted_players = sorted(
            player_dat, key=lambda player: player["classement"], reverse=True
        )
        # matches_with_players_details = list(
        #     zip(sorted_players[::2], sorted_players[1::2])
        # )
        matches = list(zip(sorted_players[::2], sorted_players[1::2]))
        sorted_players_ids = []
        for m in matches:
            for i in m:
                sorted_players_ids.append({"player": i.get("id")})

        sorted_players_ids = list(
            zip(sorted_players_ids[::2], sorted_players_ids[1::2])
        )
        print(f"Matches !!!! : {matches}")
        return sorted_players_ids

    def insertRoundScore(self, players):
        # players = self.players
        next_round_list = []
        for m in players:
            if m[0]["score"] > m[1]["score"]:
                next_round_list.append({"player": m[0]['player'] })
                # print(f"The winer is : {m[0]['player']}")
            elif m[0]["score"] < m[1]["score"] :
                next_round_list.append({"player": m[1]['player']})
                # print(f"The winer is : {m[1]['player']}")
            else:
                return f"Match Null"
        return next_round_list
        
    def next_round(self, players):
        # players = self.rounds
        # list_of_next_round = []
        list_of_next_round = self.insertRoundScore(players)
        # print("--------------------------------")
        # print(f"Your LIST OF NEXT Players: {players} ")
        # print(f"Your LIST OF NEXT ROUND: {list_of_next_round} ")
        return list(zip(list_of_next_round[::2], list_of_next_round[1::2]))

    def update_tournament(self):
        """Update tournament info (after each round) in database"""
        tournament_db = TinyDB("DB/tournaments.json")
        db = tournament_db
        db.update({"rounds": self.matches})
        db.update({"players": self.players})

    def set_results(round):
        for index, match in enumerate(round):
            print("match", index + 1)
            print(match[0], "VS", match[1])
        tournament = Tournament
        # tournament.next_round()
        tournament.update_tournament()

    def create_tournament(self):
        players_per_tournament = []
        players = self.players
        # print(f"YOUR DATA : {self.players}")
        for p in players:
            r = player_db.get(doc_id=p)
            players_per_tournament.append(r)
        rounds = self.create_first_round()
        t_id = tournament_db.insert(self.tournament_serializer())
        print(f"Your tournament created with matches : {rounds}")
        for r in rounds:
            for j in r:
                score = float(input(f"Veuillez entrer le score de joueur {j} :"))
                j.update({"score": score})
        # next = self.next_round(rounds)
        # for r in next:
        #     for j in r:
        #         score = float(input(f"Veuillez entrer le score de joueur {j} :"))
        #         j.update({"score": score})
        # rounds.extend(next)
        
        return tournament_db.update({"rounds": rounds}, doc_ids=[t_id])

    def get_one_tournament(id):
        tournament_db = TinyDB("DB/tournaments.json")
        res = tournament_db.get(doc_id=id)
        if res is not None:
            print(f"YOUR TOURNAMENT IS : {res}")
            return res
        else:
            # print(f"IL N'A Y PAS UN TOURNOI POUR L'ID {id}")
            return False

    def insert_multi_players(**players):
        for p in players:
            player = Player(
                p["first_name"],
                p["last_name"],
                p["gender"],
                p["date_of_birth"],
                p["classement"],
            )
            print(f"YOUR PLAYERS FOR A TOURNAMENT ARE : {player}")
            return player.create_player(p)

    def addPlayersToTournaments(id):
        res = tournament_db.search(TournamentQuery.doc_id == id)
        r = res["players"]
        print(f"YOUR TOURNAMENT IS : { r }")

    def InsertPlayersScore(id):
        res = tournament_db.search(TournamentQuery.doc_id == id)
        rounds = res["rounds"]
        for r in rounds:
            for j in r:
                score = float(input(f"Veuillez entrer le score de joueur {j} :"))
                j.update({"score": score})
        return rounds
        
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


    