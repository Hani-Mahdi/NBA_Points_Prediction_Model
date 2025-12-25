import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

years_to_process = 6
FEATURE_PATH = ["../data/processed/v1/player_features_" + str(2018 + i) + ".csv" for i in range(years_to_process)]
MODEL_PATH = "../models/linear_regression_v1.pkl"

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

TARGET = "pts"

dfs = [pd.read_csv(i) for i in FEATURE_PATH]
df = pd.concat(dfs, ignore_index=True).sort_values("game_date")

df = df[FEATURES + [TARGET]].dropna()

def train(df):


    split_idx = int(len(df) * 0.8)

    train_df = df.iloc[:split_idx]
    test_df  = df.iloc[split_idx:]

    X_train = train_df[FEATURES]
    y_train = train_df[TARGET]

    X_test = test_df[FEATURES]
    y_test = test_df[TARGET]

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    print("MAE:", mae)

    joblib.dump(model, MODEL_PATH)
    print("Model saved to:", MODEL_PATH)

train(df)