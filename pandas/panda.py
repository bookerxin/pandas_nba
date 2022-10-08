
import pandas as pd
import numpy as np

# - Functions

# Height format function into inches
def height_to_inches(x):
    try:
        feet, inches = x.split('-')
        inches = float(feet)*12 + float(inches) # Convert feet into inches
        return inches
    except:
        pass
    

# - Formatting

# Read in data
data = pd.read_csv('data/nba.csv')

# Replace all null values with a 0
desc = data.fillna('0')

# Make new dataframe with team, age and height. Sorted by Team alphabetically
desc = desc[['Team', 'Age', 'Height']].sort_values(by='Team')

# Applying the height format function to the height column
desc['Height'] = desc['Height'].apply(height_to_inches, 1)

# Works but because of replacing nan with 0 we now have a zero at the start
teams = { key:{'age': 0, 'height': 0} for key in desc.Team.unique() }
teams.pop('0')

# - Data organisation and final reports

# Where the final reports go
reports = np.array([])

report = pd.DataFrame({'Team': [], 'Mean Age': [], 'Median Age': [], 'Mean Height': [], 'Median Height': []})

# Cycle through each unique team name, getting each teams data and saving the ages and heights in dict
for team in teams:

    # Get all data of the team
    team_data = desc.loc[desc['Team'] == team]

    # Get all ages and heights for that team and make into arrays
    team_ages = team_data['Age'].to_numpy()
    team_heights = team_data['Height'].to_numpy()

    # Now add the corrosponding data to the dictionary
    teams[team]['age'] = team_ages
    teams[team]['height'] = team_heights

    team_age_mean = round(np.mean(teams[team]['age']))
    team_age_median = np.median(teams[team]['age'])

    team_height_mean = round(np.mean(teams[team]['height']))
    team_height_median = np.median(teams[team]['height'])

    # Add values to reports dataframe with final results
    report.loc[len(report.index)] = [team, team_age_mean, team_age_median, team_height_mean, team_height_median]

print(report)

# print(*reports)



