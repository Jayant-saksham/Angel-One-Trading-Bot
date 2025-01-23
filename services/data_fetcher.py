from urllib.request import urlopen
import ssl
import json
import pandas as pd
from config import config
from logzero import logger
from model.model import Result

def fetch_instrument_list():
    """Fetch the instrument list from the configured URL."""
    url = config['urls']['instrument_list_url']
    logger.info(f"Starting to fetch instrument list from URL: {url}")

    try:
        # Disable SSL certificate verification
        context = ssl._create_unverified_context()
        response = urlopen(url, context=context)
        instrument_list = json.loads(response.read())
        logger.info("Instrument list fetched successfully.")
        return Result(success=True, data=pd.DataFrame(instrument_list))
    except Exception as e:
        logger.error(f"Error fetching instrument list from {url}: {e}")
        return Result(success=False, error=str(e))
