import placementModule
import boardModule

grid_cpu = []
grid_player = []
grid_size = 10

if __name__ == "__main__":
    boardModule.start_board(grid_player, grid_size)
    boardModule.print_board(grid_player, grid_size)
    placementModule.shipPlacement(grid_player, "battleship", False)
    placementModule.shipPlacement(grid_player, "carrier", False)
    placementModule.shipPlacement(grid_player, "cruiser", False)
    placementModule.shipPlacement(grid_player, "destroyer", False)
    boardModule.clearConsole()
    boardModule.print_board(grid_player, grid_size)