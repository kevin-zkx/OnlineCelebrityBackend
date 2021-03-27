from datetime import datetime

from app.db.base_mysql import SQLManager

def develop_add(data):
    db = SQLManager()
    sql1 = "insert into celebrity(website, star, as_score, celebrityname, email, youtube, youtube_star, facebook, ins) \
            values ('%s', %d, %d, '%s', '%s', '%s', %d, '%s', '%s')" % ( \
                data['website'], \
                data['star'], \
                data['as_score'], \
                data['celebrityname'], \
                data['email'], \
                data['youtube'], \
                data['youtube_star'], \
                data['facebook'], \
                data['ins'])
    celebrityid = db.create(sql1)

    time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    sql2 = "insert into develop(c_id, d_way, d_remark, d_principal, addtime) \
            values (%d, '%s', '%s', '%s', '%s')" % ( \
                celebrityid, \
                data['d_way'], \
                data['d_remark'], \
                data['d_principal'], \
                str(time))
    result = db.create(sql2)
    db.close()
    if result is not None:
        return True
    return False

def develop_list():
    db = SQLManager()
    sql = "select * from v_develop where d_display=1"
    develop_list = db.get_list(sql)
    db.close()
    for develop in develop_list:
        develop["addtime"] = develop["addtime"].strftime("%Y-%m-%d %H:%M:%S")
    return develop_list

def develop_modify(data_1, data_2):
    db = SQLManager()

    table_1 = 'celebrity'
    table_2 = 'develop'
    condition_1 = ('celebrityid', data_1['c_id'])  # 更新所需条件
    condition_2 = ('c_id', data_1['c_id'])  # 更新所需条件
    del data_1['c_id']
    # 数据要划分为cerebrity和develop两张表的字段再更新数据
    sql1 = ""
    sql2 = ""
    if(data_1):
        sql1 = db.get_update_one_sql(table_1, data_1, condition_1)
    if(data_2):
        sql2 = db.get_update_one_sql(table_2, data_2, condition_2)
    # 这里应该有问题，如果result_1为False，result_2为True，怎么办
    if(sql1):
        result_1 = db.modify(sql1)
        flag = result_1 == 1
    if(sql2):
        result_2 = db.modify(sql2)
        flag = result_2 == 1
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