import numpy as np 
from grid import grid

actions = {
    (0,0) : ("d", "r"),
    (0,1) : ("l", "r", "d"),
    (0,2) : ("l", "d", "r"),
    (0,3) : ("n"),
    (1,0) : ("u", "r"),
    (1,1) : ("l", "r", "u", "d"),
    (1,2) : ("l", "r", "d", "u"),
    (1,3) : ("n"),
    (2,0) : ("u", "r"),
    (2,1) : ("l", "r", "u"),
    (2,2) : ("l", "r", "u"),
    (2,3) : ("l", "u")
}

rewards = {
    (0,0) : 0,
    (0,1) : 0,
    (0,2) : 0,
    (0,3) : 1,
    (1,0) : 0,
    (1,1) : 0,
    (1,2) : 0,
    (1,3) : -1,
    (2,0) : 0,
    (2,1) : 0,
    (2,2) : 0,
    (2,3) : 0
}

def play_game():
    
    game = grid(4,3,actions, (0,0))

    # initialise random start
    idx = np.random.randint(0,10)
    start = game.all_states[idx]

    game.set_state(start)
    
    # play game
    game_over = False

    states_visited = []
    n = 0
    for i in range(1000):
        n += 1
        if game.current_state not in states_visited:
            states_visited.append(game.current_state)

        idx = np.random.randint(0,len(actions[game.current_state]))
        action =actions[game.current_state][idx]
        game.take_move(actions[game.current_state][idx])
        
        if game.current_state == (1,3):
            game_over = True
            break
            
        if game.current_state == (0,3):
            game_over = True
            break
 
    return states_visited

