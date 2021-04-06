from flask_restful import Resource, reqparse

from app.service.user import user_login, user_list, user_auths_modify, user_delete


class UserView(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("email", type=str, location='form')
        self.parser.add_argument("password", type=str, location='form')
        super(UserView, self).__init__()

    def post(self):
        email = self.parser.parse_args()["email"]
        password = self.parser.parse_args()["password"]
        data = user_login(email, password)
        if data is False:
            return {"code": 404, "msg": "登录失敗"}
        else:
            return {"code": 10, "msg": "登录成功", "count": 2, "data": data}

    def get(self):
        return {"code": 0, "msg": "成功", "count": 7, "data": user_list()}

class UserAuthsView(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("userid", type=int, location='form')
        self.parser.add_argument("auths", type=int, location='form')
        super(UserAuthsView, self).__init__()

    def post(self):
        userid = self.parser.parse_args()["userid"]
        auths = self.parser.parse_args()["auths"]

        data = user_auths_modify(userid, auths)
        if data is False:
            return {"code": 404, "msg": "登录失敗"}
        else:
            return {"code": 200, "msg": "登录成功", "count": 2}

    def delete(self):
        id = self.parser.parse_args()['userid']
        result = user_delete(id)
        if result is True:
            return {"code": 200, "msg": "删除用户成功"}
        else:
            return {"code": 404, "msg": "删除用户失败"}
