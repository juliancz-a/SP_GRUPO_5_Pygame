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
pprint.pprint(data, indent=4)
# update_data(r"code\data\data.json", data)

# import json
# print()
# import re


# def repl_func(match: re.Match):
#     return " ".join(match.group().split())


# def main():
#     data = {
#         "lists": [
#             [1, 2, 3],
#             [4, 5, 6]
#         ],
#         "who": "me"
#     }

#     json_str = json.dumps(data, indent=4)
#     print(json_str)
#     print()
    
#     json_str = re.sub(r"(?<=\[)[^\[\]]+(?=])", repl_func, json_str)
#     print(json_str)

# main()