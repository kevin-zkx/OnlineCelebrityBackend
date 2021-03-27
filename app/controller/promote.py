from flask_restful import Resource, reqparse

from app.db.util import clear_data
from app.service.promote import promote_modify, promote_list, promote_delete


class PromoteListView(Resource):
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
        self.parser.add_argument('p_way', type=str, location='json')
        self.parser.add_argument('p_remark', type=str, location='json')
        self.parser.add_argument('p_principal', type=str, location='json')
        self.parser.add_argument('p_product', type=str, location='json')
        self.parser.add_argument('product_cost', type=int, location='json')
        self.parser.add_argument('transfer_cost', type=int, location='json')
        self.parser.add_argument('url', type=str, location='json')
        self.parser.add_argument('join_league', type=int, location='json')
        super(PromoteListView, self).__init__()

    # 修改资源
    def post(self):
        celebrity = {}
        promote = {}
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
        # promote['s_product'] = self.parser.parse_args()['s_product']
        promote['p_way'] = self.parser.parse_args()['p_way']
        promote['p_remark'] = self.parser.parse_args()['p_remark']
        promote['p_principal'] = self.parser.parse_args()['p_principal']
        promote['p_product'] = self.parser.parse_args()['p_product']
        promote['product_cost'] = self.parser.parse_args()['product_cost']
        promote['transfer_cost'] = self.parser.parse_args()['transfer_cost']
        promote['url'] = self.parser.parse_args()['url']
        promote['join_league'] = self.parser.parse_args()['join_league']

        celebrity = clear_data(celebrity)
        promote = clear_data(promote)
        flag = promote_modify(celebrity, promote)
        if flag is False:
            return {"code": 404, "description": "更新失败"}
        else:
            return {"code": 200, "description": "更新成功"}

    # 查询所有数据
    def get(self):
        return promote_list()

    # 删除单条数据
    def delete(self):
        id = self.parser.parse_args()['c_id']
        result = promote_delete(id)
        if result is True:
            return {"code": 200, "description": "删除成功"}
        else:
            return {"code": 404, "description": "删除失败"}