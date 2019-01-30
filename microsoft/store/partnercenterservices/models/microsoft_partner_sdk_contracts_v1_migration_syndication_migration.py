# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1MigrationSyndicationMigration(Model):
    """Batch for migration from syndication to CSP.

    :param id: Gets or sets the migration batch ID
    :type id: str
    :param partner_id: Gets or sets the CSP Partner ID
    :type partner_id: str
    :param created_date: Gets or sets the batch created date
    :type created_date: datetime
    :param mosi_customer_ids: Gets or sets the list of customers to be
     migrated
    :type mosi_customer_ids: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'partner_id': {'key': 'partnerId', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'mosi_customer_ids': {'key': 'mosiCustomerIds', 'type': '[str]'},
    }

    def __init__(self, id=None, partner_id=None, created_date=None, mosi_customer_ids=None):
        super(MicrosoftPartnerSdkContractsV1MigrationSyndicationMigration, self).__init__()
        self.id = id
        self.partner_id = partner_id
        self.created_date = created_date
        self.mosi_customer_ids = mosi_customer_ids
