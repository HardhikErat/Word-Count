introString=input("Enter your intro: ")
characterCount=0
wordCount=1
for i in introString:
    characterCount+=1
    if(i==' '):
        wordCount+=1
print("Number of words in the input string: ")
print(wordCount)
print("Number of characters in the input string: ")
print(characterCount)