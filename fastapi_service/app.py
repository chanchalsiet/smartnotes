from flask import Flask, request, redirect, url_for, render_template
import jwt

app = Flask(__name__)
app.secret_key = "supersecretkey"  # same as FastAPI

@app.route("/dashboard")
def dashboard():
    token = request.cookies.get("jwt_token")

    if not token:
        return redirect(url_for("auth.login"))

    try:
        data = jwt.decode(token, "supersecretkey", algorithms=["HS256"])
        username = data["sub"]
        return render_template("dashboard.html", username=username)
    except:
        return redirect(url_for("auth.login"))
