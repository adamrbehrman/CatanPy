from game.point import Point
from enum import Enum

class BuildingEnum(Enum):
    EMPTY = 'X'
    ROAD = 'R'
    SETTLEMENT = 'S'
    CITY = 'C'

class NodeEnum(Enum):
    VERTEX = [ BuildingEnum.EMPTY, BuildingEnum.SETTLEMENT, BuildingEnum.CITY ]
    EDGE = [ BuildingEnum.EMPTY, BuildingEnum.ROAD ]

class ResourceEnum(Enum):
    EMPTY = 'Empty'
    WHEAT = 'Wheat'
    WOOD = 'Wood'
    SHEEP = 'Sheep'
    ORE = 'Ore'
    BRICK = 'Brick'
    DESERT = 'Desert'
    THREE_FOR_ONE = '3:1'

class DevelopmentCardEnum(Enum):
    KNIGHT = "Move the robber and take one resource from an opponent."
    ROADBUILDER = "Build 2 roads."
    VICTORYPOINT = "Grants you one victory point."
    MONOPOLY = "Get all other players' resources of one type."
    YEAROFPLENTY = "Take 2 of any resource from the bank."
    
class PortEnum(Enum):
    SQUARE = Point(-2, -3)
    TRIANGLE = Point(-4, -1)

class PortDirectionEnum(Enum):
    BOTTOM_LEFT = Point(1, 1)
    TOP_LEFT = Point(1, -1)
    BOTTOM_RIGHT = Point(-1, 1)
    TOP_RIGHT = Point(-1, -1)

class SideEnum(Enum):
    SINGLE_RESOURCE = [1]
    DOUBLE_RESOURCE = [1, 2]

class SideDirectionEnum(Enum):
    BOTTOM = [0, 1, 2]
    BOTTOM_LEFT = [7, 3, 0]
    TOP_LEFT = [16, 12, 7]
    TOP = [18, 17, 16]
    TOP_RIGHT = [11, 15, 18]
    BOTTOM_RIGHT = [2, 6, 11]