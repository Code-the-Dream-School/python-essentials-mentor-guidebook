import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #stands for expected conditions.

# URL to scrape
url = "http://10.27.27.12:3000/dynamic"

print("=" * 50)
print("SCRAPING DYNAMIC CONTENT WITH PROPER WAITING")
print("=" * 50)

# Initialize Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the page
driver.get(url)

print("\nInitial content (no waiting):")
try:
    # Get content immediately
    dynamic_content = driver.find_element(By.ID, "dynamic-content")
    print(f"Content: {dynamic_content.text}")
except Exception as e:
    print(f"Error: {e}")

print("\nWaiting for dynamic content to update...")

# METHOD 1: Simple time-based waiting
time.sleep(2)  # Wait for 2 seconds
print("\n1. AFTER TIME-BASED WAITING:")
dynamic_content = driver.find_element(By.ID, "dynamic-content")
print(f"Content: {dynamic_content.text}")

# Refresh page to start fresh
driver.refresh()

# METHOD 2: Explicit waiting with condition
print("\n2. USING EXPLICIT WAIT:")
# Wait until text changes from "Loading data..."
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
wait.until(lambda d: d.find_element(By.ID, "dynamic-content").text != "Loading data...")
#! wait.until(EC.text_to_be_present_in_element((By.ID, "dynamic-content"), "Loaded"))  # Example: waits for the text to be "Loaded"
dynamic_content = driver.find_element(By.ID, "dynamic-content")
print(f"Content: {dynamic_content.text}")

# Close the browser
driver.quit()

print("\n" + "=" * 50)
print("RESULT: Proper waiting allows capture of dynamic content")
print("loaded via JavaScript and API calls.")
print("=" * 50)