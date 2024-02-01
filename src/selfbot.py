import requests
import time
import random

def send_message(token, message):
    url = "" #HERE GOES YOUR REQUEST URL
    payload = {"content": message}
    headers = {"Authorization": token}
    res = requests.post(url, json=payload, headers=headers)

def get_user_messages():
    messages = []
    while True:
        user_input = input("Enter your message (or press Enter twice to finish adding your message):")
        if not user_input:
            break
        messages.append(user_input)
    return messages

def main():
    token = "" #HERE GOES YOUR USER TOKEN
    repeat_count = 30

    print("Add your own messages. Press Enter twice to finish adding.")
    user_messages = get_user_messages()

    while True:
        for i in range(repeat_count):
            message = random.choice(user_messages)
            send_message(token, message)
            #time.sleep(1) <-- uncomment to change the time between sending each message

        print(f"{repeat_count} messages sent. Wait 5 seconds before resending.")
        time.sleep(5)

        user_input = input("Do you want to send another 30 messages? (y/n): ")
        if user_input.lower() != 'y':
            break

if __name__ == "__main__":
    main()