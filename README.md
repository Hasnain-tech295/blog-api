# Blog API

A blog REST API built with **FastAPI**, **SQLAlchemy** (async), and **Jinja2** templates.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — async ORM with SQLite
- [Jinja2](https://jinja.palletsprojects.com/) — HTML templating
- [Pydantic](https://docs.pydantic.dev/) — data validation

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/Hasnain-tech295/blog-api.git
   cd blog-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**
   ```bash
   fastapi dev main.py
   ```

The app will be available at `http://127.0.0.1:8000`.  
Interactive API docs: `http://127.0.0.1:8000/docs`

## Project Structure

```
blog-api/
├── main.py          # App entry point, routes, exception handlers
├── models.py        # SQLAlchemy models (User, Post)
├── schemas.py       # Pydantic schemas
├── database.py      # DB engine and session setup
├── routers/
│   ├── users.py     # User API routes
│   └── posts.py     # Post API routes
├── templates/       # Jinja2 HTML templates
├── static/          # CSS, JS, icons
└── media/           # Uploaded media files
```

## API Endpoints

### Users — `/api/users`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/users` | Create a user |
| `GET` | `/api/users/{user_id}` | Get a user |
| `GET` | `/api/users/{user_id}/posts` | Get all posts by a user |
| `PATCH` | `/api/users/{user_id}` | Update a user |
| `DELETE` | `/api/users/{user_id}` | Delete a user |

### Posts — `/api/posts`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/posts` | Get all posts |
| `POST` | `/api/posts` | Create a post |
| `GET` | `/api/posts/{post_id}` | Get a post |
| `PUT` | `/api/posts/{post_id}` | Replace a post |
| `PATCH` | `/api/posts/{post_id}` | Partially update a post |
| `DELETE` | `/api/posts/{post_id}` | Delete a post |

## License

MIT