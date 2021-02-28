
import asyncio
from botbuilder_discord import OfflineConnector


if __name__ == '__main__':
    connector = OfflineConnector(bot_api_url="http://localhost:3978/api/messages", listener_port=5789)
    response = asyncio.run(connector.send_message(745192707982491698, "Hello !"))
    print(response)
