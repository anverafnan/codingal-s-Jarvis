import nltk 
from nltk.chat.util import Chat, reflections

reflection={
    "i am " : "you are ",
    "i was" : "you were",
    "i"     : "you",
    "i'm"   : "you are",
    "i'd"   : "you would",
    "i've"  : "you have",
    "i'll"  : "you will",
    "my"    : "your",
   "you are": "iam ",
  "you were": "i was ",
   "you've" : "i have",
   "you'll" : "i will",
   "my"     : "your",
   "you are": " iam ",
   "you were":" i was ",
   "you've": "i have",
   "you'll": "i will",
   "your"  : "my",
   "yours" : "mine",
   'you'   : "me",
   "me"    : "you"
   }

pairs=[
    [
        r"my name is (.*)",
        ["hello %1, How are you today?",]

    ],
    [
        r"hi|hey|hello",
        ["hello","hey there",]
    ],
]

def chat():
    print("hi! iam achat from codingal for your service")
    chat=Chat(pairs,reflections)
    chat.converse()

if __name__=="__main__":
    chat()
