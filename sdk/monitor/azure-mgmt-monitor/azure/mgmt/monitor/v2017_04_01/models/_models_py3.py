# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ActionGroupList(msrest.serialization.Model):
    """A list of action groups.

    :param value: The list of action groups.
    :type value: list[~$(python-base-namespace).v2017_04_01.models.ActionGroupResource]
    :param next_link: Provides the link to retrieve the next set of elements.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ActionGroupResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ActionGroupResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ActionGroupList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ActionGroupPatchBody(msrest.serialization.Model):
    """An action group object for the body of patch operations.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param enabled: Indicates whether this action group is enabled. If an action group is not
     enabled, then none of its actions will be activated.
    :type enabled: bool
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        enabled: Optional[bool] = True,
        **kwargs
    ):
        super(ActionGroupPatchBody, self).__init__(**kwargs)
        self.tags = tags
        self.enabled = enabled


class Resource(msrest.serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class ActionGroupResource(Resource):
    """An action group resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param group_short_name: The short name of the action group. This will be used in SMS messages.
    :type group_short_name: str
    :param enabled: Indicates whether this action group is enabled. If an action group is not
     enabled, then none of its receivers will receive communications.
    :type enabled: bool
    :param email_receivers: The list of email receivers that are part of this action group.
    :type email_receivers: list[~$(python-base-namespace).v2017_04_01.models.EmailReceiver]
    :param sms_receivers: The list of SMS receivers that are part of this action group.
    :type sms_receivers: list[~$(python-base-namespace).v2017_04_01.models.SmsReceiver]
    :param webhook_receivers: The list of webhook receivers that are part of this action group.
    :type webhook_receivers: list[~$(python-base-namespace).v2017_04_01.models.WebhookReceiver]
    :param itsm_receivers: The list of ITSM receivers that are part of this action group.
    :type itsm_receivers: list[~$(python-base-namespace).v2017_04_01.models.ItsmReceiver]
    :param azure_app_push_receivers: The list of AzureAppPush receivers that are part of this
     action group.
    :type azure_app_push_receivers: list[~$(python-base-
     namespace).v2017_04_01.models.AzureAppPushReceiver]
    :param automation_runbook_receivers: The list of AutomationRunbook receivers that are part of
     this action group.
    :type automation_runbook_receivers: list[~$(python-base-
     namespace).v2017_04_01.models.AutomationRunbookReceiver]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'group_short_name': {'max_length': 12, 'min_length': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'group_short_name': {'key': 'properties.groupShortName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'email_receivers': {'key': 'properties.emailReceivers', 'type': '[EmailReceiver]'},
        'sms_receivers': {'key': 'properties.smsReceivers', 'type': '[SmsReceiver]'},
        'webhook_receivers': {'key': 'properties.webhookReceivers', 'type': '[WebhookReceiver]'},
        'itsm_receivers': {'key': 'properties.itsmReceivers', 'type': '[ItsmReceiver]'},
        'azure_app_push_receivers': {'key': 'properties.azureAppPushReceivers', 'type': '[AzureAppPushReceiver]'},
        'automation_runbook_receivers': {'key': 'properties.automationRunbookReceivers', 'type': '[AutomationRunbookReceiver]'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        group_short_name: Optional[str] = None,
        enabled: Optional[bool] = True,
        email_receivers: Optional[List["EmailReceiver"]] = None,
        sms_receivers: Optional[List["SmsReceiver"]] = None,
        webhook_receivers: Optional[List["WebhookReceiver"]] = None,
        itsm_receivers: Optional[List["ItsmReceiver"]] = None,
        azure_app_push_receivers: Optional[List["AzureAppPushReceiver"]] = None,
        automation_runbook_receivers: Optional[List["AutomationRunbookReceiver"]] = None,
        **kwargs
    ):
        super(ActionGroupResource, self).__init__(location=location, tags=tags, **kwargs)
        self.group_short_name = group_short_name
        self.enabled = enabled
        self.email_receivers = email_receivers
        self.sms_receivers = sms_receivers
        self.webhook_receivers = webhook_receivers
        self.itsm_receivers = itsm_receivers
        self.azure_app_push_receivers = azure_app_push_receivers
        self.automation_runbook_receivers = automation_runbook_receivers


class ActivityLogAlertActionGroup(msrest.serialization.Model):
    """A pointer to an Azure Action Group.

    All required parameters must be populated in order to send to Azure.

    :param action_group_id: Required. The resourceId of the action group. This cannot be null or
     empty.
    :type action_group_id: str
    :param webhook_properties: the dictionary of custom properties to include with the post
     operation. These data are appended to the webhook payload.
    :type webhook_properties: dict[str, str]
    """

    _validation = {
        'action_group_id': {'required': True},
    }

    _attribute_map = {
        'action_group_id': {'key': 'actionGroupId', 'type': 'str'},
        'webhook_properties': {'key': 'webhookProperties', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        action_group_id: str,
        webhook_properties: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(ActivityLogAlertActionGroup, self).__init__(**kwargs)
        self.action_group_id = action_group_id
        self.webhook_properties = webhook_properties


class ActivityLogAlertActionList(msrest.serialization.Model):
    """A list of activity log alert actions.

    :param action_groups: The list of activity log alerts.
    :type action_groups: list[~$(python-base-
     namespace).v2017_04_01.models.ActivityLogAlertActionGroup]
    """

    _attribute_map = {
        'action_groups': {'key': 'actionGroups', 'type': '[ActivityLogAlertActionGroup]'},
    }

    def __init__(
        self,
        *,
        action_groups: Optional[List["ActivityLogAlertActionGroup"]] = None,
        **kwargs
    ):
        super(ActivityLogAlertActionList, self).__init__(**kwargs)
        self.action_groups = action_groups


class ActivityLogAlertAllOfCondition(msrest.serialization.Model):
    """An Activity Log alert condition that is met when all its member conditions are met.

    All required parameters must be populated in order to send to Azure.

    :param all_of: Required. The list of activity log alert conditions.
    :type all_of: list[~$(python-base-namespace).v2017_04_01.models.ActivityLogAlertLeafCondition]
    """

    _validation = {
        'all_of': {'required': True},
    }

    _attribute_map = {
        'all_of': {'key': 'allOf', 'type': '[ActivityLogAlertLeafCondition]'},
    }

    def __init__(
        self,
        *,
        all_of: List["ActivityLogAlertLeafCondition"],
        **kwargs
    ):
        super(ActivityLogAlertAllOfCondition, self).__init__(**kwargs)
        self.all_of = all_of


class ActivityLogAlertLeafCondition(msrest.serialization.Model):
    """An Activity Log alert condition that is met by comparing an activity log field and value.

    All required parameters must be populated in order to send to Azure.

    :param field: Required. The name of the field that this condition will examine. The possible
     values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level',
     'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or
     anything beginning with 'properties.'.
    :type field: str
    :param equals: Required. The field value will be compared to this value (case-insensitive) to
     determine if the condition is met.
    :type equals: str
    """

    _validation = {
        'field': {'required': True},
        'equals': {'required': True},
    }

    _attribute_map = {
        'field': {'key': 'field', 'type': 'str'},
        'equals': {'key': 'equals', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        field: str,
        equals: str,
        **kwargs
    ):
        super(ActivityLogAlertLeafCondition, self).__init__(**kwargs)
        self.field = field
        self.equals = equals


class ActivityLogAlertList(msrest.serialization.Model):
    """A list of activity log alerts.

    :param value: The list of activity log alerts.
    :type value: list[~$(python-base-namespace).v2017_04_01.models.ActivityLogAlertResource]
    :param next_link: Provides the link to retrieve the next set of elements.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ActivityLogAlertResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ActivityLogAlertResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ActivityLogAlertList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ActivityLogAlertPatchBody(msrest.serialization.Model):
    """An activity log alert object for the body of patch operations.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param enabled: Indicates whether this activity log alert is enabled. If an activity log alert
     is not enabled, then none of its actions will be activated.
    :type enabled: bool
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        enabled: Optional[bool] = True,
        **kwargs
    ):
        super(ActivityLogAlertPatchBody, self).__init__(**kwargs)
        self.tags = tags
        self.enabled = enabled


class ActivityLogAlertResource(Resource):
    """An activity log alert resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param scopes: A list of resourceIds that will be used as prefixes. The alert will only apply
     to activityLogs with resourceIds that fall under one of these prefixes. This list must include
     at least one item.
    :type scopes: list[str]
    :param enabled: Indicates whether this activity log alert is enabled. If an activity log alert
     is not enabled, then none of its actions will be activated.
    :type enabled: bool
    :param condition: The condition that will cause this alert to activate.
    :type condition: ~$(python-base-namespace).v2017_04_01.models.ActivityLogAlertAllOfCondition
    :param actions: The actions that will activate when the condition is met.
    :type actions: ~$(python-base-namespace).v2017_04_01.models.ActivityLogAlertActionList
    :param description: A description of this activity log alert.
    :type description: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'scopes': {'key': 'properties.scopes', 'type': '[str]'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'condition': {'key': 'properties.condition', 'type': 'ActivityLogAlertAllOfCondition'},
        'actions': {'key': 'properties.actions', 'type': 'ActivityLogAlertActionList'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        scopes: Optional[List[str]] = None,
        enabled: Optional[bool] = True,
        condition: Optional["ActivityLogAlertAllOfCondition"] = None,
        actions: Optional["ActivityLogAlertActionList"] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(ActivityLogAlertResource, self).__init__(location=location, tags=tags, **kwargs)
        self.scopes = scopes
        self.enabled = enabled
        self.condition = condition
        self.actions = actions
        self.description = description


class AutomationRunbookReceiver(msrest.serialization.Model):
    """The Azure Automation Runbook notification receiver.

    All required parameters must be populated in order to send to Azure.

    :param automation_account_id: Required. The Azure automation account Id which holds this
     runbook and authenticate to Azure resource.
    :type automation_account_id: str
    :param runbook_name: Required. The name for this runbook.
    :type runbook_name: str
    :param webhook_resource_id: Required. The resource id for webhook linked to this runbook.
    :type webhook_resource_id: str
    :param is_global_runbook: Required. Indicates whether this instance is global runbook.
    :type is_global_runbook: bool
    :param name: Indicates name of the webhook.
    :type name: str
    :param service_uri: The URI where webhooks should be sent.
    :type service_uri: str
    """

    _validation = {
        'automation_account_id': {'required': True},
        'runbook_name': {'required': True},
        'webhook_resource_id': {'required': True},
        'is_global_runbook': {'required': True},
    }

    _attribute_map = {
        'automation_account_id': {'key': 'automationAccountId', 'type': 'str'},
        'runbook_name': {'key': 'runbookName', 'type': 'str'},
        'webhook_resource_id': {'key': 'webhookResourceId', 'type': 'str'},
        'is_global_runbook': {'key': 'isGlobalRunbook', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        automation_account_id: str,
        runbook_name: str,
        webhook_resource_id: str,
        is_global_runbook: bool,
        name: Optional[str] = None,
        service_uri: Optional[str] = None,
        **kwargs
    ):
        super(AutomationRunbookReceiver, self).__init__(**kwargs)
        self.automation_account_id = automation_account_id
        self.runbook_name = runbook_name
        self.webhook_resource_id = webhook_resource_id
        self.is_global_runbook = is_global_runbook
        self.name = name
        self.service_uri = service_uri


class AzureAppPushReceiver(msrest.serialization.Model):
    """The Azure mobile App push notification receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the Azure mobile app push receiver. Names must be unique
     across all receivers within an action group.
    :type name: str
    :param email_address: Required. The email address registered for the Azure mobile app.
    :type email_address: str
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        email_address: str,
        **kwargs
    ):
        super(AzureAppPushReceiver, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address


class EmailReceiver(msrest.serialization.Model):
    """An email receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the email receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param email_address: Required. The email address of this receiver.
    :type email_address: str
    :ivar status: The receiver status of the e-mail. Possible values include: 'NotSpecified',
     'Enabled', 'Disabled'.
    :vartype status: str or ~$(python-base-namespace).v2017_04_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'email_address': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        email_address: str,
        **kwargs
    ):
        super(EmailReceiver, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address
        self.status = None


class EnableRequest(msrest.serialization.Model):
    """Describes a receiver that should be resubscribed.

    All required parameters must be populated in order to send to Azure.

    :param receiver_name: Required. The name of the receiver to resubscribe.
    :type receiver_name: str
    """

    _validation = {
        'receiver_name': {'required': True},
    }

    _attribute_map = {
        'receiver_name': {'key': 'receiverName', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        receiver_name: str,
        **kwargs
    ):
        super(EnableRequest, self).__init__(**kwargs)
        self.receiver_name = receiver_name


class ErrorResponse(msrest.serialization.Model):
    """Describes the format of Error response.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ItsmReceiver(msrest.serialization.Model):
    """An Itsm receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the Itsm receiver. Names must be unique across all receivers
     within an action group.
    :type name: str
    :param workspace_id: Required. OMS LA instance identifier.
    :type workspace_id: str
    :param connection_id: Required. Unique identification of ITSM connection among multiple defined
     in above workspace.
    :type connection_id: str
    :param ticket_configuration: Required. JSON blob for the configurations of the ITSM action.
     CreateMultipleWorkItems option will be part of this blob as well.
    :type ticket_configuration: str
    :param region: Required. Region in which workspace resides. Supported
     values:'centralindia','japaneast','southeastasia','australiasoutheast','uksouth','westcentralus','canadacentral','eastus','westeurope'.
    :type region: str
    """

    _validation = {
        'name': {'required': True},
        'workspace_id': {'required': True},
        'connection_id': {'required': True},
        'ticket_configuration': {'required': True},
        'region': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'connection_id': {'key': 'connectionId', 'type': 'str'},
        'ticket_configuration': {'key': 'ticketConfiguration', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        workspace_id: str,
        connection_id: str,
        ticket_configuration: str,
        region: str,
        **kwargs
    ):
        super(ItsmReceiver, self).__init__(**kwargs)
        self.name = name
        self.workspace_id = workspace_id
        self.connection_id = connection_id
        self.ticket_configuration = ticket_configuration
        self.region = region


class SmsReceiver(msrest.serialization.Model):
    """An SMS receiver.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SMS receiver. Names must be unique across all receivers
     within an action group.
    :type name: str
    :param country_code: Required. The country code of the SMS receiver.
    :type country_code: str
    :param phone_number: Required. The phone number of the SMS receiver.
    :type phone_number: str
    :ivar status: The status of the receiver. Possible values include: 'NotSpecified', 'Enabled',
     'Disabled'.
    :vartype status: str or ~$(python-base-namespace).v2017_04_01.models.ReceiverStatus
    """

    _validation = {
        'name': {'required': True},
        'country_code': {'required': True},
        'phone_number': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        country_code: str,
        phone_number: str,
        **kwargs
    ):
        super(SmsReceiver, self).__init__(**kwargs)
        self.name = name
        self.country_code = country_code
        self.phone_number = phone_number
        self.status = None


class WebhookReceiver(msrest.serialization.Model):
    """A webhook receiver.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the webhook receiver. Names must be unique across all
     receivers within an action group.
    :type name: str
    :param service_uri: Required. The URI where webhooks should be sent.
    :type service_uri: str
    """

    _validation = {
        'name': {'required': True},
        'service_uri': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'service_uri': {'key': 'serviceUri', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        service_uri: str,
        **kwargs
    ):
        super(WebhookReceiver, self).__init__(**kwargs)
        self.name = name
        self.service_uri = service_uri
