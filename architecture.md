# MatchingCV Architecture

## Overview

MatchingCV is a two-part application that matches uploaded candidate CVs against scraped job postings using a hybrid matching engine.

- Backend: FastAPI service for CV upload, job ingestion, storage, and matching.
- Frontend: Next.js UI for uploading resumes, adding job URLs, and viewing candidate-job matches.
- Database: PostgreSQL with `pgvector` support for embedding storage.
- AI/ML: Sentence-transformers embeddings, cosine similarity, and LLM reasoning for semantic matching.

## System Components

### Backend

The backend is located in `backend/`.

Core responsibilities:

- Parse candidate resumes from PDF files.
- Scrape and extract structured information from job posting URLs.
- Normalize skills and extract entities like education, technologies, and experience.
- Generate text embeddings for both resumes and job descriptions.
- Store processed CVs and jobs in PostgreSQL.
- Compute hybrid match scores and provide match reasoning.

### Frontend

The frontend is located in `frontend/`.

Core responsibilities:

- Upload candidate CVs.
- Submit job posting URLs.
- Display stored candidates and jobs.
- Request top matches for a chosen CV.
- Render match scores and reasoning.

## Data Flow

1. Candidate uploads a PDF resume.
2. Backend extracts raw text and structured fields from the resume.
3. Backend normalizes skills and creates a sentence embedding from the resume text.
4. Candidate data is stored in PostgreSQL as a `CV` record.
5. User submits a job posting URL.
6. Backend scrapes the page, extracts and normalizes job data, and creates a job embedding.
7. Job data is stored in PostgreSQL as a `Job` record.
8. When matching, the backend compares the selected CV against all jobs.
9. The engine calculates a hybrid score using similarity, skill overlap, experience, and education.
10. The backend also generates human-readable match reasoning using an LLM.

## Backend Architecture

### FastAPI Routes

- `POST /upload-cv` - Upload a resume PDF and save candidate data.
- `POST /add-job` - Add a job using a URL and save the extracted job data.
- `GET /cvs` - Return stored candidate summaries.
- `GET /jobs` - Return stored job summaries.
- `GET /matches/{cv_id}` - Return the top matches for a specific CV.

### Database Models

- `CV` (`backend/app/db/models/cv.py`)
  - Stores personal info, skills, education, experience, and an embedding.
- `Job` (`backend/app/db/models/job.py`)
  - Stores title, company, location, URL, job details, skills, and an embedding.

### Processing Pipelines

#### CV Processing

Implemented in `backend/app/services/cv/process_cv.py`:

- `extract_pdf_text` reads the PDF.
- `extract_cv_information` parses candidate fields.
- `normalize_skills` standardizes skill lists.
- `create_embedding` builds a text embedding using `sentence-transformers`.

#### Job Processing

Implemented in `backend/app/services/jobs/process_job.py`:

- `parse_job_page` scrapes job page HTML.
- `extract_job_information` parses job fields.
- `normalize_skills` standardizes job skill lists.
- `create_embedding` builds a job description embedding.

### Hybrid Matching

Implemented in `backend/app/services/matching/hybrid_matcher.py`:

- `compute_similarity` compares CV and job embeddings with cosine similarity.
- `calculate_skill_overlap` compares normalized skill lists.
- `calculate_experience_score` compares candidate experience to job requirements.
- `calculate_education_score` compares education text.
- `semantic_match_analysis` uses `langchain_groq` and an LLM for reasoning.
- Final score is weighted across semantic similarity, skills, experience, and education.

## Frontend Architecture

- `frontend/app/page.tsx` contains the main UI flow.
- `frontend/components/upload-cv.tsx` handles CV file upload.
- `frontend/lib/api.ts` defines the backend API base URL.
- UI shows candidates, jobs, and top matches with match percentages.

## External Dependencies

- FastAPI
- PostgreSQL with `pgvector`
- SQLAlchemy
- `sentence-transformers` for embeddings
- `scikit-learn` cosine similarity
- `python-docx`, `pymupdf` for document handling
- `beautifulsoup4` and `requests` for scraping
- `openai` / `langchain_groq` for semantic reasoning
- Next.js and React for frontend

## Important Notes

- The backend reads `DATABASE_URL`, `OPENAI_API_KEY`, and `GROQ_API_KEY` from `.env`.
- The frontend currently points to `http://127.0.0.1:8003` in `frontend/lib/api.ts`.
- If you run the backend on the default Docker Compose port `8000`, update that value to `http://127.0.0.1:8000`.

## Key Files

- `backend/app/main.py` - FastAPI application entrypoint.
- `backend/docker-compose.yml` - local PostgreSQL + API service definition.
- `backend/app/services/cv/process_cv.py` - resume processing.
- `backend/app/services/jobs/process_job.py` - job URL extraction.
- `backend/app/services/matching/hybrid_matcher.py` - matching logic.
- `frontend/app/page.tsx` - main app UI.
- `frontend/lib/api.ts` - frontend/backend connector.
