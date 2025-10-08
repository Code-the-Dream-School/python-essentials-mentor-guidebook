import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path


# Setup Chrome WebDriver with debugging
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')  # Disable GPU for performance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Define base URL
url = "http://10.27.27.12:3000/pagination?page=1"

# Open the homepage
driver.get(url)

# Wait until the page is fully loaded using expected conditions
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# Prepare CSV file and write header
output_dir = Path(__file__).resolve().parent / "wk10_z_csv"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "scraped_data.csv"
with output_file.open(mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Price", "BD", "BA", "SQFT", "Address", "City", "State", "Zip", "ImageUrl", "Description", "Info"])

    # Scrape each page
    total_scraped = 0
    page_number = 1
    last_scraped_page = 0  # Start from page 0

    while True:
        # Track the current page at the start of the loop
        current_page = int(driver.find_element(By.CSS_SELECTOR, "h2.text-3xl.font-semibold").text.split()[-1])

        # Check if the current page is the same as the last scraped page
        if current_page == last_scraped_page:
            print("No more pages available.")
            break  # No more pages, break the loop

        print(f"Scraping page {page_number}...")

        # Wait for items to load on the page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".grid .bg-white"))
        )

        # Get all listing items
        items = driver.find_elements(By.CSS_SELECTOR, "li.bg-white")
        print(f"Found {len(items)} listings on page {page_number}")

        # Loop through each item and extract the necessary data
        for item in items:
            try:
                # Extract Price
                price = item.find_element(By.CSS_SELECTOR, ".text-gray-800 b").text if item.find_elements(By.CSS_SELECTOR, ".text-gray-800 b") else ""
                # print(price)

                # Extract BD, BA, SQFT - Look for the text containing "beds", "baths", and "sqft"
                bed_bath_sqft = item.find_element(By.XPATH, "//span[contains(text(),'beds')]").text if item.find_elements(By.XPATH, "//span[contains(text(),'beds')]") else ""
                # print(bed_bath_sqft)

                # Extract the individual parts of "4 beds / 4 baths / 2,156 sqft"
                bd, ba, sqft = "", "", ""
                if bed_bath_sqft:
                    parts = bed_bath_sqft.split(" / ")
                    # print(parts)
                    # print(len(parts))
                    if len(parts) == 3:
                        bd, ba, sqft = parts[0], parts[1], parts[2]
                    else:
                        print(f"Unexpected format for Listing {price} - skipping item")
                        continue  # Skip this item if format is unexpected

                # Extract address and split into city, state, zip
                full_address = item.find_element(By.CSS_SELECTOR, "address").text if item.find_elements(By.CSS_SELECTOR, "address") else ""
                # print(full_address)
                city, state_zip = "", ""
                if full_address:
                    address, city, state_zip = full_address.split(", ") if "," in full_address else ("", "")
                state, zip_code = "", ""
                if state_zip:
                    state, zip_code = state_zip.split(" ") if " " in state_zip else ("", "")

                # Image URL (use fallback if image is not available)
                image_url = item.find_element(By.TAG_NAME, "img").get_attribute("src") if item.find_elements(By.TAG_NAME, "img") else ""

                # Description
                description = item.find_element(By.CSS_SELECTOR, "p.text-sm").text if item.find_elements(By.CSS_SELECTOR, "p.text-sm") else ""

                # Info (all <ul> items concatenated)
                info_items = item.find_elements(By.CSS_SELECTOR, "ul.list-disc li")
                info = "\n".join([li.text for li in info_items]) if info_items else ""

                # Write the data to the CSV
                writer.writerow([price, bd, ba, sqft, full_address, city, state, zip_code, image_url, description, info])

                total_scraped += 1
            except Exception as e:
                print(f"Error scraping item: {e}")
                print(f"Unexpected format for Listing {price}")

        # Update the last_scraped_page to the current page after scraping
        last_scraped_page = current_page

        # Check if the next page exists
        try:
            # Wait for the "Next" button to be clickable by inner text instead of aria-label
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))
            )
            # Check if the button is disabled (end of pages)
            if 'disabled' in next_button.get_attribute('class'):
                print("No more pages available.")
                break  # No more pages
            else:
                next_button.click()  # Click to next page
                time.sleep(2)  # Wait for the next page to load
                page_number += 1
        except Exception as e:
            print(f"Error with pagination: {e}")
            print("No more pages available.")
            break

# Close the driver once all pages have been scraped
driver.quit()

print(f"Total items scraped: {total_scraped}")
