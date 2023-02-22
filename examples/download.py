from datetime import datetime, timedelta
from betfairmarketvolumesclient import Client

client = Client()

# get today's horse racing selections
horse_racing_selections = client.get_horse_racing_markets_for_date(
    date=datetime(2020,1,1)
)

for h in horse_racing_selections:
    if h.event_id == 141674319:
        all.append(h)

# get today's greyhound selections
greyhound_selections = client.get_greyhound_markets_for_date(date=datetime.utcnow())

data = client.get_horse_racing_markets_for_date(date=datetime(2018,3,24))
pass