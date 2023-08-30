from game.tilemap import TileMap
from game.display_grid import DisplayGrid
from game.enums import DevelopmentCardEnum, PortDirectionEnum, PortEnum
from game.point import Point
from game.developmentcard import DevelopmentCard
import random

class CatanBoard:
	
	sides = [] # Side()?
	players = [] # Player()!
	
	def __init__(self, border=2, scale=1, empty_icon=' '):
		self.tilemap = TileMap(border)
		self.grid = DisplayGrid(DisplayGrid.MIN_ACROSS + border*2, DisplayGrid.MIN_DOWN + border*2, scale, empty_icon)

		self.deck = []
		for _ in range(14):
			self.deck.append(DevelopmentCard(DevelopmentCardEnum.KNIGHT))
		for _ in range(5):
			self.deck.append(DevelopmentCard(DevelopmentCardEnum.VICTORYPOINT))
		for _ in range(2):
			self.deck.append(DevelopmentCard(DevelopmentCardEnum.MONOPOLY))
		for _ in range(2):
			self.deck.append(DevelopmentCard(DevelopmentCardEnum.ROADBUILDER))
		for _ in range(2):
			self.deck.append(DevelopmentCard(DevelopmentCardEnum.YEAROFPLENTY))

		random.shuffle(self.deck)

	def update_grid(self):
		for tile in self.tilemap:
			
			# self.grid.update_grid(tile.resource.value, tile.center.__copy__())
			# lower_center = tile.center.__copy__()
			# lower_center.shift(0, 1)
			# if tile.has_robber:
			# 	self.grid.update_grid('R', lower_center.__copy__())
			# else:
			# 	self.grid.update_grid(tile.dice_roll, lower_center.__copy__())
			# upper_center = tile.center.__copy__()
			# upper_center.shift(0, -1)
			# self.grid.update_grid(f'({str(tile.resource_points)})', upper_center.__copy__())

			self.grid.update_grid(str(tile.id), tile.center.__copy__())

			# for node in tile.nodes:
			# 	self.grid.update_grid(node.icon, Point(node.x, node.y))
			
		for node in self.tilemap.nodes:
			self.grid.update_grid(node.icon, Point(node.x, node.y))

		for side in self.tilemap.sides:
			for port in side.ports:
				self.grid.update_grid(port.icon, port.center)
			for point, icon in side.connections:
				self.grid.update_grid(icon, point)

		# End updating board

	def __str__(self):
		return self.grid.__str__()

