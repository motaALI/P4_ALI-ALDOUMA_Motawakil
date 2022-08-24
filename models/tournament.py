from time import sleep

from tinydb import Query, TinyDB

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

    def showAllTournamentPlayers(self):
        players_list = []
        p_details = []
        # tournament_db = TinyDB("DB/tournaments.json")
        id = self.get("tournament_id")
        sort_with = self.get("sort_with")
        res = tournament_db.get(doc_id=id)
        players = res["players"]
        for p in players:
            r = player_db.get(doc_id=p)
            p_details.append(r)

            if p:
                players_list.append(p)
        round = Round(p_details)
        pls = sorted(round.matches, key=lambda p: p[sort_with])
        return pls

    def sort_players_by_rank(self):
        """Sort players by rank (ascending)"""
        self.players = sorted(self.players, key=lambda x: x.get("classement"))

    def sort_players_by_name(self):
        """Sort players by name(ascending)"""
        self.players = sorted(self.players, key=lambda x: x.get("first_name"))

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

                if p:
                    tournament_players.append(p)
        return tournament_players

    def insert_tournament_result(self):
        print("Hello from ")

    def get_rounds_in_tournament(self):
        tournament_db = TinyDB("DB/tournaments.json")
        res = tournament_db.get(doc_id=self)
        if res is not None:
            rounds = res["rounds"]
            all_rounds = [r for r in rounds]

        return all_rounds

    def create_first_round(self):
        players = self.players
        matches = []
        player_dat = []
        for p in players:
            test = player_db.get(doc_id=p)
            test.update({"id": p})
            player_dat.append(test)
        sorted_players = sorted(
            player_dat, key=lambda player: player["classement"], reverse=True
        )
        matches = list(zip(sorted_players[::2], sorted_players[1::2]))
        sorted_players_ids = []
        for m in matches:
            for i in m:
                sorted_players_ids.append({"player": i.get("id")})

        return list(list(zip(sorted_players_ids[::2], sorted_players_ids[1::2])))

    def insertRoundScore(self, players):
        # players = self.players
        print(f"players players players players players {players}")
        next_round_list = []
        for matche in players:
            print(f"matche matche matche matche matche {matche}")
            for m in matche:
                try:
                    if m[0]["score"] > m[1]["score"]:
                        next_round_list.append({"player": m[0]["player"]})
                        print(f"The winer is : {m[0]['player']}")
                    elif m[0]["score"] < m[1]["score"]:
                        next_round_list.append({"player": m[1]["player"]})
                        print(f"The winer is : {m[1]['player']}")
                    else:
                        print("Match Null")
                except ValueError as error:
                    error(f"ERORR FROM INSERT RESULT : {m}")
        return next_round_list

    def next_round(self, players):
        list_of_next_round = self.insertRoundScore(players)
        sleep(3)
        if list_of_next_round != 2:
            return list(zip(list_of_next_round[::2], list_of_next_round[1::2]))
        else:
            return print(f"THE NEXT IS {list_of_next_round/2}")

    def next_round_with_score(self, players):
        sorted_players = sorted(
            players, key=lambda player: player["score"], reverse=True
        )

        return list(list(zip(sorted_players[::2], sorted_players[1::2])))

    def next_round_with_score_and_new_score(self, current_rounds):
        players = []
        new_round = []
        for matche in current_rounds:
            for m in matche:
                players.append(m)

        sorted_players = sorted(
            players, key=lambda player: player["rank"], reverse=True
        )

        next_round = list(list(zip(sorted_players[::2], sorted_players[1::2])))

        new_round = next_round
        for matche in new_round:
            for m in matche:
                score = int(input(f"ENTER le score POUR CE round pour le joueur {m} :"))
                new_histo = m.get("histo_score") + [score]
                rank = sum(new_histo)
                n_score = {"score": score, "rank": rank, "histo_score": new_histo}
                m.update(n_score)
        print(f"NEXT ROUND IS : {next_round}")
        print(f"NEW ROUND IS : {new_round}")

        return new_round

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
        tournament.update_tournament()

    def create_tournament(self):
        players_per_tournament = []
        players = self.players
        for p in players:
            r = player_db.get(doc_id=p)
            players_per_tournament.append(r)
        tournament_id = tournament_db.insert(self.tournament_serializer())
        d = tournament_db.get(doc_id=tournament_id)
        rounds = d["rounds"]

        rounds.append(self.create_first_round())
        tournament_db.update({"rounds": rounds}, doc_ids=[tournament_id])
        sleep(3)
        print(f"FIRST ROUND CREATED ...! {rounds}")

        for m in rounds[0]:
            for j in m:
                score = int(input(f"ENTER de joueur {j} :"))
                rank = score
                j_score = {"score": score, "rank": rank, "histo_score": [score]}
                # j_score = {"score": score}
                j.update(j_score)
        tournament_db.update({"rounds": rounds}, doc_ids=[tournament_id])
        sleep(3)

        # TODO REFACTO THIS FUNCTION
        second_round = d["rounds"][0]
        second_array = self.next_round_with_score_and_new_score(second_round)
        rounds.append(second_array)
        tournament_db.update({"rounds": rounds}, doc_ids=[tournament_id])
        sleep(3)
        print("DEUSIEMENE ROUND FINISHED ...!")

        third_round = d["rounds"][1]
        third_array = self.next_round_with_score_and_new_score(third_round)
        rounds.append(third_array)

        tournament_db.update({"rounds": rounds}, doc_ids=[tournament_id])
        sleep(3)
        print("TROISIEME ROUND CREATED ...!")
        print("TROISIEME ROUND FINISHED ...!")

        fourth_round = d["rounds"][2]
        fourth_array = self.next_round_with_score_and_new_score(fourth_round)
        rounds.append(fourth_array)
        tournament_db.update({"rounds": rounds}, doc_ids=[tournament_id])
        sleep(3)
        print("FINAL ROUND CREATED ...!")

        print("TORNAMENT FINISHED .....!")
        print(f"ALL ROUNDS {rounds}")
        return rounds

    def updateOneTournamen(self):
        id = int(self.get("id"))
        tournament = tournament_db.get(doc_id=id)
        if tournament is None:
            print(f"Il n'a y aucun tournoi avec l'id {id}")
        else:
            name = self.get("name")
            location = self.get("location")
            description = self.get("description")
            updated_tournament = tournament_db.update(
                {"name": name, "location": location, "description": description},
                doc_ids=[id],
            )
            return updated_tournament

    def get_one_tournament(id):
        tournamente_data = []
        tournament_db = TinyDB("DB/tournaments.json")
        res = tournament_db.get(doc_id=id)
        if res is not None:
            for t_d in res.values():
                tournamente_data.append(t_d)
            return tournamente_data
        else:
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
