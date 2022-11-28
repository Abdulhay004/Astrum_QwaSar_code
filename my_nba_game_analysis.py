"""import libraries"""
import csv 
import re

"""play points"""
def play_points(players, regexp, actions, abr):
    my_list = []
    for i in actions:
        try:
            my_list.append(re.compile(regexp).search(i[7])[1])
        except:
            pass

    for par in my_list:
        for p_l in players["home_team"]["players_data"]:
            if p_l["player_name"] == par:
                p_l[abr]+=1
        for p_l in players["away_team"]["players_data"]:
            if p_l["player_name"] == par:
                p_l[abr]+=1

"""reading data and print result"""
def my_data(csvfile):   
    with open(csvfile, 'r') as nba_file:
        play_by_play = [line for line in csv.reader(nba_file, delimiter="|")]

    player_table = {"home_team": {"name": "", "players_data": []}, "away_team": {"name": "", "players_data": []}}

    for play in play_by_play:
        home_team = play[4]
        relevant_team = play[2]
        prese_action = play[7]
        try:
            player_name = re.compile(r"^(\S+\. \S+|\S\. \S+-\S)").search(prese_action)[1]
            player = {"player_name": player_name, "FG": 0, "FGM": 0, "FGA": 0, "FG%": 0.0, "3P": 0, "3PM": 0, "3PA": 0, "3P%": 0.0, "2P": 0, "2PM": 0, "FT": 0, "FTM": 0, "FTA": 0, "FT%": 0.0, "ORB": 0, "DRB": 0, "TRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0, "MCPFT": 0, "MICPFT": 0}
            if relevant_team == home_team:
                if not player in player_table["home_team"]["players_data"]:
                    player_table["home_team"]["players_data"].append(player)
            else:
                if not player in player_table["away_team"]["players_data"]:
                    player_table["away_team"]["players_data"].append(player)
        except:
            pass
    reform = r"(\S+\. \S+)"
    play_points(player_table, f"{reform} makes 3-pt", play_by_play, "3P")
    play_points(player_table, f"{reform} misses 3-pt", play_by_play, "3PM")
    play_points(player_table, f"{reform} makes 2-pt", play_by_play, "2P")
    play_points(player_table, f"{reform} misses 2-pt", play_by_play, "2PM")
    play_points(player_table, f"Offensive rebound by {reform}", play_by_play, "ORB")
    play_points(player_table, f"Defensive rebound by {reform}", play_by_play, "DRB")
    play_points(player_table, f"block by {reform}", play_by_play, "BLK")
    play_points(player_table, f"steal by {reform}", play_by_play, "STL")
    play_points(player_table, f"Turnover by {reform}", play_by_play, "TOV")
    play_points(player_table, f"assist by {reform}", play_by_play, "AST")
    play_points(player_table, f"Personal foul by {reform}", play_by_play, "PF")
    play_points(player_table, f"{reform} makes free throw", play_by_play, "FT")
    play_points(player_table, f"{reform} misses free throw", play_by_play, "FTM")
    play_points(player_table, f"{reform} makes clear path free throw ", play_by_play, "MCPFT")
    play_points(player_table, f"{reform} misses clear path free throw ", play_by_play, "MICPFT")


    for team in player_table.items():
        for player in team[1]["players_data"]:
            player["FG"] = player["3P"] + player["2P"]
            player["FGA"] = player["3P"] + player["2P"] + player["3PM"] + player["2PM"]
            player['3PA'] = player['3P'] + player['3PM']
            player["FT"] = player["FT"] * 1 + player["MCPFT"] + player["MICPFT"]
            player["FTA"] = player["FT"] + player["FTM"]
            player["PTS"] = player["3P"] * 3 + player["2P"] * 2 + player["FT"]
            player["TRB"] = player["DRB"] + player["ORB"]
            try:
                player["FG%"] = round(player["FG"] / player["FGA"], 3)
            except:
                pass
            try:
                player['3P%'] = round(player['3P'] / player['3PA'], 3)
            except:
                pass
            try:
                player["FT%"] = round(player["FT"] / player["FTA"], 3)
            except:
                pass
        for player in team[1]["players_data"]:
            del player["FGM"]
            del player["2P"]
            del player["2PM"]
            del player["3PM"]
            del player["FTM"]
            del player["MCPFT"]
            del player["MICPFT"]


    for team in player_table.items():
        team_totals =  {"FG": 0, "FGA": 0, "FG%": 0.0, "3P": 0, "3PA": 0, "3P%": 0.0, "FT": 0, "FTA": 0, "FT%": 0.0, "ORB": 0, "DRB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "PF": 0, "PTS": 0}
        fg, fga, fgp, p3, p3a, p3p, ft, fta, ftp, orb, drb, trb, ast, stl, blk, tov, pf, pts = 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        print("Players name", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS", sep="   ")
        for player in team[1]["players_data"]:
            print(player["player_name"], player["FG"], player["FGA"], player["FG%"], player["3P"], player["3PA"], player["3P%"], player["FT"], player["FTA"], player["FT%"], player["ORB"], player["DRB"], player["TRB"], player["AST"], player["STL"], player["BLK"], player["TOV"], player["PF"], player["PTS"], sep="    ")
            team_totals["FG"] += player["FG"]
            team_totals["FGA"] += player["FGA"]
            team_totals["3P"] += player["3P"]
            team_totals["3PA"] += player["3PA"]
            team_totals["FT"] += player["FT"]
            team_totals["FTA"] += player["FTA"]
            team_totals["ORB"] += player["ORB"]
            team_totals["DRB"] += player["DRB"]
            team_totals["AST"] += player["AST"]
            team_totals["STL"] += player["STL"]
            team_totals["BLK"] += player["BLK"]
            team_totals["TOV"] += player["TOV"]
            team_totals["PF"] += player["PF"]
            team_totals["PTS"] +=player["PTS"]
        team_totals["FG%"] = round(team_totals["FG"]/team_totals["FGA"],3) if team_totals["FGA"] > 0 else 0
        team_totals["3P%"] = round(team_totals["3P"]/team_totals["3PA"], 3) if team_totals["FGA"] > 0 else 0
        team_totals["FT%"] = round(team_totals["FT"] / team_totals["FTA"],3) if team_totals["FGA"] > 0 else 0
        team_totals["TRB"] = team_totals["ORB"] + team_totals["DRB"]
        print("Team totals", team_totals["FG"], team_totals["FGA"], team_totals["FG%"], team_totals["3P"], team_totals["3PA"], team_totals["3P%"], team_totals["FT"], team_totals["FTA"], team_totals["FT%"], team_totals["ORB"], team_totals["DRB"], team_totals["TRB"], team_totals["AST"], team_totals["STL"], team_totals["BLK"], team_totals["TOV"], team_totals["PF"], team_totals["PTS"], "\n\n", sep ="    ")
