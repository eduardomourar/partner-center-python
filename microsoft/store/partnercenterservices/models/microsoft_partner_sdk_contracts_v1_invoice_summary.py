# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1InvoiceSummary(Model):
    """Describes a summary of the balance and total charges of an invoice.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param balance_amount: Gets or sets the balance of the invoice.
     This is the total amount of unpaid bills.
    :type balance_amount: float
    :param currency_code: Gets or sets a code that indicates the currency used
     for the balance amount.
    :type currency_code: str
    :ivar currency_symbol: Gets or sets the currency symbol used for all
     invoice item amounts and totals.
    :vartype currency_symbol: str
    :param accounting_date: Gets or sets the date the balance amount was last
     updated.
    :type accounting_date: datetime
    :param first_invoice_creation_date: Gets or sets the date the first
     invoice for the customer was created.
    :type first_invoice_creation_date: datetime
    :param links: Gets or sets the links.
    :type links:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceLinks
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'currency_symbol': {'readonly': True},
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'balance_amount': {'key': 'balanceAmount', 'type': 'float'},
        'currency_code': {'key': 'currencyCode', 'type': 'str'},
        'currency_symbol': {'key': 'currencySymbol', 'type': 'str'},
        'accounting_date': {'key': 'accountingDate', 'type': 'iso-8601'},
        'first_invoice_creation_date': {'key': 'firstInvoiceCreationDate', 'type': 'iso-8601'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceLinks'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, balance_amount=None, currency_code=None, accounting_date=None, first_invoice_creation_date=None, links=None):
        super(MicrosoftPartnerSdkContractsV1InvoiceSummary, self).__init__()
        self.balance_amount = balance_amount
        self.currency_code = currency_code
        self.currency_symbol = None
        self.accounting_date = accounting_date
        self.first_invoice_creation_date = first_invoice_creation_date
        self.links = links
        self.attributes = None
