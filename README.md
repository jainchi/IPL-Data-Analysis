# 🏏 IPL Data Analysis using Python

## 📌 Overview

This project performs an in-depth analysis of the Indian Premier League (IPL) dataset using Python.
The objective is to extract meaningful insights related to team performance, player statistics, and match outcomes.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**

---

## 📂 Dataset

The analysis is based on two datasets:

* `matches.csv` → Match-level data (teams, results, venue, toss, etc.)
* `deliveries.csv` → Ball-by-ball data (runs, batsman, bowler, etc.)

---

## ⚙️ Data Preprocessing

* Converted date column to datetime format
* Handled missing values in key columns (`city`, `winner`)
* Removed irrelevant column (`umpire3`)
* Merged datasets for combined analysis when required

---

## 📊 Key Analysis Performed

### 🔹 Match-Level Analysis

* Total matches played per season
* Most successful teams based on total wins
* Toss decision distribution (bat vs field)
* Venue-wise match distribution

---

### 🔹 Player-Level Analysis

* Top batsmen based on total runs scored
* Bowlers who conceded the most runs
* Most “Player of the Match” awards

---

### 🔹 Advanced Analysis

* Top 2 teams per season based on wins
* Toss winner vs match winner comparison
* Win margin analysis:

  * Highest win by runs (team-wise)
  * Highest win by wickets (team-wise)
* Feature engineering:

  * Created `big_win` flag for matches won by large margins

---

## 📈 Key Insights

* **Mumbai Indians** emerged as the most successful team overall
* Toss has **minimal impact** on match outcome (~50-50 win ratio)
* **M. Chinnaswamy Stadium** hosted the highest number of matches
* Top performers include:

  * **Batsmen**: Suresh Raina, Virat Kohli, Rohit Sharma
  * **Bowlers (runs conceded)**: Harbhajan Singh, Praveen Kumar, Piyush Chawla
* Certain teams consistently dominate specific seasons

---

## 📊 Visualizations

The project includes multiple visualizations:

* Top batsmen (bar chart)
* Matches per season
* Top teams by wins
* Venue distribution
* Top win margins (runs & wickets)

---

## 🧠 Learning Outcomes

* Applied real-world data cleaning techniques
* Strengthened understanding of `groupby`, aggregation, and ranking
* Performed multi-level analysis using structured datasets
* Developed ability to derive business insights from raw data

---

## 🚀 Conclusion

This project demonstrates the ability to handle structured datasets, perform exploratory data analysis, and communicate insights effectively using Python.

---

## 🔗 GitHub Repository

[https://github.com/jainchi/IPL-Data-Analysis]
