import boardModule
import placementModule

# global variables
grid_cpu = []
grid_size = 0
DIFFICULTY = {"easy": 5, "normal": 10, "hard": 15}
# CPU grid
def cpu_grid_start (game_difficulty: str):
    grid_size = DIFFICULTY[game_difficulty]
    
    # initializing grid
    boardModule.start_board(grid_cpu, grid_size)
    boardModule.print_board(grid_cpu, grid_size)       
    
    if game_difficulty == "easy":
        placementModule.ship_placement(grid_cpu, "battleship", True)
        placementModule.ship_placement(grid_cpu, "cruiser", True)
        placementModule.ship_placement(grid_cpu, "destroyer", True)
        placementModule.ship_placement(grid_cpu, "destroyer", True)


    elif game_difficulty == "normal":
        placementModule.ship_placement(grid_cpu, "carrier", True)
        placementModule.ship_placement(grid_cpu, "battleship", True)
        placementModule.ship_placement(grid_cpu, "cruiser", True)
        placementModule.ship_placement(grid_cpu, "cruiser", True)
        placementModule.ship_placement(grid_cpu, "destroyer", True)
        placementModule.ship_placement(grid_cpu, "destroyer", True)


    elif game_difficulty == "hard":
        placementModule.ship_placement(grid_cpu, "carrier", True)
        placementModule.ship_placement(grid_cpu, "battleship", True)
        placementModule.ship_placement(grid_cpu, "cruiser", True)
        placementModule.ship_placement(grid_cpu, "cruiser", True)
        placementModule.ship_placement(grid_cpu, "cruiser", True)
        placementModule.ship_placement(grid_cpu, "destroyer", True)
        placementModule.ship_placement(grid_cpu, "destroyer", True)
        placementModule.ship_placement(grid_cpu, "destroyer", True)

if __name__ == "__main__":
    cpu_grid_start("hard")
    boardModule.clear_console()
    boardModule.print_board_open(grid_cpu, grid_size)