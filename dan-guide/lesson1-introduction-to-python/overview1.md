# Lesson 1: Introduction to Python – Mentor Guide

For this lesson, I just walk through the slides PDF and the lesson with students and make sure the virtual environment is working.
I will run the commands from the main workflow.md to show tests passing, but I don't show solutions directly.  

### Emphasize to students:
“Once your virtual environment is activated, you’ll see .venv in your terminal prompt.  
Be sure that is present for all subsequent work.  
Every time you start a new terminal session, you must activate the virtual environment again.  
When the virtual environment is active, you can always use python and pip,  
no need for python3 or pip3.”

---

### VS Code Interpreter Setup

1. Open the command palette: Ctrl+Shift+P  
2. Type: Python: Select Interpreter  
3. Choose the interpreter with .venv in the path

---

### Interview Note

I like to remind them that the coding assignment is good practice without AI assistance,  
since data structures and algorithms (DSA/Leetcode) are a common theme in technical interviews.
One example that comes to mind is the operators "/" vs "//" and I usually use the sudoku solution to explain this difference.
[Valid Sudoku – LeetCode](https://leetcode.com/problems/valid-sudoku/description/)

---

### Setup Commands

Create and enter project directory:  
mkdir ctd_py && cd ctd_py  
git clone https://github.com/Code-the-Dream-School/python_homework.git  
cd python_homework

Create and activate virtual environment:  
python -m venv .venv         (or python3 -m venv .venv)  
source .venv/Scripts/activate     (Windows)  
source .venv/bin/activate         (Mac/Linux)

Install required packages:  
pip install virtualenv pytest
