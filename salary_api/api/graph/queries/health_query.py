import graphene


class HealthQuery(graphene.ObjectType):
    health = graphene.String()

    def resolve_health(self, info):  # pylint: disable=unused-argument
        return "Ok"
