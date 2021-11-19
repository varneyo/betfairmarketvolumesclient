from datetime import datetime

from betfairmarketvolumesclient import Client

client = Client()

# get todays horse racing selections
horse_racing_selections = client.get_horse_racing_markets_for_date(date=datetime.utcnow())

# get todays greyhound selections
greyhound_selections = client.get_greyhound_markets_for_date(date=datetime.utcnow())
