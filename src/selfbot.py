import requests
import time
import random
import os
import logging
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

logging.basicConfig(filename="message_sender.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def get_discord_token():
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        token = input("Please enter your Discord token: ")
    return token

def send_file(token, channel_url, file_path):
    url = channel_url
    with open(file_path, "rb") as f:
        files = {"file": f}
        headers = {"Authorization": token}
        while True:
            res = requests.post(url, files=files, headers=headers)
            if res.status_code == 200:
                logging.info(f"Successfully sent file to {channel_url}")
                break
            elif res.status_code == 429:
                retry_after = res.json().get('retry_after', 1)
                logging.warning(f"Rate limited, retrying in {retry_after} seconds...")
                time.sleep(retry_after)
            else:
                logging.error(f"Error sending file to {channel_url}: {res.status_code}, {res.text}")
                break

def send_message(token, channel_url, message):
    url = channel_url
    payload = {"content": message}
    headers = {"Authorization": token}
    while True:
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200:
            logging.info(f"Successfully sent message to {channel_url}")
            break
        elif res.status_code == 429:
            retry_after = res.json().get('retry_after', 1)
            logging.warning(f"Rate limited, retrying in {retry_after} seconds...")
            time.sleep(retry_after)
        else:
            logging.error(f"Error sending message to {channel_url}: {res.status_code}, {res.text}")
            break

def get_files_in_folder(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def random_delay(min_delay=0.1, max_delay=2): # Changeable but NOT recommended!
    delay = random.uniform(min_delay, max_delay)
    logging.info(f"Waiting for {delay:.2f} seconds before sending next message.")
    time.sleep(delay)

def get_channels_input():
    channels = []
    print("Enter channel IDs (one per line), and press Enter when done:")
    while True:
        channel_id = input("Channel ID (or press Enter to finish): ")
        if not channel_id:
            break
        channels.append(f"https://discord.com/api/v9/channels/{channel_id}/messages")
    return channels

def send_messages_in_parallel(token, user_channels, content_list, repeat_count, is_file=False, folder_path=None):
    with ThreadPoolExecutor() as executor:
        for channel_url in user_channels:
            for _ in tqdm(range(repeat_count), desc=f"Sending to {channel_url}"):
                if is_file:
                    files = get_files_in_folder(folder_path)
                    if files:
                        file_path = os.path.join(folder_path, random.choice(files))
                        executor.submit(send_file, token, channel_url, file_path)
                else:
                    message = random.choice(content_list)
                    executor.submit(send_message, token, channel_url, message)
                random_delay()

def main():
    token = get_discord_token()  # Get Discord token
    user_channels = get_channels_input()  # Get channels from user
    repeat_count = int(input("Enter the number of messages/images to send to each channel: "))

    print("Choose an option:")
    print("1. Only use text messages")
    print("2. Only use images")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        user_messages = []
        print("Enter your messages (press Enter twice to finish adding messages):")
        while True:
            message = input("Message: ")
            if not message:
                break
            user_messages.append(message)

        while True:
            send_messages_in_parallel(token, user_channels, user_messages, repeat_count)
            logging.info(f"{repeat_count} messages sent to each channel. Wait 5 seconds before resending.")
            print(f"{repeat_count} messages sent to each channel. Wait 5 seconds before resending.")
            time.sleep(5)

            user_input = input(f"Do you want to send another {repeat_count} messages to each channel? (y/n): ")
            if user_input.lower() != 'y':
                break

    elif choice == '2':
        image_folder_path = r"resources/images"  # Replace with your folder path

        if os.path.exists(image_folder_path):
            while True:
                send_messages_in_parallel(token, user_channels, [], repeat_count, is_file=True, folder_path=image_folder_path)
                logging.info(f"{repeat_count} images sent to each channel. Wait 5 seconds before resending.")
                print(f"{repeat_count} images sent to each channel. Wait 5 seconds before resending.")
                time.sleep(5)

                user_input = input(f"Do you want to send another {repeat_count} images to each channel? (y/n): ")
                if user_input.lower() != 'y':
                    break
        else:
            logging.error("Invalid folder path. Please provide a valid path.")
            print("Invalid folder path. Please provide a valid path.")

    else:
        logging.error("Invalid choice. Please enter either '1' or '2'.")
        print("Invalid choice. Please enter either '1' or '2'.")

if __name__ == "__main__":
    main()