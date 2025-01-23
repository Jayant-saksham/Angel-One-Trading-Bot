from services.initialize_client import InitializeClient
from services.data_fetcher import fetch_instrument_list
from services.websocket_manager import WebSocketManager
from config import config
from utils.logger import logger
from time import sleep
from SmartApi.smartWebSocketV2 import SmartWebSocketV2

def main():
    # Initialize the API client
    # client_initializer = InitializeClient()
    # client = client_initializer.get_client()
    # feed_token = client_initializer.get_feed_token()


    # Fetch instrument list
    # instrument_list = fetch_instrument_list()
    # if instrument_list.is_success():
    #     instrument_list = instrument_list.get_data()
    #     logger.info("Processing fetched instrument list.")
    # else:
    #     error_message = instrument_list.get_error()
    #     logger.error(f"Failed to fetch instrument list. Error: {error_message}")
    #     exit(1)

    # WebSocket client
    websocket_manager = WebSocketManager(
        jwt_token=config['api']['jwt_token'],
        api_key=config['api']['api_key'],
        client_code=config['api']['client_code'],
        feed_token=config['api']['feed_token']
    )

    # Connect to WebSocket
    websocket_manager.connect()

    # Run WebSocket connection in a loop
    # try:
    #     while True:
    #         sleep(1)  # Keep the connection alive
    # except KeyboardInterrupt:
    #     logger.info("User interrupted the connection.")
    #     websocket_manager.close()

if __name__ == "__main__":
    main()
    # print()



