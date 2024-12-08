# Discord python selfbot

A simple discord selfbot written in python.<br><br>
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE) <Br>
[Releases](https://github.com/owaii/python-selfbot/releases)



## Table of Contents

- [About](#about)
- [Features](#features)
- [How to install](#installation-process)

## Warning

I don't take any responsibility for using this program. It was made only for educational purposes and shouldnt be used in any malicious way. Using this on a user account is prohibited by the [Discord TOS](https://discord.com/terms) and can lead to getting your account banned. Use at your own risk.

## About

This selfbot was made in python using a requests library that you have to install by yourself on your computer. Made for fun, as I am a python newbie lol. I will include everything you need to do in the [installation process](#installation-process) section.

## Features

- Customizable message delay
- Choosing the words that will be spammed
- Randomizing messages/images to send from the list
- Sending messages/images to multiple channels/dms at once
- Fast request time
- Easy to use
- Secure token management
- Progress reporting with `tqdm`
- Enhanced logging to track sent messages and errors
- more features are going to be added in the future

## Installation process

Instructions on setting up your project locally. Include prerequisites, installation steps, and any other necessary information.

<h3>Step 1.</h3>

You will need to have the newest [python](https://www.python.org/downloads/) installed.
I will include a [file](https://github.com/owaii/python-selfbot/blob/main/src/resources/dependenciesCheck.bat) to check for python and request library availability on your system.

<h3>Step 2.</h3>

After installing python you will need to install a requests and tqdm module package. For the request/tqdm module to work, you need to manually install it by writing this command inside your command prompt (cmd).

```bash
pip install requests tqdm
``` 
  
<h3>Step 3.</h3>

If you succesfuly completed these steps, its time to look into the code. Open the selfbot.py and replace this line with a valid value:
```bash
image_folder_path = r"resources/images"  # Replace with your folder path
```
- To get your image file path just copy the file path of the folder images and copy it in there. It should look similar to this (eg.: C:\Users\username\Downloads\python-selfbot\src\resources\images)
  
- To get your request url (asked when running the app), you need to go to the channel that you are trying to flood and open developer tools network tab. Send a random message and look as there is a new request called "messages". Click on it and search for "Request URL". There will be an url with an id inside of it. Copy it and paste it when asked for.

- To get your token, you simply need to do the same as before but search for "Authorization". There will be your token. Copy and paste it when asked for.

<h3>Step 4</h3>

Run the program and enjoy :)

# TODO List

<!-- TODO List -->

<h3>In the near future:</h3>
<ul>
  <li>None</li>
</ul>

<h3>Late future plans:</h3>
<ul>
  <li>Overall better performance and optimalization</li>
</ul>

