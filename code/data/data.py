import json
import pprint
def update_data (path:str, data):
    with open(path, "w", encoding="utf8") as archive:
        data = json.dump(data, archive,indent=4)

data = [
    {"P, R, O, A, E, S": 
    [
        "aperos", "apreso", "aproes", "arpeos",
        "aspero", "espora", "operas", "opresa",
        "pareos", "pasero", "peoras", "posare", 
        "raspeo", "repaso", "reposa", "separo",
        "sopare", "sopear", "sopera", "pares",
        "opera", "preso", "sopar", "rapos", "paseo",
        "pera", "pose", "paro", "ropa", "sapo", 
        "repo", "rapo", "pos", "rap", "res", "par"
    ],

    "R, C, A, E, S, E": 
    [
        "aceras", "acreas", "arcase", "arceas",
        "careas", "caresa", "casare", "casera",
        "resaca", "sacare", "sacare", "secara",
        "cesara", "cesara", "escara"
    ]
    }
    ]

update_data(r"code\data\data.json", data)
