from flask_restful import Resource, reqparse

from app.db.util import get_count
from app.service.promote import promote_modify, promote_list, promote_delete


class PromoteListView(Resource):
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
        self.parser.add_argument('p_way', type=str, location='form')
        self.parser.add_argument('p_remark', type=str, location='form')
        self.parser.add_argument('p_principal', type=str, location='form')
        self.parser.add_argument('p_product', type=str, location='form')
        self.parser.add_argument('product_cost', type=str, location='form')
        self.parser.add_argument('transfer_cost', type=str, location='form')
        self.parser.add_argument('url', type=str, location='form')
        self.parser.add_argument('join_league', type=str, location='form')
        super(PromoteListView, self).__init__()

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

        data['p_way'] = self.parser.parse_args()['p_way']
        data['p_remark'] = self.parser.parse_args()['p_remark']
        data['p_principal'] = self.parser.parse_args()['p_principal']
        # data['p_product'] = self.parser.parse_args()['p_product']
        data['product_cost'] = self.parser.parse_args()['product_cost']
        data['transfer_cost'] = self.parser.parse_args()['transfer_cost']
        data['url'] = self.parser.parse_args()['url']
        data['join_league'] = self.parser.parse_args()['join_league']

        flag = promote_modify(data)
        if flag is False:
            return {"code": 404, "msg": "【更新已合作信息】失败"}
        else:
            return {"code": 200, "msg": "【更新已合作信息】成功"}

    # 查询所有数据
    def get(self):
        return {"code": 0, "msg": "【查询已合作信息】成功", "count": get_count("promote", "p_display"), "data": promote_list()}

    # 删除单条数据
    def delete(self):
        id = self.parser.parse_args()['c_id']
        result = promote_delete(id)
        if result is True:
            return {"code": 200, "msg": "【删除已合作信息】成功"}
        else:
            return {"code": 404, "msg": "【删除已合作信息】失败"}