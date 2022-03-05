# betfairmarketvolumeclient

simple downloader for the betfair [dailyspfiles](https://promo.betfair.com/betfairsp/prices/).

### Data Available

#### Horse Racing & Greyhound Racing 

- event_id (EVENT_ID) - Betfair internal event ID (market_id)
- menu_hint (MENU_HINT) - Contains the name of the race meeting
- event_name (EVENT_NAME) - The race name as it appears on the Betfair menu - place markets are always 'To Be Placed'
- event_dt (EVENT_DT) - The start time of the race
- selection_id (SELECTION_ID) - Betfair internal selection ID
- selection_name (SELECTION_NAME) - The name of the runner
- win_lose (WIN_LOSE) - 1 if the runner won (or placed), 0 if it lost (or was unplaced), 2 dead heat
- bsp (BSP) - Betfair Starting Price
- pp_wap (PPWAP) - Weighted Average Price of all bets placed pre-off
- morning_wap (MORNINGWAP) - Weighted Average Price of all bets placed before 11am GMT
- pp_max (PPMAX) - Maximum price placed before the off (only bets of a payout of more than GBP100 included)
- pp_min (PPMIN) - Minimum price placed before the off (only bets of a payout of more than GBP100 included)
- ip_max (IPMAX) - Maximum price placed in-play (only bets of a payout of more than GBP100 included)
- ip_min (IPMIN) - Minimum price placed in-play (only bets of a payout of more than GBP100 included)
- morning_traded_volume (MORNINGTRADEDVOL) - Amount traded before 11am GMT
- pp_traded_volume (PPTRADEDVOL) - Amount traded before the off
- ip_traded_volume (IPTRADEDVOL) - Amount traded in-play

### Usage

```python
from datetime import datetime
from betfairmarketvolumesclient import Client

client = Client()

# get today's horse racing selections
horse_racing_selections = client.get_horse_racing_markets_for_date(
    date=datetime.utcnow()
)

# get today's greyhound selections
greyhound_selections = client.get_greyhound_markets_for_date(date=datetime.utcnow())
```