from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser
driver = webdriver.Safari()

# Open the webpage
driver.get("https://markstats.club/laliga-players-22-23/")

# Wait for the table element to be present and find the player data
wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.XPATH, '//table[@class="ninja_footable foo_table_1023"]')))
player_data = table.find_elements_by_xpath('.//td')

# Extract the data
for element in player_data:
    print(element.text)

# Close the browser
driver.quit()
