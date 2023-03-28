#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template, request, jsonify
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    state_info = []
    for state in sorted_states:
        state_info.append("{}: <B>{}</B>".format(state.id, state.name))

    return render_template('7-states_list.html', states=state_info)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
