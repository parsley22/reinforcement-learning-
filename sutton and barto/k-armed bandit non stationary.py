
import numpy as np 
import matplotlib.pyplot as plt

class Bandit:
    def __init__(self, K, k_bandits, n_itterations, non_stationary, epsilon,c, search_method):
        self.K = K 
        self.k_bandits = k_bandits
        self.Q = np.zeros(self.K)
        self.N = np.zeros(self.K)
        self.non_stationary = non_stationary
        self.n_itterations = n_itterations
        self.epislon = epsilon
        self.c = c
        self.search_method = search_method

        self.average_reward = []

        if self.non_stationary == True:
            self.k_bandits = np.zeros(self.K) + 10

    def epsilon_greedy(self, epsilon):
        action = np.random.choice([0,1], p = [epsilon, 1-epsilon])
        if action == 0:
            A = np.argmax(self.Q)
        if action == 1:
            A = np.random.randint(0, self.K,1)
        
        return np.int(A)

    def ucb(self, c, t):
        ucb_vec = []
        for a in range(self.K):
            ucb_vec.append(self.Q[a] + (c * np.sqrt(np.log(t) / self.N[a])))

        A = np.argmax(ucb_vec)
        return A

    def run(self):
        reward_vec = []
        for iter in range(self.n_itterations):

            """
            if self.non_stationary == True:
                for q in self.k_bandits:
                    q += np.random.normal(0,.01,1)
            """
            if self.search_method == "epsilon":
                A = self.epsilon_greedy(self.epislon)
            
            if self.search_method == "ucb":
                A = self.ucb(self.c, iter)
            
            r = self.k_bandits[A]

            reward_vec.append(r)
            self.average_reward.append(np.average(reward_vec))

            self.N[A] += 1
            self.Q[A] += (1 / self.N[A]) * (r - self.Q[A])



# epsilon_test
c = 2
k = 10
e = 0.8

# find best c
for search in ["ucb", "epsilon"]:
    b = Bandit(k, np.random.normal(0,1,k), 1_000, False, e,c = c, search_method = search)
    b.run()
    plt.plot(b.average_reward, label = "{}".format(search))
plt.legend()
plt.show()


"""
k = 10
for e in [0.3, 0.5, 0.8]:
    b = Bandit(k, np.random.normal(0,1,k), 1_000, False, e)
    b.run()
    plt.plot(b.average_reward, label = "{}".format(e))
plt.legend()
plt.title("Convergence for different epsilons")
plt.show()
"""