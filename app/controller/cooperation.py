from flask_restful import Resource, reqparse

from app.db.util import get_count
from app.service.cooperation import cooperation_list, cooperation_modify, cooperation_delete, cooperation_to_sample


class CooperationListView(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=int, location='form')
        self.parser.add_argument('website', type=str, location='form')
        self.parser.add_argument('star', type=str, location='form')
        self.parser.add_argument('as_score', type=str, location='form')
        self.parser.add_argument('celebrityname', type=str, location='form')
        self.parser.add_argument('email', type=str, location='form')
        self.parser.add_argument('youtube', type=str, location='form')
        self.parser.add_argument('youtube_star', type=str, location='form')
        self.parser.add_argument('facebook', type=str, location='form')
        self.parser.add_argument('ins', type=str, location='form')
        self.parser.add_argument('c_way', type=str, location='form')
        self.parser.add_argument('c_remark', type=str, location='form')
        self.parser.add_argument('c_principal', type=str, location='form')
        self.parser.add_argument('c_channel', type=str, location='form')
        self.parser.add_argument('addtime', type=str, location='form')
        super(CooperationListView, self).__init__()

    # 修改资源
    def post(self):
        data = {}
        data['c_id'] = self.parser.parse_args()['c_id']
        data['website'] = self.parser.parse_args()['website']
        data['star'] = self.parser.parse_args()['star']
        data['as_score'] = self.parser.parse_args()['as_score']
        data['celebrityname'] = self.parser.parse_args()['celebrityname']
        data['email'] = self.parser.parse_args()['email']
        data['youtube'] = self.parser.parse_args()['youtube']
        data['youtube_star'] = self.parser.parse_args()['youtube_star']
        data['facebook'] = self.parser.parse_args()['facebook']
        data['ins'] = self.parser.parse_args()['ins']
        data['c_way'] = self.parser.parse_args()['c_way']
        data['c_remark'] = self.parser.parse_args()['c_remark']
        data['c_principal'] = self.parser.parse_args()['c_principal']
        data['c_channel'] = self.parser.parse_args()['c_channel']
        data['addtime'] = self.parser.parse_args()['addtime']

        flag = cooperation_modify(data)
        if flag is False:
            return {"code": 404, "msg": "【更新待合作信息】失败"}
        else:
            return {"code": 200, "msg": "【更新待合作信息】成功"}

    # 查询所有数据
    def get(self):
        return {"code": 0, "msg": "【查询待合作信息】成功", "count": get_count("cooperation", "c_display"), "data": cooperation_list()}

    # 删除单条数据
    def delete(self):
        id = self.parser.parse_args()['c_id']
        result = cooperation_delete(id)
        if result is True:
            return {"code": 200, "msg": "【删除待合作信息】成功"}
        else:
            return {"code": 404, "msg": "【删除待合作信息】失败"}


class Cooperation_to_Sample(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=int, location='form')
        super(Cooperation_to_Sample, self).__init__()

    # 修改资源
    def post(self):
        data = {}
        data['c_id'] = self.parser.parse_args()['c_id']

        flag = cooperation_to_sample(data['c_id'])
        if flag is False:
            return {"code": 404, "msg": "【待合作-->寄样中】转移失败"}
        else:
            return {"code": 200, "msg": "【待合作-->寄样中】转移成功"}
