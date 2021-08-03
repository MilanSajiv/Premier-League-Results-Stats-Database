import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

# set up a dictionary with the range of match id's that correspond to the season

years = {"pl17_18": range(22342, 22721), "pl16_17": range(14040, 14419), "pl15_16": range(12115, 12494), "pl14_15": range(9611, 9990), "pl13_14": range(9231, 9610),
         "pl12_13": range(7864, 8243), "pl11_12": range(7467, 7846)}


def season_scraper(seasons):
    season_list = []
    for match_id in seasons:  # iterates each id tag in the ranges given
        url = f'https://www.premierleague.com/match/{match_id}'
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        
         # scraping the main page of the match, if there is an error on the page, the try except method is used to skip the page
        try:
            date = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((
                By.XPATH, '//*[@id="mainContent"]/div/section/div[2]/section/div[1]/div/div[1]/div[1]'))).text
            date = datetime.strptime(date, '%a %d %b %Y').strftime('%d/%m/%Y')

            h_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]').text
            a_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]').text

            scores = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div').text
            h_goals = scores.split('-')[0]
            a_goals = scores.split('-')[1]

            stat_buttot = WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@class='tablist']//li[@data-tab-index='2']")))
            stat_button.click()
            
            dfs = pd.read_html(driver.page_source)
            stats = dfs[-1]

            driver.quit()
                
         except:
            driver.quit()
            continue
                  
        # creating dictionaries, one for all the home stats (h) and one for the away stats (a)
        h = {}
        a = {}

        home = stats[h_team]
        away = stats[a_team]
        stat_list = stats['Unnamed: 1']

        for row in zip(home, stats, away):
            stat = row[1]
            h_stats[stat] = row[0]
            a_stats[stat] = row[2]

        all_stats = ['Possession %', 'Shots on target', 'Shots', 'Touches', 'Passes', 'Tackles', 'Clearances', 'Corners', 'Offsides', 'Yellow cards', 'Red cards', 'Fouls conceded']

        for stat in all_stats:
            if stat not in h_stats.keys():
                h[stat] = 0
                a[stat] = 0

        match = [date, h_team, a_team, h_goals, a_goals, h['Possession %'], a['Possession %'], h['Shots on target'], a['Shots on target'], h['Shots'], a['Shots'], h['Touches'], a['Touches'], home['Passes'],
                 a['Passes'], h['Tackles'], a['Tackles'], h['Clearances'], a['Clearances'], h['Corners'], a['Corners'], h['Offsides'], a['Offsides'], h['Yellow cards'], a['Yellow cards'], h['Red cards'],
                 a['Red cards'], h['Fouls conceded'], a['Fouls conceded']]

        season_list.append(match)

        columns = ['Date', 'Home Team', 'Away Team', 'Home Score', 'Away Score']

        for stat in stats_check:
            columns.append(f'Home {stat}')
            columns.append(f'Away {stat}')
         
         # Writing the scraped data into a CSV file
         
        dataset = pd.DataFrame(season_list, columns=columns)
        dataset.to_csv(f'{seasons}.csv', index=False)
    print('.csv file exported.')

for matches in years.values():
    season_scraper(matches)   
