import random

file = open("data.txt", 'r')
name = file.read()

bot_name = "Max"
print(f"Hello, I'm {bot_name}.")
user_name = input("What is your name? ")

if user_name == name:
    print(f"Welcome back, {user_name}!")
else:
    file = open("data.txt", 'w')
    file.write(user_name)
    file.close()



    print(f"I'm glad to meet you, {user_name}.")



jokes = ["Почему компьютер замёрз? Он оставил открытыми все окна! 🥶",
    "Что сказал ноль восьмёрке? Классный ремень! 😄",
    "Почему робот пошёл в школу? Чтобы прокачать свои микросхемы! 🤖",]
not_understood = ["I didn't get it", "Write HELP"]
while True:
    text = input(f"{user_name}:")

    if text == "hello":
        print(f"Hello, {user_name}.")
    elif text == "how are you":
        print(f"Excellent.")
    elif text == "joke":
        print("🤖" + random.choice(jokes))

    else:
        print(f"Don't understand.")