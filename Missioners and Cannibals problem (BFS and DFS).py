#!/usr/bin/env python
# coding: utf-8

# # Missioners and Cannibals problem

# **Question**: In the missionaries and cannibals problem, three missionaries and three cannibals must cross a river using a boat which can carry at most two people, under the constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals (if they were, the cannibals would eat the missionaries). The boat cannot cross the river by itself with no people on board.

# ## Define Movements

# In[2]:


def move1M(state): # Move 1 missioner
    if (state[0] >= 1 and state[2] == 1): 
        successor = (state[0]-1, state[1],0) 
        if ((successor[0]>0 and successor[0] < successor[1]) or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[0] <= 2 and state[2] == 0): 
        successor = (state[0]+1, state[1],1) 
        if ((successor[0]>0 and successor[0] < successor[1]) or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            return successor
        return successor

def move2M(state): # Move 2 missioners
    if (state[0] >= 2 and state[2] == 1): 
        successor = (state[0]-2, state[1],0) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[0] <= 1 and state[2] == 0 ):  
        successor = (state[0]+2, state[1],1) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

def move1C(state): # Move 1 cannibal
    if (state[1] >= 1 and state[2] == 1): 
        successor = (state[0], state[1]-1,0) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[1] <= 2 and state[2] == 0): 
        successor = (state[0], state[1]+1,1) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

def move2C(state): # Move 2 cannibals
    if (state[1] >= 2 and state[2] == 1): 
        successor = (state[0], state[1]-2,0) 
        if ((successor[0]>0 and successor[0] < successor[1])   or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[1] <= 1 and state[2] == 0): 
        successor = (state[0], state[1]+2,1) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor


def move1M1C(state): # Move 1 missioner and 1 cannibal
    if (state[0] >=1 and state[1] >=1 and state[2] == 1): 
        successor = (state[0]-1,state[1]-1,0) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor

    elif (state[0] <= 2 and state[1] <= 2 and state[2] == 0): 
        successor = (state[0]+1,state[1]+1,1) 
        if ((successor[0]>0 and successor[0] < successor[1])  or (successor[0]<3 and 3-successor[0] < (3-successor[1]))): 
            successor = None 
            return successor
        return successor


# ## FORMAT() Function

# In[3]:


def format(parent,explored,solution,move):
  if (parent!= None):
    for node in explored:
      if (node[0] == parent):
        if move==0:
          a="1M"
        if move==1:
          a="2M"
        if move==2:
          a="1C"
        if move==3:
          a="2C"
        if move==4:
          a="1M1C"
        return format(node[1],explored,str(parent)+"->"+a+"->"+str(solution),node[2])
  return solution


# # BFS
# #### Add function for BFS

# In[4]:


def addbfs(successor,frontier,explored):
  new=True
  for node in frontier:
    if node[0]==successor[0]:
      new=False
  if (new):
    for node in explored:
      if node[0]==successor[0]:
        new=False
  if (new):
    frontier.append(successor)
  return frontier


# #### BFS function

# In[5]:


def bfs(frontier,explored,goal):
    while (frontier): 
        node = frontier.pop(0) 
        explored.append(node) 
        
        fun = [move1M(node[0]), move2M(node[0]), move1C(node[0]), move2C(node[0]), move1M1C(node[0])] 
        cost= [1,1,1,1,1]
        
        for f in range(len(fun)):
          if fun[f]!= None:
            successor = (fun[f],node[0],f,node[3]+cost[f]) 
            if (goal==fun[f]): 
              print("Path:",format(node[0],explored,successor[0],successor[2])) 
              print("Total cost:",successor[3],"movements.") 
              return True    
            frontier=addbfs(successor,frontier,explored)
    return False 


# # DFS
# #### Add function for DFS

# In[6]:


def adddfs(successor,frontier,explored):
  new=True
  for node in frontier:
    if node[0]==successor[0]:
      new=False
  if (new):
    for node in explored:
      if node[0]==successor[0]:
        new=False
  if (new):
    frontier.insert(0,successor) 
  return frontier


# #### DFS function

# In[8]:


def dfs(frontier,explored,goal):
    while (frontier): #if frontier has at least one element
        node = frontier.pop(0) #extract first node from the frontier list
        explored.append(node) #add node to explored list
        fun = [move1M(node[0]), move2M(node[0]), move1C(node[0]), move2C(node[0]), move1M1C(node[0])] 
        cost=[1,1,1,1,1]
        for f in range(len(fun)):
          if fun[f]!= None:
            successor = (fun[f],node[0],f,node[3]+cost[f]) 
            if (goal==fun[f]): #If I reach the goal state, print solution and end program
              print("Path:",format(node[0],explored,successor[0],successor[2])) #Print path
              print("Total cost:",successor[3],"movements.") #Print cost
              return True    
            frontier=adddfs(successor,frontier,explored)
    return False 


# # Results for DFS & BFS

# ### BFS

# In[9]:


state =(3,3,1) #initial state
goal=(0,0,0) #goal state

frontier=[(state,"None","None",0)] #State, parent, movement, cost
explored=[]

print("BFS result is: ")
bfs(frontier, explored,goal)


# ### DFS

# In[10]:


state =(3,3,1) #initial state
goal=(0,0,0) #goal state

frontier=[(state,"None","None",0)] #State, parent, movement, cost
explored=[]

print("DFS result is: ")
dfs(frontier, explored,goal)

