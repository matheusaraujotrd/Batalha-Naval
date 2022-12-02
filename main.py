import placementModule
import boardModule

grid_cpu = []
grid_player = []
grid_size = 50

if __name__ == "__main__":
    boardModule.start_board(grid_player, grid_size)
    boardModule.print_board(grid_player, grid_size)
    placementModule.shipPlacement(grid_player, "battleship", grid_size, False)
    placementModule.shipPlacement(grid_player, "carrier", grid_size, False)
    placementModule.shipPlacement(grid_player, "cruiser", grid_size, False)
    placementModule.shipPlacement(grid_player, "destroyer", grid_size, False)
    boardModule.clearConsole()
    boardModule.print_board(grid_player, grid_size)
