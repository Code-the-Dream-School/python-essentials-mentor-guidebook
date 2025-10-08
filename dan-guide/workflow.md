# Basic Workflow of Using This Mentor Guide

This guide was last updated for the Python 100 Summer 2025 class. Any and all feedback is welcome. You can send it to me directly on Slack or email me at politykadan@gmail.com.
Course order may shift as needs arise, but this guide uses the order for the Summer 2025 class.
I have moved over assignment files as needed for the way that I do mentor sessions.
Each assignment has a brief overview to quickly cover the lesson topics and I added notes that I use to refresh my memory.
Please note, that I speak at a fairly high rate of speed so feel free to adjust accordingly and use as little or as much of this as you'd like.
Due to a reordering of course material the slides may show different weeks, so confirm lesson name and message me if any are in the wrong place. 
---

## Lesson Order  
**Terminal commands should be run after the setup is completed below.**

- [Lesson 0: Learning to Learn](lesson0-learning-to-learn/overview0.md)

- [Lesson 1: Introduction to Python](lesson1-introduction-to-python/overview1.md) 
  - cd lesson1-introduction-to-python  
  - pytest -v -x assignment1-test.py

- [Lesson 2: Data Structures and File Handling](lesson2-data-structures-and-file-handling/overview2.md)
  - cd lesson2-data-structures-and-file-handling  
  - pytest -v -x assignment2-test.py

- [Lesson 3: Valid Sudoku and Nested Loops](lesson3-valid-sudoku-and-nested-loops/overview3.md)  
  - cd lesson3-more-python-skills
---

## Setup Instructions (from `dan-guide` root)

### macOS / Linux  
python3 -m venv .venv  
source .venv/bin/activate  
pip install -r requirements.txt

### Windows  
python -m venv .venv  
source .venv/Scripts/activate  
pip install -r requirements.txt
