import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv('urls.csv')

# Convert labels
df['label'] = df['label'].map({'legitimate': 0, 'phishing': 1})

# Feature extraction
def extract_features(url):
    return {
        'url_length': len(url),
        'has_https': int('https' in url),
        'count_digits': sum(c.isdigit() for c in url),
        'count_special': sum(not c.isalnum() for c in url)
    }

features = df['url'].apply(extract_features)
X = pd.DataFrame(features.tolist())
y = df['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
print(classification_report(y_test, model.predict(X_test)))

# Check new URL
url = input("Enter a URL to classify: ")
x_new = pd.DataFrame([extract_features(url)])
pred = model.predict(x_new)[0]
print("⚠️ Phishing" if pred else "✅ Legitimate")
