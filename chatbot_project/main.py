import nltk
pairs = [
    (["hello", "hi", "hey"], "Hi there! How can I assist you?"),
    (["weather"], "I can't have enough information! But I am learning."),
    (["what is your name"], "I'm a chatbot created by Hamza. You can call me Chatbot!"),
    (["how are you"], "I'm just a bunch of code, but I'm here to help you!"),
    (["bye"], "Goodbye! Have a great day!")
]
def chatbot_response(x):
    x = x.lower()
    for keywords, response in pairs:
        if any(keyword in x for keyword in keywords):
            return response
    return "sorry I didn't understand that!"
def main():
    print('Hi iam your chatbot')
    while True:
        x = input("you: ")
        if x == 'bye':
            print("chatbot: good bye! have a nice day")
            break
        response = chatbot_response(x)
        print("chatbot: ", response)
if  __name__ == "__main__":
    main()






