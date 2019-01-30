# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1DomainManagementDomainFederationSettings(Model):
    """Represents domain federation settings.

    :param active_log_on_uri: Active logon URI
    :type active_log_on_uri: str
    :param default_interactive_authentication_method: Default interaction
     authentication method
    :type default_interactive_authentication_method: str
    :param federation_brand_name: Federation brand name
    :type federation_brand_name: str
    :param issuer_uri: Issuer URI
    :type issuer_uri: str
    :param log_off_uri: Logoff URI
    :type log_off_uri: str
    :param metadata_exchange_uri: Meta data exchange URI
    :type metadata_exchange_uri: str
    :param next_signing_certificate: Next Signing Certificate
    :type next_signing_certificate: str
    :param open_id_connect_discovery_endpoint: Open ID connect discovery
     endpoint
    :type open_id_connect_discovery_endpoint: str
    :param passive_log_on_uri: Passive logon URI
    :type passive_log_on_uri: str
    :param preferred_authentication_protocol: Preferred authentication
     protocol. Possible values include: 'ws_fed', 'samlp'
    :type preferred_authentication_protocol: str or
     ~azure.partnercenterservices.models.enum
    :param prompt_login_behavior: Prompt login behavior. Possible values
     include: 'translate_to_fresh_password_auth', 'native_support', 'disabled'
    :type prompt_login_behavior: str or
     ~azure.partnercenterservices.models.enum
    :param signing_certificate: Signing Certificate
    :type signing_certificate: str
    :param signing_certificate_update_status: Signing certificate update
     status
    :type signing_certificate_update_status:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1DomainManagementSigningCertificateUpdateStatus
    :param supports_mfa: Supports MFA?
    :type supports_mfa: bool
    """

    _attribute_map = {
        'active_log_on_uri': {'key': 'activeLogOnUri', 'type': 'str'},
        'default_interactive_authentication_method': {'key': 'defaultInteractiveAuthenticationMethod', 'type': 'str'},
        'federation_brand_name': {'key': 'federationBrandName', 'type': 'str'},
        'issuer_uri': {'key': 'issuerUri', 'type': 'str'},
        'log_off_uri': {'key': 'logOffUri', 'type': 'str'},
        'metadata_exchange_uri': {'key': 'metadataExchangeUri', 'type': 'str'},
        'next_signing_certificate': {'key': 'nextSigningCertificate', 'type': 'str'},
        'open_id_connect_discovery_endpoint': {'key': 'openIdConnectDiscoveryEndpoint', 'type': 'str'},
        'passive_log_on_uri': {'key': 'passiveLogOnUri', 'type': 'str'},
        'preferred_authentication_protocol': {'key': 'preferredAuthenticationProtocol', 'type': 'str'},
        'prompt_login_behavior': {'key': 'promptLoginBehavior', 'type': 'str'},
        'signing_certificate': {'key': 'signingCertificate', 'type': 'str'},
        'signing_certificate_update_status': {'key': 'signingCertificateUpdateStatus', 'type': 'MicrosoftPartnerSdkContractsV1DomainManagementSigningCertificateUpdateStatus'},
        'supports_mfa': {'key': 'supportsMfa', 'type': 'bool'},
    }

    def __init__(self, active_log_on_uri=None, default_interactive_authentication_method=None, federation_brand_name=None, issuer_uri=None, log_off_uri=None, metadata_exchange_uri=None, next_signing_certificate=None, open_id_connect_discovery_endpoint=None, passive_log_on_uri=None, preferred_authentication_protocol=None, prompt_login_behavior=None, signing_certificate=None, signing_certificate_update_status=None, supports_mfa=None):
        super(MicrosoftPartnerSdkContractsV1DomainManagementDomainFederationSettings, self).__init__()
        self.active_log_on_uri = active_log_on_uri
        self.default_interactive_authentication_method = default_interactive_authentication_method
        self.federation_brand_name = federation_brand_name
        self.issuer_uri = issuer_uri
        self.log_off_uri = log_off_uri
        self.metadata_exchange_uri = metadata_exchange_uri
        self.next_signing_certificate = next_signing_certificate
        self.open_id_connect_discovery_endpoint = open_id_connect_discovery_endpoint
        self.passive_log_on_uri = passive_log_on_uri
        self.preferred_authentication_protocol = preferred_authentication_protocol
        self.prompt_login_behavior = prompt_login_behavior
        self.signing_certificate = signing_certificate
        self.signing_certificate_update_status = signing_certificate_update_status
        self.supports_mfa = supports_mfa
