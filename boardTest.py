import placementModule
import boardModule

grid_cpu = []
grid_player = []
grid_size = 10

if __name__ == "__main__":

    # boardModule.start_board(grid_player, grid_size)
    # boardModule.print_board(grid_player, grid_size)
    # placementModule.shipPlacement(grid_player, "battleship", grid_size, False)
    # placementModule.shipPlacement(grid_player, "carrier", grid_size, False)
    # placementModule.shipPlacement(grid_player, "cruiser", grid_size, False)
    # placementModule.shipPlacement(grid_player, "destroyer", grid_size, False)
    # boardModule.clearConsole()
    # boardModule.print_board(grid_player, grid_size)

    # cpu grid placement test
    boardModule.start_board(grid_cpu, grid_size)
    boardModule.print_board(grid_cpu, grid_size)
    placementModule.shipPlacement(grid_cpu, "battleship", grid_size, True)
    placementModule.shipPlacement(grid_cpu, "carrier", grid_size, True)
    placementModule.shipPlacement(grid_cpu, "cruiser", grid_size, True)
    placementModule.shipPlacement(grid_cpu, "destroyer", grid_size, True)
    boardModule.clearConsole()
    boardModule.print_board_open(grid_cpu, grid_size)