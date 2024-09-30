import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter : row.code for (index,row) in df.iterrows()}

user_input = input("Enter a word: ").upper()

# getting the 
result = [nato_alphabet_dict[letter] for letter in user_input]
           
print(result)

