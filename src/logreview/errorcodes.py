from datetime import datetime

class ErrorCodes:
    """error information for review in the logs"""
    def __init__(self, df):
        self.date_loaded=datetime.now().strftime('%x %X')
        self.data=df



        



