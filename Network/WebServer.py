from flask import Flask

app = Flask(__name__)

line_list = []


@app.route("/")
def main():
    return


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
