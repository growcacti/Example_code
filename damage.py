def enum(*sequential, **named):
    enums = dict(list(zip(sequential, list(range(len(sequential))))), **named)
    return type("Enum", (), enums)


DamageType = enum("BULLET", "FIRE", "MISSILE")


class Damage:
    def __init__(self, amount, damage_type):
        self.amount = amount
        self.type = damage_type
