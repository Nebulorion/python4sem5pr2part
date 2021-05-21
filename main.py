import random

class StateNodes():
  DEFAULT_START_STATE = dict(
    player='alice',
    alice_room='west room',
    bob_room='east room',
    red_key='east room',
    blue_key='west room',
    green_key='east room'
  )
  keyNodeList = [] #List of Nodes (else dictonary key is unhashable)
  START_STATE = None #Default, custome, random
  #dictNodes = [] #
  graph = {} #Output grash
  greenEndsList = [] #Best finish
  endsList = [] #all ends
  minEndInt = None #Best finish (count of states)

  def makeStartState0(self): #Default start state
    self.START_STATE = self.DEFAULT_START_STATE

  def makeStartState1(self, START_STATE): #Custome start state
    self.START_STATE = START_STATE

  def makeStartState2(self): #Random start state
    self.START_STATE = self.makeRandomStartState()

  def makeRandomStartState(self): #creating fields of random start state
    START_STATE = dict(
    player=random.choice(["alice", "bob"]),
    alice_room=random.choice(["west room", "east room"]),
    bob_room=random.choice(["west room", "east room"]),
    red_key=random.choice(["west room", "east room"]),
    blue_key=random.choice(["west room", "east room"]),
    green_key=random.choice(["west room", "east room"])
    )
    if ( ( START_STATE.get("alice_room") == START_STATE.get('bob_room') ) and ( START_STATE.get('green_key') != START_STATE.get('bob_room') ) ):
      return(self.makeRandomStartState()) #repeat if start state is imposible 
    else:
      return(START_STATE)

  def getStartState(self): #Get current start state
    return self.START_STATE

  def getDefaultStartState(self): #Get default start state
    return self.DEFAULT_START_STATE

  def inputStartState(self, input_int): #Start program
    if( input_int  == 0 ):
      self.makeStartState0()
    elif( input_int == 1 ):
      print('1Write "alice" or "bob"')
      print(' player = ')
      player=input()
      print('1Write "west room" or "east room"')
      print(' alice_room = ')
      alice_room=input()
      print('1Write "west room" or "east room"')
      print(' bob_room = ')
      bob_room=input()
      print('1Write "west room" or "east room"')
      print(' red_key = ')
      red_key=input()
      print('1Write "west room" or "east room"')
      print(' blue_key = ')
      blue_key=input()
      print('1Write "west room" or "east room"')
      print(' green_key = ')
      green_key=input()
      START_STATE = dict(
        player,
        alice_room,
        bob_room,
        red_key,
        blue_key,
        green_key
      ) 
      self.makeStartState1(START_STATE)
    elif( input_int == 2 ):
      self.makeStartState2()

  def getIndexNode(self, currentNode): #Get index of state for creating dictionary graph from list
    for indexNode, itemNode in enumerate(self.keyNodeList):
      if( currentNode == itemNode ):
        return(indexNode)
  
  def getItemNode(self, indexInt): #Get state from list
    return(self.keyNodeList[indexInt])
  
  def setItemGetIndNode(self, itemNode): #Set state in list and get his index
    if itemNode not in self.keyNodeList:
      self.keyNodeList.append(itemNode)
    return(self.getIndexNode(itemNode))

  def getNodePermissionList(self, currentNode): #Creating list of Permissions for current state
    nodePermissionList= []
    nodePermissionList.append('permSwitchActor')
    if( ( currentNode['alice_room'] == 'red room' ) and ( currentNode['bob_room'] == 'blue room' ) ):
      nodePermissionList.append('permFinish')
    else:
      #ALICE GET KEY
      if( currentNode['player'] == 'alice' ):
        if( currentNode['alice_room'] == currentNode['red_key'] ):
          nodePermissionList.append('permGetRedKey')
        if( currentNode['alice_room'] == currentNode['blue_key'] ):
          nodePermissionList.append('permGetBlueKey')
        if( currentNode['alice_room'] == currentNode['green_key'] ):
          nodePermissionList.append('permGetGreenKey')
        #Go To Red Room
        if( ( currentNode['red_key'] == 'alice' and currentNode['alice_room'] == 'west room' and currentNode['blue_key'] != 'alice' ) and ( not ( 
          currentNode['blue_key'] == 'west room' and currentNode['bob_room'] == 'east room' and ( currentNode['green_key'] == 'west room' or currentNode['green_key'] == 'alice') ) ) and ( not ( 
            currentNode['bob_room'] == 'west room' and currentNode['green_key'] == 'alice'
        ))):
          nodePermissionList.append('permGoToRedRoom')
        #Go To West and East Rooms
        if( currentNode['alice_room'] == 'east room' and currentNode['green_key'] == 'alice' ):
          nodePermissionList.append('permGoToWestRoom')
        if( currentNode['alice_room'] == 'west room' and currentNode['green_key'] == 'alice' ):
          nodePermissionList.append('permGoToEastRoom')
      #BOB GET KEY
      if( currentNode['player'] == 'bob'):
        if( currentNode['bob_room'] == currentNode['red_key'] ):
          nodePermissionList.append('permGetRedKey')
        if( currentNode['bob_room'] == currentNode['blue_key'] ):
          nodePermissionList.append('permGetBlueKey')
        if( currentNode['bob_room'] == currentNode['green_key'] ):
          nodePermissionList.append('permGetGreenKey')
        #Go To Blue Room
        if( ( currentNode['blue_key'] == 'bob' and currentNode['bob_room'] == 'east room' and currentNode['red_key'] != 'bob' ) and ( not ( 
          currentNode['red_key'] == 'east room' and currentNode['alice_room'] == 'west room' and ( currentNode['green_key'] == 'east room' or currentNode['green_key'] == 'bob') ) ) and ( not ( 
            currentNode['alice_room'] == 'east room' and currentNode['green_key'] == 'bob'
        ))):
          nodePermissionList.append('permGoToBlueRoom')
        #Go To West and East Rooms
        if( currentNode['bob_room'] == 'east room' and currentNode['green_key'] == 'bob' ):
          nodePermissionList.append('permGoToWestRoom')
        if( currentNode['bob_room'] == 'west room' and currentNode['green_key'] == 'bob' ):
          nodePermissionList.append('permGoToEastRoom')
      #PLAYER GIVE KEY
      if( currentNode['alice_room'] == currentNode['bob_room'] ):
        if( currentNode['player'] == currentNode['red_key'] ):
          nodePermissionList.append('permGiveRedKey')
        if( currentNode['player'] == currentNode['blue_key'] ):
          nodePermissionList.append('permGiveBlueKey')
        if( currentNode['player'] == currentNode['green_key'] ):
          nodePermissionList.append('permGiveGreenKey')
    return(nodePermissionList)
        #if( currentNode[player] == 'bob' and )

  def is_goal_state(self, x): #if best finish
    if x in self.greenEndsList:
      return(True)
    else:
      return(False)

  def find_dead_ends(self): #find not best finish list
    dead_ends = []
    for i in self.endsList:
      if( not ( self.is_goal_state(i) ) ):
        dead_ends.append(i)
    return(dead_ends)

  def go(self, currentNode, step): #find next states by permissions of current state
    currentNodeListData = []
    nodePermissionList= self.getNodePermissionList(currentNode)
    #----otherPlayer----
    if( currentNode['player'] == 'alice'):
      otherPlayer='bob'
    elif( currentNode['player'] == 'bob'):
      otherPlayer='alice'
    #--------PERMISSION-----------------------------------------------+
    if( 'permGoToRedRoom' in nodePermissionList ):
      nextNode = dict(
        player=currentNode['player'],
        alice_room='red room',
        bob_room=currentNode['bob_room'],
        red_key=currentNode['red_key'],
        blue_key=currentNode['blue_key'],
        green_key=currentNode['green_key']
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGoToBlueRoom' in nodePermissionList ):
      nextNode = dict(
        player=currentNode['player'],
        alice_room=currentNode['alice_room'],
        bob_room='blue room',
        red_key=currentNode['red_key'],
        blue_key=currentNode['blue_key'],
        green_key=currentNode['green_key']
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGoToWestRoom' in nodePermissionList ):
      if( currentNode['player'] == 'alice' ):
        nextNode = dict(
          player=currentNode['player'],
          alice_room='west room',
          bob_room=currentNode['bob_room'],
          red_key=currentNode['red_key'],
          blue_key=currentNode['blue_key'],
          green_key=currentNode['green_key']
        )
      elif( currentNode['player'] == 'bob' ):
        nextNode = dict(
          player=currentNode['player'],
          alice_room=currentNode['alice_room'],
          bob_room='west room',
          red_key=currentNode['red_key'],
          blue_key=currentNode['blue_key'],
          green_key=currentNode['green_key']
        )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGoToEastRoom' in nodePermissionList ):
      if( currentNode['player'] == 'alice' ):
        nextNode = dict(
          player=currentNode['player'],
          alice_room='east room',
          bob_room=currentNode['bob_room'],
          red_key=currentNode['red_key'],
          blue_key=currentNode['blue_key'],
          green_key=currentNode['green_key']
        )
      elif( currentNode['player'] == 'bob' ):
        nextNode = dict(
          player=currentNode['player'],
          alice_room=currentNode['alice_room'],
          bob_room='east room',
          red_key=currentNode['red_key'],
          blue_key=currentNode['blue_key'],
          green_key=currentNode['green_key']
        )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permSwitchActor' in nodePermissionList ):
      nextNode = dict(
        player=otherPlayer,
        alice_room=currentNode['alice_room'],
        bob_room=currentNode['bob_room'],
        red_key=currentNode['red_key'],
        blue_key=currentNode['blue_key'],
        green_key=currentNode['green_key']
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGiveRedKey' in nodePermissionList ):
      nextNode = dict(
        player=currentNode['player'],
        alice_room=currentNode['alice_room'],
        bob_room=currentNode['bob_room'],
        red_key=otherPlayer,
        blue_key=currentNode['blue_key'],
        green_key=currentNode['green_key']
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGiveBlueKey' in nodePermissionList ):
      nextNode = dict(
        player=currentNode['player'],
        alice_room=currentNode['alice_room'],
        bob_room=currentNode['bob_room'],
        red_key=currentNode['red_key'],
        blue_key=otherPlayer,
        green_key=currentNode['green_key']
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGiveGreenKey' in nodePermissionList ):
      nextNode = dict(
        player=currentNode['player'],
        alice_room=currentNode['alice_room'],
        bob_room=currentNode['bob_room'],
        red_key=currentNode['red_key'],
        blue_key=currentNode['blue_key'],
        green_key=otherPlayer
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGetRedKey' in nodePermissionList ):
      nextNode = dict(
        player=currentNode['player'],
        alice_room=currentNode['alice_room'],
        bob_room=currentNode['bob_room'],
        red_key=currentNode['player'],
        blue_key=currentNode['blue_key'],
        green_key=currentNode['green_key']
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGetBlueKey' in nodePermissionList ):
      nextNode = dict(
        player=currentNode['player'],
        alice_room=currentNode['alice_room'],
        bob_room=currentNode['bob_room'],
        red_key=currentNode['red_key'],
        blue_key=currentNode['player'],
        green_key=currentNode['green_key']
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permGetGreenKey' in nodePermissionList ):
      nextNode = dict(
        player=currentNode['player'],
        alice_room=currentNode['alice_room'],
        bob_room=currentNode['bob_room'],
        red_key=currentNode['red_key'],
        blue_key=currentNode['blue_key'],
        green_key=currentNode['player']
      )
      nextStep = step + 1
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      currentNodeListData[0].append(nextNode)
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      if( not ( self.getIndexNode(nextNode) in self.dictNodes ) ):
        self.dictNodes.update({self.setItemGetIndNode(nextNode):[[], nextStep]})
        self.go(nextNode, nextStep)
    #--------PERMISSION-----------------------------------------------+
    if( 'permFinish' in nodePermissionList ):
      if( self.minEndInt == None ):
        self.minEndInt = step
      elif( self.minEndInt > step ):
        self.minEndInt = step
      if( not ( currentNode in self.endsList ) ):
        self.endsList.append(currentNode)
      
        #self.go(nextNode, nextStep) #FINISH
  def findMinStep(self, currentNode, step): #find count of states of best finish
    currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
    if( ( currentNode in self.endsList ) and ( self.minEndInt > step )):
      self.minEndInt= step
    if( currentNodeListData[1] >= step ):
      currentNodeListData= [currentNodeListData[0], step]
      self.dictNodes.update({self.getIndexNode(currentNode):currentNodeListData})
      for nextNode in currentNodeListData[0]:
        nextStep= step + 1
        self.findMinStep(nextNode, nextStep)
    
  def findGreenEndsList(self):
    for currentNode in self.endsList:
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      if( ( currentNodeListData[1] == self.minEndInt ) and ( not ( currentNode in self.greenEndsList ) ) ):
        self.greenEndsList.append(currentNode)
  
  def createGraph(self): #creating dictionary graph from list of states
    #graph = {}
    for currentIndexNode in self.dictNodes:
      #print(graph)
      currentNode= self.getItemNode(currentIndexNode)
      currentNodeListData = self.dictNodes[self.getIndexNode(currentNode)]
      self.graph.update({self.getIndexNode(currentNode):currentNodeListData[0]})

  def make_model(self): #creating tree by steps
    self.dictNodes = {}
    self.setItemGetIndNode(self.getStartState())
    self.dictNodes.update({self.getIndexNode(self.getStartState()):[[], 0]})
    self.go(self.START_STATE, 0)
    self.findMinStep(self.START_STATE, 0)
    self.findGreenEndsList()
    print("List with min steps:")
    for node in self.greenEndsList:
      print("-Min finish State-Node with " + str(self.minEndInt) +" steps")
      for i in node:
        print ("  " + str(i) +" = '"+ str(node[i]) +"'")
    self.createGraph()
    #print(self.graph)

  def make_gv(self): #creating tree and print graph
    self.make_model()
    self.print_dot(self.graph, self.START_STATE)

  def print_dot(self, graph, start_key): #graph - dictNodesList, start_key - START_KEY  
  # ! """The Teeny Tiny Mansion (TTTM) is a mockup text adventure game that is formally !
  # !    proven to have no "dead ends". I.e. all player actions will result in a state  !
  # !    in which the game is still winnable."""                                        !
  # ! So dead_ends is not better points, because this game can't be with dead points    !
    dead_ends = self.find_dead_ends() #other Final Points- not dead Points
    #print(dead_ends)
    print('digraph {')
    graph_keys = list(graph.keys())
    for x in graph:
        n = graph_keys.index(x)
        if self.getItemNode(x) == start_key:
            print(f'n{n} [style="filled",fillcolor="dodgerblue",shape="circle"]')
        elif self.is_goal_state(self.getItemNode(x)):
            print(f'n{n} [style="filled",fillcolor="green",shape="circle"]') #Best Final Point
        elif self.getItemNode(x) in dead_ends:
            print(f'n{n} [style="filled",fillcolor="darkgreen",shape="circle"]') #Other Final Points
        else:
            print(f'n{n} [shape="circle"]')
    for x in graph:
        n1 = graph_keys.index(x)
        for y in graph[x]:
            n2 = graph_keys.index(self.getIndexNode(y))
            print(f'n{n1} -> n{n2}')
    print('}')
      
    #+permGoToRedRoom+ +permGoToBlueRoom+ +permGoToWestRoom+ +permGoToEastRoom+ +permSwitchActor+
    #+permGiveRedKey+ +permGiveBlueKey+ +permGiveGreenKey+
    #+permGetRedKey+ +permGetBlueKey+ +permGetGreenKey+
    #+permFinish

stateNodes=StateNodes()
print("START_STATE:")
print("Write Index Command:")
print("0 - Use DEFAULT_START_STATE:")
print("DEFAULT_START_STATE = (")
for i in stateNodes.getDefaultStartState():
    print (" " + str(i) +" = '"+ str(stateNodes.getDefaultStartState()[i]) +"'")
print(");")
print("1 - Create custome START_STATE;")
print("2 - Create START_STATE with random values.")
print("Write Command:")
input_int = int(input())
stateNodes.inputStartState(input_int)
print("START_STATE = (")
for i in stateNodes.getStartState():
    print (" " + str(i) +" = '"+ str(stateNodes.getStartState()[i]) +"'")
print(");")
stateNodes.make_gv()