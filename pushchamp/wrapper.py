"""
    wrapper class for PushChamp API
"""


import json

from pushchamp.constants import PushchampConstants, SupportedChannels
from pushchamp.exceptions import EmptyChannel, InvalidType
from urllib2 import Request, urlopen


class Pushchamp(object):
    """create an object to use APIs"""
    def __init__(self, token, **kwargs):
        super(Pushchamp, self).__init__()
        self.token = token
        self.template_vars = kwargs.get("template_vars", {})
        self.address_params = kwargs.get("addr_params", {})
        self.template_name = kwargs.get("template_name", "")
        self.request_name = kwargs.get("request_name", "")

    def set_template_vars(self, template_vars):
        """pass a dict to set template variables"""
        if not isinstance(template_vars, dict):
            raise InvalidType("template_vars", dict, type(template_vars))

        self.template_vars = template_vars

    def set_template_name(self, name):
        """pass the template name for this request"""
        if not isinstance(name, str):
            raise InvalidType("name", str, type(name))

        self.template_name = name

    def set_request_name(self, request_name):
        """pass a name(string) for this request"""
        if not isinstance(request_name, str):
            raise InvalidType("request_name", str, type(request_name))

        self.request_name = request_name

    def set_mobile_number(self, mobile_numbers):
        """pass a list of mobile numbers to send SMS on"""
        if not isinstance(mobile_numbers, list):
            raise InvalidType("mobile_numbers", list, type(mobile_numbers))

        if not self.address_params.get(SupportedChannels.SMS, {}):
            self.address_params[SupportedChannels.SMS] = {}
        self.address_params[SupportedChannels.SMS]["mobiles"] = mobile_numbers

    def send(self):
        """send a message to end user(defined by address_params)"""
        if not self.address_params:
            raise EmptyChannel("You haven't provided any channel to send this message on.")

        channel_selected = False
        for _, channel in SupportedChannels.get_channels():
            if self.address_params.get(channel, {}):
                channel_selected = True

        if not channel_selected:
            raise EmptyChannel("You haven't provided any address to send this message on.")

        if not self.template_name:
            raise Exception("Please provide template name!")

        if not self.request_name:
            raise Exception("Please provide a request name!")

        headers = {
            "Content-Type": "application/json",
            "token": self.token
        }
        data = {
            "template_vars": self.template_vars,
            "address": self.address_params,
            "template_name": self.template_name,
            "name": self.request_name
        }

        data_to_be_send = json.dumps(data)
        request = Request("%s/send/" % PushchampConstants.URL, data_to_be_send, headers)
        response = urlopen(request)
        result = response.read()
        return result
