from flask_restful import Resource, reqparse

from app.db.util import clear_data
from app.service.cooperation import cooperation_list, cooperation_modify, cooperation_delete, cooperation_to_sample


class CooperationListView(Resource):
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
        self.parser.add_argument('c_way', type=str, location='json')
        self.parser.add_argument('c_remark', type=str, location='json')
        self.parser.add_argument('c_principal', type=str, location='json')
        self.parser.add_argument('c_channel', type=str, location='json')
        super(CooperationListView, self).__init__()

    # 修改资源
    def post(self):
        celebrity = {}
        cooperation = {}
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
        cooperation['c_way'] = self.parser.parse_args()['c_way']
        cooperation['c_remark'] = self.parser.parse_args()['c_remark']
        cooperation['c_principal'] = self.parser.parse_args()['c_principal']
        cooperation['c_channel'] = self.parser.parse_args()['c_channel']

        celebrity = clear_data(celebrity)
        cooperation = clear_data(cooperation)
        flag = cooperation_modify(celebrity, cooperation)
        if flag is False:
            return {"code": 404, "description": "更新失败"}
        else:
            return {"code": 200, "description": "更新成功"}

    # 查询所有数据
    def get(self):
        return cooperation_list()

    # 删除单条数据
    def delete(self):
        id = self.parser.parse_args()['c_id']
        result = cooperation_delete(id)
        if result is True:
            return {"code": 200, "description": "删除成功"}
        else:
            return {"code": 404, "description": "删除失败"}

class Cooperation_to_Sample(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=str, location='json')
        super(Cooperation_to_Sample, self).__init__()

    # 修改资源
    def post(self):
        data = {}
        data['c_id'] = int(self.parser.parse_args()['c_id'])

        flag = cooperation_to_sample(data['c_id'])
        if flag is False:
            return {"code": 404, "description": "更新失败"}
        else:
            return {"code": 200, "description": "更新成功"}