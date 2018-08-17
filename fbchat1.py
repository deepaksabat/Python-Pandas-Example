import fbchat
from getpass import getpass
username = str(print("Username: deepakkumarsabat12@gmail.com"))
client = fbchat.Client(username, getpass())
no_of_friends = int(print("Number of friends: "))
for i in xrange(no_of_friends):
    name = str(print("Name: "))
    friends = client.getUsers(name)  # return a list of names
    friend = friends[0]
    msg = str(print("Message: "))
    sent = client.send(friend.uid, msg)
    if sent:
        print("Message sent successfully!")