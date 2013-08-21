# -*- coding: utf-8 -*-


class MessageLevels:
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    

class MessageTypes:
    INIT = 1
    APPLICABILITY = 2


class Message(object):
    def __init__(self, text, level, subject):
        self._text = text
        self._level = level
        if subject.__class__.__name__ == 'DwcALine':
            self._subject_type = 'line'
            self._line_id = subject.id
        elif subject == MessageTypes.INIT:
            self._subject_type = MessageTypes.INIT
    
    def concerns_line_with_id(self, line_id):
        """Returns true if the message is about the line whose id is passed in parameter."""
        return self._subject_type == 'line' and self._line_id == line_id
        
    def is_init(self):
        """ Returns true if the current message is of init. type. """
        return self._subject_type == MessageTypes.INIT

        
class AssessmentLog(object):
    def __init__(self):
        self._messages = []
    
    def get_messages_concerning_line(self, line_id):
        return [message for message in self._messages if message.concerns_line_with_id(line_id)]

    def get_all_init_messages(self):
        return [message for message in self._messages if message.is_init()]

    def log(self, msg, level, subject):
        m = Message(msg, level, subject)
        self._messages.append(m)
    