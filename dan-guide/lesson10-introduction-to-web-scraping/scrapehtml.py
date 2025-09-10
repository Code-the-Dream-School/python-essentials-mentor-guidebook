from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This line creates and returns a Chrome WebDriver instance
# - webdriver.Chrome(): Creates a new Chrome browser session
# - Service(ChromeDriverManager().install()): 
#   ChromeDriverManager().install() downloads the appropriate ChromeDriver for your Chrome version
#   Service() configures the ChromeDriver to work with Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the local webpage - this sends an HTTP GET request to the specified URL
print("Opening webpage...")
driver.get("http://10.27.27.12:3000/html")

# Wait for the page to load - wait up to 10 seconds for the body element to appear
print("Waiting for page to load...")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

print(f"Page title: {driver.title}")

# Find and print information about div elements
print("\n--- Div Elements ---")
divs = driver.find_elements(By.TAG_NAME, "div")
print(f"Found {len(divs)} div elements")
# Show the first div's HTML
if divs:
    print(f"First div HTML: {divs[0].get_attribute('outerHTML')}")

# Find a div with class "container" (if it exists)
try:
    container = driver.find_element(By.CLASS_NAME, "container")
    print("\n--- Container Element ---")
    print(f"Container text: {container.text[:100]}...")  # Print first 100 chars
except:
    print("\nNo container element found")

# Find and print info about images
print("\n--- Images ---")
images = driver.find_elements(By.TAG_NAME, "img")
print(f"Found {len(images)} images")
for i, img in enumerate(images):
    src = img.get_attribute("src")
    alt = img.get_attribute("alt")
    print(f"Image {i+1}: src='{src}', alt='{alt}'")

# Find and print info about links
print("\n--- Links ---")
links = driver.find_elements(By.TAG_NAME, "a")
print(f"Found {len(links)} links")
for i, link in enumerate(links):
    href = link.get_attribute("href")
    text = link.text
    print(f"Link {i+1}: href='{href}', text='{text}'")

# Find and print info about buttons
print("\n--- Buttons ---")
buttons = driver.find_elements(By.TAG_NAME, "button")
print(f"Found {len(buttons)} buttons")
for i, button in enumerate(buttons):
    print(f"Button {i+1} text: '{button.text}'")

# Find and print info about list items
print("\n--- List Items ---")
list_items = driver.find_elements(By.TAG_NAME, "li")
print(f"Found {len(list_items)} list items")
for i, item in enumerate(list_items[:3], 1):  # Show first 3 only
    print(f"List item {i}: '{item.text[:50]}...'")  # First 50 chars of each
if len(list_items) > 3:
    print(f"... and {len(list_items) - 3} more list items")

# Finding elements by CSS selector (Example using class selector)
print("\n--- Finding by CSS Selector ---")
pre_elements = driver.find_elements(By.CSS_SELECTOR, "pre.bg-gray-800")
print(f"Found {len(pre_elements)} code blocks with class 'bg-gray-800'")
if pre_elements:
    print(f"First code block contains: '{pre_elements[0].text[:50]}...'")

# Always close the driver when done
print("\nClosing the browser...")
driver.quit()