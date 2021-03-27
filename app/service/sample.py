from app.db.base_mysql import SQLManager


def sample_list():
    db = SQLManager()
    sql = "select * from v_sample where s_display=1"
    sample_list = db.get_list(sql)
    db.close()
    for sample in sample_list:
        if sample["sample_date"] is not None:
            sample["sample_date"] = sample["sample_date"].strftime("%Y-%m-%d %H:%M:%S")
    return sample_list

def sample_modify(data_1, data_2):
    db = SQLManager()

    table_1 = 'celebrity'
    table_2 = 'sample'
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

def sample_delete(id):
    db = SQLManager()
    sql1 = "delete from sample where c_id=%d" % id
    sql2 = "update cooperation set c_status=0,c_display=1 where c_id=%d" % id
    # 这里应该有判断
    result1 = db.modify(sql1)
    if result1 == 0:
        return False
    else:
        result2 = db.modify(sql2)
        db.close()
        if result2 == 0:
            return False
        return True

def sample_to_promote(id):
    db = SQLManager()
    sql1 = "select c_id,sign_for,s_display from sample where c_id=%d" % id
    sql2 = "update sample set sign_for=1,s_display=0 where c_id=%d" % id
    sql3 = "insert into promote(c_id) values(%d)" % id

    result = db.get_one(sql1)
    if result is not None:
        if result['sign_for'] == 1 and result['s_display'] == 0:
            return False
        db.modify(sql2)
        db.create(sql3)
        db.close()
        return True
    else:
        return False