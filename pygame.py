import quick_start


def print_hello():
    name = input("What's your name? ")
    print(f'Hello, {name}')
    age = input(f"What's your age {name}? ")
    if int(age) > 30:
        greeting_text = f"Nice to meet you, {name}! You are {age} years old."
        print(greeting_text)
        quick_start.greet(greeting_text)
    else :
        greeting_text = f"Hey {name}, I am also {age} years old."
        print(greeting_text)
        quick_start.greet(greeting_text)