# Lesson 1: Introduction to Python – Mentor Guide

For this lesson I just walk through the actual lesson with them and make sure the virtual environment is working. This part of the lesson I like to stress/demonstrate to them: "Once your virtual environment is activated, you see .venv as part of your terminal prompt.  Be sure that is present for all subsequent work.  When you create a new terminal session, you have to activate the virtual environment again.  When the virtual environment is active, you can always use the commands python and pip, that is, you don't need python3 or pip3."

How to open the command palette (`Ctrl+Shift+P`)
Type `Python: Select Interpreter`
Choose the one with `.venv` in the path

I also like to cover that the coding assignment is good to practice(without AI) because DSA/leetcode is a common theme in job interviews. 

Setup Commands

```bash
# Create and enter project directory name it whatever you want
mkdir ctd_py && cd ctd_py
git clone https://github.com/Code-the-Dream-School/python_homework.git
cd python_homework

# Create and activate virtual environment
python -m venv .venv       # or python3 -m venv .venv
source .venv/Scripts/activate  # Windows
# or
source .venv/bin/activate      # Mac/Linux

# Install required packages
pip install virtualenv pytest
```
