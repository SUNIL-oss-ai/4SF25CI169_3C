import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Read the Spotify dataset
df = pd.read_csv("spotify-tracks-dataset-detailed.csv")

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())


print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


#step 3
# Remove unnecessary column
df = df.drop(columns=['track_id'])

# Convert duration from milliseconds to minutes
df['duration_min'] = df['duration_ms'] / 60000

# Convert popularity to integer
df['popularity'] = df['popularity'].astype(int)

# Display transformed data
print("\nTransformed Dataset:")
print(df.head())

print("\nUpdated Dataset Shape:")
print(df.shape)

#step 4

# Check missing values before handling
print("\nMissing Values Before Imputation:")
print(df.isnull().sum())

# Fill numerical missing values with mean
numeric_columns = df.select_dtypes(include=np.number).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing text values with mode
text_columns = df.select_dtypes(include='object').columns

for col in text_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Check missing values after handling
print("\nMissing Values After Imputation:")
print(df.isnull().sum())


#step 5

# 1. Top 10 popular songs
print("\nTop 10 Popular Songs:")
print(df.nlargest(10, 'popularity')[['track_name', 'artists', 'popularity']])

# 2. Top 10 artists by average popularity
print("\nTop 10 Artists:")
print(df.groupby('artists')['popularity'].mean().sort_values(ascending=False).head(10))

# 3. Average popularity
print("\nAverage Song Popularity:")
print(df['popularity'].mean())

# 4. Average song duration
print("\nAverage Song Duration (minutes):")
print(df['duration_min'].mean())

# 5. Top 10 music genres by average popularity
print("\nTop 10 Popular Genres:")
print(df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10))

# 6. Average danceability and energy
print("\nAverage Danceability:")
print(df['danceability'].mean())

print("\nAverage Energy:")
print(df['energy'].mean())



# STEP 6: DATA VISUALIZATION

# 1. Bar Chart – Top 10 Popular Songs
top_songs = df.nlargest(10, 'popularity')

plt.figure(figsize=(12, 6))
sns.barplot(data=top_songs, x='popularity', y='track_name')
plt.title("Top 10 Popular Songs")
plt.xlabel("Popularity")
plt.ylabel("Song Name")
plt.tight_layout()
plt.savefig("chart1.png")
plt.show()
plt.close()


# 2. Histogram – Song Popularity Distribution
plt.figure(figsize=(8, 5))
plt.hist(df['popularity'], bins=20)
plt.title("Song Popularity Distribution")
plt.xlabel("Popularity")
plt.ylabel("Number of Songs")
plt.tight_layout()
plt.savefig("chart2.png")
plt.show()
plt.close()


# 3. Scatter Plot – Danceability vs Popularity
plt.figure(figsize=(8, 5))
plt.scatter(df['danceability'], df['popularity'], alpha=0.3)
plt.title("Danceability vs Popularity")
plt.xlabel("Danceability")
plt.ylabel("Popularity")
plt.tight_layout()
plt.savefig("chart3.png")
plt.show()
plt.close()


# 4. Bar Chart – Top 10 Popular Music Genres
top_genres = df.groupby('track_genre')['popularity'].mean().nlargest(10)

plt.figure(figsize=(10, 5))
top_genres.plot(kind='bar')
plt.title("Top 10 Popular Music Genres")
plt.xlabel("Genre")
plt.ylabel("Average Popularity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart4.png")
plt.show()
plt.close()

print("All 4 charts saved successfully!")
