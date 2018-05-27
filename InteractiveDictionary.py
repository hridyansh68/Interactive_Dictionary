import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) >0:
        yn = input("Did you mean "+get_close_matches(w,data.keys())[0]+". If yes type Y and if no type N:")
        if (yn=="Y" or yn=="y"):
            return data[get_close_matches(w,data.keys())[0]]
        elif (yn=="N" or yn=="n"):
            return "The word is not in our dictionary"
        else:
            return "Sorry we didn't understand your query"
    else:
        return "The word does not exist in dictionary"

word = input("Enter the word: ")
output=translate(word)

if(type(output)==list):
    for i in output:
        print(i)
else:
    print(output)
