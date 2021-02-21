# VERSION 1.2 / REQUIRES CONFIG 1.1

import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from ruamel.yaml import YAML

yaml = YAML()

with open("./config.yml", "r", encoding="utf-8") as file:
    config = yaml.load(file)

client = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all(), case_insensitive=True)
client.remove_command('help')


@client.event
async def on_command_error(error):
    if isinstance(error, CommandNotFound):
        return
    raise error


@client.event
async def on_ready():
    print('------')
    print('Online! Details:')
    print(f"Bot Username: {client.user.name}")
    print(f"BotID: {client.user.id}")
    print('------')
    for command in client.commands:
        print(f"Loaded: {command}")
    config_activity = config['bot_activity']
    activity = discord.Game(name=config['bot_status_text'])
    await client.change_presence(status=config_activity, activity=activity)


@client.command()
async def help(ctx):
    prefix = config['prefix']
    embed = discord.Embed(title="**HELP PAGE | :book:**",
                          description="Phasmophobia is a discord bot for the game Phasmophobia")
    embed.add_field(name="Prefix:", value=f"``{prefix}``")
    embed.add_field(name="unkown:", value=f"``{prefix}unkown`` *unknown*")
    embed.add_field(name="unkown:", value=f"``{prefix}unkown`` *unkown*")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def spirit(ctx):
    embed = discord.Embed(title="**SPIRIT | :ghost:**",
                          description="A Spirit is the most common Ghost you will come across however it is still very powerful and dangerous. They are usually discovered at one of their hunting grounds after an unexplained death.")
    embed.add_field(name="Strength:", value="Nothing")
    embed.add_field(name="Weakness:",
                    value="Using Smudge Sticks on a Spirit will stop it attacking for a long period of time.")
    embed.add_field(name="Evidence:", value="Fingerprints, Ghost Writing, Spirit Box")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def wraith(ctx):
    embed = discord.Embed(title="**WRAITH | :ghost:**",
                          description="A Wraith is one of the most dangerous Ghosts you will find. It is also the only known ghost that has the ability of flight and has sometimes been known to travel through walls.")
    embed.add_field(name="Strength:",
                    value="Wraiths almost never touch the ground meaning it can’t be tracked by footsteps.")
    embed.add_field(name="Weakness:", value="Wraiths have a toxic reaction to Salt")
    embed.add_field(name="Evidence:", value="Fingerprints, Freezing Temperatures, Spirit Box")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def phantom(ctx):
    embed = discord.Embed(title="**PHANTOM | :ghost:**",
                          description="A Phantom is a Ghost that can possess the living, most commonly summoned by a Ouija Board. It also induces fear into those around it.")
    embed.add_field(name="Strength:", value="Looking at a Phantom will considerably drop your sanity.")
    embed.add_field(name="Weakness:", value="Taking a photo of the Phantom will make it temporarily disappear.")
    embed.add_field(name="Evidence:", value="EMF Level 5, Freezing Temperatures, Ghost Orb")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def poltergeist(ctx):
    embed = discord.Embed(title="**POLTERGEIST | :ghost:**",
                          description="One of the most famous Ghosts, a Poltergeist, also known as a noisy ghost can manipulate objects around it to spread fear into it's victims.")
    embed.add_field(name="Strength:", value="A Poltergeist can throw huge amounts of objects at once.")
    embed.add_field(name="Weakness:", value="A Poltergeist is almost ineffective in an empty room.")
    embed.add_field(name="Evidence:", value="Fingerprints, Ghost Orb, Spirit Box")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def banshee(ctx):
    embed = discord.Embed(title="**BANSHEE | :ghost:**",
                          description="A Banshee is a natural hunter and will attack anything. It has been known to stalk its prey one at a time until making its kill.")
    embed.add_field(name="Strength:", value="A Banshee will only target one person at a time.")
    embed.add_field(name="Weakness:", value="Banshees fear the Crucifix and will be less aggressive when near one.")
    embed.add_field(name="Evidence:", value="EMF Level 5, Fingerprints, Freezing Temperatures")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def jinn(ctx):
    embed = discord.Embed(title="**JINN | :ghost:**",
                          description="A Jinn is a territorial Ghost that will attack when threatened. It also has been known to travel at significant speed.")
    embed.add_field(name="Strength:", value="A Jinn will travel at a faster speed if it’s victim is far away.")
    embed.add_field(name="Weakness:",
                    value="Turning off the locations power source will prevent the Jinn from using it’s ability")
    embed.add_field(name="Evidence:", value="EMF Level 5, Ghost Orb, Spirit Box")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def mare(ctx):
    embed = discord.Embed(title="**MARE | :ghost:**",
                          description="A Mare is the source of all nightmares, making it most powerful in the dark.")
    embed.add_field(name="Strength:", value="A Mare will have an increased chance to attack in the dark.")
    embed.add_field(name="Weakness:", value="Turning the lights on around the Mare will lower it’s chance to attack.")
    embed.add_field(name="Evidence:", value="Freezing Temperatures, Ghost Orb, Spirit Box")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def revenant(ctx):
    embed = discord.Embed(title="**REVENANT | :ghost:**",
                          description="A Revenant is a slow but violent Ghost that will attack indiscriminately. It has been rumored to travel at a significantly high speed when hunting.")
    embed.add_field(name="Strength:",
                    value="A Revenant will travel at a significantly faster speed when hunting a victim.")
    embed.add_field(name="Weakness:", value="Hiding from the Revenant will cause it to move very slowly.")
    embed.add_field(name="Evidence:", value="EMF Level 5, Fingerprints, Ghost Writing")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def shade(ctx):
    embed = discord.Embed(title="**SHADE | :ghost:**",
                          description="A Shade is known to be a Shy Ghost. There is evidence that a Shade will stop all paranormal activity if there are multiple people nearby.")
    embed.add_field(name="Strength:", value="Being shy means the Ghost will be harder to find.")
    embed.add_field(name="Weakness:", value="The Ghost will not enter hunting mode if there is multiple people nearby.")
    embed.add_field(name="Evidence:", value="EMF Level 5, Ghost Orb, Ghost Writing")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def demon(ctx):
    embed = discord.Embed(title="**DEMON | :ghost:**",
                          description="A Demon is one of the worst Ghosts you can encounter. It has been known to attack without a reason.")
    embed.add_field(name="Strength:", value="Demons will attack more often then any other Ghost.")
    embed.add_field(name="Weakness:",
                    value="Asking a Demon successful questions on the Ouija Board won’t lower the users sanity.")
    embed.add_field(name="Evidence:", value="Freezing Temperatures, Ghost Writing, Spirit Box")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def yurei(ctx):
    embed = discord.Embed(title="**YUREI | :ghost:**",
                          description="A Yurei is a Ghost that has returned to the physical world, usually for the purpose of revenge or hatred.")
    embed.add_field(name="Strength:", value="Yurei’s have been known to have a stronger effect on people’s sanity.")
    embed.add_field(name="Weakness:",
                    value="Smudging the Yurei’s room will cause it to not wander around the location for a long time.")
    embed.add_field(name="Evidence:", value="Freezing Temperatures, Orb, Ghost Writing")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def oni(ctx):
    embed = discord.Embed(title="**ONI | :ghost:**",
                          description="Onis are a cousin to the Demon and possess extreme strength. There have been rumors that they become more active around their prey.")
    embed.add_field(name="Strength:",
                    value="Oni’s are more active when people are nearby and have been seen moving objects at great speed.")
    embed.add_field(name="Weakness:", value="Being more active will make the Oni easier to find and identify.")
    embed.add_field(name="Evidence:", value="EMF Level 5, Ghost Writing, Spirit Box")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command(aliases=["ghosts"])
async def ghost(ctx):
    prefix = config['prefix']
    embed = discord.Embed(title="**GHOST TYPES | :ghost:**",
                          description=f"There are a total of 12 Ghosts in Phasmophobia. Each Ghost has their own command (eg. {prefix}revenant).")
    embed.add_field(name="Ghost Names:",
                    value="Spirit, Wraith, Phantom, Poltergeist, Banshee, Jinn, Mare, Revenant, Shade, Demon, Yurei, Oni.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command(aliases=['updates'])
async def patches(ctx):
    embed = discord.Embed(title="**Date: 18/02/2021 - Steam Build ID: 6261631 | Server Version: 0.26.6**")
    embed.add_field(name="Fixes:",
                    value="**1.** Fixed a bug where if you glitched out of the truck when it was closing the game wouldn't end.\n **2.** Fixed a bug where the power sound wouldn't play if the ghost turned it off.\n **3.** Fixed an issue where the loading text when first opening the game wasn't localised.\n **4.** School: Fixed several errors with the top floor map.\n **5.** Tanglewood: Fixed a bug where the boys bedroom monitor would not turn off with the power.\n **6.** Grafton and School: Fixed several locations where you would lose sanity if the lights were on.")
    embed.add_field(name="Changes:",
                    value="**1.** Tanglewood: Removed the thunder sound that had voices in it and replaced it with two other thunder sounds.")
    embed.add_field(name="New:",
                    value="**1.** Added a warning on the main menu which will tell you if your PC might be below the minimum requirements.\n **2.** Added an 'Are you sure?' check after clicking the training button on the main menu.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command(aliases=["maps"])
async def map(ctx):
    prefix = config['prefix']
    embed = discord.Embed(title="**MAPS | :house_abandoned:**",
                          description=f"There are a total of 8 Maps in Phasmophobia. Each Map has their own command (eg. {prefix}tanglewood).")
    embed.add_field(name="Small:",
                    value="Tanglewood Street House, Edgefield Street House, Ridgeview Street House, Grafton Farmhouse, Bleasdale Farmhouse")
    embed.add_field(name="Medium:", value="Brownstone High School, Prison")
    embed.add_field(name="Large::", value="Asylum")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def tanglewood(ctx):
    embed = discord.Embed(title="**TANGLEWOOD | :house_abandoned:**",
                          description="Tanglewood Street House is one of the locations players can visit and is also the location of the game tutorial. It is a small single-story home with three bedrooms and two bathrooms")
    embed.add_field(name="Size:", value="Small")
    embed.add_field(name="Team Size:", value="1")
    embed.add_field(name="Ouija Locations:", value="4 (1F) 2 (B)")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def edgefield(ctx):
    embed = discord.Embed(title="**EDGEFIELD | :house_abandoned:**",
                          description="A two story, six-bedroom house with a basement. Edgefield Street House is a congested, claustrophobic environment. Despite this, there are plenty of hiding spaces during a Hunt, as a room to hide in is always a few paces away.")
    embed.add_field(name="Size:", value="Small")
    embed.add_field(name="Team Size:", value="2")
    embed.add_field(name="Ouija Locations:", value="1 (2F), 2 (1F), 1 (B)")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def ridgeview(ctx):
    embed = discord.Embed(title="**RIDGEVIEW | :house_abandoned:**",
                          description="Ridgeview Road House is one of the Locations in Phasmophobia. It is a two-story, four-bedroom house with a garage and basement. It is quite congested with many linear hallways, with most of the rooms either being small, having numerous obstacles, or both. However, the presence of closets and multiple sub-rooms to dive into provides plenty of safety for a Hunt.")
    embed.add_field(name="Size:", value="Small")
    embed.add_field(name="Team Size:", value="2")
    embed.add_field(name="Ouija Locations:", value="2 (2F) 4 (1F) 2 (B)")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def grafton(ctx):
    embed = discord.Embed(title="**GRAFTON | :house_abandoned:**",
                          description="Grafton Farmhouse is one of the Small maps in Phasmophobia, and one of the two variants of the Farmhouse, alongside Bleasdale Farmhouse.")
    embed.add_field(name="Size:", value="Small")
    embed.add_field(name="Team Size:", value="2")
    embed.add_field(name="Ouija Locations:", value="3 (2F) 3 (1F)")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def bleaside(ctx):
    embed = discord.Embed(title="**BLEASIDE | :house_abandoned:**",
                          description="Bleasdale Farmhouse is one of the Small maps in Phasmophobia, and one of the two variants of the Farmhouse, alongside Grafton Farmhouse.")
    embed.add_field(name="Size:", value="Small")
    embed.add_field(name="Team Size:", value="2")
    embed.add_field(name="Ouija Locations:", value="2 (A) 3 (2F) 3 (1F)")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def brownstone(ctx):
    embed = discord.Embed(title="**BROWNSTONE | :house_abandoned:**",
                          description=" Brownstone High School is the first medium-sized map. Long decrepit hallways, ominous classrooms, grotesque bathrooms, and various vacant office spaces fill the place with a solemn atmosphere. Its square shape and general symmetry can make it intuitive to navigate, and depending on the ghost, it may be easier to run during a hunt than to hide.")
    embed.add_field(name="Size:", value="Medium")
    embed.add_field(name="Team Size:", value="3")
    embed.add_field(name="Ouija Locations:", value="5 (2F) 3 (1F)")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def prison(ctx):
    embed = discord.Embed(title="**BROWNSTONE | :house_abandoned:**",
                          description="Prison is a medium-sized map. Long decrepit hallways, big open rooms, and various vacant office spaces fill the place with a solemn atmosphere. Its size and shape can make you lost easily, and depending on the ghost, it may be easier to run during a hunt than to hide as finding a safe spot is rather difficult on Prison.")
    embed.add_field(name="Size:", value="Medium")
    embed.add_field(name="Team Size:", value="3")
    embed.add_field(name="Ouija Locations:", value="4 (2F) 3 (1F)")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


@client.command()
async def journal(ctx):
    embed = discord.Embed(title="**JOURNAL | :book:**",
                          description="The Journal holds several important bits of information on Phasmophobia and its ghosts. It has a section explaining some of the equipment and evidence, as well as information about the different sort of ghosts you may encounter. You can also see any photos you may have taken, with a brief description if applicable. The final page can be used to select what evidence you've found, and what type of ghost you think you're dealing with.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def emf(ctx):
    embed = discord.Embed(title="**EMF | :movie_camera:**",
                          description="An Electro-Magnetic Field (short: EMF) is emitted whenever the Ghost interacts with its environment. EMF can be read by the EMF Reader, allowing players to deduce the Ghost's activities from the EMF Level")
    embed.add_field(name="Price:", value="$45")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["writing", "gw"])
async def ghostwriting(ctx):
    embed = discord.Embed(title="**GHOST WRITING BOOK | :movie_camera:**",
                          description="Ghost Writing Book, also known as automatic writing, is Equipment used to obtain Ghost Writing by placing it near a Ghost. There is no way to forcefully trigger the book to be written in legitimately.")
    embed.add_field(name="Price:", value="$40")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def spiritbox(ctx):
    embed = discord.Embed(title="**SPIRIT BOX | :movie_camera:**",
                          description="The Spirit Box is a piece of Equipment, as well as a type of Evidence, that can be used to ask the Ghost questions to get more information. Only certain Ghosts will respond via the Spirit Box, which can be used as Evidence when identifying the Ghost.")
    embed.add_field(name="Price:", value="$50")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def thermometer(ctx):
    embed = discord.Embed(title="**THERMOMETER | :movie_camera:**",
                          description="The Thermometer is a purchasable piece of Equipment used to read the temperatures in the nearby environment. The Thermometer can be used to detect Evidence of Freezing Temperatures and is a reliable tool to locate the Ghost Room.")
    embed.add_field(name="Price:", value="$30")
    embed.add_field(name="Max Amount:", value="3")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["videocamera"])
async def video(ctx):
    embed = discord.Embed(title="**VIDEO CAMERA | :movie_camera:**",
                          description="The Video Camera (also known as DSLR) is used to create a Video Feed which can be seen in the Van.")
    embed.add_field(name="Price:", value="$50")
    embed.add_field(name="Max Amount:", value="6")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["uvlight"])
async def uv(ctx):
    embed = discord.Embed(title="**UV FLASHLIGHT | :movie_camera:**",
                          description="The UV Flashlight is a purchasable starter item used to detect Fingerprints and Footprints. It can be carried and activated at the same time as a standard Flashlight or Strong Flashlight, but the faint fingerprints might not be visible under their light.")
    embed.add_field(name="Price:", value="$35")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["photocamera"])
async def photo(ctx):
    embed = discord.Embed(title="**PHOTO CAMERA | :movie_camera:**",
                          description="The Photo Camera is a photographic camera that can take pictures of objects in-game. This equipment cannot be used for gathering evidence, but it may be required to complete additional objectives, daily challenges, or to acquire money from photo rewards upon finishing the investigation.")
    embed.add_field(name="Price:", value="$40")
    embed.add_field(name="Max Amount:", value="3")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def flashlight(ctx):
    embed = discord.Embed(title="**FLASHLIGHT | :movie_camera:**",
                          description="Flashlights are the primary source of illuminating dark and/or poorly-lit areas, or otherwise one would have to roam in pitch-black darkness and lose their sanity.")
    embed.add_field(name="Price:", value="$30")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def strongflashlight(ctx):
    embed = discord.Embed(title="**STRONG FLASHLIGHT | :movie_camera:**",
                          description="An upgraded version of the flashlight. It is quite self-descriptive: it creates a much brighter light than the flashlight, making navigation in the dark that much easier.")
    embed.add_field(name="Price:", value="$50")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def candle(ctx):
    embed = discord.Embed(title="**CANDLE | :movie_camera:**",
                          description="Candles are deployable light sources that can be lit using a source of fire such as the lighter, which can be used to light up a room and prevent the player's sanity from dropping.")
    embed.add_field(name="Price:", value="$15")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def crucifix(ctx):
    embed = discord.Embed(title="**CRUCIFIX | :movie_camera:**",
                          description="The Crucifix is a purchasable item that is used to prevent the Ghost from entering into a Hunt.")
    embed.add_field(name="Price:", value="$30")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["glowstick"])
async def glow(ctx):
    embed = discord.Embed(title="**GLOWSTICK | :movie_camera:**",
                          description="The Glowstick is a handheld item that emits a UV light when used. It can be thrown onto the floor to light up Footprints or Fingerprints. ")
    embed.add_field(name="Price:", value="$20")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["hmcamera"])
async def headmountedcamera(ctx):
    embed = discord.Embed(title="**HEAD MOUNTED CAMERA | :movie_camera:**",
                          description="The Head Mounted Camera can be used to help teams track each other and to see Ghost Orbs.")
    embed.add_field(name="Price:", value="$60")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["lightsensor", "infraredlightsensor"])
async def infrared(ctx):
    embed = discord.Embed(title="**INFRARED LIGHT SENSOR | :movie_camera:**",
                          description="An Infrared Light Sensor that detects both human and paranormal movement. When set off, it will illuminate the surrounding area with a bright light.")
    embed.add_field(name="Price:", value="$65")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def lighter(ctx):
    embed = discord.Embed(title="**LIGHTER | :movie_camera:**",
                          description="The Lighter is an item used to light Smudge Sticks and Candles. It emits a small amount of light when activated and held by the player.")
    embed.add_field(name="Price:", value="$10")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["motionsensor"])
async def motion(ctx):
    embed = discord.Embed(title="**MOTION SENSOR | :movie_camera:**",
                          description="The Motion Sensor is a purchasable support item. It is the most expensive piece of equipment in the game, costing $100, but it can be very handy when tracking the movement of the Ghost, providing a visual and audio cue when the ghost moves through it. The Motion Sensor also displays on the Site Map, allowing for the Ghost's movement to be detected from the safety of the Van")
    embed.add_field(name="Price:", value="$100")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def parabolic(ctx):
    embed = discord.Embed(title="**PARABOLIC MICROPHONE | :movie_camera:**",
                          description="A Parabolic Microphone can detect sound through walls and at a great distance. It serves as a portable version of the sound sensor. Although infamously finicky, it is very handy to have around in the larger locations such as the High School and Asylum, although largely useless in smaller ones.")
    embed.add_field(name="Price:", value="$50")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def salt(ctx):
    embed = discord.Embed(title="**SALT | :movie_camera:**",
                          description="Salt is a purchasable item used to detect the Ghost's footprints. It is used to place salt piles on the floor which the ghost can walk in, disturbing it and creating footprints that can be seen with the UV Flashlight, which can then be photographed with a Photo Camera for extra money.")
    embed.add_field(name="Price:", value="$15")
    embed.add_field(name="Max Amount:", value="2")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["sanitypills"])
async def sanity(ctx):
    embed = discord.Embed(title="**SANITY PILLS | :movie_camera:**",
                          description="Sanity Pills replenish your Sanity level. Each bottle replenishes 40% Sanity, up to the maximum of 100%.")
    embed.add_field(name="Price:", value="$45")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["smudgesticks"])
async def smudge(ctx):
    embed = discord.Embed(title="**SMUDGE STICKS | :movie_camera:**",
                          description="Smudge Sticks, also known as sage sticks, are a purchasable item that will deter the Ghost from hunting or attacking for a period of time when burned")
    embed.add_field(name="Price:", value="$15")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["sounds"])
async def soundsensor(ctx):
    embed = discord.Embed(title="**SOUND SENSOR | :movie_camera:**",
                          description="The Sound Sensor is a sensor that can listen to the most quiet sounds and vibrations in the air. This is displayed as data at the van.")
    embed.add_field(name="Price:", value="$80")
    embed.add_field(name="Max Amount:", value="4")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command()
async def tripod(ctx):
    embed = discord.Embed(title="**TRIPOD | :movie_camera:**",
                          description="The Tripod can be used to mount Video Cameras on. Tripods will be deployed facing the same direction as the player deploying them.")
    embed.add_field(name="Price:", value="$25")
    embed.add_field(name="Max Amount:", value="5")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.send(embed=embed)


@client.command(aliases=["items"])
async def equipment(ctx):
    prefix = config['prefix']
    embed = discord.Embed(title="**EQUIPMENT ITEMS | :ghost:**",
                          description=f"There are a total of 21 different pieces of equipment in Phasmophobia. Each item has their own command (eg. {prefix}emf).")
    embed.add_field(name="Equipment List:",
                    value="EMF, GhostWriting, SpiritBox, Thermometer, VideoCamera, UV, PhotoCamera, Flashlight, StrongFlashlight, Candle, Crucifix, GlowSticks, HeadMountedCamera, InfraredLightSensor, Lighter, MotionSensor, Parabolic, Salt, SanityPills, SmudgeSticks, SoundSensor, Tripod")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/809363157101314048/812685774566195208/cover-256.png")
    await ctx.channel.send(embed=embed)


client.run(config['token'])
