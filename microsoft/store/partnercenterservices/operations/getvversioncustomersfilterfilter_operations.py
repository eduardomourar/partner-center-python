# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class GetvversioncustomersfilterfilterOperations(object):
    """GetvversioncustomersfilterfilterOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def value(
            self, version, filter=None, size=None, seek_operation=None, ms_correlation_id=None, ms_request_id=None, custom_headers=None, raw=False, **operation_config):
        """Retrieves a segment of a partner's customers. Optional filtering of
        customers can also be applied.
        Customers can only be filtered by a string which their company name or
        domain name starts with. Full search is not supported currently.
        Customers can be filtered using a
        {Microsoft.Partner.Sdk.Contracts.V1.Query.Filters.FieldFilterOperation.StartsWith}
        filter operation and specifying either: DisplayName (Company name) or
        DefaultDomainName
        as the filter field.

        :param version: Possible values include: '1.0', '1'
        :type version: str
        :param filter: An optional customers filter. This is a Json object
         that looks like:
         {
         "Field": "your desired filter field",
         "Operator": "StartsWith"
         "Value": "Your search string"
         }
        :type filter: str
        :param size: The maximum number of customers to return.
        :type size: int
        :param seek_operation: Possible values include: 'next', 'previous',
         'first', 'last', 'pageIndex'
        :type seek_operation: str
        :param ms_correlation_id: A unique identifier for the call, useful in
         logs and network traces for troubleshooting errors. The value should
         be reset for every call. All operations should include this header.
        :type ms_correlation_id: str
        :param ms_request_id: A unique identifier for the call, used to ensure
         idempotency. In the case of a timeout, the retry call should include
         the same value. Upon receiving a response (success or business
         failure), the value should be reset for the next call.
        :type ms_request_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return:
         MicrosoftPartnerSdkContractsV1CollectionsResourceCollectionMicrosoftPartnerSdkContractsV1Customer
         or ClientRawResponse if raw=true
        :rtype:
         ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CollectionsResourceCollectionMicrosoftPartnerSdkContractsV1Customer
         or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.value.metadata['url']
        path_format_arguments = {
            'version': self._serialize.url("version", version, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if filter is not None:
            query_parameters['filter'] = self._serialize.query("filter", filter, 'str')
        if size is not None:
            query_parameters['size'] = self._serialize.query("size", size, 'int')
        if seek_operation is not None:
            query_parameters['seekOperation'] = self._serialize.query("seek_operation", seek_operation, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if ms_correlation_id is not None:
            header_parameters['MS-CorrelationId'] = self._serialize.header("ms_correlation_id", ms_correlation_id, 'str')
        if ms_request_id is not None:
            header_parameters['MS-RequestId'] = self._serialize.header("ms_request_id", ms_request_id, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 403, 404, 500]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('MicrosoftPartnerSdkContractsV1CollectionsResourceCollectionMicrosoftPartnerSdkContractsV1Customer', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    value.metadata = {'url': '/v{version}/customers'}