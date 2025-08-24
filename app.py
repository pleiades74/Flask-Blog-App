from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (use DB for real apps)
posts = []

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/add", methods=["POST"])
def add_post():
    title = request.form["title"]
    content = request.form["content"]
    if title and content:
        posts.append({"title": title, "content": content})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
