# Loan Qualifier Application

## Description  
This APP is a python CLI (command line interface) application that gives the user fast way of seeing qualifying loans from the bank. This application works by taking a sheet('daily_rate_sheet') located at path(./data/daily_rate_sheet.csv), which provided various loan providers. The providers will ask user some simple questions to evaluate users loan eligibility,and the APP will give the user a spreadsheet of qualifying loans

---

## Technologies

This project use python 3.7 and the following packages(may require installation)
* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
```

---

## Usage
To use the loan qualifier application simply clone the repository and run the **app.py** with:

```python
python app.py
```
## usage examples: 
one of our customers use these datas to test his app  
there is also a picture to show how to work with this app  
>credit_score = 750
>debt = 5000
>income = 20000
>loan_amount = 100000
>home_value = 210000
![this is the picture instruction.](https://raw.githubusercontent.com/KellenCrimson/loan_qualifier_app/main/Pic/pic_guide.jpg)
---

## Content Added History(ver1)
Add function save_csv, which read a nested list then write the contents in a csv file, provide the user a spreadsheet
code running successfully with fire library
```python
if __name__ == "__main__":
    fire.Fire(save_csv)
```
```python
python app.py [nested_list]
```

## Content Added History(ver2)   
Move function save_csv to ./qualifier/utils/fileio.py
delete import csv code
modify from qualifier.utils.fileio import (load_csv, save_csv)

## Content Added History(ver3)   
create new function 'save_qualifying_loans',which ask user friendly  
to provide a file path for the spreadsheet. instructions listed above
---

## Contributors

Brought to you by ET Home Loans.   
Vivian Liu   
Liu Lujunjin

---

## License

MIT License

Copyright (c) [2022] [Liu Lujunjin]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
