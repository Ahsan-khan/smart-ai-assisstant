from textblob import TextBlob

sad_threshold = -0.15
happy_threshold = 0.4
average = 0
message_counter = 0
happiness_level = 0

print("Enter text: ")

while True: 
    message = input("")
    message_counter = message_counter + 1
    blob = TextBlob(message)
    average = average + blob.sentiment[0]
    happiness_level = average/message_counter
    print(happiness_level)
    if happiness_level >= happy_threshold:
        print("Employee is happy")
    elif happiness_level <= sad_threshold:
        print("Employee is sad")
    else:
        print("Employee is neutral")





"""text = "I am super happy and excited"
print(text)

blob = TextBlob(text)
print(blob.sentiment[0])

print("end")
"""