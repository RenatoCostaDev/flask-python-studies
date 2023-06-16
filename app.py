from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return '<h1>hello world</h1>'



app.run(debug=True)

