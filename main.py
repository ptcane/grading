from flask import Flask, send_from_directory
app = Flask(__name__, static_folder='')

@app.route('/')
def index():
  return send_from_directory(app.root_path, 'index.html')

@app.route('/<path:path>')
def address():
  return send_from_directory(app.root_path, path)

app.run(host='0.0.0.0', port=8080, debug=True)