from datetime import datetime

from app.db.base_mysql import SQLManager


def develop_add(data_1, data_2):
    db = SQLManager()
    sql1 = ""
    sql2 = ""
    flag = False
    table_1 = 'celebrity'
    table_2 = 'develop'
    time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    data_2["addtime"] = time
    if (data_1):
        sql1 = db.get_insert_sql(table_1, data_1)
    if (sql1):
        result_1 = db.create(sql1)
        if result_1 is not None:
            data_2["c_id"] = result_1
            flag = True
    if (data_2):
        sql2 = db.get_insert_sql(table_2, data_2)
    if (sql2):
        result_2 = db.create(sql2)
        if result_2 is not None:
            flag = True
    db.close()
    return flag

def develop_list():
    db = SQLManager()
    sql = "select * from v_develop where d_display=1"
    develop_list = db.get_list(sql)
    db.close()
    for develop in develop_list:
        develop["addtime"] = develop["addtime"].strftime("%Y-%m-%d %H:%M:%S")
    return develop_list

def develop_modify(data):
    db = SQLManager()

    sql = "update celebrity,develop \
            set website=%r,star=%r,as_score=%r,celebrityname=%r,email=%r,youtube=%r,youtube_star=%r,facebook=%r,ins=%r,\
            d_way=%r,d_remark=%r,d_principal=%r\
            where celebrity.celebrityid=develop.c_id\
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
        data['d_way'], \
        data['d_remark'], \
        data['d_principal'], \
        data['c_id']
    )
    flag = False
    if(data):
        result = db.modify(sql)
        flag = result is not 0
    db.close()
    return flag


def develop_delete(id):
    db = SQLManager()
    sql1 = "delete from develop where c_id=%d" % id
    sql2 = "delete from celebrity where celebrityid=%d" % id
    # 这里应该有判断
    result1 = db.modify(sql1)
    if result1 == 0:
        return False
    else:
        result2 = db.modify(sql2) # 删除数据有问题
        db.close()
        if result2 == 0:
            return False
        return True

def develop_to_cooperation(id):
    db = SQLManager()
    sql1 = "select c_id,d_status,d_display from develop where c_id=%d" % id
    sql2 = "update develop set d_status=1,d_display=0 where c_id=%d" % id
    sql3 = "insert into cooperation(c_id) values(%d)" % id

    result = db.get_one(sql1)
    if result is not None:
        if result['d_status'] == 1 and result['d_display'] == 0:
            return False
        db.modify(sql2)
        db.create(sql3)
        db.close()
        return True
    else:
        return False