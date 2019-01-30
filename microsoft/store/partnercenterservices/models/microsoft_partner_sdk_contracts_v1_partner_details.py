# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1PartnerDetails(Model):
    """Partner Details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param aad_partner_type: Partner type flag in AAD. Possible values
     include: 'none', 'reseller', 'advisor', 'company', 'syndication',
     'microsoft_support', 'value_added_reseller'
    :type aad_partner_type: str or ~azure.partnercenterservices.models.enum
    :param has_dap_privileges: Boolean to indicate if the partner has DAP
     privileges
    :type has_dap_privileges: bool
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'aad_partner_type': {'key': 'aadPartnerType', 'type': 'str'},
        'has_dap_privileges': {'key': 'hasDapPrivileges', 'type': 'bool'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, aad_partner_type=None, has_dap_privileges=None):
        super(MicrosoftPartnerSdkContractsV1PartnerDetails, self).__init__()
        self.aad_partner_type = aad_partner_type
        self.has_dap_privileges = has_dap_privileges
        self.attributes = None