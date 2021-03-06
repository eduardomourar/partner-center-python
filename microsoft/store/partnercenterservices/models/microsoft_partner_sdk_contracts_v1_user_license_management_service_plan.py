# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1UserLicenseManagementServicePlan(Model):
    """Identifies a deployable service within a product SKU. A product can have
    many service plans.

    :param display_name: Gets or sets the localized display name for the
     service plan.
    :type display_name: str
    :param service_name: Gets or sets the service name.
    :type service_name: str
    :param id: Gets or sets the service plan identifier.
    :type id: str
    :param capability_status: Gets or sets the status of the service plan.
    :type capability_status: str
    :param target_type: Gets or sets the target type of the service plan.
     This identifies whether the service plan is applicable to a "User" or a
     "Tenant".
     For example, to determine all service plans that are applicable to user,
     filter where target type == "User".
    :type target_type: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'service_name': {'key': 'serviceName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'capability_status': {'key': 'capabilityStatus', 'type': 'str'},
        'target_type': {'key': 'targetType', 'type': 'str'},
    }

    def __init__(self, display_name=None, service_name=None, id=None, capability_status=None, target_type=None):
        super(MicrosoftPartnerSdkContractsV1UserLicenseManagementServicePlan, self).__init__()
        self.display_name = display_name
        self.service_name = service_name
        self.id = id
        self.capability_status = capability_status
        self.target_type = target_type
