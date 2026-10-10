
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data.csv")

# Display the first five rows
print("First five rows:")
print(df.head())

# Display dataset dimensions
print("\nDataset shape:")
print(df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check column data types
print("\nColumn information:")
print(df.info())

# Display rows with missing values
print("\nRows containing missing values:")
print(df[df.isnull().any(axis=1)])


# Step 8: Handle missing values

# Find the median of the available calorie values
calorie_median = df["Calories"].median()

print("Median Calories:", calorie_median)

# Fill missing Calories with the median
df["Calories"] = df["Calories"].fillna(calorie_median)

# Check missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Display the previously affected rows
print("\nUpdated rows:")
print(df.loc[[18, 22, 28]])


# Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Display duplicate rows, if any
print("\nDuplicate records:")
print(df[df.duplicated()])


# Step 10: Remove duplicate rows

df = df.drop_duplicates().copy()

print("\nDataset after removing duplicates:")
print("Total rows:", len(df))

print("\nRemaining duplicates:")
print(df.duplicated().sum())


# Step 11: Clean the Date column

# Remove quotation marks
df["Date"] = df["Date"].str.replace("'", "", regex=False)

# Convert text into datetime
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%Y/%m/%d",
    errors="coerce"
)

print("\nDates after formatting:")
print(df[["Date"]].head(10))

print("\nMissing dates:")
print(df["Date"].isnull().sum())


# Step 12: Inspect Duration values

print("\nDuration statistics:")
print(df["Duration"].describe())

print("\nRows with Duration above 120:")
print(df[df["Duration"] > 120])


# Display rows with missing or invalid dates
print("\nRows with missing or invalid dates:")
print(df[df["Date"].isna()])

# Compare with the original CSV values
original_df = pd.read_csv("data.csv")

print("\nOriginal date values for these rows:")
print(
    original_df.loc[
        df.index[df["Date"].isna()],
        ["Date", "Duration", "Pulse", "Maxpulse", "Calories"]
    ]
)


print("\nUnusual duration record:")
print(df[df["Duration"] == 450])


import pandas as pd

# Reload the original CSV to restore the date text
df = pd.read_csv("data.csv")

# Fill missing Calories with the median
df["Calories"] = df["Calories"].fillna(
    df["Calories"].median()
)

# Remove duplicate rows
df = df.drop_duplicates().copy()

# Clean the Date column
df["Date"] = (
    df["Date"]
    .astype("string")
    .str.strip()
    .str.replace("'", "", regex=False)
)

# Convert dates in YYYY/MM/DD format
dates1 = pd.to_datetime(
    df["Date"],
    format="%Y/%m/%d",
    errors="coerce"
)

# Convert dates in YYYYMMDD format
dates2 = pd.to_datetime(
    df["Date"],
    format="%Y%m%d",
    errors="coerce"
)

# Combine both date formats
df["Date"] = dates1.fillna(dates2)

# Display results
print("Missing dates:", df["Date"].isna().sum())

print("\nCorrected row 26:")
print(df.loc[[26], ["Date"]])

print("\nRows with missing dates:")
print(df[df["Date"].isna()])


# Check duration values
print("\nDuration statistics:")
print(df["Duration"].describe())

# Find unusually long sessions
print("\nSessions longer than 120 minutes:")
print(df[df["Duration"] > 120])


# Create a new column
df["Calories_Per_Minute"] = (
    df["Calories"] / df["Duration"]
)

print("\nDataset with the new column:")
print(
    df[["Duration", "Calories", "Calories_Per_Minute"]].head()
)


# Filter sessions lasting at least 60 minutes
long_sessions = df[df["Duration"] >= 60]

print("\nSessions lasting at least 60 minutes:")
print(long_sessions.head())

print("\nNumber of matching sessions:", len(long_sessions))


import matplotlib.pyplot as plt
import seaborn as sns

# Calculate average calories for each duration
avg_calories = df.groupby("Duration")["Calories"].mean()

# Create bar chart
avg_calories.plot(kind="bar", figsize=(8, 5))

plt.title("Average Calories by Exercise Duration")
plt.xlabel("Duration (minutes)")
plt.ylabel("Average Calories")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Scatter plot using Seaborn
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Duration",
    y="Calories"
)

plt.title("Exercise Duration vs Calories Burned")
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories")
plt.tight_layout()
plt.show()


# Save the cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final dataset shape:", df.shape)
print("\nFinal missing values:")
print(df.isnull().sum())
