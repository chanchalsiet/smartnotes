//const addNoteBtn = document.getElementById('addNote');
//const notesList = document.getElementById('notesList');
//const newNoteInput = document.getElementById('newNote');
//
//// Dummy array to store notes
//let notes = [];
//
//// Function to render notes
//function renderNotes() {
//    notesList.innerHTML = '';
//    notes.forEach((note, index) => {
//        const noteDiv = document.createElement('div');
//        noteDiv.className = 'note';
//        noteDiv.innerHTML = `
//            <span>${note}</span>
//            <div>
//                <button class="edit" onclick="editNote(${index})">Edit</button>
//                <button class="delete" onclick="deleteNote(${index})">Delete</button>
//            </div>
//        `;
//        notesList.appendChild(noteDiv);
//    });
//}
//
//// Add Note
//addNoteBtn.addEventListener('click', () => {
//    const noteText = newNoteInput.value.trim();
//    if (noteText === '') return;
//    notes.push(noteText);
//    newNoteInput.value = '';
//    renderNotes();
//});
//
//// Edit Note
//function editNote(index) {
//    const updatedText = prompt("Edit your note:", notes[index]);
//    if (updatedText !== null) {
//        notes[index] = updatedText;
//        renderNotes();
//    }
//}
//
//// Delete Note
//function deleteNote(index) {
//    if (confirm("Are you sure you want to delete this note?")) {
//        notes.splice(index, 1);
//        renderNotes();
//    }
//}
//logoutBtn.addEventListener("click", () => {
//    if (confirm("Are you sure you want to logout?")) {
//        localStorage.removeItem("token");
//        window.location.href = "login.html";
//    }
//});
//
//// Initial render
//renderNotes();
