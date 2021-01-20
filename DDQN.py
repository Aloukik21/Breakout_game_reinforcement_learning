
# coding: utf-8

# In[1]:


from paddle import Breakout

import random
import numpy as np
from keras import Sequential
from collections import deque
from keras.layers import Dense
import matplotlib.pyplot as plt
from keras.optimizers import adam

env = Breakout()
np.random.seed(0)


class DDQN:

    """ Implementation of double deep q learning algorithm """

    def __init__(self, action_space, state_space):

        self.action_space = action_space
        self.state_space = state_space
        self.epsilon = 1
        self.gamma = .95
        self.batch_size = 64
        self.epsilon_min = .01
        self.epsilon_decay = .995
        self.learning_rate = 0.001
        self.memory = deque(maxlen=100000)

        self.model = self.build_model()
        self.target_model = self.build_model()                             #build target network
        
        self.target_model.set_weights(self.model.get_weights())

    def build_model(self):

        model = Sequential()
        model.add(Dense(64, input_shape=(self.state_space,), activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(self.action_space, activation='linear'))
        model.compile(loss='mse', optimizer=adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    def act(self, state):

        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_space)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])
    
    def replay(self):

        if len(self.memory) < self.batch_size:
            return

        minibatch = random.sample(self.memory, self.batch_size)
        states = np.array([i[0] for i in minibatch])
        actions = np.array([i[1] for i in minibatch])
        rewards = np.array([i[2] for i in minibatch])
        next_states = np.array([i[3] for i in minibatch])
        dones = np.array([i[4] for i in minibatch])

        states = np.squeeze(states)
        next_states = np.squeeze(next_states)

        
        target_q = self.target_model.predict_on_batch(next_states)
        q = self.model.predict_on_batch(next_states)
        next_action = np.argmax(self.model.predict(next_states), axis=1)
        
        targets_full = self.model.predict_on_batch(states)
        
        for i in range(self.batch_size):
            target = rewards[i] + self.gamma * q[i][next_action[i]] * (1-dones[i])
            targets_full[i][actions[i]] = target
        

        self.model.fit(states, targets_full, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


def train_dqn(episode):

    loss = []
    agent = DDQN(3, 5)
    count = 0
    for e in range(episode):
        state = env.reset()
        state = np.reshape(state, (1, 5))
        score = 0
        max_steps = 1000
        for i in range(max_steps):
            action = agent.act(state)
            reward, next_state, done = env.next_iteration(action)
            score += reward
            next_state = np.reshape(next_state, (1, 5))
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            agent.replay()
            count+=1
            if count != 0 and count % 20 == 0:
                agent.update_target_model()
            if done:
                print("episode: {}/{}, score: {}".format(e, episode, score))
                break
        loss.append(score)
    return loss


if __name__ == '__main__':

    ep = 100
    loss = train_dqn(ep)
    plt.plot([i for i in range(ep)], loss)
    plt.xlabel('episodes')
    plt.ylabel('reward')
    plt.show()

