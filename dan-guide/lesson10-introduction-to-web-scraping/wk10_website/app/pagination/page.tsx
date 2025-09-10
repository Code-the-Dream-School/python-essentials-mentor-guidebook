'use client';

import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'next/navigation';
import Image from 'next/image';
import { useRouter } from 'next/navigation';
import listingsData from '../../data/listings.json';

interface Listing {
  id: number;
  price: string;
  beds: number;
  baths: number;
  sqft: string;
  address: string;
  image: string;
  description: string;
  features: string[]; 
}

const PaginationPage = () => {
  const [items, setItems] = useState<Listing[]>([]); 
  const [loading, setLoading] = useState(true);
  const searchParams = useSearchParams();
  const page = parseInt(searchParams?.get('page') || '1');
  const router = useRouter();

  useEffect(() => {
    setTimeout(() => {
      const start = (page - 1) * 20;
      const end = start + 20;
      const pageItems = listingsData.slice(start, end);
      setItems(pageItems);
      setLoading(false);
    }, 1000);
  }, [page]);

  return (
    <div className="min-h-screen bg-gray-900 p-4">
      <div className="flex justify-center mb-6">
        <button
          onClick={() => router.push('/')} 
          className="bg-blue-600 text-white py-2 px-4 rounded-lg shadow-md hover:bg-blue-500"
        >
          Back to Home
        </button>
      </div>
      <h2 className="text-3xl font-semibold mb-6 text-center text-gray-100">Page {page}</h2>
      {loading ? (
        <p className="text-lg text-center text-gray-600">Loading...</p>
      ) : (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 xl:grid-cols-4 gap-4">
            {items.map((item) => (
              <li key={item.id} className="bg-white p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200">
                <div className="flex flex-col">
                  <div className="flex justify-between items-center mb-2">
                    <h3 className="text-lg font-semibold text-blue-600">{`Listing ${item.id}`}</h3>
                    <button className="text-sm text-gray-600">View Details</button>
                  </div>
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm text-gray-800">Price: <b>{item.price}</b></span>
                    <span className="text-sm text-gray-600">{`${item.beds} beds / ${item.baths} baths / ${item.sqft} sqft`}</span>
                  </div>
                  <address className="text-sm mb-2 text-gray-600">{item.address}</address>
                  <div className="flex space-x-2 mb-2">
                    <a href={`https://www.zillow.com/homedetails/${item.id}`} target="_blank" className="text-blue-600 hover:text-blue-500">Visit Listing</a>
                    <a href="#" className="text-blue-600 hover:text-blue-500">Add to Favorites</a>
                  </div>
                  <div className="flex flex-col space-y-2">
                    <div className="w-full mb-2">
                      <Image
                        src={item.image}
                        alt={`Listing ${item.id}`}
                        width={200} 
                        height={150} 
                        className="w-full rounded-lg shadow-md"
                      />
                    </div>
                    <p className="text-sm text-gray-600">{item.description}</p>
                    <ul className="list-disc ml-5 space-y-1 text-sm text-gray-600">
                      {item.features.map((feature, idx) => (
                        <li key={idx}>{feature}</li> // TypeScript should no longer complain about this line
                      ))}
                    </ul>
                  </div>
                </div>
              </li>
            ))}
          </div>

          <div className="flex justify-center space-x-4 mt-6">
            <button
              className="bg-blue-600 text-white py-2 px-4 rounded-lg shadow-md hover:bg-blue-500"
              onClick={() => window.location.href = `/pagination?page=${page > 1 ? page - 1 : 1}`}
            >
              Previous
            </button>
            <button
              className="bg-blue-600 text-white py-2 px-4 rounded-lg shadow-md hover:bg-blue-500"
              onClick={() => window.location.href = `/pagination?page=${page < 5 ? page + 1 : 5}`}
            >
              Next
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default PaginationPage;
