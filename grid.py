class grid:
    def __init__(self, width, height, actions, start_state):
        self.width = width
        self.height = height
        self.terminal = False
        self.actions = actions
        self.current_state = start_state
        self.i = self.current_state[0]
        self.j = self.current_state[1]

    def update_state(self, action):

        if action in self.actions[self.current_state]:
            if action == "u":
                self.i += 1
            if action == "d":
                self.i -= 1
            if action == "l":
                self.j -= 1
            if action == "r":
                self.j += 1

            self.current_state = (self.i, self.j)

            if self.current_state == (2,3):
                self.terminal = True
    
actions = {
    (0,0) : ("u", "r"),
    (0,1) : ("l", "r"),
    (0,2) : ("l", "r", "u"),
    (0,3) : ("l", "u"),
    (1,0) : ("u", "d"),
    (1,1) : (),
    (1,2) : ("u", "d", "r"),
    (1,3) : ("u", "d", "l"),
    (2,0) : ("d", "r"),
    (2,1) : ("l", "r"),
    (2,2) : ("l", "r", "d"),
    (2,3) : ("l", "d")
}

rewards = {
    (1,3) : -1,
    (2,3) : +1
}

grid = grid(4,3,actions,(0,0))

grid.update_state("r")
print(grid.current_state)
grid.update_state("r")
print(grid.current_state)
grid.update_state("r")
print(grid.current_state)
grid.update_state("u")
grid.update_state("u")
print(grid.current_state)
print(grid.terminal)


