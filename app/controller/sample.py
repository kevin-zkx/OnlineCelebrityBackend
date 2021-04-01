from flask_restful import Resource, reqparse

from app.db.util import get_count
from app.service.sample import sample_to_promote, sample_delete, sample_list, sample_modify


class SampleListView(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=int, location='form')
        self.parser.add_argument('website', type=str, location='form')
        self.parser.add_argument('celebrityname', type=str, location='form')
        self.parser.add_argument('email', type=str, location='form')
        self.parser.add_argument('s_product', type=str, location='form')
        self.parser.add_argument('country', type=str, location='form')
        self.parser.add_argument('state', type=str, location='form')
        self.parser.add_argument('city', type=str, location='form')
        self.parser.add_argument('address', type=str, location='form')
        self.parser.add_argument('phone', type=str, location='form')
        self.parser.add_argument('postcode', type=str, location='form')
        self.parser.add_argument('s_order', type=str, location='form')
        self.parser.add_argument('sample_date', type=str, location='form')
        super(SampleListView, self).__init__()

    # 修改资源
    def post(self):
        data = {}
        data['c_id'] = self.parser.parse_args()['c_id']
        data['website'] = self.parser.parse_args()['website']
        data['celebrityname'] = self.parser.parse_args()['celebrityname']
        data['email'] = self.parser.parse_args()['email']
        data['s_product'] = self.parser.parse_args()['s_product']
        data['country'] = self.parser.parse_args()['country']
        data['state'] = self.parser.parse_args()['state']
        data['city'] = self.parser.parse_args()['city']
        data['address'] = self.parser.parse_args()['address']
        data['phone'] = self.parser.parse_args()['phone']
        data['postcode'] = self.parser.parse_args()['postcode']
        data['s_order'] = self.parser.parse_args()['s_order']
        data['sample_date'] = self.parser.parse_args()['sample_date']

        flag = sample_modify(data)
        if flag is False:
            return {"code": 404, "msg": "【更新寄样中信息】失败"}
        else:
            return {"code": 200, "msg": "【更新寄样中信息】成功"}

    # 查询所有数据
    def get(self):
        return {"code": 0, "msg": "【查询寄样中信息】成功", "count": get_count("sample", "s_display"), "data": sample_list()}

    # 删除单条数据
    def delete(self):
        id = self.parser.parse_args()['c_id']
        result = sample_delete(id)
        if result is True:
            return {"code": 200, "msg": "【删除寄样中信息】成功"}
        else:
            return {"code": 404, "msg": "【删除寄样中信息】失败"}

class Sample_to_Promote(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=int, location='form')
        super(Sample_to_Promote, self).__init__()

    # 修改资源
    def post(self):
        data = {}
        data['c_id'] = self.parser.parse_args()['c_id']

        flag = sample_to_promote(data['c_id'])
        if flag is False:
            return {"code": 404, "msg": "【寄样中-->已合作】转移失败"}
        else:
            return {"code": 200, "msg": "【寄样中-->已合作】转移成功"}