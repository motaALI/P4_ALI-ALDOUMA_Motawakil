from tinydb import TinyDB, Query
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
        player_data = [player_db.get(doc_id=p) for p in players]
        sorted_players = sorted(
            player_data, key=lambda player: player["classement"], reverse=True
        )
        # player_round = [(players[i], players[i + 4], [0, 0]) for i in range(0, len(players),2)]
        # p_one_index = 0
        # p_two_index = p_one_index+1
        # index = 0
        # TODO filter by classement => then create the tournament
        print(list(zip(sorted_players[1::2], sorted_players[2::2])))
        matches_with_players_details = list(
            zip(sorted_players[::2], sorted_players[1::2])
        )
        matches = list(zip(players[::2], players[1::2]))
        # while len(players):
        #     print(players[p_one_index])
        #     print(players[p_two_index])
        #     print("----------------")
        #     try:
        #         if not [players[index], players[index+1]] in self.rounds:
        #             matches.append([players[index], players[index+1]])
        #             del players[index]
        #             del players[index-1]
        #             index = 0
        #         else:
        #             index += 1
        #     except KeyError:
        #         matches.append([players[0], players[0 + index -1]])
        #         self.matches = (players[0], players[0 + index -1])
        #         del players[0]
        #         del players[0 + index - 1]
        rounds = Round(matches)
        # print(f"Matches : {matches_with_players_details}")
        # print(f"Matches : {matches}")
        print(f"Rounds : {rounds}")
        return matches_with_players_details

    def next_round(self):
        players = self.players
        # sorted(players, key=lambda player: player["score_tournament"])
        self.matches = list(zip(players[::2], players[1::2]))

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
        tournament.next_round()
        tournament.update_tournament()

    def create_tournament(self):
        players_per_tournament = []
        # res = tournament_db.get(doc_id=id)
        # if res is not None:
        players = self.players
        print(f"YOUR DATA : {self.players}")
        for p in players:
            r = player_db.get(doc_id=p)
            players_per_tournament.append(r)
        # print(f'YOUR Players per tournament are : {players_per_tournament}')
        print(f"ROUNDDDS :{self.create_first_round()}")
        print(f"TOURNAMENT : {tournament_db.insert(self.tournament_serializer())}")
        rounds = self.create_first_round()
        # TournamentQuery.rounds == rounds
        # tournament_db.search((TournamentQuery.rounds==rounds))
        tournament_db.insert(self.tournament_serializer())
        # tournament_db.update({'rounds': rounds}, TournamentQuery.exists())
        return tournament_db.update({"rounds": rounds})

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
