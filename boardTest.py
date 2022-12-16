import placementModule
import boardModule

grid_cpu = []
grid_player = []
grid_size = 15

if __name__ == "__main__":

    #boardModule.start_board(grid_player, grid_size)
    #boardModule.print_board(grid_player, grid_size)
    #placementModule.ship_placement(grid_player, "battleship", False)
    #placementModule.ship_placement(grid_player, "carrier", False)
    #placementModule.ship_placement(grid_player, "cruiser", False)
    #placementModule.ship_placement(grid_player, "destroyer", False)
    #boardModule.clear_console()
    #boardModule.print_board_open(grid_player, grid_size)

    # cpu grid placement test
    boardModule.start_board(grid_cpu, grid_size)
    boardModule.print_board(grid_cpu, grid_size)
    placementModule.ship_placement(grid_cpu, "battleship", True)
    placementModule.ship_placement(grid_cpu, "carrier", True)
    placementModule.ship_placement(grid_cpu, "cruiser", True)
    placementModule.ship_placement(grid_cpu, "destroyer", True)
    boardModule.clear_console()
    boardModule.print_board_open(grid_cpu, grid_size)
    print(placementModule.ships_memory)
    print(grid_cpu[placementModule.ships_memory[0][1][0]][placementModule.ships_memory[0][1][1]])