# MatchingCV

MatchingCV is a candidate-job matching platform that combines resume parsing, job posting extraction, and hybrid semantic matching.

## What this project does

- Upload candidate CVs in PDF format.
- Extract structured fields such as name, contact info, skills, education, and experience.
- Add job postings by URL and extract job details.
- Compute match scores using embeddings, skill overlap, experience, and education.
- Provide match reasoning with a semantic analysis layer.

## Repository layout

- `backend/` — FastAPI backend, PostgreSQL integration, scraping, extraction, and matching logic.
- `frontend/` — Next.js UI for uploading CVs, adding jobs, and viewing match results.
- `architecture.md` — detailed architecture and data flow documentation.

## Requirements

- Python 3.11+ (or compatible Python 3.x)
- Node.js 20+ / npm
- Docker & Docker Compose (recommended for local DB and backend)
- `POSTGRES`, `OPENAI_API_KEY`, and `GROQ_API_KEY` environment variables

## Backend setup

1. Create a Python virtual environment:

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install backend dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in `backend/` with values for:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/defense_matching
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

4. Start the database and API with Docker Compose:

```bash
docker-compose up --build
```

This starts:

- PostgreSQL with `pgvector` on `localhost:5432`
- FastAPI backend on `localhost:8000`

> Note: The frontend currently uses `http://127.0.0.1:8003` as the backend base URL in `frontend/lib/api.ts`. If you run the backend on port `8000`, update that file accordingly.

## Frontend setup

1. Open a new terminal and install frontend dependencies:

```bash
cd frontend
npm install
```

2. Start the Next.js app:

```bash
npm run dev
```

3. Open the browser at:

```text
http://localhost:3000
```

## How to use

- Upload a resume PDF from the left panel.
- Add a job posting URL using the job form.
- Select a candidate and click `Find Matches`.
- View the top matching jobs with score and reasoning.

## Notes

- CV and job embeddings are stored in PostgreSQL as JSON strings.
- The matching algorithm is hybrid: semantic similarity + skills + experience + education.
- The semantic reasoning layer uses an LLM to provide match commentary.

## Helpful files

- `backend/app/main.py` — API entrypoint.
- `backend/docker-compose.yml` — local service orchestration.
- `frontend/app/page.tsx` — main UI page.
- `frontend/lib/api.ts` — frontend HTTP client configuration.
- `architecture.md` — architecture and component descriptions.

