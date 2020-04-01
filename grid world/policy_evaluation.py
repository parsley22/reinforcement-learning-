from grid import grid
import numpy as np 

def policy_eval(pi, grid, actions, rewards,gamma, epsilon):
    n_states = (grid.height * grid.width) - 1

    V = np.zeros([grid.height, grid.width])

    for iter in range(10):
        for state in grid.all_states:
            grid.set_state(state)
            i,j = grid.current_state
            for action in actions[state]:
                grid.take_move(action)
                r = rewards[grid.current_state]
                i_prime, j_prime = grid.current_state

                # Uniform
                V[i,j] += 1/(len(actions[state])) * (r + (gamma * V[i_prime, j_prime]))
                grid.set_state((i,j))
    
    return V
        

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

x = policy_eval(1, grid(4,3,actions, (0,0)), actions, rewards, .3, .3)

print(x)