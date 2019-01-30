# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1CollectionsResourceCollectionMicrosoftPartnerSdkContractsV1Subscription(Model):
    """Contains a collection of resources with JSON properties to represent the
    output.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar total_count: Gets the total count.
    :vartype total_count: int
    :ivar items: Gets the collection items.
    :vartype items:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1Subscription]
    :param links: Gets or sets the links.
    :type links:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceLinks
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'total_count': {'readonly': True},
        'items': {'readonly': True},
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'total_count': {'key': 'totalCount', 'type': 'int'},
        'items': {'key': 'items', 'type': '[MicrosoftPartnerSdkContractsV1Subscription]'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceLinks'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, links=None):
        super(MicrosoftPartnerSdkContractsV1CollectionsResourceCollectionMicrosoftPartnerSdkContractsV1Subscription, self).__init__()
        self.total_count = None
        self.items = None
        self.links = links
        self.attributes = None
