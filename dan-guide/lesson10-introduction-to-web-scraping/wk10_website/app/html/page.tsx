'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

const HtmlPage = () => {
  const router = useRouter();

  const navigateToHomePage = () => {
    router.push('/'); 
  };

  return (
    <div className="min-h-screen flex flex-col p-5 bg-grey-50 justify-center items-center">
      <h1 className="text-4xl font-semibold text-gray-100 text-center mb-6">HTML & DOM Scraping</h1>
      <p className="text-lg text-center text-gray-200 mb-6">
        Learn how to target HTML elements using Selenium for web scraping.
      </p>
      
      <div className="w-full">
        <h2 className="text-2xl font-semibold text-gray-100 mb-4">Common HTML Tags for Scraping</h2>
        <ul className="space-y-4">
          <li>
            <h3 className="text-xl font-semibold">1. <code>&lt;div&gt;</code> (Division)</h3>
            <p className="text-gray-200">Used for defining a section or container in a page.</p>
            <p className="text-gray-200">Example: <code>&lt;div class=&quot;container&quot;&gt;Content&lt;/div&gt;</code></p>
          </li>
          <li>
            <h3 className="text-xl font-semibold">2. <code>&lt;img&gt;</code> (Image)</h3>
            <p className="text-gray-200">Used to display images on a page. You can target <code>src</code> attribute for scraping.</p>
            <p className="text-gray-200">Example: <code>&lt;img src=&quot;image.jpg&quot; alt=&quot;description&quot;&gt;</code></p>
          </li>
          <li>
            <h3 className="text-xl font-semibold">3. <code>&lt;a&gt;</code> (Anchor Links)</h3>
            <p className="text-gray-200">Used for hyperlinks. Target <code>href</code> to extract URLs.</p>
            <p className="text-gray-200">Example: <code>&lt;a href=&quot;https://example.com&quot;&gt;Visit site&lt;/a&gt;</code></p>
          </li>
          <li>
            <h3 className="text-xl font-semibold">4. <code>&lt;button&gt;</code> (Buttons)</h3>
            <p className="text-gray-200">Used for clickable buttons. Can be targeted to simulate user interaction.</p>
            <p className="text-gray-200">Example: <code>&lt;button&gt;Click me&lt;/button&gt;</code></p>
          </li>
          <li>
            <h3 className="text-xl font-semibold">5. <code>&lt;ul&gt;</code>/<code>&lt;ol&gt;</code> (Unordered & Ordered Lists)</h3>
            <p className="text-gray-200">Lists can be scraped by targeting individual <code>&lt;li&gt;</code> elements.</p>
            <p className="text-gray-200">Example: <code>&lt;ul&gt;&lt;li&gt;Item 1&lt;/li&gt;&lt;/ul&gt;</code></p>
          </li>
        </ul>
      </div>

      <div className="w-full mt-6">
        <h2 className="text-2xl font-semibold text-gray-200 mb-4">Example of DOM Structure</h2>
        <p className="text-gray-200 mb-4">Here is a simple example of an HTML DOM structure, demonstrating how to identify elements you might want to scrape:</p>
        <pre className="bg-gray-800 p-4 rounded-lg text-sm">
          {`<html>
  <head>
    <title>Web Scraping Example</title>
  </head>
  <body>
    <h1>Web Scraping Introduction</h1>
    <p>This is a paragraph that we will scrape.</p>
    <a href="https://example.com">Visit Example</a>
    <div class="container">
      <img src="image.jpg" alt="Example Image">
      <button>Click Me</button>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
      </ul>
    </div>
  </body>
</html>`}
        </pre>
      </div>

      <div className="w-full mt-6">
        <h2 className="text-2xl font-semibold text-gray-200 mb-4">Scraping HTML with Selenium</h2>
        <p className="text-gray-200 mb-4">
          Here&apos;s how you can use Selenium to target the above HTML elements. For example:
        </p>
        <pre className="bg-gray-800 p-4 rounded-lg text-sm">
          {`from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Chrome()

# Load the page
driver.get("http://example.com")

# Scraping a div element
div_element = driver.find_element(By.CLASS_NAME, "container")

# Scraping an image src attribute
image_element = driver.find_element(By.TAG_NAME, "img")
image_src = image_element.get_attribute("src")

# Scraping an anchor link href
link_element = driver.find_element(By.TAG_NAME, "a")
link_href = link_element.get_attribute("href")

# Close the driver
driver.quit()`}
        </pre>
      </div>

      

      <div className="mt-6">
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
          onClick={navigateToHomePage}
        >
          Back to Homepage
        </button>
      </div>
    </div>
  );
};

export default HtmlPage;
