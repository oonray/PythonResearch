"""
.. codeauthor:: Alexander Bjørnsrud <alexanderbjornsrud@gmail.com>
.. verson:: 0.1
.. date:: 2019-01-04


A discord bot that sends all questions to LGTFY.

"""

from discord.ext import commands
import discord, chalk, re, requests

client = commands.Bot(command_prefix="!?",status=discord.Status.idle,game=discord.Game(name="Starting.."))
url = "http://lmgtfy.com/?q={}"
me = "LMSTFY#5761"

@client.event
async def on_ready():
    """
    The client readdy state.
    What to be done when the client comes online.

    :args:
    :return:
    """

    print(chalk.green("Started"))
    await client.change_presence(status=discord.Status.online, game=discord.Game(name="LGTFY"))

@client.event
async def on_message(m):
    """
    Receive messages from the server.
    Will check for a question and send it to LGTFY.

    :param message: The message recived
    :return: None
    """

    msg = m.content
    chnl = m.channel
    author = str(m.author)
    questions = set()

    if author != me:
        reg = re.compile(r'([A-Za-z][^?]*[?])',re.M)
        msgr = reg.findall(msg)

        for i in msgr:
            if i not in questions:
                    msg2 = i.split(" ")
                    msg2 = "+".join(msg2)
                    questions.add(i)
                    await client.send_message(chnl,url.format(msg2))


client.run("NTMwODQ1MDkzNDE0OTYxMTgz.DxFXgQ.ipjO7W-fk6uEFPKt6YnrdsC24L0")
