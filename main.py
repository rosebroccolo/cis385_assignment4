from flask import Flask, request, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return "Hello notebook!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

notes = {

}

class Notebook(Resource):
    def get(self, note_id):
        return {note_id: notes[note_id]}

    def put(self, note_id):
        notes[note_id] = request.form['data']
        return {note_id: notes[note_id]}

api.add_resource(Notebook, '/<string:note_id>')

if __name__ == '__main__':
    app.run(debug=True)

