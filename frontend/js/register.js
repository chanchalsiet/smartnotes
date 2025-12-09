
import { API_URL } from './config.js';

const registerForm = document.getElementById("registerForm");
const errorMsg = document.getElementById("error");
document.querySelector("#registerForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const full_name = document.querySelector("#full_name").value;
    const first_name = document.querySelector("#first_name").value;
    const last_name = document.querySelector("#last_name").value;
    const username = document.querySelector("#username").value;
    const email = document.querySelector("#email").value;
    const password = document.querySelector("#password").value;
    if (!full_name || !first_name || !last_name || !username || !email || !password) {
        errorMsg.innerText = "All fields are required!";
        return;
    }
    const payload = {
        full_name,
        first_name,
        last_name,
        username,
        email,
        password
    };
    try {
        const res = await fetch(`${API_URL}/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (res.ok){
            alert("Registration successful! Please login.");
            window.location.href = "login.html";
        } else {
            errorMsg.innerText = data.detail || "Registration failed!";
        }
    } catch (err) {
        console.error("Error:", err);
        errorMsg.innerText = "Something went wrong!";
    }
});
