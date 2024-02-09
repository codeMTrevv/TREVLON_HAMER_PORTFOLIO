import nltk
from nltk.chat.util import Chat, reflections

print("Hello, i am Giddeon. How may i help you today?")

pairs = [
    [
        r"(.*) my name is (.*)",
        ["Hello 2%, i am Giddeon. How may i help you today?"],
    ],
    [
        r"hi|hey|hello",
        ["Hello, whats up?","How may i assist you?","how can i help today?"],
    ],
    [
        r"what is your name?",
        ["it is Giddeon. and what is your name?"],
    ],
    [
        r"how are you?",
        ["I am fine today. all my interior specs seems to be functioning well at the moment."],
    ],
    [
        r"(.*) ",
        ["I have not yet been updated with the way to respond to such a input. sorry for the inconvience"],
    ],
    [
        r"quit",
        ["Bye have good day!"],
    ]
]


class Giddeon_chat(Chat):
    def converse(self, quit="quit"):
        user_chat = ""
        while user_chat != quit:
            user_chat = quit
            try:
                user_chat = input("You: ")
            except EOFError:
                print(user_chat)
            if user_chat:
                while user_chat[-1] in "!.":
                    user_chat = user_chat[:-1]
                response = self.respond(user_chat)
                print("Giddeon: " + response)
    

Giddeon = Giddeon_chat(pairs,reflections)
Giddeon.converse() 