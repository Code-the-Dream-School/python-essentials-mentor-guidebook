'use client';

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

const DynamicPage = () => {
  const router = useRouter();
  const [apiData, setApiData] = useState('Loading data...');

  useEffect(() => {
    // Fetch data from a public API when component mounts
    const fetchData = async () => {
      try {
        // Using JSONPlaceholder API as an example public API
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        const data = await response.json();
        
        // Take some data from the response
        const randomUser = data[Math.floor(Math.random() * data.length)];
        setApiData(`Dynamic content loaded: User ${randomUser.name} works at ${randomUser.company.name}`);
      } catch (error) {
        setApiData('Failed to load dynamic content');
        console.error('Error fetching data:', error);
      }
    };

    // Add a small delay to make the dynamic loading more noticeable
    setTimeout(() => {
      fetchData();
    }, 1500);
  }, []);

  const navigateToHomePage = () => {
    router.push('/');
  };

  return (
    <div className="min-h-screen flex flex-col p-5 bg-grey-50 justify-center items-center">
      <h1 className="text-4xl font-semibold text-gray-100 text-center mb-6">Dynamic Content Page</h1>
      
      <div className="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-2xl">
        <h2 className="text-2xl font-semibold text-gray-200 mb-4">This page loads content dynamically</h2>
        
        {/* This is the dynamic content that will be loaded by API */}
        <p id="dynamic-content" className="text-xl text-yellow-400 p-4 border border-yellow-600 rounded-md mb-6">
          {apiData}
        </p>
        
        <div className="bg-gray-700 p-4 rounded-md">
          <h3 className="text-lg font-medium text-gray-200 mb-2">Why static scraping fails:</h3>
          <p className="text-gray-300">
            Initial HTML doesn&apos;t contain the API data - it only shows &quot;Loading data...&quot;
          </p>
          <p className="text-gray-300 mt-2">
            JavaScript must execute to fetch and render the actual data
          </p>
          <p className="text-gray-300 mt-2">
            Selenium needs time to wait for this process to complete
          </p>
        </div>
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

export default DynamicPage;