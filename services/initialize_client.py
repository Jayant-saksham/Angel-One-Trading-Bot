from SmartApi import SmartConnect
from utils.helper import get_totp
from config import  config
from logzero import logger

class InitializeClient:
    def __init__(self):
        """Initialize the SmartConnect API client and session."""
        self.client = None
        self.session_data = None
        self.feed_token = None
        self._initialize_client()

    def _initialize_client(self):
        try:
            self.client = SmartConnect(api_key=config['api']['api_key'])
            self.session_data = self.client.generateSession(
                config['api']['client_code'],
                config['api']['password'],
                get_totp(config['api']['token'])
            )
            self.feed_token = self.client.getfeedToken()
            logger.info("Client initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing client: {e}")
            raise

    def get_client(self):
        return self.client

    def get_feed_token(self):
        return self.feed_token
