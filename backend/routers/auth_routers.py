# import requests
# from flask import Blueprint, request, redirect, url_for, make_response, render_template
#
# auth_bp = Blueprint('auth', __name__)
#
# FASTAPI_URL = "http://127.0.0.1:8000/login"
#
# @auth_bp.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
#
#         response = requests.post(
#             FASTAPI_URL,
#             data={
#                 "username": username,
#                 "password": password
#             }
#         )
#
#         if response.status_code == 200:
#             token = response.json()["access_token"]
#
#             resp = make_response(redirect(url_for("dashboard")))
#             resp.set_cookie("jwt_token", token)  # Save JWT in browser
#             return resp
#
#         return render_template("login.html", msg="Invalid username or password")
#
#     return render_template("login.html")
