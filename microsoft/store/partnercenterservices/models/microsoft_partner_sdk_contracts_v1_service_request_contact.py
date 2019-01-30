# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ServiceRequestContact(Model):
    """Describes a contact that creates or modifies a service request.

    :param organization: Gets or sets the organization for which the service
     request is created.
    :type organization:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ServiceRequestOrganization
    :param contact_id: Gets or sets the contact's unique identifier.
    :type contact_id: str
    :param last_name: Gets or sets the last name of the contact.
    :type last_name: str
    :param first_name: Gets or sets the first name of the contact.
    :type first_name: str
    :param email: Gets or sets the email of the contact.
    :type email: str
    :param phone_number: Gets or sets the phone number of the contact.
    :type phone_number: str
    """

    _attribute_map = {
        'organization': {'key': 'organization', 'type': 'MicrosoftPartnerSdkContractsV1ServiceRequestOrganization'},
        'contact_id': {'key': 'contactId', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'first_name': {'key': 'firstName', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
    }

    def __init__(self, organization=None, contact_id=None, last_name=None, first_name=None, email=None, phone_number=None):
        super(MicrosoftPartnerSdkContractsV1ServiceRequestContact, self).__init__()
        self.organization = organization
        self.contact_id = contact_id
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone_number = phone_number