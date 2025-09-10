'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

const XPathPage = () => {
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

      <h2 className="text-3xl font-semibold mb-6 text-center">Understanding XPath</h2>

      <p className="text-lg mb-4">
        XPath is a language for selecting nodes in an XML or HTML document. It allows you to navigate the DOM and access specific elements using paths.
      </p>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">Basic XPath Axes</h3>

        <p className="mb-4">
          XPath provides several axes that define the relationship between elements. Here are some of the most commonly used:
        </p>

        <div className="bg-gray-700 p-4 rounded-lg">
          <h4 className="font-semibold">1. Descendant</h4>
          <pre>
            - //div//a  &lt;!-- Finds all &lt;a&gt; tags that are descendants of a &lt;div&gt; tag --&gt;
          </pre>

          <h4 className="font-semibold">2. Child</h4>
          <pre>
            - //div/a  &lt;!-- Finds all &lt;a&gt; tags that are direct children of a &lt;div&gt; tag --&gt;
          </pre>

          <h4 className="font-semibold">3. Ancestor</h4>
          <pre>
            - //a/ancestor::div  &lt;!-- Finds all &lt;div&gt; elements that are ancestors of &lt;a&gt; --&gt;
          </pre>

          <h4 className="font-semibold">4. Following-sibling</h4>
          <pre>
            - //h2/following-sibling::p  &lt;!-- Finds &lt;p&gt; tags that follow an &lt;h2&gt; tag --&gt;
          </pre>
        </div>
      </div>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">Example HTML Structure</h3>

        <p className="mb-4">
          Below is a simple HTML structure we’ll use to demonstrate how XPath can be used to traverse through elements:
        </p>

        <div className="bg-gray-700 p-4 rounded-lg">
          <pre>
            {`<div id="content">
  <h2 id="section1">Section 1</h2>
  <p>This is some content for section 1</p>
  <div>
    <h2 id="section2">Section 2</h2>
    <p>This is some content for section 2</p>
  </div>
</div>`}
          </pre>

          <h4 className="font-semibold mt-4">XPath Examples on the Above Structure:</h4>

          <ul className="list-disc pl-6">
            <li>
              <strong>1. Select the first &lt;h2&gt;:</strong>
              <pre>
                - //h2[1]  &lt;!-- Selects the first &lt;h2&gt; element --&gt;
              </pre>
            </li>

            <li>
              <strong>2. Select the &lt;p&gt; after the first &lt;h2&gt;:</strong>
              <pre>
                - //h2[1]/following-sibling::p  &lt;!-- Finds the &lt;p&gt; tag that is the sibling of the first &lt;h2&gt; --&gt;
              </pre>
            </li>

            <li>
              <strong>3. Select the second &lt;h2&gt; inside a &lt;div&gt;:</strong>
              <pre>
                - //div//h2[2]  &lt;!-- Finds the second &lt;h2&gt; inside any &lt;div&gt; --&gt;
              </pre>
            </li>
          </ul>
        </div>
      </div>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
  <h3 className="text-2xl font-semibold mb-4">XPath Relationships Explained</h3>
  <p className="mb-4">
    Below, we explain some of the key XPath axes relationships, showing how to use XPath to navigate through different elements in the DOM.
  </p>

  <div className="bg-gray-700 p-4 rounded-lg mb-6">
    <h4 className="font-semibold">1. Child</h4>
    <p>
      A <strong>child</strong> is an immediate direct element under a parent element.
    </p>
    <pre>
      {`<div>  <!-- Parent -->
        <h1>Heading</h1>  <!-- Child -->
        <p>Paragraph</p>  <!-- Child -->
      </div>`}
    </pre>
    <pre>
      {`//div/h1  <!-- Finds all <h1> tags that are direct children of <div> -->`}
    </pre>
  </div>

  <div className="bg-gray-700 p-4 rounded-lg mb-6">
    <h4 className="font-semibold">2. Descendant</h4>
    <p>
      A <strong>descendant</strong> refers to any element that is nested within a parent element, regardless of its level in the hierarchy.
    </p>
    <pre>
      {`<div>  <!-- Parent -->
        <h1>Heading</h1>
        <div>  <!-- Descendant -->
          <p>Paragraph</p>  <!-- Descendant -->
        </div>
      </div>`}
    </pre>
    <pre>
      {`//div//p  <!-- Finds all <p> tags that are descendants of <div> -->`}
    </pre>
  </div>

  <div className="bg-gray-700 p-4 rounded-lg mb-6">
    <h4 className="font-semibold">3. Parent</h4>
    <p>
      A <strong>parent</strong> is the element that contains other elements, the opposite of a child.
    </p>
    <pre>
      {`<div>  <!-- Parent -->
        <h1>Heading</h1>  <!-- Child -->
      </div>`}
    </pre>
    <pre>
      {`//h1/parent::div  <!-- Finds the parent <div> of the <h1> -->`}
    </pre>
  </div>

  <div className="bg-gray-700 p-4 rounded-lg mb-6">
    <h4 className="font-semibold">4. Ancestor</h4>
    <p>
      An <strong>ancestor</strong> is any element that is above the current element in the DOM hierarchy. It can be several levels up.
    </p>
    <pre>
      {`<div>  <!-- Ancestor -->
        <div>
          <p>Paragraph</p>  <!-- Descendant -->
        </div>
      </div>`}
    </pre>
    <pre>
      {`//p/ancestor::div  <!-- Finds all <div> elements that are ancestors of <p> -->`}
    </pre>
  </div>

  <div className="bg-gray-700 p-4 rounded-lg mb-6">
    <h4 className="font-semibold">5. Following Sibling</h4>
    <p>
      A <strong>following sibling</strong> is an element that is on the same level as another element but comes after it.
    </p>
    <pre>
      {`<div>  <!-- Parent -->
        <h1>Heading</h1>  <!-- First sibling -->
        <p>Paragraph</p>  <!-- Following sibling -->
      </div>`}
    </pre>
    <pre>
      {`//h1/following-sibling::p  <!-- Finds all <p> tags that follow <h1> on the same level -->`}
    </pre>
  </div>
  
  <div className="bg-gray-700 p-4 rounded-lg mb-6">
    <h4 className="font-semibold">6. Preceding Sibling</h4>
    <p>
      A <strong>preceding sibling</strong> is an element that is on the same level as another element but comes before it.
    </p>
    <pre>
      {`<div>  <!-- Parent -->
        <p>Paragraph</p>  <!-- Preceding sibling -->
        <h1>Heading</h1>  <!-- Following sibling -->
      </div>`}
    </pre>
    <pre>
      {`//h1/preceding-sibling::p  <!-- Finds all <p> tags that precede <h1> on the same level -->`}
    </pre>
  </div>
</div>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">Using XPath in Python with Selenium</h3>

        <p className="mb-4">
          Here&apos;s a simple example of how to use XPath in a Selenium script to scrape links in the &quot;See Also &quot; section of a Wikipedia page:
        </p>

        <div className="bg-gray-700 p-4 rounded-lg">
          <pre>
            {`from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/wiki/Web_scraping")  # this much you've seen before

see_also_h2 = driver.find_element(By.CSS_SELECTOR,'[id="See_also"]')  # our starting point
links = []
if (see_also_h2):
    parent_div = see_also_h2.find_element(By.XPATH, '..')  # up to the parent div
    if parent_div:
        see_also_div = parent_div.find_element(By.XPATH,'following-sibling::div' )  # over to the div with all the links
        link_elements = see_also_div.find_elements(By.CSS_SELECTOR, 'a')
        for link in link_elements:
            print(f"{link.text}: {link.get_attribute('href')}")
            name = link.text.strip()
            url = link.get_attribute("href")
            if name and url:
                links.append({"name": name, "url": url})

driver.quit()`}
          </pre>
        </div>
      </div>
    </div>
  );
};

export default XPathPage;
