from flask_restful import Api
from flask import Flask
from flask_cors import CORS

from app.controller.celebrity import CelebrityInfo
from app.controller.cooperation import CooperationListView, Cooperation_to_Sample
from app.controller.promote import PromoteListView
from app.controller.sample import Sample_to_Promote, SampleListView
from app.controller.user import UserView, UserAuthsView
from app.controller.develop import DevelopView, DevelopListView, Develop_to_Cooperation, Develop_Search

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

api.add_resource(UserView, '/user/login/', endpoint='user_login') #post
api.add_resource(UserView, '/user/', endpoint='user_list') #get
api.add_resource(UserAuthsView, '/user-auths/', endpoint='user_auths_modify') #post
api.add_resource(UserAuthsView, '/user/', endpoint='user_del') #del

api.add_resource(DevelopListView, '/develop/', endpoint='develop_add') #post
api.add_resource(DevelopListView, '/develop/', endpoint='develop_list') #get
api.add_resource(DevelopView, '/develop/', endpoint='develop_delete') #delete
api.add_resource(DevelopView, '/develop/modify/', endpoint='develop_modify') #post
api.add_resource(Develop_to_Cooperation, '/develop-to-cooperation/', endpoint='develop_to_cooperation') #post
# api.add_resource(Develop_Search, '/develop/find/', endpoint='develop_search') #get

api.add_resource(CooperationListView, '/cooperation/', endpoint='cooperation_modify') #post
api.add_resource(CooperationListView, '/cooperation/', endpoint='cooperation_list') #get
api.add_resource(CooperationListView, '/cooperation/', endpoint='cooperation_delete') #delete
api.add_resource(Cooperation_to_Sample, '/cooperation-to-sample/', endpoint='cooperation_to_sample') #post

api.add_resource(SampleListView, '/sample/', endpoint='sample_modify') #post
api.add_resource(SampleListView, '/sample/', endpoint='sample_list') #get
api.add_resource(SampleListView, '/sample/', endpoint='sample_delete') #delete
api.add_resource(Sample_to_Promote, '/sample-to-promote/', endpoint='sample_to_promote') #post

api.add_resource(PromoteListView, '/promote/', endpoint='promote_modify') #post
api.add_resource(PromoteListView, '/promote/', endpoint='promote_list') #get
api.add_resource(PromoteListView, '/promote/', endpoint='promote_delete') #delete

api.add_resource(CelebrityInfo, '/celebrity/', endpoint='celebrity_list') #get

if __name__ == '__main__':
    app.run()