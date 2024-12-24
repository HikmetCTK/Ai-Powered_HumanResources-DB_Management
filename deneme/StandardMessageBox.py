from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from path_holder import *

def Information(obj, windowTitle:str, text:str):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle(windowTitle)
    msgBox.setText(text)
    msgBox.setIcon(QMessageBox.Icon.Information)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    return msgBox

def Warning(obj, windowTitle:str, text:str):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle(windowTitle)
    msgBox.setText(text)
    msgBox.setIcon(QMessageBox.Icon.Warning)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    return msgBox

def Error(obj, windowTitle:str, text:str):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle(windowTitle)
    msgBox.setText(text)
    msgBox.setIcon(QMessageBox.Icon.Critical)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    return msgBox

def Question(obj, windowTitle:str, text:str):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle(windowTitle)
    msgBox.setText(text)
    msgBox.setIcon(QMessageBox.Icon.Critical)
    msgBox.addButton(QMessageBox.StandardButton.Yes)
    msgBox.addButton(QMessageBox.StandardButton.No)
    msgBox.setDefaultButton(QMessageBox.StandardButton.No)
    return msgBox

def Successful(obj):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle("Successul")
    msgBox.setText("The process has been completed successfully.")
    iconPixmap = QPixmap(getPath("successful"))
    iconPixmap = iconPixmap.scaled(QSize(48,48),Qt.AspectRatioMode.IgnoreAspectRatio)
    msgBox.setIconPixmap(iconPixmap)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
    obj.reload()
    return msgBox

def NoResultsFound(obj):
    msgBox = QMessageBox(obj)
    msgBox.setWindowTitle("No Results Found")
    msgBox.setText("No results found for now. Check back later.")
    iconPixmap = QPixmap(getPath("no_results_found"))
    iconPixmap = iconPixmap.scaled(QSize(48,48),Qt.AspectRatioMode.IgnoreAspectRatio)
    msgBox.setIconPixmap(iconPixmap)
    msgBox.addButton(QMessageBox.StandardButton.Ok)
    msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
    return msgBox

def NoActionForRequests(obj):
    msg = "In order to interact with pending requests to accept or reject "\
        "them, use the corresponding <span style='color: #BE8AF9'>pending requests</span> module."
    return Information(obj, "No Action for Requests", msg)