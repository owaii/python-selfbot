
# Discord python selfbot

A simple discord selfbot written in python.<br><br>
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)  
![GitHub All Releases](https://img.shields.io/github/downloads/owaii/python-selfbot/total.svg)



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
- Randomizing words to send from the list
- more features are going to be added in the future

## Installation process

Instructions on setting up your project locally. Include prerequisites, installation steps, and any other necessary information.

<h3>Step 1.</h3>

You will need to have the newest [python](https://www.python.org/downloads/) installed.
I will include a file to check for python availability on your system.

<h3>Step 2.</h3>

After installing python you will need to install a requests module package. For the request module to work, you need to manually install it by writing this command inside your command prompt (cmd).

```bash
pip install requests
```   
  
<h3>Step 3.</h3>

If you succesfuly completed these steps, its time to look into the code. Open the selfbot.py and replace those lines with valid values:
```bash
url = "" #HERE GOES YOUR REQUEST URL
[...]
token = "" #HERE GOES YOUR USER TOKEN
```
- To get your request url, you need to go to the channel that you are trying to flood and open developer tools. Send a random message and look as there is a new request called "messages". Click on it and search for "Request URL". Copy the link and paste it inside the quotes.

- To get your token, you simply need to do the same as before but search for "Authorization". There will be your token.  Copy it and paste it inside the quotes

<h3>Step 4</h3>

Run the program and enjoy :)

# TODO List

<h3>In the near future:</h3>
- Option to send messages to many channels at once,
- Option to spam dms,
- Option to send images,
<h3>Late future plans:</h3>
- Auto token grabbing, so the user doesnt have to check for it for themselves,
- List of servers and channels generated for the users account, so they can move easily between channels to spam,
- Bot mod bypassing
