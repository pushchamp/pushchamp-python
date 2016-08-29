"""
    Constants to be used throughout this project.
"""

class SupportedChannel(object):
    """channels supported by PushChamp"""
    SMS = "sms"

    @staticmethod
    def GetChannels():
        return [
            SupportedChannel.SMS
        ]

class PushchampConstants(object):
    """some constants defined by pushchamp"""
    URL = "http://api.pushchamp.com"
        