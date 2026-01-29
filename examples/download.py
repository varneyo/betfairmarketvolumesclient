from datetime import datetime, timedelta
from betfairmarketvolumesclient import Client
import pandas as pd
import re
client = Client()

start_date: datetime = datetime.utcnow() - timedelta(days=90)
all = []
# get today meetings / races
while start_date < datetime.utcnow():
    # download yesterday's horse racing markets

    market_vols = client.get_gb_win_horse_racing_markets(start_date)
    all.extend(market_vols)

    start_date += timedelta(days=1)
new = []
for market_vol in all:
    data = market_vol.model_dump()
    data["selection_name"] = re.sub(r"[`']|\([^)]*\)", "", data["selection_name"]).lower().strip()
    # create an id index from data["selection_name"] and data["event_dt"] and format in DD-MM-YYYY
    data["id"] = f"{data['selection_name']}_{data['event_dt'].strftime('%d-%m-%Y')}"

    new.append(data)
df = pd.DataFrame(new)
df.to_csv('~/horse_racing_markets.csv', index=False)

# get today's horse racing selections
horse_racing_selections = client.get_gb_win_horse_racing_markets(
    date=datetime(2018,3,25)
)
all = []
for h in horse_racing_selections:
    if h.event_id == 141674319:
        all.append(h)

# get today's greyhound selections
greyhound_selections = client.get_greyhound_markets_for_date(date=datetime.utcnow())

data = client.get_horse_racing_markets_for_date(date=datetime(2018,3,24))
pass