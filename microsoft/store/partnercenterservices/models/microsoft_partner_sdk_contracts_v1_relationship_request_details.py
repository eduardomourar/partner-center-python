# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1RelationshipRequestDetails(Model):
    """Represents a relationship request contents with a partner.

    :param partner_id: Gets or sets the partner identifier.
    :type partner_id: str
    :param contact_lines: Gets or sets the contact lines.
    :type contact_lines: list[str]
    :param address_lines: Gets or sets the address lines.
    :type address_lines: list[str]
    """

    _attribute_map = {
        'partner_id': {'key': 'partnerId', 'type': 'str'},
        'contact_lines': {'key': 'contactLines', 'type': '[str]'},
        'address_lines': {'key': 'addressLines', 'type': '[str]'},
    }

    def __init__(self, partner_id=None, contact_lines=None, address_lines=None):
        super(MicrosoftPartnerSdkContractsV1RelationshipRequestDetails, self).__init__()
        self.partner_id = partner_id
        self.contact_lines = contact_lines
        self.address_lines = address_lines
