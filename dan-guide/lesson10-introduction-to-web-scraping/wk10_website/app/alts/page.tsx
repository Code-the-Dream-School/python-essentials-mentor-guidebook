'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

const AutomationAlternativesPage = () => {
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

      <h2 className="text-3xl font-semibold mb-6 text-center">Alternatives to Selenium for Web Automation</h2>

      <p className="text-lg mb-4">
        While Selenium is a popular tool for automating web browsers, there are several other alternatives that can be used for web scraping, testing, and browser automation. Here, we will explore three prominent alternatives: **Cypress**, **Playwright**, and **Puppeteer**.
      </p>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">1. Cypress</h3>
        <p className="mb-4">
          <strong>Cypress</strong> is a powerful end-to-end testing framework built specifically for the web. It is widely used for testing JavaScript applications. Cypress operates directly in the browser, providing fast and reliable tests. It also has built-in waiting and automatic retry mechanisms, making it excellent for real-time testing.
        </p>
        <ul className="list-disc pl-6">
          <li>Works inside the browser with native access to the DOM.</li>
          <li>Best suited for testing JavaScript apps.</li>
          <li>Excellent for real-time debugging with browser developer tools integration.</li>
        </ul>
      </div>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">2. Playwright</h3>
        <p className="mb-4">
          <strong>Playwright</strong> is an open-source framework developed by Microsoft for automating web browsers. It supports multiple browsers, including Chrome, Firefox, and WebKit. Playwright is known for its ability to handle modern web app challenges, such as dealing with single-page applications (SPAs) and handling asynchronous interactions.
        </p>
        <ul className="list-disc pl-6">
          <li>Supports cross-browser automation (Chrome, Firefox, WebKit).</li>
          <li>Handles complex modern web apps, including SPAs.</li>
          <li>Supports headless testing and is highly extensible.</li>
        </ul>
      </div>

      <div className="bg-gray-800 p-4 rounded-lg mb-6">
        <h3 className="text-2xl font-semibold mb-4">3. Puppeteer</h3>
        <p className="mb-4">
          <strong>Puppeteer</strong> is a Node.js library used for browser automation. It works with the Chrome DevTools Protocol, offering precise control over a headless or full Chrome browser. Puppeteer is often used for tasks like web scraping, generating screenshots, and rendering pages.
        </p>
        <ul className="list-disc pl-6">
          <li>Primarily used for headless Chrome browser automation.</li>
          <li>Excellent for scraping, screenshot generation, and testing.</li>
          <li>Works well for tasks requiring detailed control over the browser.</li>
        </ul>
      </div>
    </div>
  );
};

export default AutomationAlternativesPage;
