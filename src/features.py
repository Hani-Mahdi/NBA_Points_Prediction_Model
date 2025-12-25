import pandas as pd
import time

years_to_process = 6
team_data = ["../data/raw/game_logs_" + str(2018 + i) + ".csv" for i in range(years_to_process)]
player_data = ["../data/raw/player_logs_" + str(2018 + i) + ".csv" for i in range(years_to_process)]
processed_path = ["../data/processed/v1/player_features_xxxx.csv"]


def build_player_features(df: pd.DataFrame, tdf: pd.DataFrame) -> pd.DataFrame:
    """
    Input: cleaned player logs
    Output: model-ready feature table (no target)
    """

    processed = df[["player_id", "player_name", "team_id", "game_id", "fga", "fta", "fg_pct", "ft_pct", "game_date", "matchup", "min", "opp_id", "home", "pts"]].copy()
    processed["3_roll_avg"] = processed.groupby("player_name")["pts"].shift(1).rolling(window=3).mean()
    processed["5_roll_avg"] = processed.groupby("player_name")["pts"].shift(1).rolling(window=5).mean()
    processed["10_roll_avg"] = processed.groupby("player_name")["pts"].shift(1).rolling(window=10).mean()

    processed["3_roll_pts_std"] = processed.groupby("player_name")["pts"].shift(1).rolling(window=3).std()
    processed["5_roll_pts_std"] = processed.groupby("player_name")["pts"].shift(1).rolling(window=5).std()
    processed["10_roll_pts_std"] = processed.groupby("player_name")["pts"].shift(1).rolling(window=10).std()

    game_lookup = tdf[["game_id", "team_id", "pts"]].set_index(["game_id", "team_id"]).sort_index()
    processed["team_pts_w_player"] = game_lookup.loc[list(zip(processed["game_id"], processed["team_id"])), "pts"].values

    processed["3_roll_team_pts_w_player"] = processed.groupby("player_name")["team_pts_w_player"].shift(1).rolling(window=3).mean()
    processed["5_roll_team_pts_w_player"] = processed.groupby("player_name")["team_pts_w_player"].shift(1).rolling(window=5).mean()
    processed["10_roll_team_pts_w_player"] = processed.groupby("player_name")["team_pts_w_player"].shift(1).rolling(window=10).mean()

    game_lookup["total_pts"] = game_lookup.groupby(level=0)["pts"].transform("sum")
    game_lookup["pts_allowed"] = game_lookup["total_pts"] - game_lookup["pts"]
    
    game_lookup["3_roll_ptsa"] = game_lookup.groupby(level=1)["pts_allowed"].shift(1).rolling(window=3).mean()
    game_lookup["5_roll_ptsa"] = game_lookup.groupby(level=1)["pts_allowed"].shift(1).rolling(window=5).mean()
    game_lookup["10_roll_ptsa"] = game_lookup.groupby(level=1)["pts_allowed"].shift(1).rolling(window=10).mean()

    processed["3_roll_ptsa"] = game_lookup.loc[list(zip(processed["game_id"], processed["opp_id"])), "3_roll_ptsa"].values
    processed["5_roll_ptsa"] = game_lookup.loc[list(zip(processed["game_id"], processed["opp_id"])), "5_roll_ptsa"].values
    processed["10_roll_ptsa"] = game_lookup.loc[list(zip(processed["game_id"], processed["opp_id"])), "10_roll_ptsa"].values

    processed["3_roll_min"] = processed.groupby("player_name")["min"].shift(1).rolling(window=3).mean()
    processed["5_roll_min"] = processed.groupby("player_name")["min"].shift(1).rolling(window=5).mean()
    processed["10_roll_min"] = processed.groupby("player_name")["min"].shift(1).rolling(window=10).mean()

    processed["3_roll_fga"] = processed.groupby("player_name")["fga"].shift(1).rolling(window=3).mean()
    processed["5_roll_fga"] = processed.groupby("player_name")["fga"].shift(1).rolling(window=5).mean()
    processed["10_roll_fga"] = processed.groupby("player_name")["fga"].shift(1).rolling(window=10).mean()

    processed["3_roll_fg_pct"] = processed.groupby("player_name")["fg_pct"].shift(1).rolling(window=3).mean()
    processed["5_roll_fg_pct"] = processed.groupby("player_name")["fg_pct"].shift(1).rolling(window=5).mean()
    processed["10_roll_fg_pct"] = processed.groupby("player_name")["fg_pct"].shift(1).rolling(window=10).mean()

    processed["3_roll_fta"] = processed.groupby("player_name")["fta"].shift(1).rolling(window=3).mean()
    processed["5_roll_fta"] = processed.groupby("player_name")["fta"].shift(1).rolling(window=5).mean()
    processed["10_roll_fta"] = processed.groupby("player_name")["fta"].shift(1).rolling(window=10).mean()

    processed["3_roll_ft_pct"] = processed.groupby("player_name")["ft_pct"].shift(1).rolling(window=3).mean()
    processed["5_roll_ft_pct"] = processed.groupby("player_name")["ft_pct"].shift(1).rolling(window=5).mean()
    processed["10_roll_ft_pct"] = processed.groupby("player_name")["ft_pct"].shift(1).rolling(window=10).mean()

    return processed.sort_values("game_date", ascending=True)

for i in range(len(team_data)):

    tdf = pd.read_csv(team_data[i])
    pdf = pd.read_csv(player_data[i])

    x = build_player_features(pdf, tdf)

    year = team_data[i][-8:-4]
    processed_path = "../data/processed/v1/player_features_" + year + ".csv"

    with open(processed_path, "w", encoding="utf-8") as f:
        f.write(x.to_csv(index=False))
