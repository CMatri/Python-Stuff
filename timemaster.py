def sendGroupChatMessage():
    """
    Send Group Chat Messages.
    """
    import Skype4Py as skype
    skypeClient = skype.Skype()
    skypeClient.Attach()
    for elem in skypeClient.ActiveChats:
        if len(elem.Members) > 2:
            for friend in elem.Members:
                  print friend.Handle
            elem.SendMessage("SomeMessageHere")

sendGroupChatMessage()