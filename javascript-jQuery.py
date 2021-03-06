from flask import Flask, url_for, render_template, request, redirect
from flask_bootstrap import Bootstrap

import db_interaction


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    # if no address is given, redirect to the index page
    return redirect(url_for('index'))

@app.route('/index.html')
def index():
    tasks_list = db_interaction.get_tasks()
    return render_template('index.html', tasks_list=tasks_list)


@app.route('/insert_task', methods=['POST'])
def insert_task():
    if ('description' in request.form and request.form['description']!=''):
        description = request.form['description']
        if ('urgent' in request.form and request.form['urgent'] == 'on'):
            urgent = 1
        else:
            urgent = 0
        db_interaction.insert_task(description, urgent)

    # back to the home page
    return redirect(url_for('index'))

@app.route('/delete_task', methods=['GET'])
def delete_task():
    if 'id_task' in request.args:
        id_task = request.args.get('id_task')
        db_interaction.remove_task_by_id(id_task)

    # back to the home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
