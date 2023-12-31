from game.enums import ResourceEnum, BuildingEnum, GrowthCardEnum

class Purchaseables():

	def __init__(self, name:str, cost:[ResourceEnum]):
		self.name = name
		self.cost = cost


class Building(Purchaseables):

    def __init__(self, type:BuildingEnum, player_id:int = -1):
        self.type = type
        self.player_id = player_id
        self.icon = self.type.value + str(self.player_id)
        name = self.type.name.title().replace('_', ' ')
        match type:
            case BuildingEnum.ROAD:
                self.victory_points = 0
                super().__init__(name, [ ResourceEnum.BRICK, ResourceEnum.WOOD ])
            case BuildingEnum.OUTPOST:
                self.victory_points = 1
                super().__init__(name, [ ResourceEnum.WHEAT, ResourceEnum.SHEEP, ResourceEnum.BRICK, ResourceEnum.WOOD ])
            case BuildingEnum.TOWN:
                self.victory_points = 2
                super().__init__(name, [ ResourceEnum.WHEAT, ResourceEnum.WHEAT, ResourceEnum.ORE, ResourceEnum.ORE, ResourceEnum.ORE ])

    def __str__(self):
        return str(self.player_id) if self.type == BuildingEnum.ROAD else self.icon + str(self.player_id)

class GrowthCard(Purchaseables):
        
    def __init__(self, type:GrowthCardEnum):
        self.type = type
        self.cost = [ ResourceEnum.WHEAT, ResourceEnum.SHEEP, ResourceEnum.ORE ]
        super().__init__(self.type.name.title().replace('_', ' '), self.cost)

    def __str__(self):
        return f'{self.name}: {self.type.value}'
    