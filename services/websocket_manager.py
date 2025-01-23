import json
import logging
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from config.config_loader import get_subscription_tokens
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebSocketManager:
    def __init__(self, jwt_token, api_key, client_code, feed_token):
        self.jwt_token = jwt_token
        self.api_key = api_key
        self.client_code = client_code
        self.feed_token = feed_token
        self.websocket = None

    def on_data(self, wsapp, message):
        if message != b'\x00':
            logger.info("WebSocket connection established.")


        # if message != b'\x00':
        #     logger.info(f"Data received: {message}")
        #     try:
        #         data = json.loads(message)
        #         logger.info(f"Processed Data: {data}")
        #     except json.JSONDecodeError as e:
        #         logger.error(f"Error decoding message: {e}")

    def on_open(self, wsapp):
        logger.info("WebSocket connection established.")
        # Fetch tokens from the config
        tokens_to_subscribe = get_subscription_tokens()
        print("Tokens to subscribe", tokens_to_subscribe)
        if tokens_to_subscribe:
            self.subscribe(tokens_to_subscribe)
        else:
            logger.error("No tokens found to subscribe to.")

    def on_error(self, wsapp, error):
        pass
        logger.error(f"Error occurred", error)

    def on_close(self, wsapp):
        pass
        logger.info("WebSocket connection closed.")

    def subscribe(self, tokens):
        if self.websocket:
            print("Yes websocket is true")
            for token in tokens:
                print("token for loop", token)
                logger.info(f"Subscribing to token: {token}")
                self.websocket.subscribe("abcde12345", 1, [token])  # Use appropriate correlation ID, mode
        else:
            logger.error("WebSocket connection not established.")

    def connect(self):
        logger.info("Establishing WebSocket connection...")
        self.websocket = SmartWebSocketV2(self.jwt_token, self.api_key, self.client_code, self.feed_token)
        self.websocket.on_open = self.on_open
        self.websocket.on_data = self.on_data
        self.websocket.on_error = self.on_error
        self.websocket.on_close = self.on_close

        self.websocket.connect()

    def close(self):
        if self.websocket:
            self.websocket.close_connection()
            logger.info("WebSocket connection closed manually.")
        else:
            logger.error("WebSocket connection was not established.")
