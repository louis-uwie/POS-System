# QuickPOS

This is a personal project that I think would be best designed specifically for use on small businesses.
QuickPOS is a straightforward Point of Sale (POS) system developed using Flask and basic HTML/CSS to facilitate efficient transaction management and secure employee access.

## Features

- **Employee Authentication:**
  - Login functionality restricted to predefined employee accounts.
  - Admin privileges to manage employee accounts.

- **Simple Interface:**
  - Easy-to-use, intuitive UI built with HTML and CSS.

- **Session Management:**
  - Utilizes Flask sessions to securely manage user state across pages.

- **Database Integration:**
  - Built-in SQLite integration for managing employee and sales data (modifiable to other databases if required).

## Routes

- `/`: Landing page for non-authenticated users.
- `/login`: Secure login page accessible only by authorized users (managers and cashiers).

## Installation

### Requirements

- Python 3.x
- Flask
- Flask-Session
- SQLite3 (or alternative database)

### Setup

1. **Clone the Repository:**
```bash
git clone https://github.com/yourusername/QuickPOS.git
cd QuickPOS
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Initialize the Database:**
- Set up your database configuration in `database/db.py`.
- Populate initial user data directly into your database.

### Run the Application
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## License
QuickPOS is open-source software licensed under the MIT license.