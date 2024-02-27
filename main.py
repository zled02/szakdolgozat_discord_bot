from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


async def send_message (message: Message, usr_message: str) -> None:
    if not usr_message:
        print('Message empty')
        return
    

    if is_private := usr_message[0] == '?':
        usr_message=usr_message[1:]

    try:
        response: str = get_responses(usr_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)



@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')



@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
         
    username: str = str(message.author)
    user_message: str = message.content
    chanel: str = str(message.channel)

    print(f'[{chanel}] {username}: "{user_message}')
    await send_message(message, user_message)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
