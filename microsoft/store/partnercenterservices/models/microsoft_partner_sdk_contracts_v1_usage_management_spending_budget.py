# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1UsageManagementSpendingBudget(Model):
    """Represents the budget allocated to this customer for usage-based
    subscriptions.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param amount: The amount allocated to this customer for usage based
     subscriptions.
     If this value is null, there is no spending budget allocated to the
     customer.
    :type amount: float
    :param usage_spending_budget: To do: to be deprecated soon. Added for
     backward compatibility
    :type usage_spending_budget: float
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'amount': {'key': 'amount', 'type': 'float'},
        'usage_spending_budget': {'key': 'usageSpendingBudget', 'type': 'float'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, amount=None, usage_spending_budget=None):
        super(MicrosoftPartnerSdkContractsV1UsageManagementSpendingBudget, self).__init__()
        self.amount = amount
        self.usage_spending_budget = usage_spending_budget
        self.attributes = None
