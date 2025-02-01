from PyQt6.QtWidgets import (QWidget, QLineEdit, QTextEdit, QCheckBox, QTableWidget, QHBoxLayout,
                             QVBoxLayout, QGraphicsDropShadowEffect, QPushButton, QLabel, QGridLayout,
                             QWidgetAction, QSpacerItem, QSizePolicy, QTableWidgetItem, QStyleOption,
                             QStyle)
from PyQt6.QtCore import pyqtSignal, Qt, QSize, QRect
from PyQt6.QtGui import QIcon, QPainter, QColor, QTextCursor, QTextCharFormat, QCursor, QPixmap
import db_man_projectv3_test
from package.PathHolder import getPath

class IconManager:
    # QPixmap: Must construct a QGuiApplication before a QPixmap
    
    # Store the icons once they are loaded to use them more than once
    # when one icon is to be used in more than one place
    iconTypeIcons = dict()
    pixmapTypeIcons = dict()

    @staticmethod    
    def getIcon(iconName:str, type="icon"):
        if type == "icon":
            cacheIcon = IconManager.iconTypeIcons.get(iconName, None)
            if cacheIcon != None:
                return cacheIcon
            
            icon = QIcon(f":/newSource/icons/{iconName}.png")
            # icon.addPixmap(QPixmap(f":/newSource/icons/{iconName}.png"), QIcon.Mode.Normal, QIcon.State.Off)

            IconManager.iconTypeIcons[iconName] = icon

            return icon
        
        elif type == "pixmap":
            cachePixmap = IconManager.pixmapTypeIcons.get(iconName, None)
            if cachePixmap != None:
                return cachePixmap
            
            pixmap = QPixmap(f":/newSource/icons/{iconName}.png")

            IconManager.pixmapTypeIcons[iconName] = pixmap

            return pixmap

class CustomQWidget(QWidget):
    """
    Widgets derived from this class are clickable and emit a special signal when clicked.
    """
    clickedValue = pyqtSignal(str)  # special signal, str will be emitted

    def __init__(self, parent):
        super().__init__(parent=parent)

    def mousePressEvent(self, event):
        # objectNames like: m_widget_summary_pm, e_widget_summary_par, ...
        
        self.clickedValue.emit(self.objectName())
        super().mousePressEvent(event)
    
    def enterEvent(self, event):
        self.setStyleSheet("""
                           CustomQWidget{
                            border: 1px solid;
                            border-radius: 20px;
                            border-color: #808080;
                           }
                           """)
    
    def leaveEvent(self, event):
        self.setStyleSheet("""
                           CustomQWidget{
                            border: 1px solid;
                            border-radius: 20px;
                            border-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 rgb(58, 62, 88), stop: 1 rgb(119, 127, 148));
                           }
                           """)
    
    def paintEvent(self, pe):
        """
        The reason of that function can be found on https://stackoverflow.com/a/18344643
        """
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)

class CustomTextEdit(QTextEdit):
    """
    TextEdit objects derived from this class are single-line and have
    a feature for special partial coloring for filter expressions.

    Contains a trigger expression (@) to open the pop-up filter menu
    designed for filter selection.

    Placeholder text feature included manually.
    """
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.originalColor = QColor("#ffffff")
        self.placeHolderText = "Search something, @filter to filter"
        # The color of the placeholder text is different from the actual text color
        self.placeHolderColor = "#d3d3d3"
        # Set placeholder text
        self.setPlaceHolderText()

    def setTextColorUntilIndex(self, toIndex:int, color:str="#DDA0DD", fromIndex:int=0, normalColor:str|None= None):
        """
        Change the color of a text with index range
        """
        cursor = self.textCursor()
        # Change the color of the specified index range
        cursor.setPosition(fromIndex)
        cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, toIndex)
        format = QTextCharFormat()
        format.setForeground(QColor(color))
        cursor.mergeCharFormat(format)
        
        # If toIndex is less than the length of the entire text, the remaining piece of text
        # must be its normal color
        if toIndex < len(self.toPlainText()):
            cursor.setPosition(toIndex)
            cursor.movePosition(QTextCursor.MoveOperation.End, QTextCursor.MoveMode.KeepAnchor)
            if not normalColor: color = QColor(self.placeHolderColor)
            else: color = QColor(normalColor)
            format.setForeground(color)
            cursor.mergeCharFormat(format)

        # Move the cursor to the end of the text
        cursor.clearSelection()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.setTextCursor(cursor)

    def setPlaceHolderText(self):
        """
        Set placeholder text
        """
        # Set text
        self.setText(self.placeHolderText)
        # Set the color of the entire text to placeholder text color
        self.setTextColorUntilIndex(len(self.placeHolderText), self.placeHolderColor)
        # Highlight the part '@filter' of the place holder text
        text = self.toPlainText()
        self.setTextColorUntilIndex(toIndex=text.find(" ", text.find("@")), fromIndex=text.find("@"), color="#DDA0DD")
        cursor = self.textCursor()
        cursor.clearSelection()
        # Cursor must be at the beginning of the line
        cursor.movePosition(QTextCursor.MoveOperation.StartOfLine)
        self.setTextCursor(cursor)

    def keyPressEvent(self, event):
        """
        Some keystrokes on this TextEdit need to be specifically checked and handled specifically.
        """
        if event.key() == Qt.Key.Key_Backspace:
            # If backspace key is pressed...

            text = self.toPlainText()
            cursor = self.textCursor()
            # Split the text into two parts based on the cursor
            text_left_side = text[:cursor.position()]
            text_remaining = text[cursor.position():]

            if text_left_side.startswith("@") and text_left_side.endswith("| "):
                # Note that left side is made up of only filter expression and cursor
                # is placed at the end of the filter expression. Delete the entire
                # filter expression with only one backspace stroke and keep the remaining
                # text, if exists.
                self.clear()
                # Remaining text must be in original text color
                self.setTextColor(self.originalColor)
                if text_remaining != "":
                    # If remaining text exists, keep it as normal text
                    self.setText(text_remaining)
                    cursor = self.textCursor()
                    cursor.clearSelection()
                    # Move the cursor to the end of the line
                    cursor.movePosition(QTextCursor.MoveOperation.EndOfLine)
                    self.setTextCursor(cursor)
            else:
                # Note that left side is not made up of filter expression, that's why
                # handle the event normally, as usual.
                super().keyPressEvent(event)
            
            if self.toPlainText() == "":
                # After handling the event of backspace stroke,
                # if there is no text left in TextEdit, set placeholder.
                self.setPlaceHolderText()
                
            
        elif event.key() in [Qt.Key.Key_Return, Qt.Key.Key_Enter]:
            # Do not allow multiple lines
            event.ignore()

        elif event.key() in [Qt.Key.Key_Left]:
            # The user cannot move the cursor into the filter expression by pressing the left key
            # We need to make sure that the cursor always remains to the right of the filter expression
            text = self.toPlainText()
            if text == self.placeHolderText or (text.startswith("@") and text.endswith("| ")):
                # Once the placeholder text is set, the TextEdit is considered as empty
                # Do not let the cursor enter inside of the filter expression
                # Ignore event
                event.ignore()
            else:
                cursor = self.textCursor()
                index = cursor.position()
                if (index <= text.find(" ", text.find("|")) + 1) and text.startswith("@"):
                    event.ignore()
                else:
                    # If the cursor is in the allowed area of the text, allow move
                    super().keyPressEvent(event)
            
        else:
            # No special conditions for other keystrokes
            text = self.toPlainText()

            self.setTextColor(self.originalColor)
            if text == self.placeHolderText:
                # If the placeholder text is set when the
                # keystroke event comes, clear placeholder
                # text and focus
                self.clear()
                self.setFocus()

            # Allow the event
            super().keyPressEvent(event)

        if self.toPlainText() == "":
            # Once the TextEdit becomes empty, set the placeholder text
            self.setPlaceHolderText()

    def mousePressEvent(self, event):
        text = self.toPlainText()
        if text == self.placeHolderText:
            # If the placeholder text is set, that is the TextEdit
            # is empty, mouse click must place the cursor at the
            # beginning of the line
            cursor = self.textCursor()
            cursor.clearSelection()
            cursor.movePosition(QTextCursor.MoveOperation.Start)
            self.setTextCursor(cursor)
        else:
            # If the TextEdit is not empty...
            cursor = self.cursorForPosition(event.pos())
            index = cursor.position()
            if index <= text.find(" ", text.find("|")):
                # Ignore the attempt made to place the cursor
                # inside the filter expression
                event.ignore()
            else:
                # Otherwise, allow the event
                return super().mousePressEvent(event)
    
    def mouseDoubleClickEvent(self, event):
        if self.toPlainText() == self.placeHolderText:
            # Double click cannot select the placeholder text
            event.ignore()
        else:
            # Otherwise, allow the event
            return super().mouseDoubleClickEvent(event)
    
    @staticmethod
    def textChanged_(obj, textEdit:QTextEdit|None):
        if not textEdit:
            return
        text = textEdit.toPlainText()
        if text == "@":
            # Open filter menu
            button_pos = textEdit.mapToGlobal(textEdit.rect().bottomLeft())
            obj.filterMenu.exec(button_pos)
        
        if not text.startswith("@"):
            # Do not apply filter, just search in the current table
            obj.search_table(search_text = text, columnNumber = None)
            obj.btn_page_search_search.setVisible(False)
        
        else:
            if text != textEdit.placeHolderText:
                obj.btn_page_search_search.setVisible(True)
            else:
                obj.btn_page_search_search.setVisible(False)

class CustomQPushButton(QPushButton):
    """
    QPushButtons derived from this class
    have a shadow effect that appear when
    mouse enter event triggered.
    """
    def __init__(self, parent):
        super().__init__(parent=parent)
    
    def enterEvent(self, event):
        shadowEffect = QGraphicsDropShadowEffect()
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0,5)
        self.setGraphicsEffect(shadowEffect)
        return super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.setGraphicsEffect(None)
        return super().leaveEvent(event)

class MessagePeopleCardWidget(QWidget):
    """
    Class for specially designed widget for people cards
    """
    clickedValue = pyqtSignal(str)  # special signal, str will be returned

    def __init__(self):
        super().__init__()

    def mousePressEvent(self, event):
        # Emit the object name when mouse click event occurs
        self.clickedValue.emit(self.objectName())
        super().mousePressEvent(event)

class CheckBoxWidget(QWidget):
    """
    Class for specially designed widget to add checkboxes into a column of a QTableWidget
    """

    # Keep record of created instances to reach them later on
    instances:list[QCheckBox] = []
    objectRowDataMatch:dict = dict()

    def __init__(self, row_index, row_data, DynamicProperties:None|dict = None):
        super().__init__()

        if DynamicProperties == None: DynamicProperties = dict()

        checkState = False if DynamicProperties.get("checkState", None) else DynamicProperties.get("checkState")
        checkBoxText = False if DynamicProperties.get("checkBoxText", None) else DynamicProperties.get("checkBoxText")
        self.placedWidget = None if DynamicProperties.get("placedWidget", None) else DynamicProperties.get("placedWidget")

        if checkState == False:
            self.checkState = Qt.CheckState.Unchecked
        else:
            self.checkState = Qt.CheckState.Checked

        layout = QHBoxLayout(self)
        
        # Create the checkbox
        self.dynamicCheckBox = QCheckBox(checkBoxText, self)
        self.dynamicCheckBox.setObjectName(f"dynamicCheckBox_{row_data[0]}")
        self.dynamicCheckBox.setStyleSheet("""
                                    QCheckBox {
                                    background-color: transparent;
                                    color: #ffffff;
                                    spacing: 5px;
                                    }
                                    QCheckBox::indicator {
                                    width: 40px; height: 25px;
                                    }
                                    """)
        self.dynamicCheckBox.setFixedSize(40,25)
        self.dynamicCheckBox.setCheckState(self.checkState)
        
        # Connect the checkbox
        self.dynamicCheckBox.checkStateChanged.connect(self.handleCheckStateChange)

        layout.addWidget(self.dynamicCheckBox)

        # Add the instance to a list to access them later
        CheckBoxWidget.instances.append(self.dynamicCheckBox)

        # Save the rowData with the objectName of the checkbox
        CheckBoxWidget.objectRowDataMatch[self.dynamicCheckBox.objectName()] = row_data
    
    def _checkIsRowHidden(table:QTableWidget|None, rowNumber:int) -> bool:
        # A table can be given or cannot be given. These functions
        # should effectively work both for these cases.

        if not table: return False
        return table.isRowHidden(rowNumber)

    @staticmethod
    def checkAll(table:QTableWidget|None = None):
        for index in range(len(CheckBoxWidget.instances)):
            if not CheckBoxWidget._checkIsRowHidden(table, index):
                CheckBoxWidget.instances[index].setCheckState(Qt.CheckState.Checked)
    
    @staticmethod
    def uncheckAll(table:QTableWidget|None = None):
        for index in range(len(CheckBoxWidget.instances)):
            if not CheckBoxWidget._checkIsRowHidden(table, index):
                CheckBoxWidget.instances[index].setCheckState(Qt.CheckState.Unchecked)
    
    @staticmethod
    def clearInstanceList():
        for instance in CheckBoxWidget.instances:
            try:
                instance.disconnect()
                instance.close()
                instance.deleteLater()
                del instance
            except RuntimeError:
                # If it is already deleted, RuntimeError occurs
                # Just pass
                pass
        
        # Clear instances
        CheckBoxWidget.instances.clear()

        # Clear matches
        CheckBoxWidget.objectRowDataMatch.clear()
    
    @staticmethod
    def alternateSelection(table:QTableWidget|None = None):
        for index in range(len(CheckBoxWidget.instances)):
            instance = CheckBoxWidget.instances[index]
            # If the row is already hidden, do not change the state
            # of the checkbox in that row
            if not CheckBoxWidget._checkIsRowHidden(table, index):
                if instance.checkState() == Qt.CheckState.Checked:
                    instance.setCheckState(Qt.CheckState.Unchecked)
                else:
                    instance.setCheckState(Qt.CheckState.Checked)
    
    @staticmethod
    def getInstances(checkStatus:Qt.CheckState):
        filteredInstances:list[QCheckBox] = []
        for instance in CheckBoxWidget.instances:
            if instance.checkState() == checkStatus:
                filteredInstances.append(instance)
        
        return filteredInstances
    
    def handleCheckStateChange(self):
        # Nothing special for here
        pass

class MonoButtonWidget(QWidget):
    """
    Class for widget includes only one QPushButton to add a column of a QTableWidget
    """
    instances:list[QPushButton] = []
    clicked_value = pyqtSignal(tuple)
    rowDataMatch = dict()
    keyType = None
    readIcon = None
    addIcon = None
    selectIcon = None
    deleteIcon = None

    def __init__(self, row_index, row_data, DynamicProperties:None|dict = None):
        super().__init__()
        self.rowDataMatch[row_data[0]] = row_data
        self.keyType = type(row_data[0])

        self.buttonType, toolTip = DynamicProperties["buttonType"], DynamicProperties["toolTip"]
        self.placedWidget = DynamicProperties.get("placedWidget", None)

        self.getButtons()

        if self.buttonType.casefold() == "read":
            icon = MonoButtonWidget.readIcon
        elif self.buttonType.casefold() == "add":
            icon = MonoButtonWidget.addIcon
        elif self.buttonType.casefold() == "select":
            icon = MonoButtonWidget.selectIcon
        elif self.buttonType.casefold() == "delete":
            icon = MonoButtonWidget.deleteIcon
        else:
            raise ValueError("Wrong buttonType!")
        
        self.toolTipText = self.buttonType.capitalize() if toolTip == None else toolTip

        layout = QHBoxLayout(self)

        # Create the button
        self.dynamicMonoButton = QPushButton("", self)
        self.dynamicMonoButton.setObjectName(f"dynamic{self.buttonType.capitalize()}_{row_data[0]}") # dynamicRead_1111
        self.dynamicMonoButton.setStyleSheet("""background-color: #85A9BC;""")
        self.dynamicMonoButton.setFixedSize(40,25)
        self.dynamicMonoButton.setIcon(icon)
        self.dynamicMonoButton.setIconSize(QSize(15,15))
        self.dynamicMonoButton.setToolTip(self.toolTipText)
        self.dynamicMonoButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Connect the button
        self.dynamicMonoButton.clicked.connect(self.monoButtonClicked)

        layout.addWidget(self.dynamicMonoButton)

        # Add the button to a list to access them later
        MonoButtonWidget.instances.append(self.dynamicMonoButton)
    
    def getButtons(self):
        # All icons have been set to None initially. Just check
        # one of them for initialization of all icons
        # Icons are created only once. Each time a new button is
        # created, do not repeat the creation of its icon for a
        # better memory optimization
        if not MonoButtonWidget.readIcon:
            MonoButtonWidget.readIcon = IconManager.getIcon("view")
            MonoButtonWidget.add = IconManager.getIcon("add")
            MonoButtonWidget.selectIcon = IconManager.getIcon("select_3")
            MonoButtonWidget.deleteIcon = IconManager.getIcon("cross_mark_3")
    
    @staticmethod
    def clickAll():
        for instance in MonoButtonWidget.instances:
            instance.click()
    
    @staticmethod
    def clearInstanceList():
        for instance in MonoButtonWidget.instances:
            try:
                instance.disconnect()
                instance.close()
                instance.deleteLater()
                del instance
            except RuntimeError:
                # If it is already deleted, RunTime error occurs
                # Just pass
                pass
        
        # Clear instances
        MonoButtonWidget.instances.clear()
        
        # Clear matches
        MonoButtonWidget.rowDataMatch.clear()
    
    def monoButtonClicked(self):
        objectName = self.sender().objectName()
        objectID = objectName[objectName.find("_") + 1:]
        self.clicked_value.emit((self.rowDataMatch[self.keyType(objectID)][0], self.buttonType))

class DoubleButtonWidget(QWidget):
    """
    Class for widget contains 2 QPushButtons considered as accept and reject buttons
    to add into a column of a QTableWidget
    """

    acceptButtonInstances:list[QPushButton] = []
    rejectButtonInstances:list[QPushButton] = []
    dynamicLabelInstances:list[QLabel] = []
    clicked_value = pyqtSignal(tuple)
    rowDataMatch = dict()
    acceptIcon = None
    rejectIcon = None

    def __init__(self, row_index, row_data, DynamicProperties:None|dict = None):
        super().__init__()
        self.rowDataMatch[row_data[0]] = row_data
        self.placedWidget = None if DynamicProperties.get("placedWidget", None) else DynamicProperties.get("placedWidget")

        layout = QHBoxLayout(self)

        # Get buttons
        self.getButtons()

        # Create accept button
        self.dynamicAcceptButton = QPushButton("", self)
        self.dynamicAcceptButton.setStyleSheet("""background-color: #85A9BC;""")
        self.dynamicAcceptButton.setFixedSize(40,25)
        self.dynamicAcceptButton.setIcon(DoubleButtonWidget.acceptIcon)
        self.dynamicAcceptButton.setIconSize(QSize(15,15))
        self.dynamicAcceptButton.setToolTip("Accept")
        self.dynamicAcceptButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dynamicAcceptButton.setObjectName(f"dynamic{self.dynamicAcceptButton.toolTip()}_{row_data[0]}")

        # Create reject button
        self.dynamicRejectButton = QPushButton("", self)
        self.dynamicRejectButton.setStyleSheet("""background-color: #FF6961;""")
        self.dynamicRejectButton.setFixedSize(40,25)
        self.dynamicRejectButton.setIcon(DoubleButtonWidget.rejectIcon)
        self.dynamicRejectButton.setIconSize(QSize(15,15))
        self.dynamicRejectButton.setToolTip("Reject")
        self.dynamicRejectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dynamicRejectButton.setObjectName(f"dynamic{self.dynamicRejectButton.toolTip()}_{row_data[0]}")

        # Create label for placeholder after clicking
        self.dynamicLabel = QLabel("", self)
        self.dynamicLabel.setStyleSheet("""background-color: transparent; color: #FFFFFF;""")
        self.dynamicLabel.setFixedSize(80,25)
        self.dynamicLabel.setObjectName(f"dynamicPlaceholderLabel_{row_data[0]}")
        self.dynamicLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dynamicLabel.setVisible(False)

        # Connect the buttons
        self.dynamicAcceptButton.clicked.connect(self.doubleButtonClicked)
        self.dynamicRejectButton.clicked.connect(self.doubleButtonClicked)

        layout.addWidget(self.dynamicAcceptButton)
        layout.addWidget(self.dynamicRejectButton)
        layout.addWidget(self.dynamicLabel)

        # Add the buttons into the corresponding lists to access them later
        DoubleButtonWidget.acceptButtonInstances.append(self.dynamicAcceptButton)
        DoubleButtonWidget.rejectButtonInstances.append(self.dynamicRejectButton)

        # Add the label into the corresponding list to access it later
        DoubleButtonWidget.dynamicLabelInstances.append(self.dynamicLabel)
    
    def getButtons(self):
        # Create the icons only once
        if not DoubleButtonWidget.acceptIcon and not DoubleButtonWidget.rejectIcon:
            DoubleButtonWidget.acceptIcon = IconManager.getIcon("accept")
            DoubleButtonWidget.rejectIcon = IconManager.getIcon("decline")
    
    def _checkIsRowHidden(table:QTableWidget|None, rowNumber:int) -> bool:
        # A table can be given or cannot be given. These functions
        # should effectively work both for these cases.

        if not table: return False
        return table.isRowHidden(rowNumber)

    @staticmethod
    def acceptAll(table:QTableWidget|None = None):
        # A note for acceptAll and rejectAll:
        # When the buttons are once clicked and disappeared,
        # they cannot be clicked any more. Accept and reject
        # operations cannot be repeated and cannot be changed.

        for index in range(len(DoubleButtonWidget.acceptButtonInstances)):
            if not DoubleButtonWidget._checkIsRowHidden(table, index):
                if DoubleButtonWidget.acceptButtonInstances[index].isVisible():
                    DoubleButtonWidget.acceptButtonInstances[index].click()
    
    @staticmethod
    def rejectAll(table:QTableWidget|None = None):
        for index in range(len(DoubleButtonWidget.rejectButtonInstances)):
            if not DoubleButtonWidget._checkIsRowHidden(table, index):
                if DoubleButtonWidget.rejectButtonInstances[index].isVisible():
                    DoubleButtonWidget.rejectButtonInstances[index].click()
    
    @staticmethod
    def getInstance(instanceObjectName:str) -> QPushButton:
        for item in DoubleButtonWidget.acceptButtonInstances + DoubleButtonWidget.rejectButtonInstances + DoubleButtonWidget.dynamicLabelInstances:
            if item.objectName() == instanceObjectName:
                return item
    
    @staticmethod
    def clearInstanceLists():
        for instance in DoubleButtonWidget.acceptButtonInstances + DoubleButtonWidget.rejectButtonInstances + DoubleButtonWidget.dynamicLabelInstances:
            try:
                instance.disconnect()
                instance.close()
                instance.deleteLater()
                del instance
            except RuntimeError:
                # If it is already deleted, RunTime error occurs
                # Just pass
                pass
        
        # Clear instances
        DoubleButtonWidget.acceptButtonInstances.clear()
        DoubleButtonWidget.rejectButtonInstances.clear()
        DoubleButtonWidget.dynamicLabelInstances.clear()
        
        # Clear matches
        DoubleButtonWidget.rowDataMatch.clear()
    
    @staticmethod
    def clearAcceptInstanceList():
        DoubleButtonWidget.acceptButtonInstances.clear()
    
    @staticmethod
    def clearRejectInstanceList():
        DoubleButtonWidget.rejectButtonInstances.clear()
    
    def doubleButtonClicked(self):
        objectName = self.sender().objectName()
        objectID = objectName[objectName.find("_") + 1:]
        color = "#44fda2" if self.sender().toolTip() == "Accept" else "#FF0000"
        text = self.sender().toolTip() + "ed" # To make it "Accepted" or "Rejected"
        # Below, we close the objects

        # Find the clicked button and make it invisible
        for item in DoubleButtonWidget.acceptButtonInstances:
            if item.objectName().endswith(objectID):
                item.setVisible(False)
        
        for item in DoubleButtonWidget.rejectButtonInstances:
            if item.objectName().endswith(objectID):
                item.setVisible(False)

        # Find the relevant label and make it visible
        for item in DoubleButtonWidget.dynamicLabelInstances:
            if item.objectName().endswith(objectID):
                item.setVisible(True)
                item.setText(text)
                item.setStyleSheet(f"""background-color: transparent; color: {color};""")
        
        # Update the sql record in handleCellWidgetBtnClick
        self.clicked_value.emit((self.rowDataMatch[int(objectID)][0], text))

class PeopleCardWidget():
    # Because of the fact that we cannot create QPixmap before constructing a QGuiApplication
    # we initially set the icon to None. We will set it at the first call after a QGuiApplication
    # constructed.
    profile_icon:QPixmap|None = None

    def createPeopleCardWidget(obj):
        obj.widget_people_card_instance = MessagePeopleCardWidget()
        # self.widget_people_card_instance.setObjectName(u"widget_people_card_instance")
        obj.widget_people_card_instance.setGeometry(QRect(80, 60, 226, 50))
        obj.widget_people_card_instance.setMinimumSize(QSize(220, 50))
        obj.widget_people_card_instance.setMaximumSize(QSize(16777215, 50))
        obj.widget_people_card_instance.setStyleSheet(u"QWidget {\n"
                                                        "	background-color: transparent;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QLabel {\n"
                                                        "	background-color: transparent;\n"
                                                        "	color: #f0f0f0;\n"
                                                        "}\n"
                                                        "\n"
                                                        "QWidget::hover {\n"
                                                        "	background-color: #808080;\n"
                                                        "	color: #f0f0f0;\n"
                                                        "}")
        obj.horizontalLayout = QHBoxLayout(obj.widget_people_card_instance)
        # self.horizontalLayout.setObjectName(u"horizontalLayout")
        obj.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        obj.widget_people_card_profile_image_container = QWidget(obj.widget_people_card_instance)
        # self.widget_people_card_profile_image_container.setObjectName(u"widget_people_card_profile_image_container")
        obj.widget_people_card_profile_image_container.setMinimumSize(QSize(32, 32))
        obj.widget_people_card_profile_image_container.setMaximumSize(QSize(32, 32))
        obj.gridLayout = QGridLayout(obj.widget_people_card_profile_image_container)
        # self.gridLayout.setObjectName(u"gridLayout")
        obj.gridLayout.setContentsMargins(0, 0, 0, 0)
        obj.lbl_people_card_profile_image = QLabel(obj.widget_people_card_profile_image_container)
        # self.lbl_people_card_profile_image.setObjectName(u"lbl_people_card_profile_image")
        obj.lbl_people_card_profile_image.setMinimumSize(QSize(30, 30))
        obj.lbl_people_card_profile_image.setMaximumSize(QSize(30, 30))
        obj.lbl_people_card_profile_image.setPixmap(PeopleCardWidget.profile_icon)
        obj.lbl_people_card_profile_image.setScaledContents(True)

        obj.gridLayout.addWidget(obj.lbl_people_card_profile_image, 0, 0, 1, 1)


        obj.horizontalLayout.addWidget(obj.widget_people_card_profile_image_container)

        obj.widget_people_card_text_container = QWidget(obj.widget_people_card_instance)
        # self.widget_people_card_text_container.setObjectName(u"widget_people_card_text_container")
        obj.widget_people_card_text_container.setMinimumSize(QSize(170, 40))
        obj.widget_people_card_text_container.setMaximumSize(QSize(16777215, 40))
        obj.verticalLayout = QVBoxLayout(obj.widget_people_card_text_container)
        # self.verticalLayout.setObjectName(u"verticalLayout")
        obj.verticalLayout.setContentsMargins(0, 0, 0, 0)
        obj.lbl_people_card_top_text = QLabel(obj.widget_people_card_text_container)
        # self.lbl_people_card_top_text.setObjectName(u"lbl_people_card_top_text")
        obj.lbl_people_card_top_text.setMinimumSize(QSize(150, 20))
        obj.lbl_people_card_top_text.setMaximumSize(QSize(16777215, 20))

        obj.verticalLayout.addWidget(obj.lbl_people_card_top_text)

        obj.lbl_people_card_bottom_text = QLabel(obj.widget_people_card_text_container)
        # self.lbl_people_card_bottom_text.setObjectName(u"lbl_people_card_bottom_text")
        obj.lbl_people_card_bottom_text.setMinimumSize(QSize(150, 20))
        obj.lbl_people_card_bottom_text.setMaximumSize(QSize(16777215, 20))

        obj.verticalLayout.addWidget(obj.lbl_people_card_bottom_text)


        obj.horizontalLayout.addWidget(obj.widget_people_card_text_container)

        return obj.widget_people_card_instance
    
    def getPeopleCard(obj, name):
        if PeopleCardWidget.profile_icon == None:
            PeopleCardWidget.profile_icon = IconManager.getIcon("login_header", "pixmap")
        obj.peopleCardMenu.clear()

        liste = db_man_projectv3_test.load_employee_for_message_selection(name)

        for i in range(len(liste)):
            custom_widget = PeopleCardWidget.createPeopleCardWidget(obj)

            obj.lbl_people_card_top_text.setText(liste[i][1] + " " + liste[i][2])
            obj.lbl_people_card_bottom_text.setText(liste[i][3] + " - " + liste[i][4])

            widget_action = QWidgetAction(obj.peopleCardMenu)

            widget_action.setDefaultWidget(custom_widget)

            # Create an object name which has a special pattern
            # We'll emit this object name as a signal to  use it
            # in the proper functions
            # Pattern: name surname*id*department/job

            record = liste[i]
            objectName = str(record[1]) + " " + str(record[2] )+ "*" + str(record[0]) + "*" + str(record[3]) + "/" + str(record[4])
            
            obj.peopleCardMenu.addAction(widget_action)
            widget_action.setObjectName(objectName)
            widget_action.triggered.connect(obj.handlePeopleCardClick)


def _setTableProperties(obj, rowCount:int, columnCount:int, table:QTableWidget, rowHeaders:list = None, columnHeaders:list = None):
    # Each time a table reconstructed, side menu restrictions should be removed
    obj.closeSideMenu()

    # Clear dynamically created objects
    obj.clearDynamicInstances()

    # Clear the search bar
    obj.textEdit_page_search_search.setPlaceHolderText()

    # Hide the buttons under the table because mostly they are
    # not needed. If need arises, they are opened in the
    # proper functions.
    obj.widget_table_1_btn_container.setVisible(False)
    
    # Reconstruct the table
    table.setRowCount(rowCount)
    table.setColumnCount(columnCount)
    if rowHeaders:
        table.setVerticalHeaderLabels(rowHeaders)
    if columnHeaders:
        table.setHorizontalHeaderLabels(columnHeaders)

def _setTableContent(obj, rowCount:int, columnCount:int, table:QTableWidget, items:list, cellWidgetAppend:bool = False,
                    ButtonWidgetType:None|str = None, DynamicProperties:None|dict = None):
            
    if ButtonWidgetType == "MonoButtonWidget": WidgetType = MonoButtonWidget
    elif ButtonWidgetType == "DoubleButtonWidget": WidgetType = DoubleButtonWidget
    elif ButtonWidgetType == "CheckBoxWidget": WidgetType = CheckBoxWidget
    else: WidgetType = None # It can be None, pass

    for row in range(len(items)):
        for column in range(len(items[0])):
            item = items[row][column]
            if item == None: item = "Null"
            else:
                try:
                    item = str(item)
                except Exception:
                    item = "ERR(CNV)"
            table.setItem(row, column, QTableWidgetItem(item))
        
        if cellWidgetAppend == True:
            btn = WidgetType(row, items[row], DynamicProperties)
            table.setCellWidget(row, columnCount - 1, btn)
            if WidgetType in [MonoButtonWidget, DoubleButtonWidget]:
                # If it is a push button, clicked_value signal must be connected
                # Otherwise, pass
                btn.clicked_value.connect(obj.handleCellWidgetBtnClick)
        
        table.setRowHeight(row, 40)
    
    # Each time after the table is reconstructed, check for
    # whether are there any checkboxes to open quick actions
    # buttons when needed

    # If side menu is not visible, quick actions cannot be accessible

    if (len(CheckBoxWidget.instances) or len(DoubleButtonWidget.dynamicLabelInstances)) and obj.stackedWidget_side_menu.isVisible():
        obj.btn_quick_actions.setVisible(True)

def setTable(obj, table:QTableWidget, items:list, rowHeaders:list = None, columnHeaders:list = None,
             cellWidgetAppend:bool = False, ButtonWidgetType:None|str = None, DynamicProperties:None|dict = None):
    
    # Each time a table is reconstructed, clear all the dynamic objects
    clearDynamicInstances()
    
    table.clear()
    row_count = len(items)
    column_count = len(items[0])
    if cellWidgetAppend == True: column_count += 1 # +1 for action column
    table.setSortingEnabled(False)
    _setTableProperties(obj, row_count, column_count, table, rowHeaders, columnHeaders)
    _setTableContent(obj, row_count, column_count, table, items, cellWidgetAppend, ButtonWidgetType, DynamicProperties)

def _addControlButtons(obj, dynamic_widget:QWidget, buttons:list|None = None, buttonColumnCount:int|None = None, rowSpan:int = 1, colSpan:int = 1):
    """ XXX Do not call individually! XXX """

    # Below, we add buttons if wanted
    added_buttons:int = 0

    # Firstly create a spacer to provide a reasonable space before adding the buttons
    obj.dynamic_verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

    obj.dynamic_gridLayout.addItem(obj.dynamic_verticalSpacer, 2, 0, 1, 1)

    if buttons and len(buttons) != 0:
        row = 0

        obj.dynamic_button_gridLayout = QGridLayout()
        # self.dynamic_gridLayout.setObjectName(u"gridLayout")
        obj.dynamic_button_gridLayout.setContentsMargins(0, 0, 0, 0)

        for _ in range(len(buttons)):
            status = 1
            for columnIndex in range(buttonColumnCount):
                obj.dynamic_pushButton = QPushButton()
                obj.dynamic_pushButton.setObjectName(f"btnDynamic_{buttons[added_buttons]}")
                obj.dynamic_pushButton.setText(buttons[added_buttons])
                obj.dynamic_pushButton.clicked.connect(obj.handleDynamicButtonClick)
                obj.dynamic_button_gridLayout.addWidget(obj.dynamic_pushButton, row, columnIndex, rowSpan, colSpan)
                added_buttons += 1

                if added_buttons == len(buttons): status = 0; break
            
            if status == 0: break

            row += 1
        
        obj.created_right_menu_dynamic_widgets.append(obj.dynamic_gridLayout)
        
        obj.dynamic_gridLayout.addLayout(obj.dynamic_button_gridLayout, 3, 0, 1, 1)

def _createSideBarControlWidget(obj):
    obj.dynamic_widget = QWidget()
    obj.dynamic_widget.setStyleSheet("""
                                    QLabel {
                                        font-size: 12px;
                                    }
                                    """)
    obj.dynamic_widget.setObjectName(u"widget")
    obj.dynamic_widget.setGeometry(QRect(90, 90, 153, 59))
    obj.dynamic_gridLayout = QGridLayout(obj.dynamic_widget)
    # self.dynamic_gridLayout.setObjectName(u"gridLayout")
    obj.dynamic_verticalLayout = QVBoxLayout()
    # self.dynamic_verticalLayout.setObjectName(u"verticalLayout")
    obj.dynamic_label = QLabel(obj.dynamic_widget)
    # self.dynamic_label.setObjectName(u"label")

    obj.dynamic_verticalLayout.addWidget(obj.dynamic_label)

    obj.dynamic_lineEdit = QLineEdit(obj.dynamic_widget)
    # self.dynamic_lineEdit.setObjectName(u"lineEdit")

    obj.dynamic_verticalLayout.addWidget(obj.dynamic_lineEdit)


    obj.dynamic_gridLayout.addLayout(obj.dynamic_verticalLayout, 0, 0, 1, 1)

    return obj.dynamic_widget

def _createControls(obj, pairs:dict, buttons:list|None = None, buttonColumnCount:int = 2, rowSpan:int = 1, colSpan:int = 1):
    """ XXX Do not call individually! XXX """
    
    for header, content in pairs.items():
        custom_widget = _createSideBarControlWidget(obj)

        obj.dynamic_label.setText(header)
        obj.dynamic_label.setObjectName(f"dynamicLbl_{header}")
        obj.dynamic_lineEdit.setText(content)
        obj.dynamic_lineEdit.setObjectName(f"dynamicLineEdit_{header}")

        for item in obj.nameDisabledLineEdits:
            if db_man_projectv3_test.arrangeText(item) in db_man_projectv3_test.arrangeText(header):
                obj.dynamic_lineEdit.setDisabled(True)

        # New objects must always be placed between two vertical spacers.
        # The bottom spacer must always remain at the bottom.
        obj.sideBarVerticalLayout.insertWidget(obj.sideBarVerticalLayout.count() - 1, custom_widget)

        obj.created_right_menu_dynamic_widgets.append(custom_widget)
    
    # custom_widget is already added where it was created
    
    _addControlButtons(obj, custom_widget, buttons, buttonColumnCount, rowSpan, colSpan)

def createSideMenuWidgets(obj, row_contents_dict, desiredDynamicButtons, desiredDynamicButtonContainerColumnSpan = 2, rowSpan = 1, colSpan = 1):
    _createControls(obj, row_contents_dict, desiredDynamicButtons, desiredDynamicButtonContainerColumnSpan, rowSpan, colSpan)

def makeAllRowsVisible(table:QTableWidget) -> None:
    for row in range(table.rowCount()):
        table.setRowHidden(row, False)

def clearDynamicInstances():
    # Clear all the objects that have been dynamically
    # created during runtime

    # They are cleared when they are no longer useless
    # or they are no longer needed

    CheckBoxWidget.clearInstanceList()
    MonoButtonWidget.clearInstanceList()
    DoubleButtonWidget.clearInstanceLists()


# END