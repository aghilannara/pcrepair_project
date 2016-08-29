from koslab.messengerbot.bot import BaseMessengerBot

#bot implementation
class ElizDoc(BaseMessengerBot):
    
    POSTBACK_HANDLERS = {
        'start_chatting':'start_chatting',
        'set_appointment':'set_appointment'
    }
    
    GREETING_TEXT = 'Hi, I\'m ElizDoc, I\'ll help you determine whether you have dengue or just a normal fever'
    STARTUP_MESSAGE = {
            'attachment': {
                'type':'template',
                'payload': {
                    'template_type':'generic',
                    'elements':[
                        {
                            'title':'ElizDoc here to help you, \"Say no to Dengue\"',
                            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Aedes_aegypti_feeding.jpg/800px-Aedes_aegypti_feeding.jpg',
                            'subtitle':'Worried you might catch dengue fever?',
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
        'check_fever':'check_fever',
        'check_headache':'check_headache',
        'check_eyes':'check_eyes',
        'joint_muscle':'joint_muscle',
        'check_fatigue':'check_fatigue',
        'check_nausea':'check_nausea',
        'vomit_rash':'vomit_rash'
    }

    def start_chatting(self, event):
        text = {             
            'text':'Do you experience sudden high fever?',
            'quick_replies':[
                {
                    'content_type': 'text',
                    'title': 'yes',
                    'payload': 'check_fever'
                },
                {
                    'content_type': 'text',
                    'title': 'no',
                    'payload': 'check_fever'
                }
            ]
        }

        self.send(recipient=event['sender'], message=text)

    def set_appointment(self, event):
        text = { 'text': 'Your appointment have been set, Thank You'}

        self.send(recipient=event['sender'], message=text)
 
    def check_fever(self, event):
        session = self.get_session(event)

        text = event['message'].get('text','')
        if text == 'yes':
            session.set('fever','true')
        else:
            session.set('fever','false')

        headache = {
            'text':'Do you have severe headaches?',
            'quick_replies':[
                {
                    'content_type': 'text',
                    'title': 'yes',
                    'payload': 'check_headache'
                },
                {
                    'content_type': 'text',
                    'title': 'no',
                    'payload': 'check_headache'
                }
            ]
        }
        self.send(recipient=event['sender'], message=headache)

    def check_headache(self, event):
        session = self.get_session(event)

        text = event['message'].get('text','')
        if text == 'yes':
            session.set('headache','true')
        else:
            session.set('headache','false')

        eyes = {
            'text':'Are you feeling any pain behind the eyes?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes',
                    'payload': 'check_eyes'
                },
                {
                    'content_type': 'text',
                    'title': 'no',
                    'payload': 'check_eyes'
                }
            ]
        }
            
        self.send(recipient=event['sender'], message=eyes)
        
    def check_eyes(self, event):
        session = self.get_session(event)

        text = event['message'].get('text','')
        if text == 'yes':
            session.set('eye_pain','true')
        else:
            session.set('eye_pain','false')
        joint_muscle = {
            'text':'Are you experiencing severe joint and muscle pain?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes',
                    'payload': 'joint_muscle'
                },
                {
                    'content_type': 'text',
                    'title': 'no',
                    'payload': 'joint_muscle'
                }
            ]
        }      
            
        self.send(recipient=event['sender'], message=joint_muscle)

    def joint_muscle(self, event):
        session = self.get_session(event)

        text = event['message'].get('text','')
        if text == 'yes':
            session.set('joint_muscle','true')
        else:
            session.set('joint_muscle','false')

        fatigue = {
            'text':'Do you feel fatigue?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes',
                    'payload': 'check_fatigue'
                },
                {
                    'content_type': 'text',
                    'title': 'no',
                    'payload': 'check_fatigue'
                }
            ]
        }
            
        self.send(recipient=event['sender'], message=fatigue)

    def check_fatigue(self, event):
        session = self.get_session(event)

        text = event['message'].get('text','')
        if text == 'yes':
            session.set('fatigue','true')
        else:
            session.set('fatigue','false')
        
        nausea = {
            'text':'How about nausea?',
            'quick_replies': [
                {
                    'content_type': 'text',
                    'title': 'yes',
                    'payload': 'check_nausea'
                },
                {
                    'content_type': 'text',
                    'title': 'no',
                    'payload': 'check_nausea'
                }
            ]
        }

        self.send(recipient=event['sender'], message=nausea)

    def check_nausea(self, event):
        session = self.get_session(event)

        text = event['message'].get('text','')
        if text == 'yes':
            session.set('nausea','true')
        else:
            session.set('nausea','false')
        
        vomitting = {
            'text':'Do you experience vomitting and skin rash?',
            'quick_replies': [
                {   
                    'content_type': 'text',
                    'title': 'yes',
                    'payload': 'vomit_rash'
                },
                {
                    'content_type': 'text',
                    'title': 'no',
                    'payload': 'vomit_rash'
                }
            ]
        }

        self.send(recipient=event['sender'], message=vomitting)
        
    def vomit_rash(self, event):
        session = self.get_session(event)

        text = event['message'].get('text','')
        if text == 'yes':
            session.set('vomit_rash','true')
        else:
            session.set('vomit_rash','false')
        
        response = { 'text': 'You are suspected to have dengue\n\nWe are setting up appointment with you for further checkup, select from below'}

        clinics = {
            'attachment': {
                'type':'template',
                'payload': {
                    'template_type':'generic',
                    'elements':[
                        {
                            'title':'Hospital Putrajaya',
                            'subtitle':'Wilayah Persekutuan Putrajaya',
                            'buttons':[
                                {
                                    'type':'postback',
                                    'title':'Set Appointment',
                                    'payload':'set_appointment'
                                }
                            ]
                        },
                        {
                            'title':'Hospital Serdang',
                            'subtitle':'Serdang, Selangor',
                            'buttons':[
                                {
                                    'type':'postback',
                                    'title':'Set Appointment',
                                    'payload':'set_appointment'
                                }
                            ]
                        },
                        {
                            'title':'Hospital Selayang',
                            'subtitle':'Selayang, Selangor',
                            'buttons':[
                                {
                                    'type':'postback',
                                    'title':'Set Appointment',
                                    'payload':'set_appointment'
                                }
                            ]
                        },
                        {
                            'title':'Hospital Columbia',
                            'subtitle':'Puchong, Selangor',
                            'buttons':[
                                {
                                    'type':'postback',
                                    'title':'Set Appointment',
                                    'payload':'set_appointment'
                                }
                            ]
                        }
                    ]
                }
            }
        }

        

        self.send(recipient=event['sender'], message=response)
        self.send(recipient=event['sender'], message=clinics)


    def quick_reply(self, event):
        payload = event['message']['quick_reply']['payload']
        method = self.QUICK_REPLY.get(payload, None)
        if method:
            getattr(self, method)(event)


    def message_hook(self, event):
        if event['message'].get('quick_reply', None):
            self.quick_reply(event)
        else:
            self.handle_message(event)
