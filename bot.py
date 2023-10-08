import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$check'):
        await message.channel.send(find_station(message.content[7:]))

def find_station(alert):
    affected = alert.split(":")

    print(affected)

    if(affected[0] in stations[0]):
        return(affected[0], stations[0].index(affected[0]))

    return "No issues found"

stations = [
    ["Finch", "North York Center", "Sheppard-Yonge", "York Mills,", "Lawrence", "Eglinton", 
    "Davisville", "St. Clair", "Summerhill", "Rosedale", "Bloor-Yonge", "Wellesley", 
    "College", "Dundas", "Queen", "King", "Union", "St. Andrew", 
    "Osgoode", "St. Patrick", "Queen's Park", "Museum", "St. George", "Spadina", 
    "Dupont", "St. Clair West", "Eglinton West", "Glencairn", "Lawrence West", "Yorkdale", 
    "Wilson", "Sheppard West", "Downsview Park", "Finch West", "York University", "Pioneer Village", 
    "Highway 407", "Vaughan"]
]

p1 = "MTE1OTIwNzY1Nz"
p2 = "U4OTE5ODkwMA.G1"
p3 = "aCiJ.8_V07tr3E-e5"
p4 = "2xVODcFkDXHoSy4"
p5 = "FxAFMCZeuqE"
client.run(f'{p1}{p2}{p3}{p4}{p5}')