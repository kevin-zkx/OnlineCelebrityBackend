from app.db.base_mysql import SQLManager


def user_login(email, password):
    db = SQLManager()
    sql = "select * from user"
    users = db.get_list(sql)
    db.close()
    data = {}
    for user in users:
        if user['email'] == email and user['password'] == password:
            data['username'] = user['username']
            data['auths'] = user['auths']
            return data
    return False
