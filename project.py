#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr

"""Get a list of Messages from the user's mailbox.
"""

from apiclient import errors
from Authentication import *
import vansh2
import html2text
import pyttsx
import Text_Speech

def ListMessagesMatchingQuery(service, user_id, query=''):
  """List all Messages of the user's mailbox matching the query.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

  Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError, error:
    print 'An error occurred: %s' % error


def ListMessagesWithLabels(service, user_id, label_ids=[]):
  """List all Messages of the user's mailbox with label_ids applied.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    label_ids: Only return Messages with these labelIds applied.

  Returns:
    List of Messages that have all required Labels applied. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate id to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               labelIds=label_ids).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id,
                                                 labelIds=label_ids,
                                                 pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError, error:
    print 'An error occurred: %s' % error

print("Say ")
search=Text_Speech.SpeechToText()
maillist=ListMessagesMatchingQuery(service, 'me','from:'+search)
#messageIDs=list()
#messageIDs.append(maillist[0]['id'])
print maillist
#current_message=vansh2.GetMimeMessage(service,"me",messageIDs[0])
#print current_message

'''
number=0
messageIDs=list()
while number < 10 :
  messageIDs.append(maillist[number]['id'])
  number=number + 1


number=0
senders=list()
while number < 10 :
  current_message=vansh2.GetMimeMessage(service,"me",messageIDs[number])
  senders.append(current_message['from'])
  number=number+1

engine=pyttsx.init()
engine.setProperty('rate',150)
#response=raw_input('Enter which message to receive :  ')
engine.say('Say the serial number of E-Mail to read !')
number=0
while number < 10 :
  engine.say(str(number)+' '+senders[number])
  number=number+1

engine.runAndWait()
del engine

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
response=r.recognize_google(audio)

response=int(response)
message=vansh2.GetMimeMessage(service,"me",messageIDs[response])
a=message.get_payload()
b=a[0].get_payload()
print type(b)
#c=b.split()
c=b
print c
engine2=pyttsx.init()
engine2.setProperty('rate',150)
#for word in c:
#  engine.say(word)
  
#engine.runAndWait()
  

engine2.say(c)
engine2.runAndWait()
'''










      

