## Python Algorithm
#### [File Owners](https://www.testdome.com/for-developers/solve-question/11846)

Implement a group_by_owners function that:

- Accepts a dictionary containing the file owner name for each file name.
- Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

---
#### [Palindrome](https://www.testdome.com/for-developers/solve-question/7962)

A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome. Character case should be ignored.

For example, is_palindrome("Deleveled") should return True as character case should be ignored, resulting in "deleveled", which is a palindrome since it reads the same backward and forward.

---
#### [LeagueTable](https://www.testdome.com/for-developers/solve-question/11195)

The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function. 
The player's rank in the league is calculated using the following logic:

- The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
- If two players are tied on score, then the player who has played the fewest games is ranked higher.
- If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.

Implement the player_rank function that returns the player at the given rank.

For example:
```python
table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))
```
All players have the same score. However, Arnold and Chris have played fewer games than Mike, and as Chris is before Arnold in the list of players, he is ranked first. Therefore, the code above should display "Chris".
