from flask_restful import Resource

from app.service.celebrity import celebrity_list


class CelebrityInfo(Resource):

    def get(self):
        count, data = celebrity_list()
        return {
            "code": 0,
            "msg": "【查询网红信息】成功",
            "count": count,
            "data": data
        }