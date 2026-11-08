# ScamShield – AI Phishing & Fraudulent Message Detection

ScamShield is an AI-assisted web application designed to identify phishing messages, suspicious links, fraudulent requests, and potentially harmful communications.

It analyzes user-submitted messages, identifies suspicious indicators, calculates a risk score, explains why a message may be dangerous, and provides safe next steps.

## Features

- **Message Analysis:** Analyze SMS, emails, and other text messages.
- **Risk Score:** Assign a risk score between 0 and 100.
- **Threat Classification:** Identify suspicious message categories.
- **Indicator Extraction:** Highlight suspicious words, phrases, and links.
- **Explanation:** Explain why a message may be suspicious.
- **Safety Recommendations:** Provide suggested actions to help users stay safe.
- **Threat History:** Store and view previously analyzed messages.
- **Cloud Database:** Store analysis records in Supabase PostgreSQL.
- **REST API:** FastAPI backend for communication between frontend and database.

## Technology Stack

### Frontend
- React.js
- TypeScript
- Vite
- HTML
- CSS

### Backend
- Python
- FastAPI
- REST API

### Database
- SQLite for local development
- Supabase PostgreSQL for cloud storage

### Cloud Computing
- Supabase – Cloud database
- Render – Backend hosting
- Vercel – Frontend hosting

## Project Structure

```text
ScamShield/
│
├── backend/
│   ├── lib/
│   │   ├── lm.py
│   │   ├── db.py
│   │   └── security.py
│   │
│   ├── models/
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
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.ts
│
├── README.md
└── .gitignore
```

## How ScamShield Works

1. The user enters a suspicious message into the application.
2. The React frontend sends the message to the FastAPI backend.
3. The backend analyzes the message using detection rules and risk-scoring logic.
4. ScamShield identifies suspicious indicators and calculates a risk score.
5. The application displays the threat category, explanation, and recommended safety steps.
6. The analysis result is stored in the configured database.
7. Users can view previously analyzed messages through the threat history feature.

## Installation and Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/bharath-chandra-2719/ScamShield-Cloud.git
cd ScamShield-Cloud
```

### 2. Backend Setup

Open a terminal:

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

Configure environment variables using the `.env.example` file.

For local SQLite development, configure the database path as required by the backend.

Start the backend:

```bash
python -m uvicorn server:app --reload --port 8000
```

Backend URL:

```text
http://localhost:8000
```

API documentation:

```text
http://localhost:8000/docs
```

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Configure the frontend API URL using the provided environment example.

Start the frontend:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

## Cloud Integration

ScamShield uses cloud computing to make the application accessible beyond a local development environment.

| Cloud Service | Purpose |
|---|---|
| Supabase | Cloud PostgreSQL database |
| Render | FastAPI backend hosting |
| Vercel | React frontend hosting |

### Cloud Data Flow

1. Users access ScamShield through the deployed frontend.
2. The frontend communicates with the backend hosted on Render.
3. The backend analyzes submitted messages.
4. Analysis records are stored in the Supabase PostgreSQL database.
5. Previous analysis records can be retrieved through the backend API.

**Security:** Database connection credentials must remain in backend environment variables. Never expose database credentials in frontend code or commit `.env` files to GitHub.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/analyze-message` | Analyze a message |
| GET | `/api/threat-history` | Retrieve analysis history |
| GET | `/health` | Check backend health |
| GET | `/` | Check API status |

## Environment Variables

Backend environment variables are configured in `backend/.env`.

Example:

```env
DATABASE_URL=your_supabase_postgresql_connection_string
FRONTEND_URL=http://localhost:5173
```

Do not upload your actual `.env` file or database password to GitHub.

For local SQLite usage, configure `DATABASE_PATH` if required.

## Future Enhancements

- Advanced machine learning-based phishing classification.
- Improved suspicious URL analysis.
- Browser extension integration.
- Real-time threat intelligence integration.
- Multi-language phishing message detection.
- Email integration for suspicious message analysis.

## Disclaimer

ScamShield is an educational and awareness-oriented security application. Its risk scores are heuristic indicators, not calibrated probabilities or guarantees that a message is safe or fraudulent. Users should independently verify suspicious communications before taking action.

## Author

Developed as an academic project focused on cybersecurity awareness, phishing detection, and cloud computing.
