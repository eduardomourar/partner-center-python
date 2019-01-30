# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ContractsConnectUsAdvisoryHoursServiceRequest(Model):
    """Class that represents an advisory hour service request.

    :param id: Gets or sets the id.
    :type id: long
    :param partner_id: Gets or sets the PartnerId(MPNID).
    :type partner_id: str
    :param title: Gets or sets the Title.
    :type title: str
    :param description: Gets or sets the Description.
    :type description: str
    :param created_date: Gets or sets the created date.
    :type created_date: datetime
    :param preferred_language_code: Gets or sets language code.
    :type preferred_language_code: str
    :param routing_country_code: Gets or sets the country code.
    :type routing_country_code: str
    :param contact_name: Gets or sets the Contact Name.
    :type contact_name: str
    :param phone_number: Gets or sets the PhoneNumber.
    :type phone_number: str
    :param email: Gets or sets the email.
    :type email: str
    :param billing_hours: Gets or sets the billing hours.
    :type billing_hours: float
    :param closed_date: Gets or sets the closed date.
    :type closed_date: datetime
    :param is_open: Gets or sets is Status Open.
    :type is_open: bool
    :param is_contract_available: Gets or sets the isContractAvailable.
    :type is_contract_available: bool
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'long'},
        'partner_id': {'key': 'partnerId', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'preferred_language_code': {'key': 'preferredLanguageCode', 'type': 'str'},
        'routing_country_code': {'key': 'routingCountryCode', 'type': 'str'},
        'contact_name': {'key': 'contactName', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'billing_hours': {'key': 'billingHours', 'type': 'float'},
        'closed_date': {'key': 'closedDate', 'type': 'iso-8601'},
        'is_open': {'key': 'isOpen', 'type': 'bool'},
        'is_contract_available': {'key': 'isContractAvailable', 'type': 'bool'},
    }

    def __init__(self, id=None, partner_id=None, title=None, description=None, created_date=None, preferred_language_code=None, routing_country_code=None, contact_name=None, phone_number=None, email=None, billing_hours=None, closed_date=None, is_open=None, is_contract_available=None):
        super(MicrosoftPartnerSdkContractsV1ContractsConnectUsAdvisoryHoursServiceRequest, self).__init__()
        self.id = id
        self.partner_id = partner_id
        self.title = title
        self.description = description
        self.created_date = created_date
        self.preferred_language_code = preferred_language_code
        self.routing_country_code = routing_country_code
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.email = email
        self.billing_hours = billing_hours
        self.closed_date = closed_date
        self.is_open = is_open
        self.is_contract_available = is_contract_available