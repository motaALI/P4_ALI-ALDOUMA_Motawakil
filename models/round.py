import random
import time
import itertools

from models.player import Player

class Round:
    def __init__(self, players, players_details):
        self.players = players
        self.players_details = players_details
        self.tournament_rounds  = {1: 'Round 1', 2: 'Round 2', 3: 'Round 3', 4: 'Round 4'}
        self.game_round = 0
        self.matches = []

    def next_round(self):
        """Go the next round of the tournament"""
        self.game_round += 1

        try:
            print(self.tournament_rounds[self.game_round])
        except KeyError:
            return


    def make_pair(self):
        """Combine two players randomly to play a chess game"""
        pairs = list(itertools.combinations(self.players, 2))
        pairs_unique = set(pairs)
        print(f'YOUR tournament players pairs : {pairs_unique}')
        print([self.players[i:i+2] for i in range(0, len(self.players), 2)])
        return pairs_unique

    def game(self):
        matches = []
        if len(self.players) < 2:
            print('Not enough players to play a matche')
            return

        self.next_round()
        print("------------------------------------------")
        self.make_pair()
        players_d = self.players_details
        for player in players_d:
            print(f'TOOOOOOOOOOOOOOOOOOOOOOOOO: {player["last_name"]}({player["classement"]})')
            matches.append(player)
        print(f'LIST OF MATCHES : {matches}')
        print("------------------------------------------")
        return matches

    def score_game(self):
        winners = []
        for player in self.players:
            total_rating = player.classement + player.classement
            player_chance = player.classement / total_rating

            maximum_range = 1000
            player_range = [i for i in range(0, int(player_chance * maximum_range))]
            choice = random.randint(0, maximum_range)
            if choice in player_range:
                print(f'{player.name} wins this round by checkmate')
                player.rating += self.game_round * 200
                winners.append(player)
            else:
                print(f'{player.opponent.name} wins this round by checkmate')
                player.opponent.rating += self.game_round * 200
                winners.append(player.opponent)

        return winners

