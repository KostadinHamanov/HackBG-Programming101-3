class Enemy:

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

        self.max_health = health
        self.max_mana = mana

        self.weapon = None
        self.spell = None

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def can_cast(self):
        if self.spell is None:
            return False
        else:
            if self.mana - self.spell.mana_cost >= 0:
                return True

            if self.mana - self.spell.mana_cost < 0:
                return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        elif self.health + healing_points >= self.max_health:
            self.health = self.max_health
            return True
        elif self.health + healing_points < self.max_health:
            self.health += healing_points
            return True

    def take_mana(self, mana_points):
        if self.mana + mana_points >= self.max_mana:
            self.mana = self.max_mana
        elif self.mana + mana_points <= 0:
            self.mana = 0
        elif self.mana + mana_points < self.max_mana:
            self.mana += mana_points

    def take_damage(self, damage_points):
        if self.health <= damage_points:
            self.health = 0
        elif self.health > damage_points:
            self.health -= damage_points

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by=""):
        if by == "weapon":
            if self.weapon is not None:
                return self.weapon.damage
            else:
                return 0
        elif by == "spell":
            if self.spell is not None:
                return self.spell.damage
            else:
                return 0
