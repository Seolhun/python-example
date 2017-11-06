from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        standings = self.standings
        standings = sorted(list(standings.items()), key=lambda x: x[1]['score'], reverse=True)
        dp = False
        for i1, s in enumerate(standings):
            for i2, e in enumerate(standings):
                if i1 != i2:
                    if s[1]['score'] == e[1]['score']:
                        dp = True
                        break
        if dp:
            standings = sorted(standings, key=lambda x: x[1]['games_played'], reverse=False)
            dp2 = False
            for i1, s in enumerate(standings):
                for i2, e in enumerate(standings):
                    if i1 != i2:
                        if s[1]['games_played'] == e[1]['games_played']:
                            dp2 = True
                            break
        print(standings)
        return standings[rank - 1][0]


table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))
