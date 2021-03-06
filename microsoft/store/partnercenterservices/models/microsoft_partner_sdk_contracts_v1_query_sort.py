# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1QuerySort(Model):
    """Specifies sort field and direction.

    :param sort_field: Gets or sets the sort field.
    :type sort_field: str
    :param sort_direction: Gets or sets the sort direction. Possible values
     include: 'ascending', 'descending'
    :type sort_direction: str or
     ~microsoft.store.partnercenterservices.models.enum
    """

    _attribute_map = {
        'sort_field': {'key': 'sortField', 'type': 'str'},
        'sort_direction': {'key': 'sortDirection', 'type': 'str'},
    }

    def __init__(self, sort_field=None, sort_direction=None):
        super(MicrosoftPartnerSdkContractsV1QuerySort, self).__init__()
        self.sort_field = sort_field
        self.sort_direction = sort_direction
