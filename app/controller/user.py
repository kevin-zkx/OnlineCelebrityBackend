from flask_restful import Resource, reqparse

from app.service.user import user_login


class UserView(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, location='json')
        self.parser.add_argument('password', type=str, location='json')
        super(UserView, self).__init__()

    def post(self):
        email = self.parser.parse_args()['email']
        password = self.parser.parse_args()['password']
        data = user_login(email, password)
        if data is False:
            return {"code": 404}
        else:
            return data