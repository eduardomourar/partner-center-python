# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1CustomerUser(Model):
    """Describes a customer user.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param usage_location: Gets or sets the usage location. The location where
     the user intends to use the license.
    :type usage_location: str
    :param id: Gets or sets the user identifier.
    :type id: str
    :param user_principal_name: Gets or sets the name of the user principal.
    :type user_principal_name: str
    :param first_name: Gets or sets the first name of the user.
    :type first_name: str
    :param last_name: Gets or sets the last name of the user.
    :type last_name: str
    :param display_name: Gets or sets the display name of the user.
    :type display_name: str
    :param immutable_id: Gets or sets the immutable id of the user.
    :type immutable_id: str
    :param password_profile: Gets or sets the user's password profile.
    :type password_profile:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ContractsPasswordProfile
    :param phone_number: Gets or sets the user's phone number.
    :type phone_number: str
    :param last_directory_sync_time: Gets or sets the last directory sync time
     for the user.
     The last time that information for this user was synced between Azure
     Active Directory
     and on-premises Active Directory. A date time value only appears if Azure
     AD Connect
     sync is enabled. Otherwise, the value is null.
    :type last_directory_sync_time: datetime
    :param user_domain_type: Gets or sets user domain type. Possible values
     include: 'none', 'managed', 'federated'
    :type user_domain_type: str or
     ~microsoft.store.partnercenterservices.models.enum
    :param state: Gets or sets the state of the user, for the deleted user
     this is "Inactive" and for the normal user it is "Active". Possible values
     include: 'active', 'inactive'
    :type state: str or ~microsoft.store.partnercenterservices.models.enum
    :param soft_deletion_time: Gets or sets the deleted time for the inactive
     user.
     Represents the start of the thirty day period after which data associated
     with a deleted user is permanently deleted and therefore unrecoverable.
    :type soft_deletion_time: datetime
    :param links: Gets or sets the links.
    :type links:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceLinks
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'usage_location': {'key': 'usageLocation', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'first_name': {'key': 'firstName', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'immutable_id': {'key': 'immutableId', 'type': 'str'},
        'password_profile': {'key': 'passwordProfile', 'type': 'MicrosoftPartnerSdkContractsV1ContractsPasswordProfile'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'last_directory_sync_time': {'key': 'lastDirectorySyncTime', 'type': 'iso-8601'},
        'user_domain_type': {'key': 'userDomainType', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'soft_deletion_time': {'key': 'softDeletionTime', 'type': 'iso-8601'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceLinks'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, usage_location=None, id=None, user_principal_name=None, first_name=None, last_name=None, display_name=None, immutable_id=None, password_profile=None, phone_number=None, last_directory_sync_time=None, user_domain_type=None, state=None, soft_deletion_time=None, links=None):
        super(MicrosoftPartnerSdkContractsV1CustomerUser, self).__init__()
        self.usage_location = usage_location
        self.id = id
        self.user_principal_name = user_principal_name
        self.first_name = first_name
        self.last_name = last_name
        self.display_name = display_name
        self.immutable_id = immutable_id
        self.password_profile = password_profile
        self.phone_number = phone_number
        self.last_directory_sync_time = last_directory_sync_time
        self.user_domain_type = user_domain_type
        self.state = state
        self.soft_deletion_time = soft_deletion_time
        self.links = links
        self.attributes = None
