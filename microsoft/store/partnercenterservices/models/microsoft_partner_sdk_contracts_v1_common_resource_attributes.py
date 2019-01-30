# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1CommonResourceAttributes(Model):
    """Refers to the common object attributes.

    :param etag: Gets or sets the etag.
     The object version in providers.
    :type etag: str
    :param object_type: The type of object.
    :type object_type: str
    """

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
    }

    def __init__(self, etag=None, object_type=None):
        super(MicrosoftPartnerSdkContractsV1CommonResourceAttributes, self).__init__()
        self.etag = etag
        self.object_type = object_type