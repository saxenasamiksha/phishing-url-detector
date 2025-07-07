import re

def is_suspicious(url):
    rules = [
        r'@', r'//', r'[-]{2,}', r'\d{5,}', r'https?\:\/\/\d+\.\d+\.\d+\.\d+',
        r'login', r'verify', r'update', r'bank', r'confirm'
    ]
    for rule in rules:
        if re.search(rule, url.lower()):
            return True
    return False

url = input("Enter a URL to check: ")
if is_suspicious(url):
    print("⚠️ Suspicious URL detected (Possible phishing)")
else:
    print("✅ URL looks safe")
