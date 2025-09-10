'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

const IntroPage = () => {
  const router = useRouter();

  const navigateToHomePage = () => {
    router.push('/'); 
  };

  return (
    <div className="min-h-screen flex flex-col p-5 bg-grey-50 justify-center items-center">
      
      <h1 className="text-4xl font-semibold text-gray-100 text-center mb-6">Introduction to Selenium</h1>
      <div className="mt-6">
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
          onClick={navigateToHomePage}
        >
          Back to Homepage
        </button>
      </div>
      <p className="text-lg text-center text-gray-200 mb-6">
        Selenium is a powerful tool for automating browsers. It can simulate user interactions on websites, making it ideal for web scraping and testing.
      </p>
      <h2 className="text-2xl font-semibold justify-left text-gray-100 mb-4">Installing Selenium</h2>
      <pre className="bg-gray-800 p-4 rounded-lg mb-4 text-sm">
      {`pip install selenium
pip install webdriver-manager`}
      </pre>
      <h2 className="text-2xl font-semibold text-gray-100 mb-4">Key Features of Selenium</h2>
      <ul className="text-gray-200 space-y-4">
        <li>
        <b>-</b> <b>Headful Mode:</b> Selenium opens a visible browser window and interacts with the page like a user would.
          <pre className="bg-gray-800 p-4 rounded-lg text-sm">
            {`from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up headful Chrome (default)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the page
driver.get("http://example.com")

# Scraping an element
div_element = driver.find_element(By.CLASS_NAME, "container")
print(div_element.text)

driver.quit()`}
          </pre>
        </li>
        <li>
        <b>-</b> <b>Headless Mode:</b> Selenium runs without opening a browser window, which is faster for automation tasks.
          <pre className="bg-gray-800 p-4 rounded-lg text-sm">
            {`from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the page
driver.get("http://example.com")

# Scraping an element
div_element = driver.find_element(By.CLASS_NAME, "container")
print(div_element.text)

driver.quit()`}
          </pre>
          <p className="text-gray-200 mt-4">
          <b>-</b> Even in <b>headless mode</b>, Selenium is capable of interacting with dynamic content, such as content that loads with JavaScript or AJAX. Selenium will wait for the page to load and interact with dynamically rendered elements, just as it would in headful mode.
          </p>
        </li>
        <li>
        <b>-</b> <b>WebDriver:</b> Selenium interacts with a browser through the WebDriver, allowing it to control browser actions like clicks, form filling, etc.
        </li>
        <li>
        <b>-</b> <b>Browser Support:</b> Works with most major browsers including Chrome, Firefox, Safari, and Edge.
        </li>
        <li>
        <b>-</b> <b>Element Selection:</b> Uses CSS selectors, XPath, and other strategies to target HTML elements on the page.
        </li>
      </ul>

      
    </div>
  );
};

export default IntroPage;
