# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ActivityLogAlertActionGroup(msrest.serialization.Model):
    """A pointer to an Azure Action Group.

    All required parameters must be populated in order to send to Azure.

    :param action_group_id: Required. The resourceId of the action group. This cannot be null or
     empty.
    :type action_group_id: str
    :param webhook_properties: The dictionary of custom properties to include with the post
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
        **kwargs
    ):
        super(ActivityLogAlertActionGroup, self).__init__(**kwargs)
        self.action_group_id = kwargs.get('action_group_id', None)
        self.webhook_properties = kwargs.get('webhook_properties', None)


class ActivityLogAlertActionList(msrest.serialization.Model):
    """A list of activity log alert actions.

    :param action_groups: The list of activity log alerts.
    :type action_groups: list[~$(python-base-
     namespace).v2017_03_01_preview.models.ActivityLogAlertActionGroup]
    """

    _attribute_map = {
        'action_groups': {'key': 'actionGroups', 'type': '[ActivityLogAlertActionGroup]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ActivityLogAlertActionList, self).__init__(**kwargs)
        self.action_groups = kwargs.get('action_groups', None)


class ActivityLogAlertAllOfCondition(msrest.serialization.Model):
    """An Activity Log alert condition that is met when all its member conditions are met.

    All required parameters must be populated in order to send to Azure.

    :param all_of: Required. The list of activity log alert conditions.
    :type all_of: list[~$(python-base-
     namespace).v2017_03_01_preview.models.ActivityLogAlertLeafCondition]
    """

    _validation = {
        'all_of': {'required': True},
    }

    _attribute_map = {
        'all_of': {'key': 'allOf', 'type': '[ActivityLogAlertLeafCondition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ActivityLogAlertAllOfCondition, self).__init__(**kwargs)
        self.all_of = kwargs.get('all_of', None)


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
        **kwargs
    ):
        super(ActivityLogAlertLeafCondition, self).__init__(**kwargs)
        self.field = kwargs.get('field', None)
        self.equals = kwargs.get('equals', None)


class ActivityLogAlertList(msrest.serialization.Model):
    """A list of activity log alerts.

    :param value: The list of activity log alerts.
    :type value: list[~$(python-base-
     namespace).v2017_03_01_preview.models.ActivityLogAlertResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ActivityLogAlertResource]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ActivityLogAlertList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


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
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


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
    :type condition: ~$(python-base-
     namespace).v2017_03_01_preview.models.ActivityLogAlertAllOfCondition
    :param actions: The actions that will activate when the condition is met.
    :type actions: ~$(python-base-namespace).v2017_03_01_preview.models.ActivityLogAlertActionList
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
        **kwargs
    ):
        super(ActivityLogAlertResource, self).__init__(**kwargs)
        self.scopes = kwargs.get('scopes', None)
        self.enabled = kwargs.get('enabled', True)
        self.condition = kwargs.get('condition', None)
        self.actions = kwargs.get('actions', None)
        self.description = kwargs.get('description', None)


class ActivityLogAlertResourcePatch(Resource):
    """An activity log alert resource for patch operations.

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
    :param enabled: Indicates whether this activity log alert is enabled. If an activity log alert
     is not enabled, then none of its actions will be activated.
    :type enabled: bool
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
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ActivityLogAlertResourcePatch, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', True)


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
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
