import random

# This does random numbers
# def main():
#     randnums = [72.4, 37, 56, 12]
#     print(randnums)
#     
#     append_random_numbers(randnums)
#     print(randnums)

#     append_random_numbers(randnums, quantity=3)
#     print(randnums)

# def append_random_numbers(numbers_list, quantity=1):

#     for i in range(quantity):
#         random_num = random.uniform(0, 100)
#         numbers_list.append(round(random_num, 1))

#this does random words from the words list
def main():
    words = ['hello', 'goodbye' , 'python', 'potato', 'screen', 'watch', 'alpha']
    randwords = []
    
    append_random_words(randwords, words)
    print(randwords)

    append_random_words(randwords, words, quantity=8)
    print(randwords)

def append_random_words(words_list, words, quantity=1):

    for i in range(quantity):
        random_index = random.randint(0, len(words) - 1)
        random_word = words[random_index]
        words_list.append(random_word)

main()