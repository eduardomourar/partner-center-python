# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ContractsOrdersOrderError(Model):
    """Represents an error that occured during order placement.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param order_group_id: Gets or sets the order group Id with failure.
    :type order_group_id: str
    :param code: Gets or sets the error code associated with the issue.
    :type code: int
    :param description: Gets or sets the description of the issue.
    :type description: str
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'order_group_id': {'key': 'orderGroupId', 'type': 'str'},
        'code': {'key': 'code', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, order_group_id=None, code=None, description=None):
        super(MicrosoftPartnerSdkContractsV1ContractsOrdersOrderError, self).__init__()
        self.order_group_id = order_group_id
        self.code = code
        self.description = description
        self.attributes = None