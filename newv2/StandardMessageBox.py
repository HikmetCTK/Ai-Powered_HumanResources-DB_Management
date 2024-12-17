from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

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