"""
    Constants to be used throughout this project.
"""

class SupportedChannels(object):
    """channels supported by PushChamp"""
    SMS = "sms"

    @staticmethod
    def get_channels():
        """return list of all channels supported by this SDK"""
        return [SupportedChannels.SMS]

class PushchampConstants(object):
    """some constants defined by pushchamp"""
    URL = "http://api.pushchamp.com"
        