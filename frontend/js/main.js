
//const API_URL = "http://13.58.138.43:8000/";
const API_URL = "http://52.15.191.175:8000/api";
document.querySelector("#loginForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.querySelector("#email").value;
    const password = document.querySelector("#password").value;
    try {
        const res = await fetch(`http://0.0.0.0:8000/api/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });
        if (!res.ok) throw new Error("Login failed");

        const data = await res.json();

        // Save data locally
        localStorage.setItem("token", data.access_token);
        localStorage.setItem("username", data.username);
        localStorage.setItem("user_id", data.user_id);

        window.location.href = "dashboard.html";
    } catch (err) {
        alert("Login failed!");
        console.error(err);
    }
});
