from datetime import datetime, timedelta
from betfairmarketvolumesclient import Client

client = Client()

# get today's horse racing selections
horse_racing_selections = client.get_aus_win_horse_racing_markets(
    date=datetime.utcnow()
)

# get today's greyhound selections
greyhound_selections = client.get_greyhound_markets_for_date(date=datetime.utcnow())

data = client.get_horse_racing_markets_for_date(date=datetime(2010,6,3))
