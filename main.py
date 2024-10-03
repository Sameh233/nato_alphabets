import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter : row.code for (index,row) in df.iterrows()}

def nato_alphabet():
    user_input = input("Enter a word: ").upper()
    try:
        result = [nato_alphabet_dict[letter] for letter in user_input]     
    except KeyError :
        print("Sorry, only letters in the alphabet please.")
        nato_alphabet()
    else:
        print(result)

nato_alphabet()
        

