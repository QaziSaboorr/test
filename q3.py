from matplotlib import pyplot as plt
import string

def count_letters(text):
    # Create a dictionary to store the letter frequency
    letter_count = {}
    for letter in string.ascii_lowercase:
        letter_count[letter] = 0
    
    # Iterate through each character in the text and update the count
    for char in text:
        if char.lower() in string.ascii_lowercase:
            letter_count[char.lower()] += 1
    
    return letter_count

f = open('2701-0.txt','r')
text = f.read()
letter_frequency = count_letters(text)
total_letters = sum(letter_frequency.values())
frequncy_list = [x/total_letters for x in letter_frequency.values()]
alphabets_list  = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
res = "\n".join("{} {}".format(x, y) for x, y in zip(alphabets_list, frequncy_list))
print(res)
plt.xlabel("Alphabet frequency")
plt.hist(frequncy_list,bins = 26,rwidth=0.9)
plt.show()