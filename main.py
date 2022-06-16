

from bs4 import BeautifulSoup
import requests
from twilio.rest import Client 
from PdgaPlayer import PdgaPlayer
import schedule 
import time

def send_message():
  account_sid = 'Your twilio sid'
  auth_token = 'Your twilio Auth token'
  client = Client(account_sid,auth_token)
  client.messages.create(
  from_="Twilio Phone number",
  to='Your Phone Number',
  body = pdga_scrape())  
  
def pdga_scrape():
    url = "https://www.pdga.com/tour/event/56148"
    result = requests.get(url)
    doc = BeautifulSoup(result.text,"html.parser")
    trs = doc.findAll('table')[1].findAll('tr')
    players = {}
    count = 0
    for tr in trs:
        name = tr.contents[2].string
        pdga_number = tr.contents[3].string
        roundRating= tr.contents[4].string
        roundScore = tr.contents[5].string
        payout = tr.contents[len(tr.contents) - 1].string
        players[count] = PdgaPlayer(pdga_number,name,roundScore,roundRating,payout)
        count+=1
    emailOutput = "Pdga Results"

    for i in players:
        if i == 0:
            continue
        if i > 45:
            break
      
        name = players[i].get_name()
        roundScore = players[i].get_roundTotal()
        roundRating = players[i].get_ratingRound()
        payout = players[i].get_payout()
        
        if payout is None :
            payout = ""
        if roundScore is None: 
            roundScore = "DNF"
        emailOutput += "\n"
        if (i < 10):
            emailOutput += "  {} {:<10} {:<4} {} ".format(i,name,roundScore,payout)    
        elif(i < 100):
            emailOutput += " {} {:<10} {:<4} {} ".format(i,name,roundScore,payout)
   
    return emailOutput
  

schedule.every().thursday.at('17:30').do(send_message)
schedule.every().friday.at('17:30').do(send_message)
schedule.every().saturday.at('17:30').do(send_message)
schedule.every().sunday.at('17:30').do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)




