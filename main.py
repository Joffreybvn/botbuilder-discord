
import asyncio
from botbuilder_discord import OfflineConnector


if __name__ == '__main__':
    connector = OfflineConnector()
    response = asyncio.run(connector.send_message(745192707982491698, "Hello !"))
    print(response)
