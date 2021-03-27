from app.db.base_mysql import SQLManager


def promote_list():
    db = SQLManager()
    sql = "select * from v_promote where p_display=1"
    promote_list = db.get_list(sql)
    db.close()
    # for promote in promote_list:
    #     if promote["sample_date"] is not None:
    #         promote["sample_date"] = promote["sample_date"].strftime("%Y-%m-%d %H:%M:%S")
    return promote_list

def promote_modify(data_1, data_2):
    db = SQLManager()

    table_1 = 'celebrity'
    table_2 = 'promote'
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

def promote_delete(id):
    db = SQLManager()
    sql1 = "delete from promote where c_id=%d" % id
    sql2 = "update sample set sign_for=0,s_display=1 where c_id=%d" % id
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