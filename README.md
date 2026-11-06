# 4SF25CI169_3C
Spotify music data analysis using Python, Pandas, NumPy, and data visualization.
# Spotify Data Analysis using Python and Pandas

## Project Description
This project focuses on analyzing a Spotify music dataset using Python and Pandas. The dataset contains information about songs, artists, albums, popularity, duration, danceability, energy, tempo, and music genres.

The main objective is to perform data transformation, handle missing values, generate useful insights, and visualize the results.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code

## Dataset
**Dataset Name:** Spotify Tracks Dataset Detailed

The dataset contains 114,000 rows and 20 columns.

## Tasks Performed

### 1. Data Loading
- Imported the Spotify CSV dataset using Pandas.
- Displayed the first five rows.

### 2. Data Understanding
- Checked dataset shape and column names.
- Examined data types and statistical summaries.

### 3. Data Transformation
- Removed the unnecessary track ID column.
- Converted song duration from milliseconds to minutes.
- Converted popularity values into integers.

### 4. Missing Value Handling
- Identified missing values.
- Used mean imputation for numerical columns wherever required.
- Used mode imputation for missing text values.
- Verified missing values after handling.

### 5. Insight Generation
- Identified the top 10 popular songs.
- Found the top 10 artists by average popularity.
- Calculated average song popularity.
- Calculated average song duration.
- Identified the top 10 popular music genres.
- Calculated average danceability and energy.

### 6. Data Visualization
Created four visualizations:
1. Top 10 Popular Songs – Bar Chart
2. Song Popularity Distribution – Histogram
3. Danceability vs Popularity – Scatter Plot
4. Top 10 Popular Music Genres – Bar Chart

## Project Files
- `main.py` – Python code for data analysis and visualization.
- `spotify-tracks-dataset-detailed.csv` – Spotify dataset.
- `chart1.png` – Top 10 popular songs.
- `chart2.png` – Song popularity distribution.
- `chart3.png` – Danceability vs popularity.
- `chart4.png` – Top 10 popular music genres.

## Conclusion
This project demonstrates how Python and Pandas can be used to analyze real-world music data. Data transformation, missing value handling, insight generation, and visualization help understand Spotify music trends and characteristics.
