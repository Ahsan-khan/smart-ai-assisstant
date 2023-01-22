import random
import json
import pickle
import numpy as np
from textblob import TextBlob
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

class BotAIandAnalyzer:
    def __init__(self) -> None:
        self.sad_threshold = -0.15
        self.happy_threshold = 0.4
        self.happiness_level = 0
        self.employee_state = ""

        self.lemmatizer = WordNetLemmatizer()
        self.msgCounter = 0
        self.intents = json.loads(open('intents.json').read())

        self.words = pickle.load(open('words.pkl', 'rb'))
        self.classes = pickle.load(open('classes.pkl', 'rb'))

        self.model = load_model('chatbot_model.h5')

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word) for word in sentence_words]
        return sentence_words

    def bag_of_words(self, sentence):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for w in sentence_words:
            for i,word in enumerate(self.words):
                if word == w:
                    bag[i] = 1
        return np.array(bag)

    def predict_class(self, sentence):
        bow = self.bag_of_words(sentence)
        res = self.model.predict(np.array([bow]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i, r in enumerate(res) if r> ERROR_THRESHOLD]
        
        results.sort(key=lambda x: x[1], reverse=True)
        
        return_list = []
        
        for r in results:
            return_list.append({'intent': self.classes[r[0]], 'probability': str(r[1])})
            
        return return_list

    def get_response(self, intents_list, intents_json):
        #Could not find intent
        result = "Sorry I did not understand, please be more specific"
        tag = intents_list[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
        return result

    def get_score_and_employee_state(self, message):
        #happiness level is the metric used to determine employee hapiness
        blob = TextBlob(message)
        score = blob.sentiment[0]
        self.happiness_level = (self.happiness_level + score)/2
        if self.happiness_level >= self.happy_threshold:
            self.employee_state = "Happy"
            #print("Employee is happy")
        elif self.happiness_level <= self.sad_threshold:
            self.employee_state = "Sad"
            #print("Employee is sad")
        else:
            self.employee_state = "Neutral"
            #print("Employee is neutral")
        #return both 'employee_state' and 'happiness_level' to HR
        return (self.happiness_level, self.employee_state)

    def get_bot_reply(self, message):
        ints = self.predict_class(message)
        res = self.get_response(ints, self.intents)
        return res


# print("Bot Running")
        
# while True: 
#     #Employee input text
#     """message = input("")

#     #Sending employee message to chatbot and getting resply
#     reply = bot_reply(message)
#     print(reply)
#     """


#     #sentiment analysis
#     message_counter = message_counter + 1
#     blob = TextBlob(message)
#     average = average + blob.sentiment[0]
    
#     """#using happy_sad function to get happiness_level
#     employee_level = happy_sad(message, average, message_counter)[0]

#     #using happy_sad function to get employee_state
#     employee_level = happy_sad(message, average, message_counter)[1]
#     """

    
    