import random

#data
#greating 
gt = [
    "It is (12:00) , may I suggest you something to eat ?",
    "How are how today ?",
    "Ask me anything ?",
    "What is your name ?",
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "Your welcome."
    ]
kw = [
    "fat",
    "bitch",
    "cunt"
    ]
kw_response = [
    "that is not nice ",
    "why are you saying that ",
    "very not nice "
    ]
ph = [
    "how old are you ?",
    "how can I assit you today ?",
    "Have seen our new service ?",
    "Do you know our most popular service ?",
    "Do ypu want to view the listing of our services ?"
    ]
#
def hello(n):
    txt = "Hello vistor , my name is Laetitia , I am a chatbot . I will assist you ."
    print txt + gt[n]

# catch particular words
def key_words(msg):
    # do you want 'fattest' to trigger this?
    return [random.choice(kw_response) for k in kw if k in msg][0]

# check regular sentence
hello (random.randint(1,3))  # this does not 'check' for anything? assume will be used later in an input loop

txt = raw_input("Visitor :")
print key_words(txt)
  






