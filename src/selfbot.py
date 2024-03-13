import requests
import time
import random
import os
from concurrent.futures import ThreadPoolExecutor

repeat_count = 0 # Don't change!

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

def get_user_input(prompt, exit_condition):
    user_input_list = []
    while True:
        user_input = input(prompt)
        if not user_input:
            break
        user_input_list.append(user_input)
    return user_input_list

def send_messages_in_parallel(token, user_channels, content_list, is_file=False, folder_path=None):
    global repeat_count
    with ThreadPoolExecutor() as executor:
        for i in range(repeat_count):
            if is_file:
                files = get_files_in_folder(folder_path)
                if files:
                    file_path = os.path.join(folder_path, random.choice(files))
                    executor.submit(send_file, token, random.choice(user_channels), file_path)
            else:
                message = random.choice(content_list)
                executor.submit(send_message, token, random.choice(user_channels), message)

def main():
    global repeat_count
    # Add your user token and channels directly in the code
    token = "YOUR_USER_TOKEN"
    user_channels = [
        "https://discord.com/api/v9/channels/CHANNEL_ID/messages"
        # Add more channel URLs as needed
    ]

    repeat_count = int(input("Enter the number of messages/images to send: "))

    print("Choose an option:")
    print("1. Only use text messages")
    print("2. Only use images")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        user_messages = get_user_input("Enter your message (or press Enter twice to finish adding your message): ", "")

        while True:
            send_messages_in_parallel(token, user_channels, user_messages)
            print(f"{repeat_count} messages sent to {len(user_channels)} channels. Wait 5 seconds before resending.")
            time.sleep(5)

            user_input = input(f"Do you want to send another {repeat_count} messages? (y/n): ")
            if user_input.lower() != 'y':
                break

    elif choice == '2':
        image_folder_path = r"resources\images"  # Replace with your folder path

        if os.path.exists(image_folder_path):
            while True:
                send_messages_in_parallel(token, user_channels, [], is_file=True, folder_path=image_folder_path)
                print(f"{repeat_count} images sent to {len(user_channels)} channels. Wait 5 seconds before resending.")
                time.sleep(5)

                user_input = input(f"Do you want to send another {repeat_count} images? (y/n): ")
                if user_input.lower() != 'y':
                    break
        else:
            print("Invalid folder path. Please provide a valid path.")

    else:
        print("Invalid choice. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()
