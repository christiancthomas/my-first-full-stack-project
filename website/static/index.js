function deleteNote(noteId) {
    // Function will delete the note using POST method and reload the webpage.
    fetch('/delete-note',{
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/"; // Reload to homepage
    });
}