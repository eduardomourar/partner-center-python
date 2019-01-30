# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1DeviceDeploymentDevicePolicyUpdateRequest(Model):
    """Provides the information required to update a list of devices with a
    policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param devices: Sets the list of devices to be updated. Each object
     specifies a device.
     The following properties are required:  Id, Policies.
    :type devices:
     list[~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1DeviceDeploymentDevice]
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'devices': {'key': 'devices', 'type': '[MicrosoftPartnerSdkContractsV1DeviceDeploymentDevice]'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, devices=None):
        super(MicrosoftPartnerSdkContractsV1DeviceDeploymentDevicePolicyUpdateRequest, self).__init__()
        self.devices = devices
        self.attributes = None
