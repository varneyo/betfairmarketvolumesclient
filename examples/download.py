from datetime import datetime, timedelta
from betfairmarketvolumesclient import Client
import logging
from betfairmarketvolumesclient import resources
import time
from typing import List, Optional
import pandas as pd
from betfairmarketvolumesclient.utils import parse_to_data_frame
import os

logger = logging.getLogger(__name__)

"""
This script can be run using the terminal, navigating to the examples folder and running python download.py
"""
client = Client()
local_directory: str = (
    "please add a path in here"  # i.e. "/Users/yourname/Downloads/betfair_bsp_files/"
)

download_historical: bool = (
    False  # This will take some time to download all the files if set to True
)
run_daily_download_loop: bool = (
    True  # This will also run the daily download of the files
)
historical_start_date: datetime = datetime(2010, 1, 1)
check_frequency_sec: int = 60
overwrite_files: bool = (
    False  # set to true if you want to overwrite files that already exist
)


def exception_handled_download(
    download_date: datetime,
) -> List[resources.MarketSelection]:
    try:
        uk: List[resources.MarketSelection] = client.get_gb_win_horse_racing_markets(download_date)

        ire: List[resources.MarketSelection] = client.get_ire_win_horse_racing_markets(download_date)

        return uk + ire
    except Exception as e:
        logger.exception(f"Issue ({e} when download the file for {download_date}")
        return []


def save_data_frame_to_csv(data: List[resources.MarketSelection], data_date: Optional[datetime] = None):

    df: Optional[pd.DataFrame] = parse_to_data_frame(data)
    if df is not None:

        if data_date is None:
            data_date = data[0].event_dt

        if not os.path.isfile(local_directory) or overwrite_files:
            file_name: str = (
                f"{local_directory}{data_date.strftime('%Y-%m-%d')}.csv"
            )
            df.to_csv(file_name)
            logger.info(
                f"Saved file for {data_date.strftime('%Y-%m-%d')} at location {file_name}"
            )


# this section of code will run historical downloads
if download_historical:
    while historical_start_date < datetime.utcnow():
        bsp_data: List[resources.MarketSelection] = exception_handled_download(
            historical_start_date
        )
        if bsp_data:
            save_data_frame_to_csv(bsp_data)

        historical_start_date += timedelta(days=1)
        time.sleep(1)

# this section of code will run the daily download loop
if run_daily_download_loop:
    while True:
        bsp_data: List[resources.MarketSelection] = exception_handled_download(
            datetime.utcnow()
        )
        if bsp_data:
            save_data_frame_to_csv(bsp_data)

        # sleep to not bombard the server
        time.sleep(check_frequency_sec)
