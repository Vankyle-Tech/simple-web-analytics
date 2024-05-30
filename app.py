from flask import Flask
from flask_cors import CORS

from v1.report import v1bp

app = Flask(__name__)
app.register_blueprint(v1bp)
CORS(app)
if __name__ == '__main__':
    app.run()
