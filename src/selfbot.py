import requests
import time
import random
import os
from concurrent.futures import ThreadPoolExecutor

def send_file(token, channel_url, file_path):
    url = channel_url
    files = {"file": open(file_path, "rb")}
    headers = {"Authorization": token}
    res = requests.post(url, files=files, headers=headers)

def send_message(token, channel_url, message):
    url = channel_url
    payload = {"content": message}
    headers = {"Authorization": token}
    res = requests.post(url, json=payload, headers=headers)

def get_files_in_folder(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def get_user_messages():
    messages = []
    while True:
        user_input = input("Enter your message (or press Enter twice to finish adding your message): ")
        if not user_input:
            break
        messages.append(user_input)
    return messages

def get_user_channels():
    channels = []
    while True:
        user_input = input("Enter channel URL (or press Enter twice to finish adding channels): ")
        if not user_input:
            break
        channels.append(user_input)
    return channels

def send_messages_in_parallel(token, user_channels, message):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda channel: send_message(token, channel, message), user_channels)

def send_files_in_parallel(token, user_channels, image_path):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda channel: send_file(token, channel, image_path), user_channels)

def main():
    # Add your user token and channels directly in the code
    token = "YOUR_USER_TOKEN"
    user_channels = [
        "https://discord.com/api/v9/channels/YOUR_CHANNEL_ID_1/messages",
        "https://discord.com/api/v9/channels/YOUR_CHANNEL_ID_2/messages"
        # Add more channel URLs as needed
    ]

    repeat_count = 30
    image_folder_path = "resources/images"  # Replace with your folder path

    print("Add your own messages. Press Enter twice to finish adding.")
    user_messages = get_user_messages()

    while True:
        for i in range(repeat_count):
            if random.choice([True, False]):  # Randomly choose whether to send a message or an image
                message = random.choice(user_messages)
                send_messages_in_parallel(token, user_channels, message)
            else:
                images = get_files_in_folder(image_folder_path)
                if images:
                    image_path = os.path.join(image_folder_path, random.choice(images))
                    send_files_in_parallel(token, user_channels, image_path)

            # time.sleep(1) <-- uncomment to change the time between sending each message

        print(f"{repeat_count} messages/images sent to {len(user_channels)} channels. Wait 5 seconds before resending.")
        time.sleep(5)

        user_input = input("Do you want to send another 30 messages/images? (y/n): ")
        if user_input.lower() != 'y':
            break

if __name__ == "__main__":
    main()
