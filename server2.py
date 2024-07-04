import requests
from flask import Flask

GEN = "https://api.genderize.io?name="
AGE = "https://api.agify.io?name="

app = Flask(__name__)


@app.route("/")
def home():
    return (f"<h1>Enter '/guess/' and your name in the URL bar "
            f"to tell you your average age and approximate gender...</h1>")


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


if __name__ == "__main__":
    app.run(debug=True)
