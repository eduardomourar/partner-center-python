# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1CustomerBillingProfile(Model):
    """Additional information used for billing the customer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: The profile identifier.
    :type id: str
    :param first_name: Gets or sets the first name of the billing contact at
     the customer's company.
     This is the person that invoices and other billing communication will be
     directed to.
    :type first_name: str
    :param last_name: Gets or sets the last name of the billing contact.
    :type last_name: str
    :param email: The email address of the billing contact.
    :type email: str
    :param culture: Gets or sets the customer's preferred culture for
     communication and currency, such as "en-us".
    :type culture: str
    :param language: Gets or sets the customer's preferred language for
     communication.
    :type language: str
    :param company_name: The name of the company or organization.
    :type company_name: str
    :param default_address: The default address for the customer.
     The address that bills are sent to, where the billing contact works.
    :type default_address:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1Address
    :param links: Gets or sets the links.
    :type links:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceLinks
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'first_name': {'key': 'firstName', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'culture': {'key': 'culture', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'company_name': {'key': 'companyName', 'type': 'str'},
        'default_address': {'key': 'defaultAddress', 'type': 'MicrosoftPartnerSdkContractsV1Address'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceLinks'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, id=None, first_name=None, last_name=None, email=None, culture=None, language=None, company_name=None, default_address=None, links=None):
        super(MicrosoftPartnerSdkContractsV1CustomerBillingProfile, self).__init__()
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.culture = culture
        self.language = language
        self.company_name = company_name
        self.default_address = default_address
        self.links = links
        self.attributes = None
