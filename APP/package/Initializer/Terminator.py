from PyQt6.QtWidgets import QPushButton, QStackedWidget

"""
Disconnect unnecessary signals for a better memory
optimization. Connect signals and set icons when
necessary using initializer modules.
"""

def terminatePageWithIndex(stackedWidget:QStackedWidget, pageIndexNumber:int):
    page = stackedWidget.widget(pageIndexNumber)

    if not page:
        return
    
    buttons = page.findChildren(QPushButton)

    for button in buttons:
        try:
            # Disconnect the button
            button.clicked.disconnect()
            # Remove the icon if exists
        except:
            # It is not crucial. Pass
            pass

    pass


# END