from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "blerp derp"

@app.route('/')
def home():
	return "Eyyyy Tint"

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)
