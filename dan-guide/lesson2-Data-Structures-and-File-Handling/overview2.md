# Lesson 2: Data Structures and File Handling – Mentor Guide

This session covers the most commonly used built-in data structures in Python — lists, dictionaries, tuples, and sets — as well as file handling basics. I usually ask students which ones they’ve used before and how comfortable they feel with them.

This is the first time students work with reading and writing files, so I give them space to struggle a bit and figure out common issues (e.g., missing files, wrong paths, forgetting to close the file).

---

## Topics to Cover

- Mutable vs immutable types  
- Lists: indexing, slicing, appending, popping  
- Dictionaries: key-value access, looping  
- Tuples: when and why to use  
- Sets: deduplication and set operations  
- Reading from a file (with `open`)  
- Writing to a file  
- Using `with open(...) as f:` for file context management

---

## Example Prompts for Discussion

- What’s the difference between a list and a tuple?  
- When would you use a dictionary instead of a list?  
- Why is it useful to use `with open(...)` instead of just `open()`?

---

## Commands (Run after setup from `dan-guide` root)

cd lesson2-data-structures-and-file-handling  
pytest -v -x assignment2-test.py
