from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, notebook!"


if __name__ == '__main__':
    app.run(debug=True)

notes= {
     '1': {'id': 1, 'name': 'assignments', 'description':'complete assignment 1'}
}

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)


class Notebook(Resource):
    def get(self, note_name):
        return {note_name: notes[note_name]}

    def put(self, note_name):
        notes[note_name] = request.form['data']
        return {note_name: notes[note_name]}


    @api.route('/', methods=['GET'])
    @json
    def get_notes():
        return.query

    @api.route('/', methods=['GET'])
    @json
    def get_notes():
        return.query.get_or_404()

    @api.route('/', methods=['POST'])
    @json
    def new_note():
        note = ()
        note.import_data(request.json)
        return {}, 201, {'note': note.get_url()}

    @api.route('/', methods=['PUT'])
    @json
    def edit_notes():
        notes =.query.get_or_404()
        return {}

api.add_resource(Notebook, '/notes/')