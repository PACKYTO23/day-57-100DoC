from flask import Flask, render_template
import random
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    current_year = str(dt.datetime.now()).split()[0].split("-")[0]
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
