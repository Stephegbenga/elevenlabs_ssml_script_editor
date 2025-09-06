from flask import Flask, request, session, jsonify
from flask_cors import CORS
from flask import render_template, send_from_directory, redirect, Response
from flask_cors import CORS

# --- Flask App Initialization ---
app = Flask(__name__)
files_folder = ""

# CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    return send_from_directory(files_folder, 'index.html')

if __name__ == '__main__':
    app.run()
