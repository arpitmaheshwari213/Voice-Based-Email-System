from Text_Speech import *
  
def choice():
   while 1:
    TextToSpeech('Speak 1 to Recieve e-mails')
    TextToSpeech('Speak 2 to Send an e-mail')
    TextToSpeech('Speak 3 to Log Out')

    response=SpeechToText();

    if response==1 : break
    elif response==2 : break
    elif response==3 : break
    else: TextToSpeech('Invalid Command')
     
     
                 

