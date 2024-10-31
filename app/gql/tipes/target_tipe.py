from graphene import ObjectType, Int, String


class TargetType(ObjectType):
    target_id = Int()
    target_industry = String()
    target_priority = String()
    target_type_id = Int()
    city_id = Int()
    mission_id = Int()
