# Python Tennis Library
[![PyPI](https://img.shields.io/pypi/v/tennis)](https://pypi.org/project/tennis/)
[![GitHub](https://img.shields.io/badge/GitHub-bear102-%2312100E.svg?style=flat&logo=github)](https://github.com/bear102/tennis)
![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

The Tennis library is a Python package that provides functionalities for simulating tennis matches and tiebreakers. It offers easy-to-use methods to simulate and track scores, tiebreakers, and various statistics. The tennis library is perfect for tracking real time data input.

<br>

## [**Table Of Contents**](#table-of-contents)
- [Tennis Library](#tennis-library)
  - [**Table Of Contents**](#table-of-contents)
  - [Features](#features)
    - [1. Match Simulation](#1-match-simulation)
    - [2. Tiebreaker](#2-tiebreaker)
    - [Tracking Stats](#tracking-stats)
  - [Usage](#usage)
    - [Quick Start](#quick-start)
    - [Match Methods](#match-methods)
      - [tennis\_match (self, player1:str, player2:str, matchFormat:dict=None)](#tennis_match-self-player1str-player2str-matchformatdictnone)
      - [backup\_match ()](#backup_match-)
      - [load\_backup (self, backup\_data)](#load_backup-self-backup_data)
      - [win\_point (self, player:str, how\_won=\[\])](#win_point-self-playerstr-how_won)
      - [serve\_fault (self, player:str)](#serve_fault-self-playerstr)
      - [win\_game (self, player:str)](#win_game-self-playerstr)
      - [win\_set (self, player:str)](#win_set-self-playerstr)
      - [get\_all\_info (self)](#get_all_info-self)
      - [get\_scoreboard (self, player:str)](#get_scoreboard-self-playerstr)
      - [match\_stats (self, player:str)](#match_stats-self-playerstr)
    - [Tiebreak Methods](#tiebreak-methods)
      - [match\_stats (self, player1:str, player2:str, matchFormat:tiebreak=None)](#match_stats-self-player1str-player2str-matchformattiebreaknone)
      - [backup\_tiebreak ()](#backup_tiebreak-)
      - [load\_backup (self, backup\_data)](#load_backup-self-backup_data-1)
      - [win\_point (self, player:str, how\_won=\[\])](#win_point-self-playerstr-how_won-1)
      - [tiebreak\_stats (self, player:str)](#tiebreak_stats-self-playerstr)
      - [get\_scoreboard (self, player:str)](#get_scoreboard-self-playerstr-1)




## [Features](#features)

The Tennis library offers the following main features:
<br>
### [1. Match Simulation](#1-match-simulation)

The match simulation feature allows you to simulate a full tennis match between two players. It will automatically keep track of match stats and comply with complicated rules like tiebreakers, AD, and serving
<br>
### [2. Tiebreaker](#2-tiebreaker)

The tiebreaker feature enables you to simulate a tiebreakerIt provides an easy-to-use interface for conducting tiebreakers, scoring points, and tracking statistics.
<br>
### [Tracking Stats](#tracking-stats)

Both the match simulation and tiebreaker features include built-in mechanisms for tracking various statistics. These statistics include:

- Aces
- Double faults
- First serve percentage
- First serve points won
- Second serve percentage
- Second serve points won
- Serve games won
- Return games won
- Winners
- Unforced errors
- Points won by volley
- Points won by dropshot
- Points won by overhead

These statistics help analyze player performance and provide insights into the gameplay.


<br>

***

<br>

## [Usage](#usage)

To use the Tennis library, follow these steps:

1. Install the library by running <br> `pip install tennis`.
   <br><br>
2. import libraries<br>
```python
from tennis import match

from tennis import tiebreak
```


### [Quick Start](#quick-start)
<br>
Here's an example of how to simulate a tennis match using the Tennis library:

```python
from tennis import match

# create a new match instance
a = match.TennisMatch("a","b",{"num_games_to_win":6, "best_of_num_sets":3, "whos_serve":"a", "with_AD":True})

# call win_point() player "a" won the point by an "overhead, opponent unforced error, and a dropshot"
a.win_point("a", ["overhead"])
a.win_point("a",['unforced_errors'])
a.win_point("a", ["win_by_dropshot"])

# gets a string representation of the scoreboard. Player "a" score will be displayed on top
print(a.get_scoreboard("a"))

# gets a string representation of the stats. Player "a" will be displayed on the left
print(a.match_stats("a"))

```

output: 
```
╔═════════════════════════════════════╗
              Match Score

    M  S  G  T
    0  0  40   *                a
    0  0  0                    b

╚═════════════════════════════════════╝


════════════════════════════════════════

a vs b
100 - First Serve Percentage - NA

3 - First Serve Points Won - 0

NA - Second Serve Percentage - NA

0 - Second Serve Points Won - 0

0 - Serve Games Won - 0

0 - Return Games Won - 0

3 - Total Points Won - 0

0 - Aces - 0

0 - Double Faults - 0

0 - Winners - 0

0 - Unforced Errors - 1

0 - Points Won By Volley - 0

1 - Points Won By Dropshot - 0

0 - Points Won By Overhead - 0



════════════════════════════════════════
```


<br>

***

<br>

Here's an example of how to simulate a tennis tiebreak using the Tennis library:

```python
from tennis import tiebreak

#create a new tiebreak instance
tb = tiebreak.tiebreak("a","b",{"first_to_num_points":7, "win_by":2, "whos_serve":"a"})

#player "a" wins the point
tb.win_point("a")

#player "b" misses a first serve
tb.serve_fault("b")

#returns a string representation of the scoreboard
print(tb.get_scoreboard("a"))

```

output:
```
╔═════════════════════════════════════╗
            Tiebreak Score

     T
     1                   a
     0  *                b

╚═════════════════════════════════════╝



════════════════════════════════════════

a vs b
100 - First Serve Percentage - NA

3 - First Serve Points Won - 0

NA - Second Serve Percentage - NA

0 - Second Serve Points Won - 0

0 - Serve Games Won - 0

0 - Return Games Won - 0

3 - Total Points Won - 0

0 - Aces - 0

0 - Double Faults - 0

0 - Winners - 0

0 - Unforced Errors - 1

0 - Points Won By Volley - 0

1 - Points Won By Dropshot - 0

0 - Points Won By Overhead - 0



════════════════════════════════════════
```

<br><br><br>

  

### <h1>Match Methods</h1>

#### [tennis_match](#tennis_match) (self, player1:str, player2:str, matchFormat:dict=None)
Creates a new instance of a tennis match.
**Parameters**

- player1 (str): The name of player 1.
- player2 (str): The name of player 2.
- matchFormat (dict): A dictionary of match settings.
  
**Example**
```python
match = TennisMatch("a", "b",{"num_games_to_win":2, "best_of_num_sets":3, "whos_serve":"a", "with_AD":True})
```



<br>

***

<br>

#### [backup_match](#backup_match) ()
Creates a backup for the current tennis match instance

#### [load_backup](#load_backup) (self, backup_data)
Loads a backup into a new match

**Parameters**
- backup_data (dict): The backup data created by the backup_match method


**Example**
```python
backup_data = match.backup_match()

new_match = TennisMatch("dawda","nnnn",{"num_games_to_win":2, "best_of_num_sets":3, "whos_serve":"a", "with_AD":True})

new_match = new_match.load_backup(backup_data)

print(new_match.match_stats("a"))

```



<br>

***

<br>



#### [win_point](#win_point) (self, player:str, how_won=[])
method that handles a player winning or loosing a point. Do not call this method if it is a double fault. Instead, call the [`serve_fault` (self, player:str)](#serve_fault-self-playerstr) method

**Parameters**
- player (str): The name of the player who won the point.
- how_won (Array): How the point was won (more than 1 in a method call is ok, just append them to the end of the list like ['winner','win_by_volley'])
  - `Ace`: player A wins by by acing player b (Player A's serves the ball in and player B does not even touch the ball)
  - `winner`: player A wins the point by hitting a winner. (The opponent doesnt touch the ball at all)
  - `unforced_error`: player A wins the point because player B made an unforced error (An error that was not caused by player A. For example player B got an easy ball and missed it)
  - `win_by_volley`: player A wins the point on a volley (Hitting the ball when it hasnt bounced right out of the air)
  - `win_by_dropshot`: player A wins the point with a dropshot (player A lightly hits a short ball close to the net)
  - `win_by_overhead`: player A wins the point via an overhead (player A "smashes" the ball right out of the air)


**Example**
```python
match.win_point("a")
match.win_point("b", ['win_by_volley'])
match.win_point("b", ['win_by_volley','winner'])
```

<br>

***

<br>

#### [serve_fault](#serve_fault) (self, player:str)
method to call when a server misses a first or second serve

**Parameters**
- player (str): The name of the player who missed the serve

**Example**
```python
#double fault
match.serve_fault("a")
match.serve_fault("a")

#missed first serve and made second serve
match.serve_fault("a")
match.win_point("a")
```

<br>

***

<br>

#### [win_game](#win_game) (self, player:str)
A method that will win the game for a player. This method is intended for development and testing. The statistics for the match will be off.

**Parameters**
- player (str): the player that will win the game

**Example**
```python
match.win_game("a")
```


<br>

***

<br>

#### [win_set](#win_set) (self, player:str)
A method that will win the set for a player. This method is intended for development and testing. The statistics for the match will be off.

**Parameters**
- player (str): the player that will win the set

**Example**
```python
match.win_set("a")
```

<br>

***

<br>


#### [get_all_info](#get_all_info) (self)
A method that will return all the info about the match in a dictionary format

```python
return {"winner":self.winner, "game_history":self.gameHistory, "set_history": self.setHistory, "set_tiebreak_history":self.setTieBreakScoresHistory, "match_tiebreak_history":self.matchTieBreakScore,"match_format":self.matchFormat,"match_stats":self.matchStats}
```

**example output**
```python
{'winner': '', 'game_history': [{'a': 0, 'b': 0}], 'set_history': [{'a': 0, 'b': 0}, {'a': 0, 'b': 0}], 'set_tiebreak_history': [], 'match_tiebreak_history': {'a': 1, 'b': 4}, 'match_format': {'num_games_to_win': 2, 'best_of_num_sets': 3, 'whos_serve': 'b', 'with_AD': True}, 'match_stats': {'Aces': {'a': 0, 'b': 0}, 'Double_fault': {'a': 2, 'b': 1}, 'first_serve_percent': {'a': 33, 'b': 33.33}, 'first_serve_points_won': {'a': 0, 'b': 1}, 'second_serve_percent': {'a': 0, 'b': 0}, 'second_serve_points_won': {'a': 0, 'b': 0}, 'winners': {'a': 0, 'b': 0}, 'unforced_errors': {'a': 0, 'b': 0}, 'win_by_volley': {'a': 0, 'b': 0}, 'win_by_dropshot': {'a': 0, 'b': 0}, 'win_by_overhead': {'a': 0, 'b': 0}, 'serve_games_won': {'a': 0, 'b': 0}, 'return_games_won': {'a': 0, 'b': 0}}}
```

<br>

***

<br>

#### [get_scoreboard](#get_scoreboard) (self, player:str)
A method that will return a string representation of the current scoreboard.

**Parameters**
- player (str): the player whos name and score will appear on the top half of the scoreboard

**Example Output**

```python
╔═════════════════════════════════════╗
              Match Score

    M  S  G  T
    1  0  0  1                  a
    1  0  0  4 *                b

╚═════════════════════════════════════╝
```

<br>

***

<br>

#### [match_stats](#match_stats) (self, player:str)
A method that will return the statistics about the match in a string format

**Parameters**
- player (str): the player who will appear on the left side of the stats

**Example Output**
```python
════════════════════════════════════════

a vs b
33 - First Serve Percentage - 33.33

0 - First Serve Points Won - 1

0 - Second Serve Percentage - 0

0 - Second Serve Points Won - 0

0 - Serve Games Won - 0

0 - Return Games Won - 0

1 - Total Points Won - 4

0 - Aces - 0

2 - Double Faults - 1

0 - Winners - 0

0 - Unforced Errors - 0

0 - Points Won By Volley - 0

0 - Points Won By Dropshot - 0

0 - Points Won By Overhead - 0



════════════════════════════════════════
```
<br><br>

### <h1>Tiebreak Methods</h1>

#### [match_stats](#tiebreak) (self, player1:str, player2:str, matchFormat:tiebreak=None)
Creates a new instance of a tiebreak.

**Parameters**
- player1 (str): the name of the first player
- player2 (str): the name of the second player
- matchFormat (dict): A dictionary of match settings.

**Example**
```python
match = tiebreak("a","b",{"first_to_num_points":7, "win_by":2, "whos_serve":"a"})
```

<br>

***

<br>

#### [backup_tiebreak](#backup_tiebreak) ()
A method to backup tiebreak data

**Example**
```python
match = tiebreak("a","b",{"first_to_num_points":7, "win_by":2, "whos_serve":"a"})
backup_data = match.backup_tiebreak()
```

#### [load_backup](#load_backup) (self, backup_data)
A method to load backup data from another tiebreak object

**Parameters**
- backup_data (dict): the data to load. use the backup_tiebreak method to obtain this

**Example**
```python
#backup old data
match = tiebreak("a","b",{"first_to_num_points":7, "win_by":2, "whos_serve":"a"})
backup_data = match.backup_tiebreak()

#create new tiebreak
new_tiebreak = tiebreak("player1","player2")

#load data into new tiebreak
new_tiebreak = new_tiebreak.load_backup(backup_data)

#print out stats of old tiebreak
print(new_tiebreak.tiebreak_stats("a"))
```

<br>

***

<br>

#### [win_point](#win_point) (self, player:str, how_won=[])
method that handles a player winning or loosing a point. Do not call this method if it is a double fault. Instead, call the [`serve_fault` (self, player:str)](#serve_fault-self-playerstr) method
**Parameters**
- player (str): The name of the player who won the point.
- how_won (Array): How the point was won (more than 1 in a method call is ok, just append them to the end of the list like ['winner','win_by_volley'])
  - `Ace`: player A wins by by acing player b (Player A's serves the ball in and player B does not even touch the ball)
  - `winner`: player A wins the point by hitting a winner. (The opponent doesnt touch the ball at all)
  - `unforced_error`: player A wins the point because player B made an unforced error (An error that was not caused by player A. For example player B got an easy ball and missed it)
  - `win_by_volley`: player A wins the point on a volley (Hitting the ball when it hasnt bounced right out of the air)
  - `win_by_dropshot`: player A wins the point with a dropshot (player A lightly hits a short ball close to the net)
  - `win_by_overhead`: player A wins the point via an overhead (player A "smashes" the ball right out of the air)


**Example**
```python
match.win_point("a")
match.win_point("b", ['win_by_volley'])
match.win_point("b", ['win_by_volley','winner'])
```

<br>

***

<br>

#### [tiebreak_stats](#tiebreak_stats) (self, player:str)
A method that returns a string representation of the statistics of the tiebreak

**Parameters**
- player (str): the name of the player whos stats will be displayed on the left side

**Example**
```python
print(tb.tiebreak_stats("a"))
```


<br>

***

<br>

#### [get_scoreboard](#get_scoreboard) (self, player:str)
A method that returns a string representation of the current score

**Parameters**
- player (str): the name of the player whos stats will be displayed on the top of the scoreboard

**Example**
```python
print(match.get_scoreboard("a"))
```

**output:**
```python
╔═════════════════════════════════════╗
              Match Score

    M  S  G  T
    1  0  0  1                  a
    1  0  0  4 *                b

╚═════════════════════════════════════╝
```


