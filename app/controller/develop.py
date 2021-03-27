from flask_restful import Resource, reqparse

from app.db.util import clear_data
from app.service.develop import develop_add, develop_list, develop_delete, develop_to_cooperation, develop_modify


class DevelopListView(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('website', type=str, location='json')
        self.parser.add_argument('star', type=int, location='json')
        self.parser.add_argument('as_score', type=int, location='json')
        self.parser.add_argument('celebrityname', type=str, location='json')
        self.parser.add_argument('email', type=str, location='json')
        self.parser.add_argument('youtube', type=str, location='json')
        self.parser.add_argument('youtube_star', type=int, location='json')
        self.parser.add_argument('facebook', type=str, location='json')
        self.parser.add_argument('ins', type=str, location='json')
        self.parser.add_argument('d_way', type=str, location='json')
        self.parser.add_argument('d_remark', type=str, location='json')
        self.parser.add_argument('d_principal', type=str, location='json')
        super(DevelopListView, self).__init__()

    # 添加资源
    def post(self):
        data = {}
        data['website'] = self.parser.parse_args()['website']
        data['star'] = self.parser.parse_args()['star']
        data['as_score'] = self.parser.parse_args()['as_score']
        data['celebrityname'] = self.parser.parse_args()['celebrityname']
        data['email'] = self.parser.parse_args()['email']
        data['youtube'] = self.parser.parse_args()['youtube']
        data['youtube_star'] = self.parser.parse_args()['youtube_star']
        data['facebook'] = self.parser.parse_args()['facebook']
        data['ins'] = self.parser.parse_args()['ins']
        data['d_way'] = self.parser.parse_args()['d_way']
        data['d_remark'] = self.parser.parse_args()['d_remark']
        data['d_principal'] = self.parser.parse_args()['d_principal']

        flag = develop_add(data)
        if flag is False:
            return {"code": 404}
        else:
            return {"code": 200}

    # 查询所有数据
    def get(self):
        # return {"code": 200, "test": "test_list"}
        return develop_list()

class DevelopView(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=int, location='json')
        self.parser.add_argument('website', type=str, location='json')
        self.parser.add_argument('star', type=int, location='json')
        self.parser.add_argument('as_score', type=int, location='json')
        self.parser.add_argument('celebrityname', type=str, location='json')
        self.parser.add_argument('email', type=str, location='json')
        self.parser.add_argument('youtube', type=str, location='json')
        self.parser.add_argument('youtube_star', type=int, location='json')
        self.parser.add_argument('facebook', type=str, location='json')
        self.parser.add_argument('ins', type=str, location='json')
        self.parser.add_argument('d_way', type=str, location='json')
        self.parser.add_argument('d_remark', type=str, location='json')
        self.parser.add_argument('d_principal', type=str, location='json')
        super(DevelopView, self).__init__()

    # 修改资源
    def post(self):
        celebrity = {}
        develop = {}
        celebrity['c_id'] = self.parser.parse_args()['c_id']
        celebrity['website'] = self.parser.parse_args()['website']
        celebrity['star'] = self.parser.parse_args()['star']
        celebrity['as_score'] = self.parser.parse_args()['as_score']
        celebrity['celebrityname'] = self.parser.parse_args()['celebrityname']
        celebrity['email'] = self.parser.parse_args()['email']
        celebrity['youtube'] = self.parser.parse_args()['youtube']
        celebrity['youtube_star'] = self.parser.parse_args()['youtube_star']
        celebrity['facebook'] = self.parser.parse_args()['facebook']
        celebrity['ins'] = self.parser.parse_args()['ins']
        develop['d_way'] = self.parser.parse_args()['d_way']
        develop['d_remark'] = self.parser.parse_args()['d_remark']
        develop['d_principal'] = self.parser.parse_args()['d_principal']

        celebrity = clear_data(celebrity)
        develop = clear_data(develop)
        flag = develop_modify(celebrity, develop)
        if flag is False:
            return {"code": 404, "description": "更新失败"}
        else:
            return {"code": 200, "description": "更新成功"}

    # 删除单条数据
    def delete(self):
        id = self.parser.parse_args()['c_id']
        result = develop_delete(id)
        if result is True:
            return {"code": 200, "description": "删除成功"}
        else:
            return {"code": 404, "description": "删除失败"}

class Develop_to_Cooperation(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=str, location='json')
        super(Develop_to_Cooperation, self).__init__()

    # 修改资源
    def post(self):
        data = {}
        data['c_id'] = int(self.parser.parse_args()['c_id'])

        flag = develop_to_cooperation(data['c_id'])
        if flag is False:
            return {"code": 404, "description": "更新失败"}
        else:
            return {"code": 200, "description": "更新成功"}