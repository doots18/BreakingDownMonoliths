from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api, Resource

class Modulus(Resource): 
    def get(self, num1, num2):
        a = int(num1)
        b = int(num2)
        # Compute the modulus
        modulus = a % b
        return {'result': modulus}

app = Flask(__name__)
api = Api(app)
api.add_resource(Modulus, '/<int:num1>/<int:num2>')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5062,
        host="0.0.0.0"
    )
