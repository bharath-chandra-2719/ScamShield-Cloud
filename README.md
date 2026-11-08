# 🛡️ ScamShield – AI Phishing & Fraudulent Message Deconstructor

ScamShield is a web-based phishing and fraudulent message detection system designed to help users identify suspicious messages, understand potential threats, and stay safe from online scams.

It analyzes text messages using a rule-based detection engine, identifies suspicious phrases, calculates a risk score from 0 to 100, classifies the threat level, and provides recommendations to help users avoid fraud.

---

## 📌 1. Project Overview

With the increasing use of digital payments, online banking, SMS, emails, and messaging platforms, phishing attacks and fraudulent messages have become common.

ScamShield aims to provide a simple platform where users can paste suspicious messages and understand whether they may be fraudulent.

The system examines suspicious words, phrases, urgency, payment requests, account threats, credential requests, and suspicious links to generate a security assessment.

## 🎯 2. Objectives

- Detect potentially fraudulent and phishing messages.
- Identify suspicious words and phrases.
- Calculate a threat score between 0 and 100.
- Classify messages into different risk levels.
- Explain why a message may be suspicious.
- Provide safe next steps and recommendations.
- Maintain a history of previously analyzed messages.

## ✨ 3. Key Features

### 1. Message Analysis
Users can paste suspicious SMS messages, emails, or other text messages for analysis.

### 2. Threat Score
Each analyzed message receives a score from 0 to 100 based on detected warning signs.

### 3. Risk Classification

| Score | Risk Level |
|---|---|
| 0–34 | Low |
| 35–59 | Medium |
| 60–79 | High |
| 80–100 | Critical |

### 4. Suspicious Phrase Detection
The system identifies warning signs such as:
- Requests for OTPs, passwords, PINs, and CVVs.
- Urgent payment requests.
- Account blocking or suspension threats.
- Suspicious verification links.
- Impersonation of banks or official departments.

### 5. Explanation of Threats
ScamShield displays detected suspicious phrases along with explanations of why they may be dangerous.

### 6. Safety Recommendations
Users receive suggestions such as:
- Do not share OTPs or passwords.
- Avoid clicking suspicious links.
- Do not transfer money to unknown accounts.
- Verify messages through official channels.

### 7. Threat History
Previously analyzed messages can be stored and viewed using the SQLite database.

---

## 🛠️ 4. Technologies Used

### Frontend
- React.js
- TypeScript
- Vite
- HTML
- CSS

### Backend
- Python
- FastAPI
- Uvicorn

### Database
- SQLite

### Detection Engine
- Python Regular Expressions
- Rule-based suspicious phrase detection
- Context-based risk scoring

---

## 📂 5. Project Folder Structure

```text
ScamShield/
│
├── backend/
│   ├── lib/
│   │   ├── __init__.py
│   │   ├── lm.py
│   │   ├── db.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── verdict.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── analyze.py
│   │   └── history.py
│   │
│   ├── tests/
│   │   └── test_analyze.py
│   │
│   ├── requirements.txt
│   ├── .env
│   ├── .env.example
│   └── server.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   │
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── README.md
└── .gitignore
```

---

## ⚙️ 6. Installation and Setup

### Prerequisites

Install the following before running the project:

- Python 3.10 or above
- Node.js and npm
- Visual Studio Code

### Step 1: Download or Clone the Project

Open the project folder in Visual Studio Code.

### Step 2: Setup the Backend

Open the VS Code terminal and navigate to the backend folder:

```powershell
cd backend
```

Install the required Python packages:

```powershell
pip install -r requirements.txt
```

### Step 3: Setup the Frontend

Open another terminal and navigate to the frontend folder:

```powershell
cd frontend
```

Install the required Node.js packages:

```powershell
npm install
```

---

## ▶️ 7. How to Run the Project

Whenever you close VS Code or shut down your computer, follow these steps to run ScamShield again.

### Terminal 1 – Start the Backend

Open the project in VS Code.

Open the first terminal:

```powershell
cd backend
```

Start the FastAPI server:

```powershell
python -m uvicorn server:app --reload --port 8000
```

Backend URL:

```text
http://localhost:8000
```

### Terminal 2 – Start the Frontend

Open a second terminal by clicking the `+` button in the terminal panel.

Run:

```powershell
cd frontend
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

### Step 3 – Open ScamShield

Open your browser and visit:

**http://localhost:5173**

The ScamShield application should now be running.

**Important:** Keep both terminal windows open while using the application.

---

## 🔗 8. API Endpoints

The backend provides the following API endpoints:

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/analyze-message` | Analyzes a suspicious message |
| GET | `/api/threat-history` | Retrieves analysis history |
| GET | `/health` | Checks backend health |
| GET | `/` | Backend root endpoint |

### API Documentation

FastAPI provides interactive API documentation.

Open:

```text
http://localhost:8000/docs
```

You can test the backend endpoints directly from the Swagger interface.

---

## 🔍 9. How ScamShield Works

1. The user enters a suspicious message into the frontend.
2. The frontend sends the message to the FastAPI backend.
3. The backend validates the input.
4. The detection engine checks for suspicious words and phrases.
5. The system identifies warning categories and calculates a risk score.
6. The message is classified into a risk level.
7. An explanation and safety recommendations are generated.
8. The analysis is stored in the SQLite database.
9. The results are displayed on the frontend.

---

## 📊 10. Risk Scoring Method

ScamShield uses a rule-based scoring mechanism.

Different categories of suspicious indicators have different weights.

Examples include:

- Credential theft requests.
- Urgent or threatening language.
- Account suspension threats.
- Payment requests.
- Suspicious links.
- Impersonation of trusted organizations.

Additional scoring adjustments are applied when multiple warning signs appear together.

The final score is limited to a range of 0–100.

**Note:** The score is a heuristic risk indicator, not a statistically calibrated probability that a message is fraudulent. A low score does not guarantee that a message is safe.

---

## 🔐 11. Security Considerations

- Never share real OTPs, passwords, PINs, or banking details.
- Avoid clicking links in suspicious messages.
- Verify important requests through official websites or customer support.
- Keep API keys and other secrets private.
- Do not upload confidential personal information for testing.

---

## 🧪 12. Testing

Test ScamShield using different types of messages:

1. Phishing messages requesting OTPs.
2. Fake bank account suspension alerts.
3. Fraudulent payment requests.
4. Suspicious verification links.
5. Normal messages without suspicious requests.

Compare the detected indicators, risk scores, and explanations.

---

## ⚠️ 13. Troubleshooting

### Problem 1: Uvicorn command not recognized

Use:

```powershell
python -m uvicorn server:app --reload --port 8000
```

### Problem 2: npm is not recognized

Install Node.js and restart VS Code.

### Problem 3: ModuleNotFoundError

Navigate to the backend folder and run:

```powershell
pip install -r requirements.txt
```

### Problem 4: Frontend packages missing

Navigate to the frontend folder and run:

```powershell
npm install
```

### Problem 5: Frontend cannot connect to backend

Make sure:
- The backend is running on port 8000.
- The frontend is running on port 5173.
- The API base URL in the frontend configuration is correct.

---

## 🚀 14. Future Enhancements

- Email and URL reputation checking.
- Multilingual phishing message detection.
- Browser extension for real-time detection.
- Machine learning-based phishing classification.
- Improved detection of context-dependent scams.
- Additional threat intelligence integration.

---

## 👨‍💻 15. Conclusion

ScamShield provides a simple and accessible approach to identifying potentially fraudulent messages. By combining suspicious phrase detection, rule-based risk scoring, explanations, and safety recommendations, the system helps users become more aware of phishing attempts and online fraud.

The project demonstrates the practical use of React, FastAPI, Python, and SQLite in developing a cybersecurity awareness application.

---

**Project Name:** ScamShield – AI Phishing & Fraudulent Message Deconstructor

**Domain:** Cybersecurity / Fraud Detection

**Project Type:** Full-Stack Web Application
