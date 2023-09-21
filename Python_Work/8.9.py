def send_messages(unsent_messages, sent_messages):
    """Showing short messages"""
    while unsent_messages:
        sending_messages = unsent_messages.pop()
        print(f"{sending_messages}")
        sent_messages.append(send_messages)

def show_sent_messages(sent_messages):
    """Show sending the messages"""
    for sent_message in sent_messages:
        print(sent_message)

unsent_messages = ['How are you?', 'Have a great day!', 'Go Packers!']
sent_messages = []

send_messages(unsent_messages, sent_messages)
show_sent_messages(sent_messages)