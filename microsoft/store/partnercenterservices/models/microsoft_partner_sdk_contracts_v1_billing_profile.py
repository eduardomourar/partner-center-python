# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1BillingProfile(Model):
    """Describes a partner's billing profile.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param company_name: Gets or sets the billing company name.
    :type company_name: str
    :param address: Gets or sets the billing address of the company or
     organization.
    :type address:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1Address
    :param primary_contact: Gets or sets the primary contact for the company
     or organization.
    :type primary_contact:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1Contact
    :param purchase_order_number: Gets or sets the company or organization's
     purchase order number.
    :type purchase_order_number: str
    :param tax_id: Gets or sets the company or organization's tax Id.
    :type tax_id: str
    :param billing_day: Gets or sets the billing day.
    :type billing_day: int
    :param billing_currency: Gets or sets the currency used by the company or
     organization.
    :type billing_currency: str
    :ivar profile_type: OldProperty: Gets the partner profile type. Possible
     values include: 'mpn_profile', 'billing_profile', 'support_profile',
     'legal_business_profile', 'organization_profile'
    :vartype profile_type: str or
     ~microsoft.store.partnercenterservices.models.enum
    :param links: Gets or sets the links.
    :type links:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceLinks
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'profile_type': {'readonly': True},
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'company_name': {'key': 'companyName', 'type': 'str'},
        'address': {'key': 'address', 'type': 'MicrosoftPartnerSdkContractsV1Address'},
        'primary_contact': {'key': 'primaryContact', 'type': 'MicrosoftPartnerSdkContractsV1Contact'},
        'purchase_order_number': {'key': 'purchaseOrderNumber', 'type': 'str'},
        'tax_id': {'key': 'taxId', 'type': 'str'},
        'billing_day': {'key': 'billingDay', 'type': 'int'},
        'billing_currency': {'key': 'billingCurrency', 'type': 'str'},
        'profile_type': {'key': 'profileType', 'type': 'str'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceLinks'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, company_name=None, address=None, primary_contact=None, purchase_order_number=None, tax_id=None, billing_day=None, billing_currency=None, links=None):
        super(MicrosoftPartnerSdkContractsV1BillingProfile, self).__init__()
        self.company_name = company_name
        self.address = address
        self.primary_contact = primary_contact
        self.purchase_order_number = purchase_order_number
        self.tax_id = tax_id
        self.billing_day = billing_day
        self.billing_currency = billing_currency
        self.profile_type = None
        self.links = links
        self.attributes = None
