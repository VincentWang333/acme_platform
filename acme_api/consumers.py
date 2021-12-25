import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class ACMEDataConsumer(AsyncJsonWebsocketConsumer):
    async def websocket_connect(self, message):
        await self.channel_layer.group_add(
            'data_update_group',
            self.channel_name
        )
        return await super().websocket_connect(message)
    
    async def websocket_receive(self, message):
        return await super().websocket_receive(message)

    async def websocket_disconnect(self, message):
        await self.channel_layer.group_discard(
            'data_update_group',
            self.channel_name
        )
        return await super().websocket_disconnect(message)


    async def send_update_signal(self, event):
        print('sending refresh signal', event)
        messageData = event['message']
        await self.send(text_data=json.dumps({ 
            'text': messageData
        }))

    


