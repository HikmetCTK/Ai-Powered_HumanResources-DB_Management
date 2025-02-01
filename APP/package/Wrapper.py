from package import StandardMessageBox

def handler(func:callable):
    def innerWrapper(obj, *args, **kwargs):
        objClass = obj.__class__
        
        # The following values ​​are required for the reload function
        objClass.func = func
        objClass.args = args
        objClass.kwargs = kwargs

        try:
            func(obj, *args, **kwargs)
        except TypeError:
            try:
                func(obj)
            except Exception as e:
                StandardMessageBox.Error(obj, "Error (handler - inner)",
                                            f"An error occurred during the latest process! | {str(e)}").exec()
        except Exception as e:
            StandardMessageBox.Error(obj, "Error (handler - outer)",
                                        f"An error occurred during the latest process! | {str(e)}").exec()
        
    return innerWrapper

def errorCatcher(func:callable):
    def innerWrapper(obj, *args, **kwargs):
        try:
            return func(obj, *args, **kwargs)
        except TypeError:
            try:
                return func(obj)
            except Exception as e:
                StandardMessageBox.Error(obj, "Error (errorCatcher - inner)",
                                            f"An error occurred during the latest process! | {str(e)}").exec()
        except Exception as e:
            StandardMessageBox.Error(obj, "Error (errorCatcher - outer)",
                                        f"An error occurred during the latest process! | {str(e)}").exec()
    return innerWrapper


# END