from datetime import datetime, timedelta
from betfairmarketvolumesclient import Client

client = Client()

# get today's horse racing selections
horse_racing_selections = client.get_horse_racing_markets_for_date(
    date=datetime.utcnow()-timedelta(days=1)
)

# get today's greyhound selections
greyhound_selections = client.get_greyhound_markets_for_date(date=datetime.utcnow())

pass