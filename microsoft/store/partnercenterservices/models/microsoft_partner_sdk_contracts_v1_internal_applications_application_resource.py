# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1InternalApplicationsApplicationResource(Model):
    """Resource for an application to register/unregister.

    :param registration_resource: The registration resource. Possible values
     include: 'none', 'v1', 'v2'
    :type registration_resource: str or
     ~microsoft.store.partnercenterservices.models.enum
    :param status: Registration status of the application. Possible values
     include: 'none', 'active', 'disabled'
    :type status: str or ~microsoft.store.partnercenterservices.models.enum
    """

    _attribute_map = {
        'registration_resource': {'key': 'registrationResource', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, registration_resource=None, status=None):
        super(MicrosoftPartnerSdkContractsV1InternalApplicationsApplicationResource, self).__init__()
        self.registration_resource = registration_resource
        self.status = status
