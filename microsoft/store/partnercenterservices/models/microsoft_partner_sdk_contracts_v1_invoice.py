# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1Invoice(Model):
    """Represents a monthly billing statement issued to a partner.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Gets or sets the invoice unique identifier.
    :type id: str
    :param invoice_date: Gets or sets the date the invoice was generated.
    :type invoice_date: datetime
    :param total_charges: Gets or sets the total charges in this invoice.
     Total charges includes charges for transactions and any adjustments.
    :type total_charges: float
    :param paid_amount: Gets or sets the amount paid by the partner.
     The paid amount is negative if a payment was received.
    :type paid_amount: float
    :param currency_code: Gets or sets a code that indicates the currency used
     for all invoice item amounts and totals.
    :type currency_code: str
    :ivar currency_symbol: Gets or sets the currency symbol used for all
     invoice item amounts and totals.
    :vartype currency_symbol: str
    :param pdf_download_link: Gets or sets a link to download the invoice in
     PDF format. This link is not returned as part
     of the search results, and is populated only if the invoice is accessed by
     ID.
     This link auto-expires in 30 minutes.
    :type pdf_download_link: str
    :param invoice_details: Gets or sets the invoice details.
    :type invoice_details:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1InvoiceDetail]
    :param amendments: Gets or sets the amendments to this invoice.
    :type amendments:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1Invoice]
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
        'id': {'key': 'id', 'type': 'str'},
        'invoice_date': {'key': 'invoiceDate', 'type': 'iso-8601'},
        'total_charges': {'key': 'totalCharges', 'type': 'float'},
        'paid_amount': {'key': 'paidAmount', 'type': 'float'},
        'currency_code': {'key': 'currencyCode', 'type': 'str'},
        'currency_symbol': {'key': 'currencySymbol', 'type': 'str'},
        'pdf_download_link': {'key': 'pdfDownloadLink', 'type': 'str'},
        'invoice_details': {'key': 'invoiceDetails', 'type': '[MicrosoftPartnerSdkContractsV1InvoiceDetail]'},
        'amendments': {'key': 'amendments', 'type': '[MicrosoftPartnerSdkContractsV1Invoice]'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceLinks'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, id=None, invoice_date=None, total_charges=None, paid_amount=None, currency_code=None, pdf_download_link=None, invoice_details=None, amendments=None, links=None):
        super(MicrosoftPartnerSdkContractsV1Invoice, self).__init__()
        self.id = id
        self.invoice_date = invoice_date
        self.total_charges = total_charges
        self.paid_amount = paid_amount
        self.currency_code = currency_code
        self.currency_symbol = None
        self.pdf_download_link = pdf_download_link
        self.invoice_details = invoice_details
        self.amendments = amendments
        self.links = links
        self.attributes = None
