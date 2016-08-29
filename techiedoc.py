from koslab.messengerbot.bot import BaseMessengerBot

#bot implementation
class TechieDoc(BaseMessengerBot):

    POSTBACK_HANDLERS = { 
        'start_chatting':'start_chatting'
    }
    
    GREETING_TEXT = 'Hello!. Aghilan, at your service!'
    STARTUP_MESSAGE = {
        'attachment': {
            'type':'template',
            'payload': {
                'template_type':'generic',
                'elements':[
                    {   
                        'title':'TechieDoc is here to help you.',
                        'image_url':'http://wpjuices.com/wp-content/uploads/2012/12/Techie.jpg',
                        'subtitle':'Worried of computer problems lately? Try to chat us up',
                        'buttons':[
                            {
                             'type':'postback',
                             'title':'Start Chatting',
                             'payload':'start_chatting'
                            }
                        ]
                    }
                ]
            }
        }
    }
    
    PERSISTENT_MENU = [{
        'type': 'postback',
        'title': 'Start Assessment',
        'payload': 'messengerbot.get_started'
    }]



    QUICK_REPLY = {
        'choose_category':'choose_category',
        'blue_screen_of_death':'blue_screen_of_death',
        'corrupt_software':'corrupt_software',
        #'empty_screen':'empty_screen',
        #'windows_license':'windows_license',
        #'slow_performance':'slow_performance'
    }

    def start_chatting(self,event):
        text = {
            'text':'Do you experience computer problem?',
            'quick_replies':[
                {
                    'content_type':'text',
                    'title':'yes',
                    'payload':'choose_category'
                },
                {
                    'content_type':'text',
                    'title':'no',
                    'payload':'choose_category'
                }
            ]
        }
        self.send(recipient=event['sender'], message=text)
    def choose_category(self,event):
        text = event['message'].get('text','') 
        if text == 'yes':

            choice = {
                'attachment':{
                    'type':'template',
                    'payload':{
                        'template_type':'button',
                        'text':'Choose a common category',
                        'buttons':[
                            {
                                'type':'postback',
                                'title':'blue screen',
                                'payload':'blue_screen_of_death'
                            },
                            {
                                'type':'postback',
                                'title':'Program not running/missing/corrupted',
                                'payload':'corrupt_software'
                            }
                        ]
                    }
                }
            }

    def quick_reply(self,event):
        payload = event['message']['quick_reply']['payload']
        method = self.QUICK_REPLY.get(payload,None)
        if method:
            getattr(self, method)(event)

    def message_hook(self,event):
        if event['message'].get('quick_reply',None):
            self.quick_reply(event)
        else:
            self.handle_message(event)
    
