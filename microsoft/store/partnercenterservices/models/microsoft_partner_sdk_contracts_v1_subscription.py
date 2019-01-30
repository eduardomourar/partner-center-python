# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftPartnerSdkContractsV1Subscription(Model):
    """The subscription resource represents the life cycle of a subscription and
    includes properties that define the states throughout the subscription life
    cycle.
    A subscription lets a customer use a service for a certain period of time.
    Not all fields will apply to all subscriptions,
    and many only apply at certain points in the life cycle, such as if a
    subscription is suspended or cancelled.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Gets or sets the subscription identifier.
    :type id: str
    :param offer_id: Gets or sets the offer identifier.
    :type offer_id: str
    :param entitlement_id: Gets or sets the entitlement (azure's subscription)
     identifier.
    :type entitlement_id: str
    :param offer_name: Gets or sets the offer name.
    :type offer_name: str
    :param friendly_name: Gets or sets the friendly name for the subscription.
     The friendly name is defined by the partner to help disambiguate the
     subscription.
    :type friendly_name: str
    :param quantity: The quantity. A Read-only property defined by the unit
     type.
     For example, in the case of license-based billing, this property is set to
     the license count.
     For usage based subscriptions, this property is ignored (set to 0).
    :type quantity: int
    :param unit_type: Gets or sets the type of units that define the quantity
     for the subscription.
    :type unit_type: str
    :param parent_subscription_id: Gets or sets the parent subscription
     identifier.
    :type parent_subscription_id: str
    :param has_purchasable_addons: Gets or sets a value indicating whether the
     subscription has purchasable addons.
    :type has_purchasable_addons: bool
    :param creation_date: Gets or sets the creation date.
    :type creation_date: datetime
    :param effective_start_date: Gets or sets the effective start date for
     this subscription, in date-time format.
     The effective start date is used to back date a migrated subscription or
     to align it with another.
    :type effective_start_date: datetime
    :param commitment_end_date: Gets or sets the commitment end date for this
     subscription, in date-time format.
     For subscription which are not auto renewable, this represents a date far
     away in the future.
    :type commitment_end_date: datetime
    :param status: Gets or sets the subscription status. Possible values
     include: 'none', 'active', 'suspended', 'deleted'
    :type status: str or ~azure.partnercenterservices.models.enum
    :param auto_renew_enabled: Gets or sets a value indicating whether the
     subscription is renewed automatically.
    :type auto_renew_enabled: bool
    :param is_trial: Gets or sets a value indicating whether the subscription
     is a trial one.
    :type is_trial: bool
    :param billing_type: Gets or sets a value indicating how the subscription
     is billed. For example, "usage" or "license".
     Revisit this property - do we need this having UnitType. Possible values
     include: 'none', 'usage', 'license'
    :type billing_type: str or ~azure.partnercenterservices.models.enum
    :param billing_cycle: Gets or sets a value indicating the frequency with
     which the partner is billed for this subscription.
     The default value is monthly. Possible values include: 'unknown',
     'monthly', 'annual', 'none', 'one_time'
    :type billing_cycle: str or ~azure.partnercenterservices.models.enum
    :param actions: Gets or sets the actions.
    :type actions: list[str]
    :param partner_id: Gets or sets the MPN ID of the reseller of record, used
     in the indirect partner model.
    :type partner_id: str
    :param suspension_reasons: Read-only. If the subscription was suspended,
     this property gets a value indicating why.
    :type suspension_reasons: list[str]
    :param attention_needed: Gets or sets a value indicating if attention is
     needed for this subscription.
    :type attention_needed: bool
    :param attention_reason: Gets or sets the reason why attention is
     required.
    :type attention_reason: str
    :param action_taken: Gets or sets a value indicating if action is already
     taken on the subscription.
    :type action_taken: bool
    :ivar contract_type: Read-only. Gets the type of the contract. For
     example, "subscription". Possible values include: 'subscription',
     'product_key', 'redemption_code'
    :vartype contract_type: str or ~azure.partnercenterservices.models.enum
    :param links: Gets or sets the subscription links.
    :type links:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1ContractsLinksSubscriptionLinks
    :param order_id: The order identifier.
    :type order_id: str
    :ivar attributes: Gets the attributes.
    :vartype attributes:
     ~azure.partnercenterservices.models.MicrosoftPartnerSdkContractsV1CommonResourceAttributes
    """

    _validation = {
        'contract_type': {'readonly': True},
        'attributes': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
        'entitlement_id': {'key': 'entitlementId', 'type': 'str'},
        'offer_name': {'key': 'offerName', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'int'},
        'unit_type': {'key': 'unitType', 'type': 'str'},
        'parent_subscription_id': {'key': 'parentSubscriptionId', 'type': 'str'},
        'has_purchasable_addons': {'key': 'hasPurchasableAddons', 'type': 'bool'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'effective_start_date': {'key': 'effectiveStartDate', 'type': 'iso-8601'},
        'commitment_end_date': {'key': 'commitmentEndDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'auto_renew_enabled': {'key': 'autoRenewEnabled', 'type': 'bool'},
        'is_trial': {'key': 'isTrial', 'type': 'bool'},
        'billing_type': {'key': 'billingType', 'type': 'str'},
        'billing_cycle': {'key': 'billingCycle', 'type': 'str'},
        'actions': {'key': 'actions', 'type': '[str]'},
        'partner_id': {'key': 'partnerId', 'type': 'str'},
        'suspension_reasons': {'key': 'suspensionReasons', 'type': '[str]'},
        'attention_needed': {'key': 'attentionNeeded', 'type': 'bool'},
        'attention_reason': {'key': 'attentionReason', 'type': 'str'},
        'action_taken': {'key': 'actionTaken', 'type': 'bool'},
        'contract_type': {'key': 'contractType', 'type': 'str'},
        'links': {'key': 'links', 'type': 'MicrosoftPartnerSdkContractsV1ContractsLinksSubscriptionLinks'},
        'order_id': {'key': 'orderId', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'MicrosoftPartnerSdkContractsV1CommonResourceAttributes'},
    }

    def __init__(self, id=None, offer_id=None, entitlement_id=None, offer_name=None, friendly_name=None, quantity=None, unit_type=None, parent_subscription_id=None, has_purchasable_addons=None, creation_date=None, effective_start_date=None, commitment_end_date=None, status=None, auto_renew_enabled=None, is_trial=None, billing_type=None, billing_cycle=None, actions=None, partner_id=None, suspension_reasons=None, attention_needed=None, attention_reason=None, action_taken=None, links=None, order_id=None):
        super(MicrosoftPartnerSdkContractsV1Subscription, self).__init__()
        self.id = id
        self.offer_id = offer_id
        self.entitlement_id = entitlement_id
        self.offer_name = offer_name
        self.friendly_name = friendly_name
        self.quantity = quantity
        self.unit_type = unit_type
        self.parent_subscription_id = parent_subscription_id
        self.has_purchasable_addons = has_purchasable_addons
        self.creation_date = creation_date
        self.effective_start_date = effective_start_date
        self.commitment_end_date = commitment_end_date
        self.status = status
        self.auto_renew_enabled = auto_renew_enabled
        self.is_trial = is_trial
        self.billing_type = billing_type
        self.billing_cycle = billing_cycle
        self.actions = actions
        self.partner_id = partner_id
        self.suspension_reasons = suspension_reasons
        self.attention_needed = attention_needed
        self.attention_reason = attention_reason
        self.action_taken = action_taken
        self.contract_type = None
        self.links = links
        self.order_id = order_id
        self.attributes = None