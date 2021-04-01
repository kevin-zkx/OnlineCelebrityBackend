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

def sample_modify(data):
    db = SQLManager()

    sql = "update celebrity,sample \
                set website=%r,celebrityname=%r,email=%r,\
                s_product=%r,country=%r,state=%r,city=%r,address=%r,phone=%r,postcode=%r,s_order=%r,sample_date=%r\
                where celebrity.celebrityid=sample.c_id\
                and c_id=%d" % ( \
        data['website'], \
        data['celebrityname'], \
        data['email'], \
        data['s_product'], \
        data['country'], \
        data['state'], \
        data['city'], \
        data['address'], \
        data['phone'], \
        data['postcode'], \
        data['s_order'], \
        data['sample_date'], \
        data['c_id']
    )
    flag = False
    if (data):
        result = db.modify(sql)
        flag = result is not 0
    db.close()
    return flag

def sample_delete(id):
    db = SQLManager()

    sql1 = "delete from sample where c_id=%d" % id
    sql2 = "update cooperation set c_status=0,c_display=1 where c_id=%d" % id
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
    sql1 = "select c_id,sign_for,s_display,s_product from sample where c_id=%d" % id
    sql2 = "update sample set sign_for=1,s_display=0 where c_id=%d" % id
    result = db.get_one(sql1)
    if result is not None:
        if result['sign_for'] == 1 and result['s_display'] == 0:
            return False
        if result['s_product'] is None:
            sql3 = "insert into promote(c_id) values(%d)" % id
        else:
            sql3 = "insert into promote(c_id,p_product) values(%d, %r)" % (id,result['s_product'])
        db.modify(sql2)
        db.create(sql3)
        db.close()
        return True
    else:
        return False