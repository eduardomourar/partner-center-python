# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ContractsLinksManagedServiceLinks(Model):
    """Contains the links that allow the partner with delegated admin permissions
    to provide support for the service.

    :param admin_service: Gets or sets the admin service URI.
    :type admin_service:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param service_health: Gets or sets the service health URI.
    :type service_health:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonLink
    :param service_ticket: Gets or sets the service ticket URI.
    :type service_ticket:
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
        'admin_service': {'key': 'adminService', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'service_health': {'key': 'serviceHealth', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'service_ticket': {'key': 'serviceTicket', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'self': {'key': 'self', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'next': {'key': 'next', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
        'previous': {'key': 'previous', 'type': 'MicrosoftPartnerSdkContractsV1CommonLink'},
    }

    def __init__(self, admin_service=None, service_health=None, service_ticket=None, self=None, next=None, previous=None):
        super(MicrosoftPartnerSdkContractsV1ContractsLinksManagedServiceLinks, self).__init__()
        self.admin_service = admin_service
        self.service_health = service_health
        self.service_ticket = service_ticket
        self.self = self
        self.next = next
        self.previous = previous
