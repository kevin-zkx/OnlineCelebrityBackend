def clear_data(data):
    for v in list(data.keys()):
        if data[v] is None:
            del data[v]
    return data