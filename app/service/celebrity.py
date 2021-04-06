from app.db.base_mysql import SQLManager


def celebrity_list():
    db = SQLManager()
    sql = "select * from v_celebrity"
    tablename = "v_celebrity"
    celebrity_list = db.get_list(sql)
    count = db.count(tablename)
    db.close()
    for celebrity in celebrity_list:
        if celebrity["d_addtime"] is not None:
            celebrity["d_addtime"] = celebrity["d_addtime"].strftime("%Y-%m-%d %H:%M:%S")
        if celebrity["c_addtime"] is not None:
            celebrity["c_addtime"] = celebrity["c_addtime"].strftime("%Y-%m-%d %H:%M:%S")
        if celebrity["s_sample_date"] is not None:
            celebrity["s_sample_date"] = celebrity["s_sample_date"].strftime("%Y-%m-%d %H:%M:%S")
    return count['count'], celebrity_list
