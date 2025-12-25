# src/predict.py

import pandas as pd
import joblib

FEATURE_PATH = ["../data/processed/v1/player_features_2025.csv"]
MODEL_PATH = "../models/linear_regression_v1.pkl"
OUTPUT_PATH = "../data/processed/predictions_v1.csv"

FEATURES = [
    "3_roll_avg",
    "5_roll_avg",
    "10_roll_avg",
    "3_roll_min",
    "5_roll_min",
    "3_roll_fga",
    "5_roll_fga",
    "3_roll_fta",
    "5_roll_fta",
    "3_roll_ptsa",
    "3_roll_team_pts_w_player",
    "5_roll_team_pts_w_player",
    "10_roll_team_pts_w_player",
    "3_roll_pts_std",
    "5_roll_pts_std",
    "home"
]

df = pd.read_csv(FEATURE_PATH)

def predict(df):
    
    df_pred = df[FEATURES].dropna()
    
    model = joblib.load(MODEL_PATH)

    preds = model.predict(df_pred)

    df.loc[df_pred.index, "pred_pts"] = preds

    out_cols = [
        "player_id",
        "player_name",
        "game_date",
        "matchup",
        "pts",
        "pred_pts"
    ]

    df[out_cols].dropna().to_csv(
        OUTPUT_PATH,
        index=False
    )

    print("Predictions saved to:", OUTPUT_PATH)

predict()
