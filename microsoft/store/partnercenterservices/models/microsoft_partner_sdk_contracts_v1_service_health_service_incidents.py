# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ServiceHealthServiceIncidents(Model):
    """Represents an office service health incident message.

    :param workload: Workload display name
    :type workload: str
    :param incidents: Gets or sets the Incident list
    :type incidents:
     list[~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ServiceHealthServiceIncidentDetail]
    :param status: Gets or sets the cumulative status of the service. Possible
     values include: 'normal', 'information', 'warning', 'critical'
    :type status: str or ~azure.partnercenterservices.models.enum
    :param message_center_messages: Gets or sets the message center messages
    :type message_center_messages:
     list[~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ServiceHealthServiceIncidentDetail]
    """

    _attribute_map = {
        'workload': {'key': 'workload', 'type': 'str'},
        'incidents': {'key': 'incidents', 'type': '[MicrosoftPartnerSdkContractsV1ServiceHealthServiceIncidentDetail]'},
        'status': {'key': 'status', 'type': 'str'},
        'message_center_messages': {'key': 'messageCenterMessages', 'type': '[MicrosoftPartnerSdkContractsV1ServiceHealthServiceIncidentDetail]'},
    }

    def __init__(self, workload=None, incidents=None, status=None, message_center_messages=None):
        super(MicrosoftPartnerSdkContractsV1ServiceHealthServiceIncidents, self).__init__()
        self.workload = workload
        self.incidents = incidents
        self.status = status
        self.message_center_messages = message_center_messages