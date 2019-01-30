# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ContractsConnectUsConsultationType(Model):
    """Represent the Connect Us Consultation Type object.

    :param name: Gets or sets the name of the consultation type.
    :type name: str
    :param code: Gets or sets the code.
    :type code: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'code': {'key': 'code', 'type': 'int'},
    }

    def __init__(self, name=None, code=None):
        super(MicrosoftPartnerSdkContractsV1ContractsConnectUsConsultationType, self).__init__()
        self.name = name
        self.code = code
