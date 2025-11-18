// Example: simple alert for login
function handleLogin(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if(username && password) {
        alert("Login successful for user: " + username);
        window.location.href = "dashboard.html";
    } else {
        alert("Please enter username and password!");
    }
}

// Example: simple alert for register
function handleRegister(event) {
    event.preventDefault();
    const username = document.getElementById("reg_username").value;
    const email = document.getElementById("reg_email").value;
    const password = document.getElementById("reg_password").value;

    if(username && email && password) {
        alert("Registration successful for user: " + username);
        window.location.href = "login.html";
    } else {
        alert("Please fill all fields!");
    }
}
