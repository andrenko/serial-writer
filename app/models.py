from datetime import datetime


class Data:
    def __init__(self, in_waiting, string):
        self.in_waiting = in_waiting
        self.string = string
        self.request_time = str(datetime.now().time())

    def to_dict(self):
        data = {
            'in_waiting': self.in_waiting,
            'string': self.string,
            'request_time': self.request_time,
            }
        return data
