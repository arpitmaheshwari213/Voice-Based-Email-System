"""Get a list of Messages from the user's mailbox.
"""

from apiclient import errors
from Authentication import *
import vansh2
import html2text
import pyttsx

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



maillist=ListMessagesMatchingQuery(service, 'me')

number=0
messageIDs=list()
while number < 10 :
  messageIDs.append(maillist[number]['id'])
  number=number + 1
print messageIDs
response=raw_input('Enter which message to receive :  ')
response=int(response)
message=vansh2.GetMimeMessage(service,"me",messageIDs[response])
print "message----------",message
print message['from']

a=message.get_payload()
print "---------------a---------",a
print "--------------a[0]--------",a[0]
b=a[0].get_payload()
print type(b)
print  "--------------a[]--------",a[1]
#c=b.split()
c=b
print c
engine=pyttsx.init()
for word in c:
  engine.say(word)
  
engine.runAndWait()
  
engine=pyttsx.init()
engine.say(c)
engine.runAndWait()










      

