import { API_URL } from './config.js';

document.querySelector("#loginForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.querySelector("#email").value;
    const password = document.querySelector("#password").value;
    console.log("API_URL is:", API_URL);
    console.log("Sending login request with:", { email, password });
    try {
        const res = await fetch(`${API_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });
        console.log("Login response status:", res.status);

        if (!res.ok) throw new Error("Login failed");

        const data = await res.json();

        // Save data locally
        console.log("Login successful, storing token:", data);
        localStorage.setItem("token", data.access_token);
        localStorage.setItem("username", data.username);
        localStorage.setItem("user_id", data.user_id);

        window.location.href = "dashboard.html";
    } catch (err) {
        alert("Login failed!");
        console.error(err);
    }
});
