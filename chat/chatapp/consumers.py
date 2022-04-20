from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):  
        async_to_sync(self.channel_layer.group_add)("programmer", self.channel_name)  #create channel group
        print('websocket connected', event)
        print('channel layer....', self.channel_layer) #get default channel layer
        print('channel name... ', self.channel_name)  #get default channel name
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('websocket message received', event['text'])
        
        # self.send({
        #     "type": "websocket.send",
        #     "text": event["text"],
        # })
        async_to_sync(self.channel_layer.group_send)('programmer',{
            'type': 'chat.message',
            "message": event['text'],
        })

    def chat_message(self,event):
        print('event....', event)
        print('message...', event['message'])
        self.send({
            'type': 'websocket.send',
            'text': event['message'],
        })
        # self.send(text_data=event["text"])
    
        
    def websocket_disconnect(self, event):
        print('websocket disconnected', event)