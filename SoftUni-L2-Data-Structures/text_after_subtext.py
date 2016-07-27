# Напишете код, който взима два текста от потребителя, използвайки input(), след което покажете първия текст,
# но само частта, която се намира след втория текст.

text = input("Write a sentence: \n")
word = input("Write a word or a symbol that is a part of the first sentence: \n")

start_index = text.find(word)
if start_index == -1:
    print('"{}" wasn\'t found in the sentence "{}".' .format(word, text))
else:
    print(text[start_index + len(word):])
