# Contact Management Application

A simple FastAPI-based RESTful API for managing contacts, using SQLite as the database.

## Features

- CRUD operations for contacts (Create, Read, Update, Delete).
- Search contacts by various fields.
- Automatic database initialization and sample data population on startup.
- Data validation for contact fields.

## Stack & Requirements

- **Language:** Python 3.9+
- **Framework:** FastAPI
- **Database:** SQLite
- **Validation:** Pydantic
- **Package Manager:** pip

### Prerequisites

Ensure you have Python installed. You can check your version with:
```bash
python --version
```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd FastAPIProject
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI server using `uvicorn`:

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

- **API Documentation (Swagger UI):** `http://127.0.0.1:8000/docs`
- **Alternative Documentation (ReDoc):** `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint, returns a welcome message. |
| GET | `/contacts` | List all contacts. |
| POST | `/contacts` | Create a new contact. |
| GET | `/contacts/{id}` | Get details of a specific contact. |
| PUT | `/contacts/{id}` | Update an existing contact. |
| DELETE | `/contacts/{id}` | Delete a contact. |
| GET | `/contacts/search?q={query}` | Search contacts by name, email, etc. |

### Sample Contact Data
```json
{
  "first_name": "John",
  "middle_initial": "D",
  "last_name": "Doe",
  "age": 30,
  "date_of_birth": "1994-01-01",
  "email": "john.doe@example.com",
  "favorite_color": "Blue",
  "pronouns": "he/him"
}
```

## Running Tests

The project uses `unittest` and `FastAPI TestClient`. Run tests with:

```bash
python test_main.py
```
Or using `pytest` if installed:
```bash
pytest
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `CONTACTS_DATABASE_PATH` | Path to the SQLite database file. | `contacts.db` |

## Project Structure

```text
FastAPIProject/
├── main.py            # Main application entry point and API routes
├── test_main.py       # Unit and integration tests
├── test_main.http     # HTTP client requests for testing
├── requirements.txt   # Project dependencies
├── contacts.db        # SQLite database (generated on startup)
└── README.md          # Project documentation
```

## License

TODO: Add license information.
