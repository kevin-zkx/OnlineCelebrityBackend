from app.db.base_mysql import SQLManager


def cooperation_list():
    db = SQLManager()
    sql = "select * from v_cooperation where c_display=1"
    cooperation_list = db.get_list(sql)
    db.close()
    for cooperation in cooperation_list:
        if cooperation["addtime"] is not None:
            cooperation["addtime"] = cooperation["addtime"].strftime("%Y-%m-%d %H:%M:%S")
    return cooperation_list

def cooperation_modify(data):
    db = SQLManager()

    sql = "update celebrity,cooperation \
                set website=%r,star=%r,as_score=%r,celebrityname=%r,email=%r,youtube=%r,youtube_star=%r,facebook=%r,ins=%r,\
                c_way=%r,c_remark=%r,c_principal=%r,c_channel=%r,addtime=%r\
                where celebrity.celebrityid=cooperation.c_id\
                and c_id=%d" % ( \
        data['website'], \
        data['star'], \
        data['as_score'], \
        data['celebrityname'], \
        data['email'], \
        data['youtube'], \
        data['youtube_star'], \
        data['facebook'], \
        data['ins'], \
        data['c_way'], \
        data['c_remark'], \
        data['c_principal'], \
        data['c_channel'], \
        data['addtime'], \
        data['c_id']
    )
    flag = False
    if (data):
        result = db.modify(sql)
        flag = result is not 0
    db.close()
    return flag

def cooperation_delete(id):
    db = SQLManager()
    sql1 = "delete from cooperation where c_id=%d" % id
    sql2 = "update develop set d_status=0,d_display=1 where c_id=%d" % id
    # 这里应该有判断
    result1 = db.modify(sql1)
    if result1 == 0:
        return False
    else:
        result2 = db.modify(sql2) # 有问题
        db.close()
        if result2 == 0:
            return False
        return True

def cooperation_to_sample(id):
    db = SQLManager()
    sql1 = "select c_id,c_status,c_display from cooperation where c_id=%d" % id
    sql2 = "update cooperation set c_status=1,c_display=0 where c_id=%d" % id
    sql3 = "insert into sample(c_id) values(%d)" % id

    result = db.get_one(sql1)
    if result is not None:
        if result['c_status'] == 1 and result['c_display'] == 0:
            return False
        db.modify(sql2)
        db.create(sql3)
        db.close()
        return True
    else:
        return False