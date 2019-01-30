# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1SubscriptionRegistrationStatus(Model):
    """Provides information about the provisioning status of a subscription.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param subscription_id: Gets or sets a GUID formatted string that
     identifies the subscription.
    :type subscription_id: str
    :param status:
    :type status: str
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, subscription_id=None, status=None):
        super(MicrosoftPartnerSdkContractsV1SubscriptionRegistrationStatus, self).__init__()
        self.subscription_id = subscription_id
        self.status = status
        self.attributes = None