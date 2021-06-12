# DiscordTwitchChatIntergration

## Introduction

>This is a Twitch intergration with Discord Webhooks.
>When someone send a message in your chat, this message will be send to a specific channel of you Discord Server.

> Warning : This project use IRC chat, so at the startup of the bot, a couple of message was send in your channel.
<img src="https://repository-images.githubusercontent.com/369836298/7750d380-bb22-11eb-951d-ecc08f8a72a1" width=50% height=50%>

## Installation

> You need Python 3
> You need theses modules too :

`socket`,
`discordwebhook`,
`time`

You have to create a Twitch account for you bot

>  You have to fill the lines `8`, `14`, `15`, `16` of the file main.py for make the bot work.


###### 8: Your server > Settings of the channel you want to send the messages > Integration > Create new webhook > Copy the webhook url and paste it
###### 14: The name of your bot (like in the twitch page url of your bot)
###### [15: Put your twitch bot token](https://twitchapps.com/tmi/)
###### 16: The channel you want to read



### Thanks to [DarkMatter](https://www.twitch.tv/darkmatterh1), to let me use his chat to make my things. [His discord](https://discord.gg/edMq4uWeGU)
