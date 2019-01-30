# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1QueryFiltersFieldFilter(Model):
    """Represents a filter that can be applied to a search results field.

    :param operator: Gets or sets the filter operator. Possible values
     include: 'equals', 'not_equals', 'greater_than', 'greater_than_or_equals',
     'less_than', 'less_than_or_equals', 'substring', 'and', 'or',
     'starts_with', 'not_starts_with'
    :type operator: str or ~azure.partnercenterservices.models.enum
    """

    _attribute_map = {
        'operator': {'key': 'operator', 'type': 'str'},
    }

    def __init__(self, operator=None):
        super(MicrosoftPartnerSdkContractsV1QueryFiltersFieldFilter, self).__init__()
        self.operator = operator