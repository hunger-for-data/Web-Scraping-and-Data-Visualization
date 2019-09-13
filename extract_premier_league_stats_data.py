#!/bin/python
"""
The data is extracted from offical premier league website (https://www.premierleague.com) with the help
of python library called Beautifulsoup and then stored in CSV format.

Exloratory Data Anaysis is then formed on this data with Tableau Public and visualization are 
stored in Tableau Cloud.

Data Visulaization with Tableau Public can be viewed in below URL :
https://public.tableau.com/profile/vipin.ragashetti#!/vizhome/ExporatoryDataAnalysisforEnglishPremierLeagueClubs/Dashboard-PLAnalysis
"""

__author__ = "Vipin Ragashetti"
__version__ = "1.0.1"
__maintainer__ = "Vipin Ragashetti"
__email__ = "vipin.ragashetti@gmail.com"
__credits__ = ["https://www.premierleague.com"]

from bs4 import BeautifulSoup as soup 
import requests, csv, time

file_name = "premier_league_%s" % int(time.time()) + ".csv"
premier_league_url = "https://www.premierleague.com"
club_names = [
         "/clubs/1/Arsenal/stats", "/clubs/2/Aston-Villa/stats", 
         "/clubs/127/Bournemouth/stats", "/clubs/131/Brighton-and-Hove-Albion/stats", 
         "/clubs/43/Burnley/stats", "/clubs/4/Chelsea/stats", 
         "/clubs/6/Crystal-Palace/stats", "/clubs/7/Everton/stats", 
         "/clubs/26/Leicester-City/stats", "/clubs/10/Liverpool/stats", 
         "/clubs/11/Manchester-City/stats", "/clubs/12/Manchester-United/stats",
         "/clubs/23/Newcastle-United/stats", "/clubs/14/Norwich-City/stats",
         "/clubs/18/Sheffield-United/stats", "/clubs/20/Southampton/stats",
         "/clubs/21/Tottenham-Hotspur/stats", "/clubs/33/Watford/stats",
         "/clubs/25/West-Ham-United/stats", "/clubs/38/Wolverhampton-Wanderers/stats"
         ]

# Fetch the webpage www.premierleague.com/clubs for scrapping
overall_data = []
for club_name in club_names:
    overall_data.append(requests.get(premier_league_url+club_name))

# Fetch the content from webpages with BeautifulSoup
soup_clubs_data = []
for item in overall_data:
    soup_clubs_data.append(soup(item.content, "html.parser"))

headers = ["team", "offical_website", "matches_played", "total_wins", "total_loses", "total_goals", 
           "goals_conceded", "clean_sheets", "goals_per_match", "shooting_accuracy", "total_passes", "pass_accuracy",
           "own_goals", "errors_leading_to_goal", "yellow_cards", "red_cards"]

with open(file_name, 'ab') as csv_file:
    writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    writer.writerow(headers)

for soup_club in soup_clubs_data:
    team = soup_club.find_all("h1", {"class": "team js-team"})[0].text.strip()
    website = soup_club.find_all("div", {"class": "website"})[0].text.split(":")[1].strip()
    total_matches_played = soup_club.find_all("span", {"class": "allStatContainer statmatches_played"})[0].text.replace(",", "").strip()
    total_wins = soup_club.find_all("span", {"class": "allStatContainer statwins"})[0].text.replace(",", "").strip()
    total_losses = soup_club.find_all("span", {"class": "allStatContainer statlosses"})[0].text.replace(",", "").strip()
    total_goals = soup_club.find_all("span", {"class": "allStatContainer statgoals"})[0].text.replace(",", "").strip()
    goals_conceded = soup_club.find_all("span", {"class": "allStatContainer statgoals_conceded"})[0].text.replace(",", "").strip()
    clean_sheets = soup_club.find_all("span", {"class": "allStatContainer statclean_sheet"})[0].text.strip()
    goals_per_match = soup_club.find_all("span", {"class": "allStatContainer statgoals_per_game"})[0].text.replace(",", "").strip()
    shooting_accuracy = soup_club.find_all("span", {"class": "allStatContainer statshot_accuracy"})[0].text.replace("%", "").strip()
    total_passes =  soup_club.find_all("span", {"class": "allStatContainer stattotal_pass_per_game"})[0].text.replace("%", "").strip()
    pass_accuracy = soup_club.find_all("span", {"class": "allStatContainer statpass_accuracy"})[0].text.replace("%", "").strip()
    own_goals = soup_club.find_all("span", {"class": "allStatContainer statown_goals"})[0].text.replace(",", "").strip()
    errors_leading_to_goal = soup_club.find_all("span", {"class": "allStatContainer staterror_lead_to_goal"})[0].text.strip()
    yellow_cards = soup_club.find_all("span", {"class": "allStatContainer statyellow_card"})[0].text.replace(",", "").strip()
    red_cards = soup_club.find_all("span", {"class": "allStatContainer statred_card"})[0].text.replace(",", "").strip()
    final_list = [team, website, total_matches_played, total_wins, total_losses, total_goals, goals_conceded, clean_sheets,
                  goals_per_match, shooting_accuracy, total_passes, pass_accuracy, own_goals, errors_leading_to_goal, yellow_cards, red_cards]
    
    with open(file_name, 'ab') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(final_list)



