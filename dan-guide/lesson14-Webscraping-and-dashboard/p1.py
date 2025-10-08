from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

options = Options()
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0")

try:
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.baseball-almanac.com/hitting/hibavg3.shtml")

    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    rows = table.find_elements(By.TAG_NAME, "tr")[1:]

    data = []
    for row in rows:
        try:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 8:
                year_al = cells[0].text.strip()
                player_al = cells[1].text.strip()
                avg_al = cells[2].text.strip().split()[0]
                team_al = cells[3].text.strip()

                year_nl = cells[4].text.strip()
                player_nl = cells[5].text.strip()
                avg_nl = cells[6].text.strip().split()[0]
                team_nl = cells[7].text.strip()

                data.append([year_al, "AL", player_al, team_al, avg_al])
                data.append([year_nl, "NL", player_nl, team_nl, avg_nl])
        except Exception as row_err:
            print(f"Error parsing row: {row_err}")
finally:
    driver.quit()

try:
    df = pd.DataFrame(data, columns=["Year", "League", "Player", "Team", "AVG"])
    df.to_csv("batting_avg_league_leaders.csv", index=False)
    print("Saved batting_avg_league_leaders.csv")
except Exception as file_err:
    print(f"Error writing CSV: {file_err}")
