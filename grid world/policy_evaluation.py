from grid import grid
import numpy as np 



def policy_eval(pi, grid, actions, rewards,gamma, epsilon):
    
    # Initial random policy
    pi = np.zeros([grid.height, grid.width])
    
    for state in grid.all_states:
        pi[state] = np.random.choice(len(actions[state]))

    # Initialise empty V
    
    V = np.zeros([grid.height, grid.width])

    n_iterations = 0
    convergence = []
    while True:

        while True:
            n_iterations += 1
            biggest_change = 0 

            for state in grid.all_states:
                grid.set_state(state)
                i,j = grid.current_state
                old_v = V[i,j]

                if state in actions:
                    v = 0
                    p_a = 1.0 / len(actions[state])
                        
                    for action in actions[state]:
                        grid.take_move(action)
                        i_prime, j_prime = grid.current_state
                        r = rewards[i_prime, j_prime]
                        v += p_a * (r + gamma * V[i_prime,j_prime])
                        grid.set_state(state)
                    V[i,j] = v
                    biggest_change = max(biggest_change, np.abs(old_v - V[i,j]))

            convergence.append(biggest_change)

            if biggest_change < epsilon:
                break
    
        for state in grid.all_states:
            old_a = pi[state]
            pi[state] = 


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

x = policy_eval(1, grid(4,3,actions, (0,0)), actions, rewards, .3, .0001)

print(x)