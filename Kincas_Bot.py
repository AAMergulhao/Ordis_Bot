import telebot
from requests import get
from bs4 import BeautifulSoup

token = open("token.txt", "r")
bot = telebot.TeleBot(token.read())
@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.reply_to(message, "is everything in ordis operator ? \n""Welcome Operator, there is some suggestions for you sir: \n Warframes, Missions, Factions, Syndicates.")

@bot.message_handler(regexp="Warframes")	
def wr(message):
	bot.reply_to(message, "The Warframe is an advanced weapons system used exclusively by the Tenno in their missions throughout the Origin System.The Warframes possess regenerative shields, greatly enhanced mobility, and enable the use of an array of supernatural abilities,\
    all of which further augment the Tenno's deadly use of traditional combat arts.\n"+ "If you to know more, there is some options Operator:\n Excalibur, Ash, Frost, Loki, Mag, Nova, Nyx, Rhino, Trinity,\
    Volt, Atals, Banshee, Baruuk, Chroma.")

@bot.message_handler(regexp="Missions")
def wr(message):
	bot.reply_to(message, "Missions are the primary playable content in WARFRAME. Up to four players can participate in the same mission as a Squad, and upon completing the objective(s) extract themselves from the site with their Landing Craft.\
        Missions are primarily accessed through the Star Chart, and are PvE (Player vs Environment) only. PvP (Player vs Player) content may be found in Teshin's Conclave, accessible from the Orbiter or from Tenno Relays.\n \nHere's are some options for you sir:\nAssassination, Defense, Capture, Defection, Excavation, Exterminate, Interception, Rescue, Sabotage, Spy.")

#################WARFRAMES#########################
@bot.message_handler(regexp="Excalibur")
@bot.message_handler(regexp="Ash")
@bot.message_handler(regexp="Frost")
@bot.message_handler(regexp="Loki")
@bot.message_handler(regexp="Mag") 
@bot.message_handler(regexp="Nova")
@bot.message_handler(regexp="Nyx")
@bot.message_handler(regexp="Rhino")
@bot.message_handler(regexp="Trinity")
@bot.message_handler(regexp="Volt")
@bot.message_handler(regexp="Atlas")
@bot.message_handler(regexp="Banshee")
@bot.message_handler(regexp="Baruuk")
@bot.message_handler(regexp="Chroma")
def waframe(message):
    x = message.text
    print(x)
    url = "https://warframe.fandom.com/wiki/" + x
    response = get(url)

    html_soup = BeautifulSoup(response.text, "html.parser")
    type(html_soup)

    definicao = html_soup.find_all("div", class_ = "cquote-text")
    status = html_soup.find_all("div", class_ = "pi-item pi-data pi-item-spacing pi-border-color")
    

    reply_definicao = "Definition: " + "\n" + definicao[0].text
    reply_status = "Status: " + "\n" + "\n" + status[0].h3.text + ": " + status[0].div.text + "\n" + status[1].h3.text + ": " + status[1].div.text + "\n" + status[2].h3.text + ": " + status[2].div.text + "\n" + status[3].h3.text + ": " + status[3].div.text + "\n" + status[4].h3.text + ": " + status[4].div.text 
    
    
    bot.reply_to(message, (reply_definicao + reply_status))
    
#################'''WARFRAMES'''#########################

#################'''MISSIONS'''##########################

@bot.message_handler(regexp="Assassination")
@bot.message_handler(regexp="Defense")
@bot.message_handler(regexp="Capture")
@bot.message_handler(regexp="Defection")
@bot.message_handler(regexp="Excavation")
@bot.message_handler(regexp="Exterminate")
@bot.message_handler(regexp="Interception")
@bot.message_handler(regexp="Rescue")
@bot.message_handler(regexp="Sabotage")
@bot.message_handler(regexp="Spy")
def mission(message):
    x = message.text
    print(x)
    url = "https://warframe.fandom.com/wiki/" + x
    response = get(url)

    html_soup = BeautifulSoup(response.text, "html.parser")
    type(html_soup)

    definition = html_soup.find_all("div", class_ = "mw-content-ltr mw-content-text")
    
    reply_definition = "Definition: " + "\n" + "\n" + definition[0].p.text
    
    bot.reply_to(message, reply_definition)

#################'''Missions'''#########################

#################'''Factions'''#########################

@bot.message_handler(regexp="Grineer")
@bot.message_handler(regexp="Corpus")
@bot.message_handler(regexp="Infested")
@bot.message_handler(regexp="Orokin")
def grineer(message):
    x = message.text
    print(x)
    url = "https://warframe.fandom.com/wiki/" + x
    response = get(url)

    html_soup = BeautifulSoup(response.text, "html.parser")
    type(html_soup)

    definition = html_soup.find_all("div", class_ = "WikiaArticle")

    reply_definition = "Definition: " + "\n" + "\n" + definition[0].p.text
    
    bot.reply_to(message, reply_definition)
    
#################'''Factions'''##########################

#################'''Syndicates'''##########################
@bot.message_handler(regexp="Steel Meridian")
@bot.message_handler(regexp="Arbiters of Hexis")
@bot.message_handler(regexp="Cephalon Suda")
@bot.message_handler(regexp="The Perrin Sequence")
@bot.message_handler(regexp="Red Veil")
@bot.message_handler(regexp="New Loka")
@bot.message_handler(regexp="Conclave")
@bot.message_handler(regexp="Cephalon Simaris")
@bot.message_handler(regexp="Ostron")
@bot.message_handler(regexp="The Quills")
@bot.message_handler(regexp="Solaris United")
def grineer(message):
    x = message.text
    print(x)
    url = "https://warframe.fandom.com/wiki/" + x
    response = get(url)

    html_soup = BeautifulSoup(response.text, "html.parser")
    type(html_soup)

    definition = html_soup.find_all("div", class_ = "cquote-text")
    
    reply_definition = "Definition: " + "\n" + "\n" + definition[0].p.text
    
    bot.reply_to(message, reply_definition)
#################'''Syndicates'''##########################
    
up = bot.get_updates()
bot.polling()

