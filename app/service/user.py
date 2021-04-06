from app.db.base_mysql import SQLManager


def user_login(email, password):
    db = SQLManager()
    sql = "select * from user"
    users = db.get_list(sql)
    db.close()
    data = {}
    for user in users:
        if user["email"] == email and user["password"] == password:
            data["username"] = user["username"]
            data["auths"] = user["auths"]
            data["super"] = user["super"]
            return data
    return False

def user_list():
    db = SQLManager()
    sql = "select * from user"
    user_list = db.get_list(sql)
    db.close()
    return user_list

def user_auths_modify(userid, auths):
    db = SQLManager()
    sql = "update user set auths=%d where userid=%d" % (auths, userid)
    flag = False
    if (sql):
        result = db.modify(sql)
        flag = result == 1
        db.close()
    return flag

def user_delete(id):
    db = SQLManager()
    sql = "delete from user where userid=%d" % id
    # 这里应该有判断
    result1 = db.modify(sql)
    db.close()
    if result1 == 0:
        return False
    else:
        return True