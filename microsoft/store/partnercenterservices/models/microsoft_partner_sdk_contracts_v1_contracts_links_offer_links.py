# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ContractsLinksOfferLinks(Model):
    """Contains links for learning more information about the offer.

    :param learn_more: Gets or sets the "learn more" link.
    :type learn_more:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param self: The self uri.
    :type self:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param next: The next page of items.
    :type next:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param previous: The previous page of items.
    :type previous:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    """

    _attribute_map = {
        'learn_more': {'key': 'learnMore', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'self': {'key': 'self', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'next': {'key': 'next', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'previous': {'key': 'previous', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
    }

    def __init__(self, learn_more=None, self=None, next=None, previous=None):
        super(MicrosoftPartnerSdkContractsV1ContractsLinksOfferLinks, self).__init__()
        self.learn_more = learn_more
        self.self = self
        self.next = next
        self.previous = previous