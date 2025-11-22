brew install postgresql
brew services start postgresql
psql postgres
psql -U chanchal -d admin -h localhost -W
\conninfo

CREATE DATABASE smartnotes;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(200)  NOT NULL,
    first_name VARCHAR(100)  NOT NULL,
    last_name VARCHAR(100)  NOT NULL,
    username VARCHAR(200) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(500),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (full_name, first_name, last_name, username, email, password, status)
VALUES
('ram verma', 'ram', 'verma', 'ramu', 'ramu@gmail.com', 'ramu123', 'active'),
('ram verma1', 'ram1', 'verma1', 'ramu1', 'ramu1@gmail.com', 'ramu1123', 'active');

CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    
);

INSERT INTO notes (user_id,notes )
VALUES
(1, 'hello i am chanchal');


python3 --version
pip --version
source venv/bin/activate
pip install uvicorn
which uvicorn
uvicorn backend.main:app --reload
python -m backend.main
pip install PyJWT

python3 -m http.server 5500
pip install fastapi[all]