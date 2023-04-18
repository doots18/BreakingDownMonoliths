from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restful import Api, Resource

class LCM(Resource): 
    def get(self, num1, num2):
        a = int(num1)
        b = int(num2)
        lcm = a
        while lcm % b != 0:
            lcm += a
        return {'result': lcm}

app = Flask(__name__)
api = Api(app)
api.add_resource(LCM, '/<int:num1>/<int:num2>')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5061,
        host="0.0.0.0"
    )
