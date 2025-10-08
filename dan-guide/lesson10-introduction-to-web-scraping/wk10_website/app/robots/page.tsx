'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

const RobotsPage = () => {
  const router = useRouter();

  return (
    <div className="min-h-screen bg-gray-900 p-4 text-white">
      <div className="flex justify-center mb-6">
        <button
          onClick={() => router.push('/')} 
          className="bg-blue-600 text-white py-2 px-4 rounded-lg shadow-md hover:bg-blue-500"
        >
          Back to Home
        </button>
      </div>

      <h2 className="text-3xl font-semibold mb-6 text-center">Ethical Web Scraping & Robots.txt</h2>

      <p className="text-lg mb-4">
        Web scraping can be a powerful tool to collect data, but it&apos;s important to do it ethically. 
        One important aspect of ethical scraping is respecting the <code>robots.txt</code> file, which tells 
        web crawlers which parts of a website they can or cannot access.
      </p>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">What is robots.txt?</h3>
        <p className="mb-4">
          <code>robots.txt</code> is a file placed by website owners to guide web crawlers (like search engines and 
          scraping bots) on which parts of their site they can and cannot access. 
          It is part of the <strong>Robots Exclusion Standard (REP)</strong>, a protocol to manage web scraping 
          and crawling behavior.
        </p>

        <h4 className="text-xl font-semibold mb-2">Why is robots.txt important?</h4>
        <p className="mb-4">
          - It helps website owners control the traffic to their site, ensuring that servers are not overloaded.
          <br />
          - It defines what web crawlers can index, making sure that only the public sections of the website are accessed.
          <br />
          - It helps prevent private, confidential, or resource-heavy sections of the website from being scraped.
        </p>

        <h4 className="text-xl font-semibold mb-2">Common Rules in robots.txt</h4>
        <pre className="bg-gray-700 p-4 rounded-lg mb-4">
          <code>
{`# Allow all robots to access everything
User-agent: *
Disallow:

# Block access to the /private directory
User-agent: *
Disallow: /private/

# Block a specific crawler (Googlebot) from accessing any part of the site
User-agent: Googlebot
Disallow: /

# Block a crawler from a specific URL
User-agent: *
Disallow: /confidential/page.html`}
          </code>
        </pre>
      </div>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">Example Code: Accessing robots.txt</h3>
        <p className="mb-4">
          Here’s how you can access a website&apos;s <code>robots.txt</code> file using Python and Selenium:
        </p>
        <div className="bg-gray-700 p-4 rounded-lg mb-4">
          <pre>
            <code>
{`from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
robots_url = "https://en.wikipedia.org/robots.txt"
driver.get(robots_url)
print(driver.page_source)  # Print the robots.txt content
driver.quit()`}
            </code>
          </pre>
        </div>

        <h4 className="font-semibold">Explanation:</h4>
        <ul className="list-disc pl-6 text-sm mb-4">
          <li>The script uses Selenium to visit the <code>robots.txt</code> file on Wikipedia.</li>
          <li>The <code>driver.page_source</code> command outputs the content of the <code>robots.txt</code> file to the console.</li>
          <li>You can use this method to check the rules set by other websites.</li>
        </ul>
      </div>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">Activity: Explore robots.txt for Wikipedia</h3>
        <p className="mb-4">
          Open up the <code>robots.txt</code> file for Wikipedia:
        </p>
        <a
          href="https://en.wikipedia.org/robots.txt"
          target="_blank"
          className="text-blue-600 hover:text-blue-500"
        >
          Wikipedia robots.txt
        </a>

        <p className="mt-4">
          Identify the restricted sections of the site and discuss why they are restricted. Common restricted sections include:
        </p>
        <ul className="list-disc pl-6 text-sm mb-4">
          <li>Private data or sensitive content (e.g., login pages, user profiles).</li>
          <li>Search engine bots may be restricted from crawling certain sections to avoid overloading the server.</li>
        </ul>
      </div>
    </div>
  );
};

export default RobotsPage;
