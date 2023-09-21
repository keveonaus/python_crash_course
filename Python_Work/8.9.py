def show_messages(messages):
    """Showing short messages"""
    for message in messages:
        print(message.title())

messages = ['how are you?', 'have a great day!', 'go packers!']
show_messages(messages)