'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

export default function Page() {
  const router = useRouter();

  const handlePageNavigation = (page: number) => {
    router.push(`/pagination?page=${page}`);
  };

  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gray-900 p-4">
      <h1 className="text-4xl font-semibold text-gray-100 text-center mb-6">Web Scraping Demo</h1>
      <p className="text-lg text-center text-gray-100 mb-6">Welcome to scraping the Document Object Model(DOM) and HTML.</p>
      <div className="flex space-x-4 p-4">
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
          onClick={() => router.push('/intro')}
        >
          Intro to Selenium
        </button>
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
          onClick={() => router.push('/dynamic')}
        >
          Dynamic Content Page
        </button>
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
          onClick={() => router.push('/ec')}
        >
          EC Example Page
        </button>
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500 ml-4"
          onClick={() => router.push('/html')}
        >
          HTML & DOM Scraping
        </button>
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500 ml-4"
          onClick={() => router.push('/robots')}
        >
          ROBOTS!!!
        </button>
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500 ml-4"
          onClick={() => router.push('/xpath')}
        >
          Xpath info
        </button>
        <button
          className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500 ml-4"
          onClick={() => router.push('/alts')}
        >
          Alternatives to Selenium
        </button>
      </div>

      <div className="border-2 border-blue-600 p-6 mt-6 rounded-lg shadow-md w-full max-w-xl text-center">
        <h2 className="text-2xl font-semibold text-gray-100 mb-4">Pagination Buttons</h2>
        <div className="flex space-x-4 justify-center">
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
            onClick={() => handlePageNavigation(1)}
          >
            Page 1
          </button>
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
            onClick={() => handlePageNavigation(2)}
          >
            Page 2
          </button>
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
            onClick={() => handlePageNavigation(3)}
          >
            Page 3
          </button>
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
            onClick={() => handlePageNavigation(4)}
          >
            Page 4
          </button>
          <button
            className="bg-blue-600 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-500"
            onClick={() => handlePageNavigation(5)}
          >
            Page 5
          </button>
        </div>
      </div>
    </div>
  );
}
