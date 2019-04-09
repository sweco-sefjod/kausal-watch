import graphene
from graphene_django import DjangoObjectType
import graphene_django_optimizer as gql_optimizer

from actions.models import (
    Plan, Action, ActionSchedule, ActionStatus, Category, CategoryType,
    ActionTask
)
from indicators.models import (
    Indicator, RelatedIndicator, ActionIndicator, IndicatorGraph, IndicatorLevel
)
from people.models import Person
from django_orghierarchy.models import Organization


class WithImageMixin:
    image_url = graphene.String()

    def resolve_image_url(self, info, **kwargs):
        return self.get_image_url(info.context)


class PersonNode(DjangoObjectType):
    avatar_url = graphene.String()

    class Meta:
        model = Person
        only_fields = [
            'id', 'first_name', 'last_name', 'avatar_url',
        ]

    def resolve_avatar_url(self, info):
        return self.get_avatar_url()


class PlanNode(DjangoObjectType, WithImageMixin):
    id = graphene.ID(source='identifier')
    last_action_identifier = graphene.ID()

    class Meta:
        model = Plan
        only_fields = [
            'id', 'name', 'identifier', 'image_url', 'action_schedules',
            'actions', 'category_types', 'action_statuses', 'indicator_levels',
            'indicators',
        ]


class ActionScheduleNode(DjangoObjectType):
    class Meta:
        model = ActionSchedule


class ActionStatusNode(DjangoObjectType):
    class Meta:
        model = ActionStatus


class CategoryTypeNode(DjangoObjectType):
    class Meta:
        model = CategoryType


class CategoryNode(DjangoObjectType, WithImageMixin):
    class Meta:
        model = Category


class ActionTaskNode(DjangoObjectType):
    class Meta:
        model = ActionTask


class ActionNode(DjangoObjectType, WithImageMixin):
    next_action = graphene.Field('aplans.schema.ActionNode')
    previous_action = graphene.Field('aplans.schema.ActionNode')

    class Meta:
        model = Action
        only_fields = [
            'id', 'plan', 'name', 'official_name', 'identifier', 'description', 'status',
            'completion', 'schedule', 'decision_level', 'responsible_parties',
            'categories', 'indicators', 'contact_persons', 'updated_at', 'tasks',
            'related_indicators',
        ]

    def resolve_next_action(self, info):
        return self.get_next_action()

    def resolve_previous_action(self, info):
        return self.get_previous_action()


class RelatedIndicatorNode(DjangoObjectType):
    class Meta:
        model = RelatedIndicator


class ActionIndicatorNode(DjangoObjectType):
    class Meta:
        model = ActionIndicator


class IndicatorGraphNode(DjangoObjectType):
    class Meta:
        model = IndicatorGraph


class IndicatorLevelNode(DjangoObjectType):
    class Meta:
        model = IndicatorLevel


class IndicatorNode(DjangoObjectType):
    class Meta:
        model = Indicator


class OrganizationNode(DjangoObjectType):
    class Meta:
        model = Organization


class Query(graphene.ObjectType):
    plan = gql_optimizer.field(graphene.Field(PlanNode, id=graphene.ID(required=True)))
    all_plans = graphene.List(PlanNode)

    action = graphene.Field(ActionNode, id=graphene.ID(), identifier=graphene.ID(), plan=graphene.ID())
    plan_actions = graphene.List(ActionNode, plan=graphene.ID(required=True))
    plan_categories = graphene.List(CategoryNode, plan=graphene.ID(required=True))
    plan_organizations = graphene.List(OrganizationNode, plan=graphene.ID(required=True))
    plan_indicators = graphene.List(IndicatorNode, plan=graphene.ID(required=True))

    def resolve_plan(self, info, **kwargs):
        qs = Plan.objects.all()
        return gql_optimizer.query(qs, info).get(identifier=kwargs['id'])

    def resolve_all_plans(self, info):
        return Plan.objects.all()

    def resolve_plan_actions(self, info, **kwargs):
        qs = Action.objects.all()
        plan = kwargs.get('plan')
        if plan is not None:
            qs = qs.filter(plan__identifier=plan)
        return gql_optimizer.query(qs, info)

    def resolve_plan_categories(self, info, **kwargs):
        qs = Category.objects.all()
        plan = kwargs.get('plan')
        if plan is not None:
            qs = qs.filter(type__plan__identifier=plan)
        return gql_optimizer.query(qs, info)

    def resolve_plan_organizations(self, info, **kwargs):
        qs = Organization.objects.all()
        plan = kwargs.get('plan')
        if plan is not None:
            qs = qs.filter(responsible_actions__plan__identifier=plan).distinct()
        return gql_optimizer.query(qs, info)

    def resolve_plan_indicators(self, info, **kwargs):
        qs = Indicator.objects.all()
        plan = kwargs.get('plan')
        if plan is not None:
            qs = qs.filter(levels__plan__identifier=plan).distinct()
        return gql_optimizer.query(qs, info)

    def resolve_action(self, info, **kwargs):
        obj_id = kwargs.get('id')
        identifier = kwargs.get('identifier')
        plan = kwargs.get('plan')
        if identifier and not plan:
            raise Exception("You must supply the 'plan' argument when using 'identifier'")
        qs = Action.objects.all()
        if obj_id:
            qs = qs.filter(id=obj_id)
        if identifier:
            qs = qs.filter(identifier=identifier, plan__identifier=plan)

        qs = gql_optimizer.query(qs, info)

        try:
            obj = qs.get()
        except Action.DoesNotExist:
            return None

        return obj


schema = graphene.Schema(query=Query)