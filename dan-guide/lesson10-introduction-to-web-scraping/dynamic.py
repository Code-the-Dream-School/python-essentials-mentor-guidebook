import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# URL to scrape
url = "http://10.27.27.12:3000/dynamic"

print("=" * 50)
print("SCRAPING DYNAMIC CONTENT WITHOUT WAITING")
print("=" * 50)

# METHOD 1: Using requests (won't execute JavaScript)
print("\n1. USING REQUESTS:")
response = requests.get(url)
print(f"Status code: {response.status_code}")

# Try to find the dynamic content in the requests response
if 'id="dynamic-content"' in response.text:
    # Extract content between the dynamic-content tags using simple string operations
    start_idx = response.text.find('id="dynamic-content"')
    content_start = response.text.find('>', start_idx) + 1
    content_end = response.text.find('</p>', content_start)
    content = response.text[content_start:content_end].strip()
    print(f"Dynamic content from requests: {content}")
else:
    print("Couldn't find dynamic content element in the HTML")

# METHOD 2: Using Selenium without waiting
print("\n2. USING SELENIUM WITHOUT WAITING:")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the page and immediately check the content
driver.get(url)

# Try to extract just the dynamic content without waiting
try:
    dynamic_content = driver.find_element(By.ID, "dynamic-content")
    print(f"Dynamic content from Selenium: {dynamic_content.text}")
except Exception as e:
    print(f"Error finding dynamic content: {e}")

# Close the browser
driver.quit()

print("\n" + "=" * 50)
print("RESULT: Both methods show 'Loading data...' instead of API data")
print("because they don't wait for JavaScript to execute and API calls to complete.")
print("=" * 50)