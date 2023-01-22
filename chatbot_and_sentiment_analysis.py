import random
import json
import pickle
import numpy as np
from textblob import TextBlob
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

sad_threshold = -0.15
happy_threshold = 0.4
average = 0
message_counter = 0
happiness_level = 0
employee_state = ""

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r> ERROR_THRESHOLD]
    
    results.sort(key=lambda x: x[1], reverse=True)
    
    return_list = []
    
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
        
    return return_list

def get_response(intents_list, intents_json):
    result = "empty"
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def happy_sad(message, average, message_counter):
    

    #happiness level is the metric used to determine employee hapiness
    happiness_level = average/message_counter
    if happiness_level >= happy_threshold:
        employee_state = "Happy"
        #print("Employee is happy")
    elif happiness_level <= sad_threshold:
        employee_state = "Sad"
        #print("Employee is sad")
    else:
        employee_state = "Neutral"
        #print("Employee is neutral")
    #return both 'employee_state' and 'happiness_level' to HR
    print(happiness_level)
    return happiness_level, employee_state

def bot_reply(message):
    ints = predict_class(message)
    res = get_response(ints, intents)
    return res


print("Bot Running")
        
while True: 
    #Employee input text
    """message = input("")

    #Sending employee message to chatbot and getting resply
    reply = bot_reply(message)
    print(reply)
    """


    #sentiment analysis
    message_counter = message_counter + 1
    blob = TextBlob(message)
    average = average + blob.sentiment[0]
    
    """#using happy_sad function to get happiness_level
    employee_level = happy_sad(message, average, message_counter)[0]

    #using happy_sad function to get employee_state
    employee_level = happy_sad(message, average, message_counter)[1]
    """

    
    