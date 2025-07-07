import tkinter as tk
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load and prepare model
df = pd.read_csv('urls.csv')
df['label'] = df['label'].map({'legitimate': 0, 'phishing': 1})

def extract_features(url):
    return {
        'url_length': len(url),
        'has_https': int('https' in url),
        'count_digits': sum(c.isdigit() for c in url),
        'count_special': sum(not c.isalnum() for c in url)
    }

X = pd.DataFrame(df['url'].apply(extract_features).tolist())
y = df['label']
model = RandomForestClassifier()
model.fit(X, y)

# GUI
def detect_url():
    url = entry.get()
    features = pd.DataFrame([extract_features(url)])
    result = model.predict(features)[0]
    output.config(text="⚠️ Phishing" if result else "✅ Legitimate")

root = tk.Tk()
root.title("Phishing URL Detector")

tk.Label(root, text="Enter URL:").pack()
entry = tk.Entry(root, width=50)
entry.pack()
tk.Button(root, text="Check", command=detect_url).pack()
output = tk.Label(root, text="", font=("Arial", 14))
output.pack()

root.mainloop()
