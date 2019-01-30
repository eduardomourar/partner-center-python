# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ContractsRateCardsAzureMeter(Model):
    """This class defines the meter included in an Azure rate card.

    :param id: The meter unique identifier.
    :type id: str
    :param name: The name of the meter.
    :type name: str
    :param rates: The rates.
     Key - meter quantity
     Value - meter rate
    :type rates: dict[str, float]
    :param tags: Gets or sets the azure meter tags.
    :type tags: list[str]
    :param category: The category of the meter.
     Example: Storage
    :type category: str
    :param subcategory: The subcategory of the meter.
     Example: Sku
    :type subcategory: str
    :param region: The region.
    :type region: str
    :param unit: The base unit for the rates.
    :type unit: str
    :param included_quantity: The included quantity which is free of charge.
    :type included_quantity: float
    :param effective_date: The date this meter is in effect.
    :type effective_date: datetime
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'rates': {'key': 'rates', 'type': '{float}'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'category': {'key': 'category', 'type': 'str'},
        'subcategory': {'key': 'subcategory', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'float'},
        'effective_date': {'key': 'effectiveDate', 'type': 'iso-8601'},
    }

    def __init__(self, id=None, name=None, rates=None, tags=None, category=None, subcategory=None, region=None, unit=None, included_quantity=None, effective_date=None):
        super(MicrosoftPartnerSdkContractsV1ContractsRateCardsAzureMeter, self).__init__()
        self.id = id
        self.name = name
        self.rates = rates
        self.tags = tags
        self.category = category
        self.subcategory = subcategory
        self.region = region
        self.unit = unit
        self.included_quantity = included_quantity
        self.effective_date = effective_date
