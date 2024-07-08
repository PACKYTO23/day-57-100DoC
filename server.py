from flask import Flask, render_template
import random
import datetime as dt
import requests

GEN = "https://api.genderize.io?name="
AGE = "https://api.agify.io?name="

app = Flask(__name__)


@app.route("/")
def home():
    current_year = str(dt.datetime.now()).split()[0].split("-")[0]
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def get_name(name):
    g_response = requests.get(url=GEN + name)
    a_response = requests.get(url=AGE + name)
    g_data = g_response.json()
    a_data = a_response.json()
    gender = g_data["gender"]
    age = a_data["age"]

    return f"<h1>Hey, {name.title()}...</h1>" \
           f"<h2>I think you are {gender},</h2>" \
           f"<h3>And maybe {age} years old.</h3>"


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
