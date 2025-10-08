import streamlit as st
import pandas as pd
import altair as alt

# Load cleaned CSV
df = pd.read_csv("batting_avg_cleaned.csv")

# Ensure Year is numeric and remove any thousand separator issues
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df.dropna(subset=["Year"], inplace=True)
df["Year"] = df["Year"].astype(int)

# Sidebar filters
st.sidebar.title("Filter Options")
min_year, max_year = int(df["Year"].min()), int(df["Year"].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (2000, max_year))
avg_threshold = st.sidebar.slider("Minimum Batting Average", 0.25, 0.45, 0.30, 0.005)
league = st.sidebar.multiselect("Select League(s)", ["AL", "NL"], default=["AL", "NL"])

# Filtered DataFrame
filtered_df = df[
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1]) &
    (df["AVG"] >= avg_threshold) &
    (df["League"].isin(league))
]

st.title("MLB Batting Average Leaders Dashboard")
st.markdown("Explore league-leading hitters by year, team, and AVG.")

# Bar chart: Top Hitters by AVG across selected years
st.subheader(f"Top Hitters by AVG ({year_range[0]}–{year_range[1]})")
top_hitters = (
    filtered_df.groupby("Player", as_index=False)
    .agg({"AVG": "max"})
    .sort_values("AVG", ascending=False)
    .head(10)
)

if not top_hitters.empty:
    bar_chart = alt.Chart(top_hitters).mark_bar().encode(
        x=alt.X("Player:N", sort="-y", title="Player"),
        y=alt.Y("AVG:Q", title="Batting Average"),
        color=alt.Color("Player:N", legend=None)
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(bar_chart, use_container_width=True)
else:
    st.info("No hitters meet the selected criteria.")

# Line chart: Best AVG per year
st.subheader("Best AVG Per Year")
top_avgs = df[df["League"].isin(league)]
top_avgs = top_avgs.groupby("Year")["AVG"].max().reset_index()
top_avgs["Year"] = top_avgs["Year"].astype(str)
st.line_chart(top_avgs.set_index("Year"))

# Bar chart: Count of players by Team (top 10 teams)
st.subheader("Most Frequent League Leaders by Team")
team_counts_df = filtered_df["Team"].value_counts().nlargest(10).reset_index()
team_counts_df.columns = ["Team", "Count"]

if not team_counts_df.empty:
    bar_chart = alt.Chart(team_counts_df).mark_bar().encode(
        x=alt.X("Team:N", sort="-y"),
        y="Count:Q",
        color="Team:N"
    )
    st.altair_chart(bar_chart, use_container_width=True)
else:
    st.info("No team data available for the selected filters.")

# Generate distinct HSL color strings for each team
def generate_hsl_colors(n):
    colors = []
    for i in range(n):
        hue = int((i * 137.508) % 360)  
        lightness = 45 + (i % 3) * 10   
        colors.append(f"hsl({hue}, 70%, {lightness}%)")
    return colors

# Prepare data
team_avg = df.groupby(["Player", "Team"], as_index=False)["AVG"].max()
team_avg_grouped = (
    team_avg.groupby("Team", as_index=False)["AVG"]
    .mean()
    .sort_values("AVG", ascending=False)
)

# Generate colors and build scale
teams = team_avg_grouped["Team"].tolist()
colors = generate_hsl_colors(len(teams))
color_scale = alt.Scale(domain=teams, range=colors)

# Build pie chart
pie_chart = alt.Chart(team_avg_grouped).mark_arc().encode(
    theta=alt.Theta(field="AVG", type="quantitative"),
    color=alt.Color(field="Team", type="nominal", scale=color_scale),
    tooltip=["Team", "AVG"]
).properties(width=600, height=600)

st.altair_chart(pie_chart, use_container_width=True)

# Table of results
st.subheader("Filtered Player Data")
display_df = filtered_df.copy()
display_df["Year"] = display_df["Year"].astype(str)
display_df["AVG"] = display_df["AVG"].round(3) 
st.dataframe(display_df)

st.markdown("Data Source: Baseball Almanac - Top League Batting Averages")
