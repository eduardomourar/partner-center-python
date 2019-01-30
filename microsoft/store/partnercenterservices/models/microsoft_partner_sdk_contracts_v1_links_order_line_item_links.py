# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1LinksOrderLineItemLinks(Model):
    """Represents navigation links for an order line item, including
    a link to the full subscription associated with the order.

    :param subscription: Gets or sets the link to the full subscription
     information.
    :type subscription:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param sku: Gets or sets the SKU URI.
    :type sku:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param provisioning_status: Gets or sets the Provisioning Status URI.
    :type provisioning_status:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    """

    _attribute_map = {
        'subscription': {'key': 'subscription', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'sku': {'key': 'sku', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'provisioning_status': {'key': 'provisioningStatus', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
    }

    def __init__(self, subscription=None, sku=None, provisioning_status=None):
        super(MicrosoftPartnerSdkContractsV1LinksOrderLineItemLinks, self).__init__()
        self.subscription = subscription
        self.sku = sku
        self.provisioning_status = provisioning_status