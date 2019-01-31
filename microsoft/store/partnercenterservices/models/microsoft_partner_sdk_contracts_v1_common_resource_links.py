# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1CommonResourceLinks(Model):
    """Navigation links for the resource.

    :param self: The self uri.
    :type self:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param next: The next page of items.
    :type next:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param previous: The previous page of items.
    :type previous:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    """

    _attribute_map = {
        'itself': {'key': 'self', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'next': {'key': 'next', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'previous': {'key': 'previous', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
    }

    def __init__(self, itself=None, next=None, previous=None):
        super(MicrosoftPartnerSdkContractsV1CommonResourceLinks, self).__init__()
        self.itself = itself
        self.next = next
        self.previous = previous
