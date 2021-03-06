# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ServiceHealthServiceIncidentHistory(Model):
    """Represents the message history for an office incident.

    :param published_time: Gets or sets the published time
    :type published_time: datetime
    :param message_text: Gets or sets the Message text
    :type message_text: str
    """

    _attribute_map = {
        'published_time': {'key': 'publishedTime', 'type': 'iso-8601'},
        'message_text': {'key': 'messageText', 'type': 'str'},
    }

    def __init__(self, published_time=None, message_text=None):
        super(MicrosoftPartnerSdkContractsV1ServiceHealthServiceIncidentHistory, self).__init__()
        self.published_time = published_time
        self.message_text = message_text
