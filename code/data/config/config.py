import json

def update_data (path:str, data):
    with open(path, "w", encoding="utf8") as archive:
        data = json.dump(data,archive,indent=4)

def read_data(path:str) -> list[dict]:
    with open(path, "r", encoding="utf8") as archive:
        data = json.load(archive)
    
    return data

