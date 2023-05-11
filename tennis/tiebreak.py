
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


class tiebreak:
    def __init__(self, player1:str, player2:str, matchFormat:dict=None):
        """
        Creates a new tiebreak obj


        Parameters:
        
            player1 (str): a string, player1's name

            player2 (str): a string, player2's name

            matchFormat (dict): an dictionary of match settings. example: {"first_to_num_points":7, "win_by":2, "whos_serve":"a"}.
            
        """
        self.player1 = player1
        self.player2 = player2
        if matchFormat is None:
            self.matchFormat = {"first_to_num_points":7, "win_by":2, "whos_serve":"a"}
        else:
            self.matchFormat = matchFormat #num_games_to_win, best_of_num_sets, who_serve,
            
        self.tiebreakScore = {player1:0,player2:0}
        self.startTieBreakServer = ''
        self.tiebreakStats = {"Aces":{player1: 0, player2: 0},"Double_fault":{player1: 0, player2: 0},"first_serve_percent":{player1: "NA", player2: "NA"},"first_serve_points_won":{player1: 0, player2: 0},"second_serve_percent":{player1: "NA", player2: "NA"},"second_serve_points_won":{player1: 0, player2: 0}, "winners":{player1: 0, player2: 0},"unforced_errors":{player1: 0, player2: 0},"win_by_volley":{player1: 0, player2: 0},"win_by_dropshot":{player1: 0, player2: 0},"win_by_overhead":{player1: 0, player2: 0}}
        self.totalPointsWon = {player1:0,player2:0}
        self.firstServe = True
        self.currentServerFaults = 0
        self.totalPointsWon = {player1: 0, player2: 0}
        self.firstServesAttempted = {player1: 0, player2: 0}
        self.secondServesAttempted = {player1: 0, player2: 0}
        self.firstServesMade = {player1: 0, player2: 0}
        self.secondServesMade = {player1: 0, player2: 0}


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function to save backup data for a tiebreak

    def backup_tiebreak(self):
        """

        save current data with the backup_tiebreak() method and import it into a new object with the load_backup() method
        example usage:

            backup_data = match.backup_tiebreak()
            new_tiebreak = tiebreak("player1","player2")
            new_tiebreak = new_tiebreak.load_backup(backup_data)
            print(new_tiebreak.tiebreak_stats("a"))
        """
        backup_data = {
            'player1': self.player1,
            'player2': self.player2,
            'matchFormat': self.matchFormat,
            'tiebreakScore': self.tiebreakScore,
            'startTieBreakServer': self.startTieBreakServer,
            'tiebreakStats': self.tiebreakStats,
            'totalPointsWon': self.totalPointsWon,
            'firstServe': self.firstServe,
            'currentServerFaults': self.currentServerFaults,
            'firstServesAttempted': self.firstServesAttempted,
            'secondServesAttempted': self.secondServesAttempted,
            'firstServesMade': self.firstServesMade,
            'secondServesMade': self.secondServesMade
        }
        return backup_data
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function to load the saved backup_data


    def load_backup(self, backup_data):
        """

        save current data with the backup_tiebreak() method and import it into a new object with the load_backup() method
        example usage:

            backup_data = tiebreak.backup_tiebreak()
            new_tiebreak = tiebreak("player1","player2")
            new_tiebreak = new_tiebreak.load_backup(backup_data)
            print(new_tiebreak.tiebreak_stats("a"))
        """
        self.player1 = backup_data['player1']
        self.player2 = backup_data['player2']
        self.matchFormat = backup_data['matchFormat']
        self.tiebreakScore = backup_data['tiebreakScore']
        self.startTieBreakServer = backup_data['startTieBreakServer']
        self.tiebreakStats = backup_data['tiebreakStats']
        self.totalPointsWon = backup_data['totalPointsWon']
        self.firstServe = backup_data['firstServe']
        self.currentServerFaults = backup_data['currentServerFaults']
        self.firstServesAttempted = backup_data['firstServesAttempted']
        self.secondServesAttempted = backup_data['secondServesAttempted']
        self.firstServesMade = backup_data['firstServesMade']
        self.secondServesMade = backup_data['secondServesMade']
        return self
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function that returns other player string name


    def get_other_player(self, player):
        if player == self.player1:
            return self.player2
        elif player == self.player2:
            return self.player1
        else:
            raise ValueError("Invalid player name.")
     
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function checks if the tiebreak has been won

    def check_set_break_win(self, player):
        otherPlayer = self.get_other_player(player)
        if self.tiebreakScore[player] >= self.matchFormat['first_to_num_points'] and self.tiebreakScore[player] - self.tiebreakScore[otherPlayer] >self.matchFormat['win_by']-1:
            return True
        return False

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function that handles a serve fault
    # Function that handles double faults


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

    # Function that updates the first serve percent and second serve percent


    def update_percentages(self,player):
        otherPlayer = self.get_other_player(player)
        if self.firstServesAttempted[player] != 0:
            self.tiebreakStats['first_serve_percent'][player] = round((self.firstServesMade[player]/self.firstServesAttempted[player])*100, 2)
        if self.secondServesAttempted[player] != 0:
            self.tiebreakStats['second_serve_percent'][player] = round((self.secondServesMade[player]/self.secondServesAttempted[player])*100)
        if self.firstServesAttempted[otherPlayer] != 0:
            self.tiebreakStats['first_serve_percent'][otherPlayer] = round((self.firstServesMade[otherPlayer]/self.firstServesAttempted[otherPlayer])*100)
        if self.secondServesAttempted[otherPlayer] != 0:
            self.tiebreakStats['second_serve_percent'][otherPlayer] = round((self.secondServesMade[otherPlayer]/self.secondServesAttempted[otherPlayer])*100)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function handles winning a point


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
                self.secondServesMade[player] +=1
                self.currentServerFaults = 0
                self.secondServesAttempted[player] +=1



        if "Ace" in how_won:
            self.tiebreakStats["Aces"][player]+=1
        if "Double_fault" in how_won:
            self.tiebreakStats["Double_fault"][otherPlayer]+=1
            self.secondServesAttempted[otherPlayer] +=1
        if "winner" in how_won:
            self.tiebreakStats["winners"][player]+=1
        if "unforced_errors" in how_won:
            self.tiebreakStats["unforced_errors"][otherPlayer]+=1
        if "win_by_volley" in how_won:
            self.tiebreakStats["win_by_volley"][player]+=1
        if "win_by_dropshot" in how_won:
            self.tiebreakStats["win_by_dropshot"][player]+=1
        if "win_by_overhead" in how_won:
            self.tiebreakStats["win_by_overhead"][player]+=1

        if (self.tiebreakScore[player] == 0 and self.tiebreakScore[otherPlayer] == 0):
            self.startTieBreakServer = self.matchFormat['whos_serve'][:]

        if self.matchFormat['whos_serve'] == player and self.firstServe == True:
            self.tiebreakStats["first_serve_points_won"][player]+=1
        if self.matchFormat['whos_serve'] == player and self.firstServe == False:
            self.tiebreakStats["second_serve_points_won"][player]+=1

        self.tiebreakScore[player]+=1
        self.totalPointsWon[player] +=1

        totalm = self.tiebreakScore[player] + self.tiebreakScore[otherPlayer]+1
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

        if (self.tiebreakScore[player] == 1 and self.tiebreakScore[otherPlayer] ==0) or (self.tiebreakScore[player] == 0 and self.tiebreakScore[otherPlayer] ==1):
            self.matchFormat['whos_serve']=self.get_other_player(self.startTieBreakServer)
        


        print("we are going to a SET tiebreak" , self.matchFormat['whos_serve']," to serve" )
        print(self.tiebreakScore)
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
            self.tiebreakScoreHistory.append(self.tiebreakScore)
            self.tiebreakScore[player] = 0
            self.tiebreakScore[self.get_other_player(player)] = 0
        self.firstServe=True

        self.update_percentages(player)
        return
                
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function that returns a string representation of the stats


    def tiebreak_stats(self, player:str) -> str:
            """
            returns a string representation of all the stats from the tiebreak

            Parameters:
                player (str): A player's name, will put this player on the left side of the board
            """
            otherPlayer = self.get_other_player(player)
            return(f"""
    ════════════════════════════════════════

    {player} vs {self.get_other_player(player)}                
    {self.tiebreakStats['first_serve_percent'][player]} - First Serve Percentage - {self.tiebreakStats['first_serve_percent'][otherPlayer]}

    {self.tiebreakStats['first_serve_points_won'][player]} - First Serve Points Won - {self.tiebreakStats['first_serve_points_won'][otherPlayer]}

    {self.tiebreakStats['second_serve_percent'][player]} - Second Serve Percentage - {self.tiebreakStats['second_serve_percent'][otherPlayer]}

    {self.tiebreakStats['second_serve_points_won'][player]} - Second Serve Points Won - {self.tiebreakStats['second_serve_points_won'][otherPlayer]}

    {self.totalPointsWon[player]} - Total Points Won - {self.totalPointsWon[otherPlayer]}

    {self.tiebreakStats['Aces'][player]} - Aces - {self.tiebreakStats['Aces'][otherPlayer]}

    {self.tiebreakStats['Double_fault'][player]} - Double Faults - {self.tiebreakStats['Double_fault'][otherPlayer]}

    {self.tiebreakStats['winners'][player]} - Winners - {self.tiebreakStats['winners'][otherPlayer]}

    {self.tiebreakStats['unforced_errors'][player]} - Unforced Errors - {self.tiebreakStats['unforced_errors'][otherPlayer]}

    {self.tiebreakStats['win_by_volley'][player]} - Points Won By Volley - {self.tiebreakStats['win_by_volley'][otherPlayer]}

    {self.tiebreakStats['win_by_dropshot'][player]} - Points Won By Dropshot - {self.tiebreakStats['win_by_dropshot'][otherPlayer]}

    {self.tiebreakStats['win_by_overhead'][player]} - Points Won By Overhead - {self.tiebreakStats['win_by_overhead'][otherPlayer]}



    ════════════════════════════════════════

            """)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # Function that returns a string representation of the scoreboard



    def get_scoreboard(self, player:str) -> str:
        """
        returns a string representation of the scoreboard

        Parameters:
            player (str): any player's name. The player parameter puts the player on the top half of the scoreboard
        """
        tb1 = str(self.tiebreakScore[player])
        tb2 = str(self.tiebreakScore[self.get_other_player(player)])

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
            Tiebreak Score

     T
     {tb1}  {st1}                {player}
     {tb2}  {st2}                {self.get_other_player(player)}

╚═════════════════════════════════════╝
""") 