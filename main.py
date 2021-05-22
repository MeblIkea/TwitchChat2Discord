# DiscordTwitchChatIntegration

import socket
from discordwebhook import Discord
import time

webhook = Discord(
    url='')

sock = socket.socket()

server = 'irc.chat.twitch.tv'
port = 6667
nickname = ''  # Your bot name
token = 'oauth:##############################'  # Your bot token (https://twitchapps.com/tmi/)
channel = '#darkmatterh1'  # The channel you want to print

if nickname == '':
    print('YOU HAVE TO SETUP THE NICKNAME, THE TOKEN AND A DISCORD CHANNEL WEBHOOK!')
    exit()

sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

while True:
    try:
        resp = sock.recv(2048).decode('utf-8')
        nom = resp.split('!', 1)
        resp = resp.split(' ', 3)
        nom = str(nom.pop(0))
        rep = str(resp.pop(3))
        nom = nom[1:]
        rep = rep[1:]

        print(rep)
        print(nom)
        webhook.post(content=rep, username=f'{nom} - {time.localtime().tm_hour}:{time.localtime().tm_min}',
                     avatar_url='https://cdn.icon-icons.com/icons2/2845/PNG/512/twitch_logo_icon_181273.png')
    except Exception:
        pass
