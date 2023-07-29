from flask import Flask
from flask_restful import Api
from urls.moves import api_blueprint

# Creating a flask app
app = Flask(__name__)
api = Api(app)
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
	app.run(debug=True, port=8000)

