from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/history")
def history():
    return render_template('historia.html')

if __name__ == '__main__':
    app.run(debug=True)
