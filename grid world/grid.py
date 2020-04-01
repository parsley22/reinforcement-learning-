class grid:
    def __init__(self, width, height, actions, start_state):
        self.width = width
        self.height = height
        self.terminal = False
        self.actions = actions
        self.current_state = start_state
        self.i = self.current_state[0]
        self.j = self.current_state[1]

        self.all_states = [
            (0,0),
            (0,1),
            (0,2),
            (0,3),
            (1,0),
            (1,2),
            (1,3),
            (2,0),
            (2,1),
            (2,2),
            (2,3)
        ]

    def take_move(self, action):
        
        i,j = self.current_state
        if action in self.actions[self.current_state]:

            if action == "u":
                i += -1
            elif action == "d":
                i += +1
            elif action == "l":
                j += -1
            elif action == "r":
                j += 1
            elif action == "n":
                pass

            
            self.current_state = (i,j)

            if self.current_state == (1,3):
                self.terminal = True
            
            if self.current_state == (0,3):
                self.terminal == True

        else:
            pass

    def set_state(self, state):
        self.current_state = state

    def undo_move(self, action):

        if action in self.actions[self.current_state]:
            if action == "u":
                self.i += -1
            if action == "d":
                self.i += 1
            if action == "l":
                self.j += 1
            if action == "r":
                self.j += -1
                
            self.current_state = (self.i, self.j)






