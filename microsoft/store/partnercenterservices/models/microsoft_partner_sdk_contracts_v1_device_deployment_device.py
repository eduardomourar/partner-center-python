# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1DeviceDeploymentDevice(Model):
    """Provides information about a device associated with a customer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Gets or sets a GUID-formatted string that identifies the
     device.
    :type id: str
    :param serial_number: Gets or sets the serial number uniquely associated
     with the device.
    :type serial_number: str
    :param product_key: Gets or sets the product key uniquely associated with
     the device.
    :type product_key: str
    :param hardware_hash: Gets or sets the hardware hash associated with the
     device.
    :type hardware_hash: str
    :param model_name: Gets or sets the model name associated with the device.
    :type model_name: str
    :param oem_manufacturer_name: Gets or sets the OEM manufacturer name
     associated with the device.
    :type oem_manufacturer_name: str
    :param policies: Gets or sets the list of policies assigned to the device.
    :type policies:
     list[~azure.partnercenterservices.models.SystemCollectionsGenericKeyValuePairMicrosoftPartnerSdkContractsV1DeviceDeploymentPolicyCategorySystemString]
    :param uploaded_by: Gets or sets the ID of the tenant who uploaded the
     device.
    :type uploaded_by: str
    :param uploaded_date: Gets or sets the UTC date and time the device
     details were uploaded.
    :type uploaded_date: datetime
    :param allowed_operations: Gets or sets the list of HTTP methods allowed
     on a device sync. (Example : GET, PATCH, DELETE)
    :type allowed_operations: list[str]
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
        'serial_number': {'key': 'serialNumber', 'type': 'str'},
        'product_key': {'key': 'productKey', 'type': 'str'},
        'hardware_hash': {'key': 'hardwareHash', 'type': 'str'},
        'model_name': {'key': 'modelName', 'type': 'str'},
        'oem_manufacturer_name': {'key': 'oemManufacturerName', 'type': 'str'},
        'policies': {'key': 'policies', 'type': '[SystemCollectionsGenericKeyValuePairMicrosoftPartnerSdkContractsV1DeviceDeploymentPolicyCategorySystemString]'},
        'uploaded_by': {'key': 'uploadedBy', 'type': 'str'},
        'uploaded_date': {'key': 'uploadedDate', 'type': 'iso-8601'},
        'allowed_operations': {'key': 'allowedOperations', 'type': '[str]'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceLinks'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, id=None, serial_number=None, product_key=None, hardware_hash=None, model_name=None, oem_manufacturer_name=None, policies=None, uploaded_by=None, uploaded_date=None, allowed_operations=None, links=None):
        super(MicrosoftPartnerSdkContractsV1DeviceDeploymentDevice, self).__init__()
        self.id = id
        self.serial_number = serial_number
        self.product_key = product_key
        self.hardware_hash = hardware_hash
        self.model_name = model_name
        self.oem_manufacturer_name = oem_manufacturer_name
        self.policies = policies
        self.uploaded_by = uploaded_by
        self.uploaded_date = uploaded_date
        self.allowed_operations = allowed_operations
        self.links = links
        self.attributes = None
