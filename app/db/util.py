from app.db.base_mysql import SQLManager


def clear_data(data):
    for v in list(data.keys()):
        if data[v] is None:
            del data[v]
    return data

def get_count(tablename, condition):
    db = SQLManager()
    a = db.count_item(tablename, condition)
    db.close()
    return a["count"]
