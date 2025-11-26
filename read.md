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
(3, 'hello i am chanchal');


python3 --version
pip --version
source venv/bin/activate
pip install uvicorn
which uvicorn
uvicorn backend.main:app --reload
python -m backend.main
pip install PyJWT
python3 main.py

python3 -m http.server 5500
pip install fastapi[all]
git remote set-url origin https://github.com/chanchalsiet/smartnotes.git
git push -u origin main

document.addEventListener("DOMContentLoaded", function() {
        const token = localStorage.getItem("token");
        const username = localStorage.getItem("username");
        const user_id = localStorage.getItem("user_id");

        if (!token) {
            // If no token, redirect to login
            window.location.href = "login.html";
            return;
        }

        // Show username in the header
        document.querySelector("header h2").innerText = `Welcome, ${username}`;

        // Logout button
        document.getElementById("logoutBtn").addEventListener("click", function() {
            localStorage.removeItem("token");
            localStorage.removeItem("username");
            localStorage.removeItem("user_id");
            window.location.href = "login.html";
        });

        // Add note form
        document.getElementById("addNoteForm").addEventListener("submit", async (e) => {
            e.preventDefault();

            const title = document.getElementById("noteTitle").value;
            const content = document.getElementById("newNote").value;

            const res = await fetch("http://127.0.0.1:8000/add_note", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "token": token
                },
                body: JSON.stringify({ title, content })
            });

            const data = await res.json();
            if (res.ok) {
                alert("Note added!");
                document.getElementById("addNoteForm").reset();
            } else {
                alert(data.detail || "Error adding note");
            }
        });
    });
<!--    document.querySelector("header h2").innerText = `Welcome, ${username}`;-->
<!--    document.getElementById("logoutBtn").addEventListener("click", function () {-->
<!--        alert("hello")-->
<!--        // Remove both tokens from local storage-->
<!--        localStorage.removeItem("token");-->
<!--        localStorage.removeItem("username");-->
<!--        localStorage.removeItem("user_id");-->
<!--        localStorage.removeItem("refresh_token");-->

<!--        window.location.href = "/frontend/login.html";-->
<!--    });-->
<!--    const addNoteBtn = document.getElementById('addNote');-->
<!--    const notesList = document.getElementById('notesList');-->
<!--    const newNoteInput = document.getElementById('newNote');-->
<!--    const noteTitleInput = document.getElementById('noteTitle');-->

<!--    // Dummy array to store notes-->
<!--    let notes = [];-->

<!--    // Function to render notes-->
<!--    function renderNotes() {-->
<!--        notesList.innerHTML = '';-->
<!--        notes.forEach((note, index) => {-->
<!--            const noteDiv = document.createElement('div');-->
<!--            noteDiv.className = 'note';-->
<!--            noteDiv.innerHTML = `-->
<!--                <span>${note}</span>-->
<!--                <div>-->
<!--                    <button class="edit" onclick="editNote(${index})">Edit</button>-->
<!--                    <button class="delete" onclick="deleteNote(${index})">Delete</button>-->
<!--                </div>-->
<!--            `;-->
<!--            notesList.appendChild(noteDiv);-->
<!--        });-->
<!--    }-->

<!--    // Add Note-->
<!--    addNoteBtn.addEventListener('click', () => {-->
<!--        const noteTitle = noteTitleInput.value.trim();-->
<!--        const noteText = newNoteInput.value.trim();-->
<!--        alert(noteText)-->
<!--        if (noteTitle === '' && noteText === '') return;-->
<!--        notes.push(noteTitle);-->
<!--        notes.push(noteText);-->
<!--        noteTitleInput.value = '';-->
<!--        newNoteInput.value = '';-->
<!--        renderNotes();-->
<!--    });-->

<!--    // Edit Note-->
<!--    function editNote(index) {-->
<!--        const updatedText = prompt("Edit your note:", notes[index]);-->
<!--        if (updatedText !== null) {-->
<!--            notes[index] = updatedText;-->
<!--            renderNotes();-->
<!--        }-->
<!--    }-->

<!--    // Delete Note-->
<!--    function deleteNote(index) {-->
<!--        if (confirm("Are you sure you want to delete this note?")) {-->
<!--            notes.splice(index, 1);-->
<!--            renderNotes();-->
<!--        }-->
<!--    }-->
<!--    logoutBtn.addEventListener("click", () => {-->
<!--        if (confirm("Are you sure you want to logout?")) {-->
<!--            localStorage.removeItem("token");-->
<!--            window.location.href = "login.html";-->
<!--        }-->
<!--    });-->

<!--    // Initial render-->
<!--    renderNotes();-->