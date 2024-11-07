import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

BOT_TOKEN = ''
GUILD_ID = 1203948268384555059 
CHANNEL_ID = 1299060121267339327  

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
scheduler = AsyncIOScheduler()

async def send_activity_poll():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        poll_message = ("** @everyone What will you help with in class today? **\n\n"
                        "🥊 Bring down equipment (2-3ppl)\n"
                        "📝 Sign people in (3-4ppl)\n"
                        "👨‍🏫 Coaching (2ppl)\n"
                        "🙋‍♂️ General help\n"
                        "👎 Not coming to class\n"
                        "React to vote!")
        message = await channel.send(poll_message)
        emojis = ["🥊", "📝", "👨‍🏫", "🙋‍♂️", "👎"]
        for emoji in emojis:
            await message.add_reaction(emoji)

@bot.command(name='tasks')
async def test_poll(ctx):
    print("Poll command triggered!")
    await send_activity_poll()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    scheduler.add_job(send_activity_poll, CronTrigger(day_of_week='mon,wed,thu', hour=10, minute=0))
    scheduler.start()

bot.run(BOT_TOKEN)