# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1MigrationSyndicationMigrationStatus(Model):
    """Status of migration from syndication to CSP.

    :param id: Gets or sets the migration batch ID
    :type id: str
    :param partner_id: Gets or sets the CSP Partner ID
    :type partner_id: str
    :param customers_data: Gets or sets the migration data of customers
    :type customers_data:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1MigrationCustomerSyndicationMigration]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'partner_id': {'key': 'partnerId', 'type': 'str'},
        'customers_data': {'key': 'customersData', 'type': '[MicrosoftPartnerSdkContractsV1MigrationCustomerSyndicationMigration]'},
    }

    def __init__(self, id=None, partner_id=None, customers_data=None):
        super(MicrosoftPartnerSdkContractsV1MigrationSyndicationMigrationStatus, self).__init__()
        self.id = id
        self.partner_id = partner_id
        self.customers_data = customers_data
