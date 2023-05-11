
#    ____        _                   _     
#   |  _ \ _   _| |_ ___ _ __  _ __ (_)___ 
#   | |_) | | | | __/ _ \ '_ \| '_ \| / __|
#   |  __/| |_| | ||  __/ | | | | | | \__ \
#   |_|    \__, |\__\___|_| |_|_| |_|_|___/
#          |___/  
#
#                                   v 0.1.0 
# by: bear102
# https://github.com/bear102/                      



class TennisMatch:
    def __init__(self, player1:str, player2:str, matchFormat:dict=None):
        """
        Constructor for the TennisMatch class

        Parameters:
        
            player1 (str): a string, player1's name

            player2 (str): a string, player2's name

            matchFormat (dict): an dictionary of match settings. example: {"num_games_to_win":6, "best_of_num_sets":3, "whos_serve":"a", "with_AD":True}. defaults to: {"num_games_to_win":6, "best_of_num_sets":3, "whos_serve": player1, "with_AD":True} .
            

        """
        self.player1 = player1
        self.player2 = player2
        self.gameScore = {player1: 0, player2: 0}
        self.setScore = {player1: 0, player2: 0}
        self.matchScore = {player1: 0, player2: 0}
        self.gameHistory = []
        self.setHistory = []
        if matchFormat is None:
            self.matchFormat = {"num_games_to_win":6, "best_of_num_sets":3, "whos_serve": player1, "with_AD":True}
        else:
            self.matchFormat = matchFormat #num_games_to_win, best_of_num_sets, who_serve,

        self.matchStats = {"Aces":{player1: 0, player2: 0},"Double_fault":{player1: 0, player2: 0},"first_serve_percent":{player1: "NA", player2: "NA"},"first_serve_points_won":{player1: 0, player2: 0},"second_serve_percent":{player1: "NA", player2: "NA"},"second_serve_points_won":{player1: 0, player2: 0}, "winners":{player1: 0, player2: 0},"unforced_errors":{player1: 0, player2: 0},"win_by_volley":{player1: 0, player2: 0},"win_by_dropshot":{player1: 0, player2: 0},"win_by_overhead":{player1: 0, player2: 0},"serve_games_won":{player1: 0, player2: 0},"return_games_won":{player1: 0, player2: 0}}
        self.inSetTiebreak = False
        self.inMatchTiebreak = False
        self.winner = ''
        self.setTieBreakScores = {player1: 0, player2: 0}
        self.setTieBreakScoresHistory = []
        self.matchTieBreakScore = {player1: 0, player2: 0}
        self.startTieBreakServer = ""
        self.firstServe = True
        self.currentServerFaults = 0
        self.totalPointsWon = {player1: 0, player2: 0}
        self.firstServesAttempted = {player1: 0, player2: 0}
        self.secondServesAttempted = {player1: 0, player2: 0}
        self.firstServesMade = {player1: 0, player2: 0}
        self.secondServesMade = {player1: 0, player2: 0}


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # creates the backup data

    def backup_match(self):
        """

        save current data with the backup_match() method and import it into a new object with the load_backup() method
        example usage:

        #backup_data = match.backup_match()
        #new_match = TennisMatch("player1","player2",{"num_games_to_win":6, "best_of_num_sets":3, "whos_serve":"a", "with_AD":True})
        #new_match = new_match.load_backup(backup_data)
        #print(new_match.match_stats("playerA"))
        """
        backup_data = {
            'player1': self.player1,
            'player2': self.player2,
            'gameScore': self.gameScore,
            'setScore': self.setScore,
            'matchScore': self.matchScore,
            'gameHistory': self.gameHistory,
            'setHistory': self.setHistory,
            'matchFormat': self.matchFormat,
            'matchStats': self.matchStats,
            'inSetTiebreak': self.inSetTiebreak,
            'inMatchTiebreak': self.inMatchTiebreak,
            'winner': self.winner,
            'setTieBreakScores': self.setTieBreakScores,
            'setTieBreakScoresHistory': self.setTieBreakScoresHistory,
            'matchTieBreakScore': self.matchTieBreakScore,
            'startTieBreakServer': self.startTieBreakServer,
            'firstServe': self.firstServe,
            'currentServerFaults': self.currentServerFaults,
            'totalPointsWon': self.totalPointsWon,
            'firstServesAttempted': self.firstServesAttempted,
            'secondServesAttempted': self.secondServesAttempted,
            'firstServesMade': self.firstServesMade,
            'secondServesMade': self.secondServesMade
        }
        return backup_data
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # loads a saved backup

    def load_backup(self, backup_data):
        """

        save current data with the backup_match() method and import it into a new object with the load_backup() method
        example usage:

        #backup_data = match.backup_match()
        #new_match = TennisMatch("player1","player2",{"num_games_to_win":6, "best_of_num_sets":3, "whos_serve":"a", "with_AD":True})
        #new_match = new_match.load_backup(backup_data)
        #print(new_match.match_stats("playerA"))
        """
        # checks if valid backup
        try:
            if not isinstance(backup_data, dict):
                raise ValueError("Backup data must be a dictionary")

            expected_keys = ["player1", "player2", "gameScore", "setScore", "matchScore",                         "gameHistory", "setHistory", "matchFormat", "matchStats",                         "inSetTiebreak", "inMatchTiebreak", "winner", "setTieBreakScores",                         "setTieBreakScoresHistory", "matchTieBreakScore", "startTieBreakServer",                         "firstServe", "currentServerFaults", "totalPointsWon",                         "firstServesAttempted", "secondServesAttempted", "firstServesMade",                         "secondServesMade"]
            for key in expected_keys:
                if key not in backup_data:
                    raise ValueError(f"Backup data missing key '{key}'")

            new_match = TennisMatch(player1=backup_data['player1'], player2=backup_data['player2'], matchFormat=backup_data['matchFormat'])
            new_match.gameScore = backup_data['gameScore']
            new_match.setScore = backup_data['setScore']
            new_match.matchScore = backup_data['matchScore']
            new_match.gameHistory = backup_data['gameHistory']
            new_match.setHistory = backup_data['setHistory']
            new_match.matchStats = backup_data['matchStats']
            new_match.inSetTiebreak = backup_data['inSetTiebreak']
            new_match.inMatchTiebreak = backup_data['inMatchTiebreak']
            new_match.winner = backup_data['winner']
            new_match.setTieBreakScores = backup_data['setTieBreakScores']
            new_match.setTieBreakScoresHistory = backup_data['setTieBreakScoresHistory']
            new_match.matchTieBreakScore = backup_data['matchTieBreakScore']
            new_match.startTieBreakServer = backup_data['startTieBreakServer']
            new_match.firstServe = backup_data['firstServe']
            new_match.currentServerFaults = backup_data['currentServerFaults']
            new_match.totalPointsWon = backup_data['totalPointsWon']
            new_match.firstServesAttempted = backup_data['firstServesAttempted']
            new_match.secondServesAttempted = backup_data['secondServesAttempted']
            new_match.firstServesMade = backup_data['firstServesMade']
            new_match.secondServesMade = backup_data['secondServesMade']

            return new_match

        except Exception as e:
            print(f"Error loading backup: {e}")
            return None

    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
    # returns other player

    def get_other_player(self, player):
        if player == self.player1:
            return self.player2
        elif player == self.player2:
            return self.player1
        else:
            raise ValueError("Invalid player name.")
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    # checks if the game has been won


    def check_game_win(self,player, status):
        otherPlayer =  self.get_other_player(player)
        if status == "WON":
            self.setScore[player]+=1
            self.gameHistory.append(self.gameScore.copy())
            self.gameScore[player] = 0
            self.gameScore[otherPlayer] = 0
            if self.matchFormat['whos_serve'] == player:
                self.matchStats["serve_games_won"][player]+=1
            else:
                self.matchStats["return_games_won"][player]+=1

            self.matchFormat['whos_serve'] = self.get_other_player(self.matchFormat["whos_serve"])
            self.check_set_win(player)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        # checks if the set has been won

    def check_set_win(self, player):
        otherPlayer = self.get_other_player(player)
        if self.setScore[player] == self.matchFormat['num_games_to_win'] and self.setScore[player] - self.setScore[otherPlayer] >1:
            self.matchScore[player]+=1
            self.setHistory.append(self.setScore.copy())
            self.setScore[player] = 0
            self.setScore[otherPlayer] = 0
            self.check_match_win(player)
            self.setTieBreakScoresHistory.append({player:0,otherPlayer:0})

        if self.setScore[player]  == self.matchFormat['num_games_to_win']-1 and self.setScore[otherPlayer] == self.matchFormat['num_games_to_win']-1:
            self.inSetTiebreak = True
            self.startTieBreakServer = self.matchFormat['whos_serve']


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
       
        # checks if the match has been won

    def check_match_win(self,player):
        otherPlayer = self.get_other_player(player)

        num_sets_to_win = (self.matchFormat["best_of_num_sets"] // 2) + 1

        if self.matchScore[player] ==num_sets_to_win-1 and self.matchScore[otherPlayer] ==num_sets_to_win-1:
            self.inMatchTiebreak = True
            self.gameHistory.append(self.gameScore.copy())
            self.gameScore[player] = 0
            self.gameScore[otherPlayer] = 0
            self.startTieBreakServer = self.matchFormat['whos_serve']

        elif self.matchScore[player] == num_sets_to_win:
            self.winner = player
            print("Player " + player + " has won the match")
            quit
        else:
            return False
        

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # checks if the set tiebreak has been won

    def check_set_break_win(self, player):
        otherPlayer = self.get_other_player(player)
        if self.setTieBreakScores[player] >= 7 and self.setTieBreakScores[player] - self.setTieBreakScores[otherPlayer] >1:
            self.inSetTiebreak = False
            return True
        return False
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    # checks if the match tiebreak has been won

    def check_match_break_win(self, player):
        otherPlayer = self.get_other_player(player)
        if self.matchTieBreakScore[player] >= 10 and self.matchTieBreakScore[player] - self.matchTieBreakScore[otherPlayer] >1:
            self.inMatchTiebreak = False
            return True
        return False

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # handles point win

    def win_point(self, player:str, how_won=[]):
        """
        function to handle a player winning a point
        
        Parameters:
            player (str): name of the player who won the point. 
            how_won (list): an list of values on how the point was won, defaults to []. possible values include Ace, winner, unforced_errors,win_by_volley,win_by_dropshot,win_by_overhead


        """
        otherPlayer = self.get_other_player(player)
        if self.firstServe == True and "from_fault" not in how_won and self.matchFormat['whos_serve'] == player:
            self.firstServesAttempted[player] +=1
            self.firstServesMade[player]+=1

        if self.firstServe == True and self.matchFormat['whos_serve'] == otherPlayer:
            self.firstServesAttempted[otherPlayer] +=1
            self.firstServesMade[otherPlayer]+=1

        if self.firstServe == False and self.matchFormat['whos_serve'] == otherPlayer and 'Double_fault' not in how_won:
            self.secondServesAttempted[otherPlayer] +=1
            self.secondServesMade[otherPlayer]+=1

        if self.firstServe==False:
            if "Double_fault" not in how_won:
                self.secondServesAttempted[player] +=1
                self.secondServesMade[player] +=1
                self.currentServerFaults = 0

        elif self.firstServe == False and "from_fault" not in how_won:
            self.firstServesMade[player]+=1
        if "Ace" in how_won:
            self.matchStats["Aces"][player]+=1
        if "Double_fault" in how_won:
            self.matchStats["Double_fault"][otherPlayer]+=1
            self.secondServesAttempted[otherPlayer] +=1
        if "winner" in how_won:
            self.matchStats["winners"][player]+=1
        if "unforced_errors" in how_won:
            self.matchStats["unforced_errors"][otherPlayer]+=1
        if "win_by_volley" in how_won:
            self.matchStats["win_by_volley"][player]+=1
        if "win_by_dropshot" in how_won:
            self.matchStats["win_by_dropshot"][player]+=1
        if "win_by_overhead" in how_won:
            self.matchStats["win_by_overhead"][player]+=1

        if self.winner != '':
            raise Exception("match is completed, you cant score any more points")
        

        if self.inMatchTiebreak == False and self.inSetTiebreak == False:
            if self.matchFormat['whos_serve'] == player and self.firstServe == True:
                self.matchStats["first_serve_points_won"][player]+=1
            if self.matchFormat['whos_serve'] == player and self.firstServe == False:
                self.matchStats["second_serve_points_won"][player]+=1

        #-------------------------------------------------------------------------------------------------#
            # handles setTiebreak

        if self.inSetTiebreak == True:
            if (self.setTieBreakScores[player] == 0 and self.setTieBreakScores[otherPlayer] == 0):
                self.startTieBreakServer = self.matchFormat['whos_serve'][:]

            self.setTieBreakScores[player] +=1
            self.totalPointsWon[player] +=1




            if self.matchFormat['whos_serve'] == player and self.firstServe == True:
                self.matchStats["first_serve_points_won"][player]+=1
            if self.matchFormat['whos_serve'] == player and self.firstServe == False:
                self.matchStats["second_serve_points_won"][player]+=1

            total = self.setTieBreakScores[player] + self.setTieBreakScores[otherPlayer]+1
            if total %2  != 0:
                if ((total-1)/2)%2==0:
                    self.matchFormat['whos_serve'] = self.startTieBreakServer
                else:
                    self.matchFormat['whos_serve'] = self.get_other_player(self.startTieBreakServer)
            else:
                if total%4 == 0:
                    self.matchFormat['whos_serve'] = self.startTieBreakServer
                else:
                    self.matchFormat['whos_serve'] = self.get_other_player(self.startTieBreakServer)

            if (self.setTieBreakScores[player] == 1 and self.setTieBreakScores[otherPlayer] ==0) or (self.setTieBreakScores[player] == 0 and self.setTieBreakScores[otherPlayer] ==1):
                self.matchFormat['whos_serve']=self.get_other_player(self.startTieBreakServer)

            print("we are going to a SET tiebreak" , self.matchFormat['whos_serve']," to serve" )
            print(self.setTieBreakScores)
            self.update_percentages(player)

            if self.check_set_break_win(player):
                self.matchScore[player] +=1
                self.setScore[player] +=1
                self.setHistory.append(self.setScore.copy())
                self.setScore[player] = 0
                self.setScore[otherPlayer] = 0
                self.matchFormat['who_serve'] = self.get_other_player(self.startTieBreakServer)
                self.startTieBreakServer = ""
                self.check_match_win(player)
                self.setTieBreakScoresHistory.append(self.setTieBreakScores)
                self.setTieBreakScores[player] = 0
                self.setTieBreakScores[self.get_other_player(player)] = 0
            self.firstServe=True

            return
        
        #-------------------------------------------------------------------------------------------------#
            # handles matchTiebreak

        if self.inMatchTiebreak == True:
            if (self.matchTieBreakScore[player] == 0 and self.matchTieBreakScore[otherPlayer] == 0):
                self.startTieBreakServer = self.matchFormat['whos_serve'][:]
            self.matchTieBreakScore[player]+=1
            self.totalPointsWon[player] +=1

            if self.matchFormat['whos_serve'] == player and self.firstServe == True:
                self.matchStats["first_serve_points_won"][player]+=1
            if self.matchFormat['whos_serve'] == player and self.firstServe == False:
                self.matchStats["second_serve_points_won"][player]+=1

            totalm = self.matchTieBreakScore[player] + self.matchTieBreakScore[otherPlayer]+1
            if totalm %2  != 0:
                if ((totalm-1)/2)%2==0:
                    self.matchFormat['whos_serve'] = self.startTieBreakServer
                else:
                    self.matchFormat['whos_serve'] = self.get_other_player(self.startTieBreakServer)
            else:
                if totalm%4 == 0:
                    self.matchFormat['whos_serve'] = self.startTieBreakServer
                else:
                    self.matchFormat['whos_serve'] = self.get_other_player(self.startTieBreakServer)

            if (self.matchTieBreakScore[player] == 1 and self.matchTieBreakScore[otherPlayer] ==0) or (self.matchTieBreakScore[player] == 0 and self.matchTieBreakScore[otherPlayer] ==1):
                self.matchFormat['whos_serve']=self.get_other_player(self.startTieBreakServer)


            print("we are going to a Match tiebreak | ", self.matchFormat['whos_serve']," to serve" )        
            print(self.matchTieBreakScore)
            self.update_percentages(player)

            if self.check_match_break_win(player):
                self.matchScore[player] +=1
                if self.matchScore[player] == (self.matchFormat["best_of_num_sets"] // 2) + 1:
                    self.winner = player
                    print("Player " + player + " has won the match")
                    return
                else:
                    self.firstServe=True
                    return False
            self.firstServe=True
            return

        if self.matchFormat["with_AD"] == True:
            if self.gameScore[player] == 40 and self.gameScore[otherPlayer] == 40:
                self.gameScore[player] = "AD"
            elif self.gameScore[player] == 40 and self.gameScore[otherPlayer] == "AD":
                self.gameScore[otherPlayer] = 40
            elif self.gameScore[player] == "AD":
                self.check_game_win(player, "WON")
            elif self.gameScore[player] == 40:
                self.check_game_win(player, "WON")
            elif self.gameScore[player] == 30:
                self.gameScore[player] = 40
            elif self.gameScore[player] == 15:
                self.gameScore[player] = 30
            elif self.gameScore[player] == 0:
                self.gameScore[player] = 15

        else:
            if self.gameScore[player] == 40:
                self.check_game_win(player, "WON")
            elif self.gameScore[player] == 30:
                self.gameScore[player] = 40
            elif self.gameScore[player] == 15:
                self.gameScore[player] = 30
            elif self.gameScore[player] == 0:
                self.gameScore[player] = 15 


        self.totalPointsWon[player] +=1




        self.firstServe=True

        self.update_percentages(player)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Handles what happens if the server misses a serve. 
    # Handles Double Faults
    

    def serve_fault(self, player:str):
        """
        function to handle when a server misses a serve. If a point is lost because of a double fault, call the serve_fault() func 2 times to handle the point win/loss instead of the win_point() func

        Parameters:
            player (str): a string, the player who missed the serve's name
        """
        if player != self.matchFormat['whos_serve']:
            raise Exception("Player is not serving")
        otherPlayer = self.get_other_player(player)
        if self.firstServe:
            self.firstServe=False
            self.currentServerFaults+=1
            self.firstServesAttempted[player]+=1
            print("fault, second serve")
            self.update_percentages(player)
            return 
        if self.currentServerFaults == 1:
            self.currentServerFaults = 0
            self.win_point(self.get_other_player(player),["Double_fault","from_fault"])
            print("double fault")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Handles updating the first and second serve %

    def update_percentages(self,player):
        otherPlayer = self.get_other_player(player)
        if self.firstServesAttempted[player] != 0:
            self.matchStats['first_serve_percent'][player] = round((self.firstServesMade[player]/self.firstServesAttempted[player])*100, 2)
        if self.secondServesAttempted[player] != 0:
            self.matchStats['second_serve_percent'][player] = round((self.secondServesMade[player]/self.secondServesAttempted[player])*100)
        if self.firstServesAttempted[otherPlayer] != 0:
            self.matchStats['first_serve_percent'][otherPlayer] = round((self.firstServesMade[otherPlayer]/self.firstServesAttempted[otherPlayer])*100)
        if self.secondServesAttempted[otherPlayer] != 0:
            self.matchStats['second_serve_percent'][otherPlayer] = round((self.secondServesMade[otherPlayer]/self.secondServesAttempted[otherPlayer])*100)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function for development and testing. Automatically wins the game for param:player

    def win_game(self, player:str):
        """
        a func to increase the game set for a player, not designed for use only for testing purposes
        """
        if self.inSetTiebreak == True or self.inMatchTiebreak == True:
            raise Exception("Can not call win_game during a tiebreak, use win_point(player, how_won) instead")
        self.gameHistory.append(self.gameScore)
        self.gameScore[player] = 0
        self.gameScore[self.get_other_player(player)] = 0
        self.check_game_win(player, "WON")
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function for development and testing. Automatically wins the set for param:player

    def win_set(self,player:str):
        """
        a func to increase the set match for a player, not designed for use only for testing purposes
        """
        self.setHistory.append(self.setScore.copy())
        self.matchScore[player] +=1
        self.setScore[player] = 0
        self.setScore[self.get_other_player(player)] = 0
        self.inSetTiebreak = False
        self.inMatchTiebreak = False
        self.check_match_win(player)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Returns a dictionary with match results and info including statistics and score history.

    def get_all_info(self):
        """
        returns a dictionary with all the info about the match

        """
        return {"winner":self.winner, "game_history":self.gameHistory, "set_history": self.setHistory, "set_tiebreak_history":self.setTieBreakScoresHistory, "match_tiebreak_history":self.matchTieBreakScore,"match_format":self.matchFormat,"match_stats":self.matchStats}

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Returns a string representation of a scoreboard

    def get_scoreboard(self, player:str) -> str:
        """
        returns a string representation of the scoreboard

        Parameters:
            player (str): any player's name. The player parameter puts the player on the top half of the scoreboard
        """
        tb1 = str(self.setTieBreakScores[player])
        tb2 = str(self.setTieBreakScores[self.get_other_player(player)])
        mb1 = str(self.matchTieBreakScore[player])
        mb2 = str(self.matchTieBreakScore[self.get_other_player(player)])

        if mb1 == '0' and mb2 == '0':
            mb1 = ''
            mb2 = ''
        if tb1 == '0' and tb2 == '0':
            tb1 = ""
            tb2 = ""

        st1=""
        st2=""
        if self.matchFormat['whos_serve'] == player:
            st1 = "*"
            st2=" "

        else:
            st2="*"
            st1=" "
    
        return (f"""
╔═════════════════════════════════════╗
              Match Score

    M  S  G  T
    {str(self.matchScore[player])}  {str(self.setScore[player])}  {str(self.gameScore[player])} {tb1} {mb1} {st1}                {player}
    {str(self.matchScore[self.get_other_player(player)])}  {str(self.setScore[self.get_other_player(player)])}  {str(self.gameScore[self.get_other_player(player)])} {tb2} {mb2} {st2}                {self.get_other_player(player)}

╚═════════════════════════════════════╝
""") 
    


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Returns a string representation of the stats of the match 


    def match_stats(self, player:str) -> str:
        """
        returns a string representation of all the stats from the match

        Parameters:
            player (str): A player's name, will put this player on the left side of the board
        """
        otherPlayer = self.get_other_player(player)
        return(f"""
════════════════════════════════════════

{player} vs {self.get_other_player(player)}                
{self.matchStats['first_serve_percent'][player]} - First Serve Percentage - {self.matchStats['first_serve_percent'][otherPlayer]}

{self.matchStats['first_serve_points_won'][player]} - First Serve Points Won - {self.matchStats['first_serve_points_won'][otherPlayer]}

{self.matchStats['second_serve_percent'][player]} - Second Serve Percentage - {self.matchStats['second_serve_percent'][otherPlayer]}

{self.matchStats['second_serve_points_won'][player]} - Second Serve Points Won - {self.matchStats['second_serve_points_won'][otherPlayer]}

{self.matchStats['serve_games_won'][player]} - Serve Games Won - {self.matchStats['serve_games_won'][otherPlayer]}

{self.matchStats['return_games_won'][player]} - Return Games Won - {self.matchStats['return_games_won'][otherPlayer]}

{self.totalPointsWon[player]} - Total Points Won - {self.totalPointsWon[otherPlayer]}

{self.matchStats['Aces'][player]} - Aces - {self.matchStats['Aces'][otherPlayer]}

{self.matchStats['Double_fault'][player]} - Double Faults - {self.matchStats['Double_fault'][otherPlayer]}

{self.matchStats['winners'][player]} - Winners - {self.matchStats['winners'][otherPlayer]}

{self.matchStats['unforced_errors'][player]} - Unforced Errors - {self.matchStats['unforced_errors'][otherPlayer]}

{self.matchStats['win_by_volley'][player]} - Points Won By Volley - {self.matchStats['win_by_volley'][otherPlayer]}

{self.matchStats['win_by_dropshot'][player]} - Points Won By Dropshot - {self.matchStats['win_by_dropshot'][otherPlayer]}

{self.matchStats['win_by_overhead'][player]} - Points Won By Overhead - {self.matchStats['win_by_overhead'][otherPlayer]}



════════════════════════════════════════

        """)