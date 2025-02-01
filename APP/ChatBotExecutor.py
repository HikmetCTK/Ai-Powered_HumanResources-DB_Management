from PyQt6.QtCore import QThread, pyqtSignal
import DB_Agent

class ChatBotWorker(QThread):
    response = pyqtSignal(str)
    isWorking = pyqtSignal(bool)

    def ask(self, inputValue):
        self.inputValue = inputValue

    def run(self):
        self.isWorking.emit(True)
        
        ret = DB_Agent.ask_chatbot(self.inputValue)

        if not isinstance(ret, str):
            newRet = f"Returned a non-string response -> {type(ret)} | {str(ret)}"
            ret = newRet
        
        self.response.emit(ret)
        self.isWorking.emit(False)


# END