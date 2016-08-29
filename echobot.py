from koslab.messengerbot.bot import BaseMessengerBot
import pudb

class EchoBot(BaseMessengerBot):

    GREETING_TEXT = 'Hello!. Aghilan, at your service!'
    STARTUP_MESSAGE = {'text':'Welcome to PC self-diagnostic repair centre. Please answer the following questions. Type OK to get started'}
        
    def message_hook(self,event):
        #text = event['message'].get('text','')
        #self.send(recipient=event['sender'], sender_action='mark_seen')
        #self.send(recipient=event['sender'], message={'text':text})
#        self.send(recipient=event['sender'], message={
#            'attachment':{
#                  'type':'image',
#                  'payload':{
#                      'url':'http://www.sevacall.com/blog/wp-content/uploads/2013/07/how-to-replace-a-laptop-screen.jpg'
#                            }
#                        }
#                    })

        self.send(recipient=event['sender'], 
                  message={'text':'Pick a common problem'}, 
                  {'quick_replies':
                   [
                       {'content_type':'text','title':'RAM','payload':RAM_chosen}
                   ]
                  }
                 )
