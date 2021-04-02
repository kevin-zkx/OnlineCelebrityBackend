from app.db.base_mysql import SQLManager


def promote_list():
    db = SQLManager()
    sql = "select * from v_promote"
    promote_list = db.get_list(sql)
    db.close()
    return promote_list

def promote_modify(data):
    db = SQLManager()

    if data['join_league'] is None:
        data['join_league'] = 0

    sql = "update celebrity,promote \
                    set website=%r,star=%r,as_score=%r,celebrityname=%r,email=%r,youtube=%r,youtube_star=%r,facebook=%r,ins=%r,\
                    p_way=%r,p_remark=%r,p_principal=%r,product_cost=%s,transfer_cost=%s,url=%r,join_league=%s \
                    where celebrity.celebrityid=promote.c_id\
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
        data['p_way'], \
        data['p_remark'], \
        data['p_principal'], \
        # data['p_product'], \
        data['product_cost'], \
        data['transfer_cost'], \
        data['url'], \
        data['join_league'], \
        data['c_id']
    )
    flag = False
    if (data):
        result = db.modify(sql)
        flag = result is not 0
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