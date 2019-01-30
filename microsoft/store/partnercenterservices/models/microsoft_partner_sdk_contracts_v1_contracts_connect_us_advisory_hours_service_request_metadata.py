# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1ContractsConnectUsAdvisoryHoursServiceRequestMetadata(Model):
    """Advisory hours service request metadata.

    :param countries: Gets or sets the countries.
    :type countries:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ContractsConnectUsCountry]
    :param languages: Gets or sets the languages.
    :type languages:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ContractsConnectUsLanguage]
    :param technologies: Gets or sets the technologies.
    :type technologies:
     list[~microsoft.store.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ContractsConnectUsTechnology]
    """

    _attribute_map = {
        'countries': {'key': 'countries', 'type': '[MicrosoftPartnerSdkContractsV1ContractsConnectUsCountry]'},
        'languages': {'key': 'languages', 'type': '[MicrosoftPartnerSdkContractsV1ContractsConnectUsLanguage]'},
        'technologies': {'key': 'technologies', 'type': '[MicrosoftPartnerSdkContractsV1ContractsConnectUsTechnology]'},
    }

    def __init__(self, countries=None, languages=None, technologies=None):
        super(MicrosoftPartnerSdkContractsV1ContractsConnectUsAdvisoryHoursServiceRequestMetadata, self).__init__()
        self.countries = countries
        self.languages = languages
        self.technologies = technologies
