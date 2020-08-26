# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable

class NumberContextRequest(DefaultObject):
    @property
    @serializable(name="to", type='basestring')
    def to(self):
        """
        Property is a list of: 'basestring'
        """
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        """
        Property is a list of: 'basestring'
        """
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self