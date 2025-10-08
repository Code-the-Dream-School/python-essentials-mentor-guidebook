
'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

const ECPage = () => {
  const router = useRouter();

  const navigateToHomePage = () => {
    router.push('/'); 
  };

  return (
    <div className="min-h-screen flex flex-col p-5 bg-grey-50 justify-center items-center">
      <h1 className="text-4xl font-semibold text-gray-100 text-center mb-6">Selenium Expected Conditions</h1>
      <div className="mt-6">
        <button
          className="bg-blue-600 text-white py-2 px-6 justify-center rounded-lg shadow-md hover:bg-blue-500"
          onClick={navigateToHomePage}
        >
          Back to Homepage
        </button>
      </div>
      <div className="w-full mb-6">
      
        <h2 className="text-2xl font-semibold text-gray-100 mb-4">Selenium Expected Conditions (EC)</h2>
        <pre className="bg-gray-800 p-4 rounded-lg text-sm text-white">
{`EC.presence_of_element_located(locator)
Waits for the presence of an element in the DOM (not necessarily visible).

Example: wait.until(EC.presence_of_element_located((By.ID, "dynamic-content")))

---

EC.visibility_of_element_located(locator)
Waits for the element to be visible on the page (not only present but also displayed, i.e., it must have a non-zero width and height).

Example: wait.until(EC.visibility_of_element_located((By.ID, "dynamic-content")))

---

EC.element_to_be_clickable(locator)
Waits for the element to be visible and enabled (i.e., it can be clicked).

Example: wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))

---

EC.text_to_be_present_in_element(locator, text)
Waits for the specific text to be present in the element.

Example: wait.until(EC.text_to_be_present_in_element((By.ID, "dynamic-content"), "Loaded"))

---

EC.text_to_be_present_in_element_value(locator, text)
Waits for the specified text to be present in the value attribute of an element (commonly used with input fields).

Example: wait.until(EC.text_to_be_present_in_element_value((By.ID, "input-field"), "Expected Text"))

---

EC.frame_to_be_available_and_switch_to_it(locator)
Waits for a frame to be available and then switches to it.

Example: wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "iframe-name")))

---

EC.invisibility_of_element_located(locator)
Waits for an element to become invisible (or not present in the DOM).

Example: wait.until(EC.invisibility_of_element_located((By.ID, "loading-spinner")))

---

EC.staleness_of(element)
Waits for an element to become stale (i.e., it's no longer attached to the DOM).

Example: wait.until(EC.staleness_of(some_element))

---

EC.element_to_be_selected(locator)
Waits for an element to be selected (useful for checkboxes or option elements).

Example: wait.until(EC.element_to_be_selected((By.ID, "checkbox")))

---

EC.element_located_to_be_selected(locator)
Waits for an element located by the given locator to be selected.

Example: wait.until(EC.element_located_to_be_selected((By.CSS_SELECTOR, "option[selected]")))

---

EC.alert_is_present()
Waits for an alert to be present on the page.

Example: wait.until(EC.alert_is_present())

---

EC.alert_text_contains(text)
Waits for an alert to have the specified text.

Example: wait.until(EC.alert_text_contains("Are you sure?"))

---

EC.url_changes(url)
Waits for the URL to change (e.g., after a form submission).

Example: wait.until(EC.url_changes("http://example.com/old"))

---

EC.url_to_be(url)
Waits for the URL to be exactly equal to the given URL.

Example: wait.until(EC.url_to_be("http://example.com/success"))

---

EC.title_is(title)
Waits for the page title to be exactly the specified title.

Example: wait.until(EC.title_is("Expected Page Title"))

---

EC.title_contains(title)
Waits for the page title to contain the specified text.

Example: wait.until(EC.title_contains("Page Title"))`}
        </pre>
      </div>

      
    </div>
  );
};

export default ECPage;
