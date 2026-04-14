import pandas as pd
matches= pd.read_csv("matches.csv")
deliveries= pd.read_csv("deliveries.csv")

df1=pd.DataFrame(matches)
df2=pd.DataFrame(deliveries)

print(df1.head(5))
df1["date"]=pd.to_datetime(df1["date"])
# df1.info()
df1.dropna(subset=["city"],inplace=True)
df1.dropna(subset=["winner"],inplace=True)
df1.drop("umpire3",axis=1,inplace=True)
print(df1)
df1.info()
# Workdone=Drop null values of city and winner column
# Completely drop the 3rd umpire column




print(df2)
df2.info()

merged = deliveries.merge(matches, left_on="match_id", right_on="id", how="inner")
print(merged.head(25))



# merged table, so we can use according to the requirements^^^^^

# 3. Match‑Level Analysis.>>>>>>>>>>>..>>>>>>>>>>>>>>>>>>>>...>>>>>>>>
#1. Total matches per season:
#2. Most successful teams:
#3. Toss decision distribution:
#4. Venue analysis:

print(df1.groupby("season")['id'].count().sort_values(ascending=False))
# Maximum matches played in the year 2013,2012 and the lowest matches played in year 2015, 2014

print(df1.groupby("winner")["id"].count().sort_values(ascending=False).head(2))
print(df1.groupby("winner")["id"].count().sort_values(ascending=False).tail(2))
# Team with maximum win is Mumbai Indians followed by Chennai super kings
# Rising Pune Supergiant performed worst followed by Kochi_Tuskers_Kerala


print(df1.groupby("toss_decision")["winner"].count())
print(df1["venue"].value_counts().head(2))
print(df1["venue"].value_counts().tail(2))
#Maxium matches have been played in M Chinnaswamy Stadium followed by Eden gardens
#Minimum matches had been played in OUTsurance Oval followed by Vidarbha Cricket Association Stadium, Jamtha

print("----------------------------------------------------------------------------------------------")

# Player‑Level Analysis (Deliveries)
# Top run scorers:
# Baller Conceded most runs:
# Man of the match count

topscorer=df2.groupby("batsman")["batsman_runs"].sum().sort_values(ascending=False)
# topplayers=SK Raina,V kohli, RG Sharma

visualoftopscorer=df2.groupby("batsman")["total_runs"].sum().sort_values(ascending=False).head(7)
# for visualisation of top scorers in last 

print(df2.groupby("batsman")["total_runs"].sum().sort_values(ascending=False).head(10))
# Top players by all runs(including extras)= SK Raina,V Kohli, G Gambhir



bowler_runs = (
    df2.groupby("bowler")["batsman_runs"].sum() +
    df2.groupby("bowler")["extra_runs"].sum()
).sort_values(ascending=False)

print(bowler_runs.head(10))
# Harbhajan Singh, P kumar, Pp Chawla

mom = df1["player_of_match"].value_counts().head(10)
print(mom)
# CH Gayle, YK pathan,DA Warner


print("-----------------------------------------------------------------------------------")
import numpy as np
#Advanced Pandas Concepts
#1. Pivot table: Average runs per team per season
# df1.groupby(["winner","season"])["total"]


df1["big_win"] = np.where(df1["win_by_runs"]>50, "Yes", "No")
# print(df1)


# 2. Top 2 team performed by season

team_season = df1.groupby(["season", "winner"])["id"].count().reset_index(name="wins")

top2_per_season = team_season.sort_values(["season", "wins"], ascending=[True, False]).groupby("season").head(2)

print(top2_per_season)

# 3.  Toss Winner vs Match Winner

df1["toss_match_win"] = df1["toss_winner"] == df1["winner"]

print(df1["toss_match_win"].value_counts())


print("---------------------------------------------------------------------------------------")
# Visualization (Matplotlib)

# Bar chart of top scorers
# Line chart of team wins across seasons
import matplotlib.pyplot as plt



top_scorers = df2.groupby("batsman")["total_runs"].sum().sort_values(ascending=False).head(10)
print(top_scorers)
plt.figure(figsize=(6,5))
top_scorers.plot(kind="bar", color="skyblue")
plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Batsman")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.show()





matches_per_season = df1.groupby("season")["id"].count()

plt.figure(figsize=(6,5))
matches_per_season.plot(kind="bar")
plt.title("Matches per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.xticks(rotation=45)
plt.show()






top_teams = df1["winner"].value_counts().head(5)
print(top_teams)

plt.figure(figsize=(6,5))
top_teams.plot(kind="bar")
plt.title("Top 5 Teams by Wins")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.xticks(rotation=35)
plt.show()





topvenues=df1["venue"].value_counts().head(7)
print(topvenues)
plt.figure(figsize=(6,5))
topvenues.plot(kind="bar",color="lightgreen")
plt.title("Top 7 Venues")
plt.ylabel("Matches")
plt.xlabel("Venue")
plt.show()


plt.figure(figsize=(6,5))
visualoftopscorer.plot(kind="bar",color="lightcoral")
plt.title("Top 7 Run Scorers")
plt.xlabel("Batsman")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.show()





topwinmarginbyrun=df1.groupby("winner")["win_by_runs"].max().sort_values(ascending=False).head(7)
print(topwinmarginbyrun)
plt.figure(figsize=(6,5))
topwinmarginbyrun.plot(kind="bar",color="k")
plt.title("Top teams based on winning margin by runs")
plt.xlabel("Team")
plt.ylabel("Margin")
plt.xticks(rotation=45)
plt.show()

topwinmarginbywic=df1.groupby("winner")["win_by_wickets"].max().sort_values(ascending=False).head(7)
print(topwinmarginbywic)
# topwinmarginbyrun.plot(kind="bar",color="brown")
# plt.title("Top teams based on winning margin")
# plt.xlabel("Team")
# plt.ylabel("Margin")
# plt.show()


# What we have calculated:>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Maximum matches played in the year 2013,2012 and the lowest matches played in year 2015, 2014
# Team with maximum win is Mumbai Indians followed by Chennai super kings
# Rising Pune Supergiant performed worst followed by Kochi_Tuskers_Kerala
# Maxium matches have been played in M Chinnaswamy Stadium followed by Eden gardens
# Minimum matches had been played in OUTsurance Oval followed by Vidarbha Cricket Association Stadium, Jamtha
# topplayers=SK Raina,V kohli, RG Sharma
# Top players by all runs(including extras)= SK Raina,V Kohli, G Gambhir
# Bowlers who conceded most runs = Harbhajan Singh, P Kumar, PP Chawla
#  Top 3 venues in terms of matches hosted= M Chinnaswamy Stadium, Eden gardens, Feroz Shah Kotla
# top teams by wins= Mumbai Indians, Kolkata Knight Riders,Chennai super kings, Royal Challengers Bangalore,KingsX1 Punjab


# Visualization of top scorers,matches per season, top teams by wins, matches per season, top venues, top run scorers