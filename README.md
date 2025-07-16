# Flask Trello App

A Trello-like task management application built with Flask, featuring user authentication, boards, lists, cards, and more.

## Features

- User registration and authentication
- Create and manage boards
- Add lists to boards
- Create cards with descriptions and due dates
- Checklist functionality
- Card activities tracking
- Premium user features
- Public/private board settings

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/GouriSahil/Flask-Trello.git
   cd Flask-Trello
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv env
   ```

3. **Activate the virtual environment**
   ```bash
   # On Linux/Mac:
   source env/bin/activate
   
   # On Windows:
   env\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**
   ```bash
   python create_db.py
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Access the application**
   Open your browser and go to `http://localhost:5000`

## Project Structure

```
Flask-Trello/
├── trello/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes
│   └── templates/           # HTML templates
├── migrations/              # Database migrations
├── instance/               # Database files
├── requirements.txt        # Python dependencies
├── create_db.py           # Database creation script
└── run.py                 # Application entry point
```

## Dependencies

The main dependencies include:
- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-Login**: User authentication
- **Flask-Migrate**: Database migrations
- **Flask-WTF**: Form handling
- **Flask-Bcrypt**: Password hashing
- **Alembic**: Database migration tool

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE). 