# phishing-url-detector
A lightweight tool to detect phishing URLs using rule-based and ML-based logic.
#  Phishing Website Detection Tool

A lightweight Python-based tool that detects potentially harmful URLs using rule-based logic or machine learning. Built as part of the **RISE Internship Program**, the tool helps users avoid phishing attacks by flagging suspicious links.

##  Problem Statement

Phishing websites trick users into revealing personal information such as passwords, bank details, and credit card numbers. These attacks lead to identity theft and fraud.


##  Objective

To develop a tool that:
- Detects suspicious URLs
- Flags phishing attempts
- Uses either rule-based or machine learning-based logic
- Offers an optional GUI for user interaction

---

## Tech Stack

| Component        | Technology          |
|------------------|---------------------|
| Programming      | Python              |
| Dataset Handling | Pandas              |
| ML Model         | Scikit-learn        |
| Rule Engine      | Regex (re module)   |
| GUI (Optional)   | Tkinter             |

---

##  Project Structure
phishing-url-detector/
├── urls.csv # Dataset of phishing & legitimate URLs
├── rule_based_detector.py # Pattern-based detection script
├── ml_detector.py # ML-based phishing detection script
└── gui.py # Tkinter GUI (optional

---

##  Dataset Format (`urls.csv`)

The dataset contains labeled URLs:
```csv
url,label
http://login-update-security.com,phishing
https://accounts.google.com,legitimate

