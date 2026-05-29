# Contribution Guidelines for NeuroPath

Thank you for your interest in contributing to NeuroPath! This document provides guidelines for contributing to this project.

## Code of Conduct

Please be respectful, inclusive, and constructive in all interactions with the community.

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- PostgreSQL 13+
- Docker (optional but recommended)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yoyochiqui/neuropath.git
   cd neuropath
   ```

2. **Backend setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Frontend setup**
   ```bash
   cd ../frontend
   npm install
   npm start
   ```

4. **Database setup**
   ```bash
   cd ../backend
   alembic upgrade head
   ```

5. **Start development servers**
   ```bash
   # Terminal 1 - Backend
   cd backend
   uvicorn app.main:app --reload

   # Terminal 2 - Frontend
   cd frontend
   npm start
   ```

## Development Workflow

### Branch Naming

- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test additions

### Commit Messages

Use clear, descriptive commit messages:

```
type(scope): subject

- description line 1
- description line 2
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Code Standards

### Python

- Follow PEP 8
- Use type hints
- Use `black` for formatting

### JavaScript/React

- Use functional components with hooks
- Follow Airbnb style guide

## Testing

### Backend Tests

```bash
pytest
pytest --cov=app tests/
```

### Frontend Tests

```bash
npm test
npm test -- --coverage
```

## License

By contributing to NeuroPath, you agree that your contributions will be licensed under its MIT License.
