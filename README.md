# 🛡️ ScamShield – Cloud-Based Phishing & Fraud Detection System

**ScamShield** is a web-based cybersecurity application that helps users identify phishing messages, suspicious communications, fraudulent requests, and potential online scams.

Users can submit SMS messages, emails, and other text content for analysis. ScamShield evaluates suspicious indicators, calculates a risk score, explains potential threats, and provides recommended safety actions.

The application is deployed using cloud computing services, making it accessible online without requiring local installation.

## 🌐 Live Application

| Component | URL |
|---|---|
| Live Frontend | https://scam-shield-cloud.vercel.app |
| Backend API | https://scamshield-cloud.onrender.com |
| API Documentation | https://scamshield-cloud.onrender.com/docs |
| Backend Health | https://scamshield-cloud.onrender.com/health |

## ✨ Key Features

- **Phishing Message Detection:** Analyze suspicious SMS messages, emails, and notices.
- **Risk Scoring:** Calculate a threat score between 0 and 100.
- **Threat Classification:** Identify suspicious categories such as urgency, threats, account suspension, and payment requests.
- **Suspicious Indicator Extraction:** Highlight potentially dangerous phrases and indicators.
- **Threat Explanation:** Explain why a message may be suspicious.
- **Safety Recommendations:** Suggest appropriate actions to avoid potential scams.
- **Threat History:** Retrieve previously analyzed messages.
- **Cloud Database Integration:** Store analysis records in Supabase PostgreSQL.
- **REST API:** Communicate between the frontend and backend using FastAPI.

## 🛠️ Technology Stack

### Frontend
- React.js
- TypeScript
- Vite
- HTML5
- CSS3

### Backend
- Python
- FastAPI
- REST API

### Detection Engine
- Rule-based message analysis
- Suspicious keyword and phrase detection
- Risk scoring and threat classification

### Database
- SQLite – Local development
- PostgreSQL – Cloud database through Supabase

### Cloud Computing Services

| Service | Purpose |
|---|---|
| Vercel | Frontend hosting |
| Render | Backend hosting |
| Supabase | Cloud PostgreSQL database |
| GitHub | Source code management and deployment integration |

## 🏗️ System Architecture

```text
             USER
               |
               v
      REACT FRONTEND
          (Vercel)
               |
               v
       FASTAPI BACKEND
           (Render)
               |
               v
       MESSAGE ANALYSIS
               |
       +-------+-------+
       |               |
       v               v
  RULE-BASED       RISK SCORE
  DETECTION        & CLASSIFICATION
       |               |
       +-------+-------+
               |
               v
       SUPABASE DATABASE
        (PostgreSQL)
               |
               v
       ANALYSIS RESPONSE
               |
               v
       RESULTS TO USER
```

## 📂 Project Structure

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
│   │   ├── analyze.py
│   │   └── history.py
│   │
│   ├── tests/
│   │   └── test_analyze.py
│   │
│   ├── requirements.txt
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
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.ts
│
├── README.md
└── .gitignore
```

## ⚙️ Installation and Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/bharath-chandra-2719/ScamShield-Cloud.git
cd ScamShield-Cloud
```

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your environment variables using `.env.example`.

For local SQLite development, configure the database path as required by the backend.

Start the backend server:

```bash
python -m uvicorn server:app --reload --port 8000
```

Backend URL:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

### 3. Frontend Setup

Open another terminal and navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Create a frontend `.env` file with:

```env
VITE_API_BASE_URL=http://localhost:8000
```

Start the frontend:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

## ☁️ Cloud Deployment

ScamShield uses cloud computing services to host the frontend, backend, and database independently.

### Frontend Deployment – Vercel

- Connect the GitHub repository to Vercel.
- Set the root directory to `frontend`.
- Select Vite as the framework preset.
- Build command: `npm run build`.
- Output directory: `dist`.
- Configure `VITE_API_BASE_URL` with the deployed Render backend URL.

### Backend Deployment – Render

- Connect the GitHub repository to Render.
- Set the root directory to `backend`.
- Build command: `pip install -r requirements.txt`.
- Start command:

```bash
uvicorn server:app --host 0.0.0.0 --port $PORT
```

- Configure backend environment variables in Render.

### Database Deployment – Supabase

- Create a PostgreSQL database project in Supabase.
- Configure the backend database connection using `DATABASE_URL`.
- Store database credentials only in backend environment variables.
- Save and retrieve message analysis records through the backend.

## 🔌 API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| POST | `/api/analyze-message` | Analyze a suspicious message |
| GET | `/api/threat-history` | Retrieve previous analyses |
| GET | `/health` | Check backend health |
| GET | `/` | Check API status |

Interactive API documentation:

https://scamshield-cloud.onrender.com/docs

## 🔐 Security Considerations

- Keep database credentials in backend environment variables.
- Never commit `.env` files to GitHub.
- Restrict database access through appropriate permissions and security policies.
- Configure CORS to allow the deployed frontend origin.
- Validate incoming API requests.
- Avoid exposing private database connection strings in frontend code.

## 🚀 Future Enhancements

- Advanced machine learning-based phishing classification.
- Improved suspicious URL analysis.
- Browser extension integration.
- Real-time threat intelligence integration.
- Multi-language phishing message detection.
- Enhanced threat history and analytics.

## ⚠️ Disclaimer

ScamShield is an educational cybersecurity awareness application. Its risk scores are heuristic indicators and should not be interpreted as calibrated probabilities or guarantees. Users should independently verify suspicious communications before sharing personal information or making payments.

## 👨‍💻 Project Information

**Project Name:** ScamShield – Cloud-Based Phishing & Fraud Detection System

**Domain:** Cybersecurity and Cloud Computing

**Repository:** https://github.com/bharath-chandra-2719/ScamShield-Cloud

**Deployment:** Vercel + Render + Supabase

---

*Built to promote safer digital communication through phishing awareness and cloud computing.*