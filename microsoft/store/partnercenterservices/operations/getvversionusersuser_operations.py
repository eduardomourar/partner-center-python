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


class GetvversionusersuserOperations(object):
    """GetvversionusersuserOperations operations.

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

    def idpreferencesnotificationsnotification_areachannel_type(
            self, notification_area, version, user_id, channel_type, ms_correlation_id=None, ms_request_id=None, custom_headers=None, raw=False, **operation_config):
        """Get  the notification preferences for a particular config.

        :param notification_area: Notification area. Possible values include:
         'none', 'ratedUsage', 'serviceHealth'
        :type notification_area: str
        :param version: Possible values include: '1.0', '1'
        :type version: str
        :param user_id:
        :type user_id: str
        :param channel_type:
        :type channel_type: str
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
         MicrosoftPartnerSdkContractsV1NotificationPreferenceNotificationPreference
         or ClientRawResponse if raw=true
        :rtype:
         ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1NotificationPreferenceNotificationPreference
         or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.idpreferencesnotificationsnotification_areachannel_type.metadata['url']
        path_format_arguments = {
            'notificationArea': self._serialize.url("notification_area", notification_area, 'str'),
            'version': self._serialize.url("version", version, 'str'),
            'user_id': self._serialize.url("user_id", user_id, 'str'),
            'channelType': self._serialize.url("channel_type", channel_type, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

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
            deserialized = self._deserialize('MicrosoftPartnerSdkContractsV1NotificationPreferenceNotificationPreference', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    idpreferencesnotificationsnotification_areachannel_type.metadata = {'url': '/v{version}/users/{user_id}/preferences/notifications/{notificationArea}/{channelType}'}
