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

def cooperation_modify(data_1, data_2):
    db = SQLManager()

    table_1 = 'celebrity'
    table_2 = 'cooperation'
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