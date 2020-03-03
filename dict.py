import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("dictionary.json"))

def meaning(word):
    word = word.upper()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0 :
        print("You have entered a wrong word!")
        print("Did you mean: {}".format(get_close_matches(word,data.keys())[0]))
        answer = input("Y or N : ")
        if answer == "Y" :
            return meaning(get_close_matches(word,data.keys())[0])
        elif answer == "N" :
            print("Is your word in the list- {}".format(get_close_matches(word,data.keys(),n=5)))
            if input("Y or N: ") == "Y": 
                choice = int(input("Enter index of word in the list: "))
                return "{} :- ".format(get_close_matches(word,data.keys(),n=5)[choice]) +meaning(get_close_matches(word,data.keys(),n=5)[choice])
            else: return "your word was not present, Sorry!"
        else: return "your word was not present, Sorry!"
    else : return "Entry not understood, Sorry!"
word = input("Enter a word : ")
print(meaning(word))