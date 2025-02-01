from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *
from PyQt6.QtGui import QPixmap

def _CreateInformativeMessageBox(obj, windowTitle:str, text:str, icon):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle(windowTitle)
    msgBox.setText(text)
    msgBox.setIcon(icon)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    return msgBox

def _CreateResultNotifierMessageBox(obj, windowTitle:str, text:str, iconPixmap:QPixmap):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle(windowTitle)
    msgBox.setText(text)
    iconPixmap = iconPixmap.scaled(QSize(48,48), Qt.AspectRatioMode.IgnoreAspectRatio)
    msgBox.setIconPixmap(iconPixmap)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
    return msgBox

def Information(obj, windowTitle:str, text:str):
    icon = QMessageBox.Icon.Information
    return _CreateInformativeMessageBox(obj, windowTitle, text, icon)

def Warning(obj, windowTitle:str, text:str):
    icon = QMessageBox.Icon.Warning
    return _CreateInformativeMessageBox(obj, windowTitle, text, icon)

def Error(obj, windowTitle:str, text:str):
    icon = QMessageBox.Icon.Critical
    return _CreateInformativeMessageBox(obj, windowTitle, text, icon)

def Successful(obj, reload:bool|None = True):
    title = "Successul"
    text = "The process has been completed successfully."
    iconPixmap = QPixmap(":/newSource/icons/successful.png")

    try:
        if reload == True: obj.reload()
        elif reload == False: obj.LoadDashboard()
        else: pass
    except:
        pass
    
    return _CreateResultNotifierMessageBox(obj, title, text, iconPixmap)

def NoResultsFound(obj):
    title = "No Results Found"
    text = "No results found for now. Check back later."
    iconPixmap = QPixmap(":/newSource/icons/no_results_found.png")
    return _CreateResultNotifierMessageBox(obj, title, text, iconPixmap)

def NoActionForRequests(obj):
    msg = "In order to interact with pending requests to accept or reject "\
        "them, use the corresponding <span style='color: #BE8AF9'>pending requests</span> module."
    return Information(obj, "No Action for Requests", msg)

def Question(obj, windowTitle:str, text:str):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle(windowTitle)
    msgBox.setText(text)
    msgBox.setIcon(QMessageBox.Icon.Critical)
    msgBox.addButton(QMessageBox.StandardButton.Yes)
    msgBox.addButton(QMessageBox.StandardButton.No)
    msgBox.setDefaultButton(QMessageBox.StandardButton.No)
    return msgBox


# END