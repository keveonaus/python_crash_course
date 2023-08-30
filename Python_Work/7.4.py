prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished with your toppings. "

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f"Adding {message.title()} to your pizza!")