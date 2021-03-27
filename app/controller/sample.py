from flask_restful import Resource, reqparse

from app.db.util import clear_data
from app.service.sample import sample_to_promote, sample_delete, sample_list, sample_modify


class SampleListView(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=int, location='json')
        self.parser.add_argument('website', type=str, location='json')
        self.parser.add_argument('celebrityname', type=str, location='json')
        self.parser.add_argument('email', type=str, location='json')
        self.parser.add_argument('s_product', type=str, location='json')
        self.parser.add_argument('country', type=str, location='json')
        self.parser.add_argument('state', type=str, location='json')
        self.parser.add_argument('city', type=str, location='json')
        self.parser.add_argument('address', type=str, location='json')
        self.parser.add_argument('phone', type=str, location='json')
        self.parser.add_argument('postcode', type=str, location='json')
        self.parser.add_argument('order', type=str, location='json')
        self.parser.add_argument('sample_date', type=str, location='json')
        super(SampleListView, self).__init__()

    # 修改资源
    def post(self):
        celebrity = {}
        sample = {}
        celebrity['c_id'] = self.parser.parse_args()['c_id']
        celebrity['website'] = self.parser.parse_args()['website']
        celebrity['celebrityname'] = self.parser.parse_args()['celebrityname']
        celebrity['email'] = self.parser.parse_args()['email']
        sample['s_product'] = self.parser.parse_args()['s_product']
        sample['country'] = self.parser.parse_args()['country']
        sample['state'] = self.parser.parse_args()['state']
        sample['city'] = self.parser.parse_args()['city']
        sample['address'] = self.parser.parse_args()['address']
        sample['phone'] = self.parser.parse_args()['phone']
        sample['postcode'] = self.parser.parse_args()['postcode']
        sample['order'] = self.parser.parse_args()['order']
        sample['sample_date'] = self.parser.parse_args()['sample_date']

        celebrity = clear_data(celebrity)
        sample = clear_data(sample)
        flag = sample_modify(celebrity, sample)
        if flag is False:
            return {"code": 404, "description": "更新失败"}
        else:
            return {"code": 200, "description": "更新成功"}

    # 查询所有数据
    def get(self):
        return sample_list()

    # 删除单条数据
    def delete(self):
        id = self.parser.parse_args()['c_id']
        result = sample_delete(id)
        if result is True:
            return {"code": 200, "description": "删除成功"}
        else:
            return {"code": 404, "description": "删除失败"}

class Sample_to_Promote(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('c_id', type=str, location='json')
        super(Sample_to_Promote, self).__init__()

    # 修改资源
    def post(self):
        data = {}
        data['c_id'] = int(self.parser.parse_args()['c_id'])

        flag = sample_to_promote(data['c_id'])
        if flag is False:
            return {"code": 404, "description": "更新失败"}
        else:
            return {"code": 200, "description": "更新成功"}