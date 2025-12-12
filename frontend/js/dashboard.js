import { API_URL } from './config.js';
document.addEventListener("DOMContentLoaded", () => {
  const username = localStorage.getItem("username");
  if (username) {
      document.getElementById("welcomeMessage").innerText = `Welcome, ${username}`;
  } else {
      window.location.href = "login.html";
  }

  document.getElementById("logoutBtn").addEventListener("click", function() {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("user_id");
      window.location.href = "login.html";
  });
});
const addNoteBtn = document.getElementById('addNote');
const notesList = document.getElementById('notesList');
const newNoteInput = document.getElementById('newNote');

let notes = [];

// ------- Render Notes -------- //
function renderNotes() {
    notesList.innerHTML = "";
    if (notes.length === 0) {
        notesList.innerHTML = "<p>No notes found.</p>";
        return;
    }
    notes.forEach(note => {
        const div = document.createElement("div");
        div.classList.add("note");

        div.innerHTML = `
            <p>${note.notes}</p>
            <div class="note-buttons">
                <button onclick="editNote(${note.id})">Edit</button>
                <button onclick="deleteNote(${note.id})">Delete</button>
            </div>
        `;
        notesList.appendChild(div);
    });
}
function editNote(noteId) {
    const noteToEdit = notes.find(n => n.id === noteId);
    if (!noteToEdit) {
        alert("Note not found!");
        return;
    }

    const newContent = prompt("Edit your note:", noteToEdit.notes);
    if (newContent === null) return; // User cancelled

    noteToEdit.notes = newContent;
    renderNotes();

    const token = localStorage.getItem("token");
    fetch(`${API_URL}/edit_notes/${noteId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ notes: newContent })
    })
    .then(res => res.json())
    .then(data => console.log("Note updated:", data))
    .catch(err => console.error("Error updating note:", err));
}

function deleteNote(noteId) {
    const noteIndex = notes.findIndex(n => n.id === noteId);
    if (noteIndex === -1) {
        alert("Note not found!");
        return;
    }
    const confirmed = confirm("Are you sure you want to delete this note?");
    if (!confirmed) return;

    notes.splice(noteIndex, 1);
    renderNotes();

    // Send delete request to backend
    const token = localStorage.getItem("token");
    fetch(`${API_URL}/delete_notes/${noteId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        }
    })
    .then(res => res.json())
    .then(data => console.log("Note deleted:", data))
    .catch(err => console.error("Error deleting note:", err));
}
window.editNote = editNote;
window.deleteNote = deleteNote;

// ------- Add Note (SAVE IN DB) -------- //
addNoteBtn.addEventListener("click", async (e) => {
    e.preventDefault();
    const notesText = newNoteInput.value.trim();
    if (!notesText) return;
    const token = localStorage.getItem("token");
    alert(token)
    const user_id = localStorage.getItem("user_id");
    if (!token) {
        alert("Please login again.");
        window.location.href = "login.html";
        return;
    }
    alert(API_URL)
    const res = await fetch(`${API_URL}/add_notes`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ note: notesText })
    });
    if (res.status === 401) {
        alert("Session expired. Login again.");
        window.location.href = "login.html";
        return;
    }
    const data = await res.json();
    if (Array.isArray(notes)) {
        notes.push(data);
    } else {
        notes = [data];
    }

    newNoteInput.value = "";
    renderNotes();
});

// ------- Load Notes on Page Load -------- //
async function loadNotes() {
//    const token = localStorage.getItem("token");
//    const res = await fetch("${API_URL}/all_notes/", {
//        headers: {
//            "Authorization": `Bearer ${token}`
//        }
//    });
//    const data = await res.json();
//    notes = Array.isArray(data) ? data : (data.users || data.notes);
//    console.log("Notes loaded:", notes);
//    renderNotes();
    try {
        const token = localStorage.getItem("token");

        const res = await fetch(`${API_URL}/all_notes`, {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });
        if (!res.ok) {
            console.warn("API returned error:", res.status);
            notes = [];
            renderNotes();
            return;
        }
        const data = await res.json();
        notes = data?.notes || data?.users || [];
        if (!Array.isArray(notes)) {
            notes = [];
        }
        console.log("Notes loaded:", notes);
        renderNotes();

    } catch (error) {
        console.error("Error loading notes:", error);
        notes = [];
        renderNotes();
    }
}
loadNotes();
