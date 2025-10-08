import pandas as pd

original_df = pd.read_csv("batting_avg_league_leaders.csv")

# Filter invalid rows
valid_year = original_df["Year"].notna() & (original_df["Year"].str.lower() != "year")
valid_league = original_df["League"].isin(["AL", "NL"])
valid_avg = original_df["AVG"].str.contains(r"\d", na=False)

# Combine all valid conditions
is_valid = valid_year & valid_league & valid_avg

# Separate valid and removed rows
removed_rows = original_df[is_valid == False]
cleaned_rows = original_df[is_valid == True]

# Save removed rows
removed_rows.to_csv("removed.txt", index=False, sep="\t")

# Clean the valid data
df = cleaned_rows.copy()
df["Year"] = df["Year"].astype(int)
df["AVG"] = df["AVG"].astype(str).str.extract(r"([\d.]+)")[0].astype(float)
df["Player"] = df["Player"].astype(str).str.strip()
df["Team"] = df["Team"].astype(str).str.strip()
df = df[df["AVG"] > 0]

# Save final cleaned data
df.to_csv("batting_avg_cleaned.csv", index=False)

# Print for CLI inspection
print("\nRemoved rows:")
print(removed_rows.to_string(index=False))
print("\nSaved: batting_avg_cleaned.csv and removed.txt")
