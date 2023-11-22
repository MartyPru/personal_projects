import pywhatkit
import config
import random

# Uses pywhatkit to send a random quote via WhatsApp Web to a number at a desired interval.

time_to_send = 11
mins_to_send = 40
quotes = config.quotes
random_quote_index = random.randrange(len(quotes))

while time_to_send < 21:
    pywhatkit.sendwhatmsg(config.target_number, quotes[random_quote_index], time_to_send, mins_to_send)
    del quotes[random_quote_index]
    random_quote_index = random.randrange(len(quotes))
    time_to_send += 2


