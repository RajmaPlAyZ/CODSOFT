from flask import Flask, render_template, request
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    title = 'To-Do List'
    heading = 'To-Do List'
    message = 'This is a simple Flask app'
    return render_template('index.html', title=title, heading=heading, message=message)


@app.route('/submit', methods=['POST'])
def submit():
    task1 = request.form.get('task1')
    task2 = request.form.get('task2')
    task3 = request.form.get('task3')

    # Process the form data as needed

    return render_template('result.html', task1=task1, task2=task2, task3=task3)


def run():
    app.run(host="0.0.0.0", port=8001)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
