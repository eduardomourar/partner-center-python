# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ContractsOrdersCartCheckoutResult(Model):
    """Represents the result of placing an order using a cart.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param orders: Gets or sets the orders created.
    :type orders:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1Order]
    :param order_errors: Gets or sets a collection of order failure
     information.
    :type order_errors:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ContractsOrdersOrderError]
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'orders': {'key': 'orders', 'type': '[MicrosoftPartnerSdkContractsV1Order]'},
        'order_errors': {'key': 'orderErrors', 'type': '[MicrosoftPartnerSdkContractsV1ContractsOrdersOrderError]'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, orders=None, order_errors=None):
        super(MicrosoftPartnerSdkContractsV1ContractsOrdersCartCheckoutResult, self).__init__()
        self.orders = orders
        self.order_errors = order_errors
        self.attributes = None
