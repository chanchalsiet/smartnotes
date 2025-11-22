const API_URL = "http://127.0.0.1:8000";

//document.querySelector("#loginForm").addEventListener("submit", async (e) => {
//    e.preventDefault();
//    const email = document.querySelector("#email").value;
//    const password = document.querySelector("#password").value;
//    alert(email)
//    alert(password)
//    try {
//        const res = await fetch(`${API_URL}/login`, {
//            method: "POST",
//            headers: { "Content-Type": "application/json" },
//            body: JSON.stringify({ email: email, password: password })
//        });
//
//        if (!res.ok) throw new Error("Login failed");
//
//        const data = await res.json();
//        localStorage.setItem("token", data.access_token);
//
//        window.location.href = "dashboard.html";
//    } catch (err) {
//        alert(err)
//        document.getElementById("errorMessage").innerText = "Login Failed!";
//        document.getElementById("errorMessage").style.display = "block";
//        console.error(err);
//    }
//});
document.querySelector("#loginForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.querySelector("#email").value;
    const password = document.querySelector("#password").value;

    try {
        const res = await fetch(`http://127.0.0.1:8000/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        if (!res.ok) throw new Error("Login failed");

        const data = await res.json();
        localStorage.setItem("token", data.access_token);
        // Redirect to dashboard
        window.location.href = "dashboard.html";

    } catch (err) {
        alert(err)
        alert("Login failedxxxx!");
        console.error(err);
    }
});