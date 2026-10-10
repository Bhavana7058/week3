## Project Overview
This project focuses on data cleaning, manipulation, analysis, and visualization using Python. The dataset contains exercise-related information, including duration, date, pulse rate, maximum pulse rate, and calories burned.

## Objectives
- Understand Python data structures and basic scripting.
- Load and inspect datasets using Pandas.
- Identify and handle missing values.
- Detect and remove duplicate records.
- Standardize date formats and inspect unusual values.
- Filter data and create new columns.
- Visualize data using Matplotlib and Seaborn.

## Technologies Used
- **Python 3**
- **Pandas** – Data manipulation and cleaning
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Visual Studio Code** – Development environment

## Dataset Description
The dataset contains the following columns:

| Column | Description |
|---|---|
| Duration | Exercise duration in minutes |
| Date | Date of the exercise |
| Pulse | Pulse rate |
| Maxpulse | Maximum pulse rate |
| Calories | Calories burned |

## Data Cleaning and Processing
The following operations were performed:
1. Loaded the CSV dataset using Pandas.
2. Inspected dataset dimensions, column types, and missing values.
3. Filled missing calorie values using the median.
4. Identified and removed duplicate records.
5. Standardized date formats and identified missing dates.
6. Investigated unusually large duration values.
7. Created a `Calories_Per_Minute` column.
8. Filtered sessions with a duration of at least 60 minutes.

## Data Visualization
The project includes:
- **Bar Chart:** Average calories burned by exercise duration.
- **Scatter Plot:** Relationship between exercise duration and calories burned.

## Project Files
- `data.csv` – Original dataset.
- `datawrangling.py` – Python source code.
- `cleaned_data.csv` – Processed dataset.
- `average_calories.png` – Bar chart.
- `duration_vs_calories.png` – Scatter plot.

## How to Run
1. Install Python 3.
2. Install the required libraries:

   ```bash
   python -m pip install pandas matplotlib seaborn
   ```

3. Place the dataset and Python script in the same folder.
4. Run the script:

   ```bash
   python datawrangling.py
   ```

## Key Learnings
- Working with Pandas DataFrames.
- Handling missing values and duplicate records.
- Converting text into date formats.
- Filtering data and creating calculated columns.
- Generating charts to explore data patterns.

## Conclusion
This project demonstrates fundamental Python data-wrangling techniques and introductory data visualization skills that can be applied to real-world datasets.
