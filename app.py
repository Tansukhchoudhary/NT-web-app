from flask import Flask, render_template, request, redirect, session
from admin_config import ADMIN_USERNAME, ADMIN_PASSWORD
import os

app = Flask(__name__)
app.secret_key = "2190121318"

IMAGES_FOLDER = "static/images"
app.config["IMAGES_FOLDER"] = IMAGES_FOLDER

@app.route("/")
def home():
    images = os.listdir(IMAGES_FOLDER) if os.path.exists(IMAGES_FOLDER) else []
    return render_template("home.html", images=images)

@app.route("/gallery")
def gallery():
    images = os.listdir(IMAGES_FOLDER) if os.path.exists(IMAGES_FOLDER) else []
    return render_template("gallery.html", images=images)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# ---------- ADMIN ----------
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if (request.form["username"] == ADMIN_USERNAME and
            request.form["password"] == ADMIN_PASSWORD):
            session["admin"] = True
            return redirect("/dashboard")
    return render_template("admin_login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if not session.get("admin"):
        return redirect("/admin")

    if request.method == "POST":
        file = request.files["image"]
        if file:
            file.save(os.path.join(app.config["IMAGES_FOLDER"], file.filename))

    images = os.listdir(IMAGES_FOLDER)
    return render_template("admin_dashboard.html", images=images)

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000", debug=True)
