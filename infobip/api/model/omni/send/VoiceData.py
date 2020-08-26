# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.util.TimeUnit import TimeUnit


class VoiceData(DefaultObject):
    @property
    @serializable(name="language", type='basestring')
    def language(self):
        """
        Property is of type: 'basestring'
        """
        return self.get_field_value("language")

    @language.setter
    def language(self, language):
        """
        Property is of type: 'basestring'
        """
        self.set_field_value("language", language)

    def set_language(self, language):
        self.language = language
        return self

    @property
    @serializable(name="text", type='basestring')
    def text(self):
        """
        Property is of type: 'basestring'
        """
        return self.get_field_value("text")

    @text.setter
    def text(self, text):
        """
        Property is of type: 'basestring'
        """
        self.set_field_value("text", text)

    def set_text(self, text):
        self.text = text
        return self

    @property
    @serializable(name="validityPeriod", type=float)
    def validity_period(self):
        """
        Property is of type: float
        """
        return self.get_field_value("validity_period")

    @validity_period.setter
    def validity_period(self, validity_period):
        """
        Property is of type: float
        """
        self.set_field_value("validity_period", validity_period)

    def set_validity_period(self, validity_period):
        self.validity_period = validity_period
        return self

    @property
    @serializable(name="validityPeriodTimeUnit", type=TimeUnit)
    def validity_period_time_unit(self):
        """
        Property is of type: TimeUnit
        """
        return self.get_field_value("validity_period_time_unit")

    @validity_period_time_unit.setter
    def validity_period_time_unit(self, validity_period_time_unit):
        """
        Property is of type: TimeUnit
        """
        self.set_field_value("validity_period_time_unit", validity_period_time_unit)

    def set_validity_period_time_unit(self, validity_period_time_unit):
        self.validity_period_time_unit = validity_period_time_unit
        return self