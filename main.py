from assistant.brain import ask_ai
from assistant.voice import speak

while True:
    user = input("You: ")

    if user == "exit":
        break

    answer = ask_ai(user)

    print("AI:", answer)

    speak(answer)
