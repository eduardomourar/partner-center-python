# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1CollectionsPagedResourceCollectionMicrosoftPartnerSdkContractsV1DeviceDeploymentDevice(Model):
    """Paged Resource Collection.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param continuation_token: Gets or sets the continuation token.
    :type continuation_token: str
    :ivar total_count: Gets the total count.
    :vartype total_count: int
    :ivar items: Gets the collection items.
    :vartype items:
     list[~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1DeviceDeploymentDevice]
    :param links: Gets or sets the links.
    :type links:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceLinks
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'total_count': {'readonly': True},
        'items': {'readonly': True},
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'total_count': {'key': 'totalCount', 'type': 'int'},
        'items': {'key': 'items', 'type': '[MicrosoftPartnerSdkContractsV1DeviceDeploymentDevice]'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceLinks'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, continuation_token=None, links=None):
        super(MicrosoftPartnerSdkContractsV1CollectionsPagedResourceCollectionMicrosoftPartnerSdkContractsV1DeviceDeploymentDevice, self).__init__()
        self.continuation_token = continuation_token
        self.total_count = None
        self.items = None
        self.links = links
        self.attributes = None
