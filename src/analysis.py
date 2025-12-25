import pandas as pd

pred_path = "../data/processed/predictions_v1.csv"

pred_data = pd.read_csv(pred_path)
pred_data = pred_data[pred_data["pts"] > 0]

pred_data["p_err"] = (pred_data["pred_pts"] - pred_data["pts"])/pred_data["pts"]
pred_data["abs_p_err"] = abs((pred_data["pred_pts"] - pred_data["pts"])/pred_data["pts"])

pred_data["avg_p_err"] = pred_data.groupby("player_name")["abs_p_err"].transform("mean").copy()

pred_err = pred_data[["player_name", "avg_p_err"]].set_index("player_name")

print(pred_err[pred_err["avg_p_err"] < 0.2])