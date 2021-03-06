# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.mt.send.Message import Message


class SMSMultiBinaryRequest(DefaultObject):
    @property
    @serializable(name="messages", type=Message)
    def messages(self):
        """
        Property is a list of: Message
        """
        return self.get_field_value("messages")

    @messages.setter
    def messages(self, messages):
        """
        Property is a list of: Message
        """
        self.set_field_value("messages", messages)

    def set_messages(self, messages):
        self.messages = messages
        return self

    @property
    @serializable(name="bulkId", type='basestring')
    def bulk_id(self):
        """
        Property is of type: 'basestring'
        """
        return self.get_field_value("bulk_id")

    @bulk_id.setter
    def bulk_id(self, bulk_id):
        """
        Property is of type: 'basestring'
        """
        self.set_field_value("bulk_id", bulk_id)

    def set_bulk_id(self, bulk_id):
        self.bulk_id = bulk_id
        return self