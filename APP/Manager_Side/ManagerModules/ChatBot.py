
def addMessageToChatBotArea(obj, msg, color = "#FFFFFF"):
    obj.textEdit_chatbot.append(msg)
    length = len(obj.textEdit_chatbot.toPlainText())
    obj.textEdit_chatbot.setTextColorUntilIndex(length + len(msg), color, fromIndex = length - len(msg))

def restartChatBotAgent(obj):
    if obj.chatBotAgent.isRunning():
        obj.chatBotAgent.terminate()
        obj.isChatBotInputPermitted(isWorking = False)

def getResponseFromChatBot(obj, response):
    if response:
        obj.addMessageToChatBotArea("ChatBot:", "#BE8AF9")
        obj.addMessageToChatBotArea(f"{response}\n")

def isChatBotInputPermitted(obj, isWorking):
    if isWorking == True:
        obj.btn_chatbot_send.setEnabled(False)
        obj.lineEdit_chatbot_input.setReadOnly(True)
        obj.lineEdit_chatbot_input.setPlaceholderText("Generating response...")
    else:
        obj.btn_chatbot_send.setEnabled(True)
        obj.lineEdit_chatbot_input.setReadOnly(False)
        obj.lineEdit_chatbot_input.setPlaceholderText("Send your message to ChatBot")

def sendMessageToChatBot(obj):
    msg = obj.lineEdit_chatbot_input.text().strip()
    if msg == "": return
    obj.lineEdit_chatbot_input.clear()
    obj.addMessageToChatBotArea(f"{obj.name.capitalize()}:", "#98FB98")
    obj.addMessageToChatBotArea(f"{msg}\n")

    obj.chatBotAgent.ask(msg)
    obj.chatBotAgent.start()

    obj.lineEdit_chatbot_input.setFocus()

def LoadChatBot(obj):
    restartChatBotAgent(obj)

    obj.stackedWidget_side_menu.setVisible(True)
    obj.stackedWidget_side_menu.setCurrentIndex(5)
    obj.textEdit_chatbot.clear()
    obj.lineEdit_chatbot_input.clear()
    obj.addMessageToChatBotArea("ChatBot:", "#BE8AF9")
    obj.addMessageToChatBotArea(f"Hello {obj.name.capitalize()}, what can I help you with today?\n")
    obj.lineEdit_chatbot_input.setFocus()


# END