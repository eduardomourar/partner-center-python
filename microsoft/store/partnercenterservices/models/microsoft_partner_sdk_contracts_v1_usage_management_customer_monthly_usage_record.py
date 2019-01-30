# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1UsageManagementCustomerMonthlyUsageRecord(Model):
    """Represents the estimated monetary cost of a customer's usage in the current
    month.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param budget: The spending budget allocated for the customer.
    :type budget:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1UsageManagementSpendingBudget
    :param customer_spending_budget: To do: to be deprecated with next
     release. The spending budget allocated for a specific customer.
    :type customer_spending_budget:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1UsageManagementSpendingBudget
    :param percent_used: The percentage used out of the allocated budget.
    :type percent_used: float
    :param resource_id: Gets or sets the resource unique identifier. A GUID
     formatted string.
    :type resource_id: str
    :param id: To do: To be deprecated: The resource unique identifier.
    :type id: str
    :param resource_name: Gets or sets the name of the resource.
    :type resource_name: str
    :param name: To do: To be deprecated soon. The name of the resource.
    :type name: str
    :param total_cost: Gets or sets the estimated total cost of using the
     resources in the subscription.
    :type total_cost: float
    :param currency_locale: Gets or sets the locale in which the subscription
     was used, determines the currency to use on the invoice.
    :type currency_locale: str
    :param last_modified_date: Gets or sets the day, in date-time format, that
     this record was last modified.
    :type last_modified_date: datetime
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'budget': {'key': 'budget', 'type': 'MicrosoftPartnerSdkContractsV1UsageManagementSpendingBudget'},
        'customer_spending_budget': {'key': 'customerSpendingBudget', 'type': 'MicrosoftPartnerSdkContractsV1UsageManagementSpendingBudget'},
        'percent_used': {'key': 'percentUsed', 'type': 'float'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'resource_name': {'key': 'resourceName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'total_cost': {'key': 'totalCost', 'type': 'float'},
        'currency_locale': {'key': 'currencyLocale', 'type': 'str'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, budget=None, customer_spending_budget=None, percent_used=None, resource_id=None, id=None, resource_name=None, name=None, total_cost=None, currency_locale=None, last_modified_date=None):
        super(MicrosoftPartnerSdkContractsV1UsageManagementCustomerMonthlyUsageRecord, self).__init__()
        self.budget = budget
        self.customer_spending_budget = customer_spending_budget
        self.percent_used = percent_used
        self.resource_id = resource_id
        self.id = id
        self.resource_name = resource_name
        self.name = name
        self.total_cost = total_cost
        self.currency_locale = currency_locale
        self.last_modified_date = last_modified_date
        self.attributes = None
