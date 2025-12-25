import json
import pandas as pd
from nba_api.stats.endpoints import leaguegamelog

#Filepaths to put the raw CSV files into
years_to_process = 6
cleanedTeamFile = ["../data/raw/game_logs_" + str(2018 + i) + ".csv" for i in range(years_to_process)]
cleanedPlayerFile = ["../data/raw/player_logs_" + str(2018 + i) + ".csv" for i in range(years_to_process)]

#toCSV function that takes arguments filepath and data (json) of type List[List[str]] and returns the same data in CSV format
def toCSV(filepath: str, data: list[list[str]]) -> None :
    with open(filepath, "w",  encoding="utf-8") as f:
        for i in data:
            line = line = ",".join(map(str, i))
            f.write(line + "\n")

#Given the layout of the nba api data, dataParse takes the str json data and extracts and parses data so it can be used by toCSV
def dataParse(json: str):
    
    gamelogHead = json["resultSets"][0]["headers"]
    gamelogBody = json["resultSets"][0]["rowSet"]
    
    return [gamelogHead] + gamelogBody

#requesting api info for teams
team_data = []

for i in cleanedTeamFile:
    x = str(int(i[-8:-4]) - 1)
    season = f"{x}-{str(int(x[-2:])+1)}"
    team_log = leaguegamelog.LeagueGameLog(season=season, season_type_all_star="Regular Season")
    team_data.append(json.loads(team_log.get_json()))

#requesting api info for players
player_data = []

for i in cleanedPlayerFile:
    x = str(int(i[-8:-4]) - 1)
    season = f"{x}-{str(int(x[-2:])+1)}"
    player_log = leaguegamelog.LeagueGameLog(season=season, season_type_all_star="Regular Season", player_or_team_abbreviation="P")
    player_data.append(json.loads(player_log.get_json()))

def clean(filepath, player=""):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.lower()

    abbr_to_id = df[["team_id", "team_abbreviation"]].drop_duplicates().set_index("team_abbreviation")["team_id"]
    
    df["game_date"] = pd.to_datetime(df["game_date"])
    df["opp_abr"] = df["matchup"].str[-3:]
    df["opp_id"] = df["opp_abr"].map(abbr_to_id)
    df["home"] = df["matchup"].str.contains("vs.")

    if player == "p":
        df.sort_values(["player_id", "game_date"], inplace=True)
        df = df[df["min"] > 0]
 
        # block of code to only limit data to player that score within a certain range
        # hypothesis: players within a certain range are more predictable

        """ 
        df["player_type"] = df.groupby("player_id")["pts"].transform("mean")
        df = df[(df["player_type"] >= 26) & (df["player_type"] <= 28) ]
        """
    else:
        df.sort_values(["team_name", "game_date"], inplace=True)


    with open(filepath, "w", encoding="utf-8") as f:
        f.write(df.to_csv(index=False))

#Parsing and exporting CSV data for players and teams
for i in range(len(team_data)):
    toCSV(cleanedTeamFile[i], dataParse(team_data[i]))
    toCSV(cleanedPlayerFile[i], dataParse(player_data[i]))

    clean(cleanedTeamFile[i])
    clean(cleanedPlayerFile[i], "p")
