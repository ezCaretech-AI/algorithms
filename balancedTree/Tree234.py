class DataItem:

	def __init__(self, dd):	#special method to create objects
	#with instances customized to a specific initial state
		self.dData = dd 

	def displayItem(self):
		print('/', self.dData)


class Node:
	_ORDER = 4
	def __init__(self):
		self._numItems = 0
		self._pParent = None
		self._childArray = []	#array of nodes
		self._itemArray = []	#array of data
		for j in range(self._ORDER):	#initialize arrays
			self._childArray.append(None)
		for k in range(self._ORDER - 1):
			self._itemArray.append(None)

			#connect child to this node
	def connectChild(self, childNum, pChild):
		self._childArray[childNum] = pChild
		if pChild:
			pChild._pParent = self

			#disconnect child from this node, return it
	def disconnectChild(self, childNum):
		pTempNode = self._childArray[childNum]
		self._childArray[childNum] = None
		return pTempNode

	def getChild(self, childNum):
		return self._childArray[childNum]

	def getParent(self):
		return self._pParent

	def isLeaf(self):
		return not self._childArray[0]

	def getNumItems(self):
		return self._numItems

	def getItem(self, index):	#get DataItem at index
		return self._itemArray[index]

	def isFull(self):
		return self._numItems==self._ORDER - 1

	def findItem(self, key):	#return index of
		for j in range(self._ORDER-1):	#item (within node)
			if not self._itemArray[j]:
				break	
			elif self._itemArray[j].dData == key:	#return -1
				return j
		return -1

	def insertItem(self, pNewItem):
		#assumes node is not full
		self._numItems += 1	#will add new item
		newKey = pNewItem.dData	#key of new item

		for j in reversed(range(self._ORDER-1)):	#start on right,	#examine items
			if self._itemArray[j] == None:
				pass
			else:
				itsKey = self._itemArray[j].dData
				if newKey < itsKey:	
					self._itemArray[j+1] = self._itemArray[j]
				else:
					self._itemArray[j+1] = pNewItem
					return j+1

		self._itemArray[0] = pNewItem
		return 0

	def removeItem(self):	#remove largest item
		#assumes node not empty
		pTemp = self._itemArray[self._numItems-1]	#save item
		self._itemArray[self._numItems-1] = None	#disconnect it
		self._numItems -= 1
		return pTemp

	def displayNode(self):	
		for j in range(self._numItems):
			self._itemArray[j].displayItem()	#format "/56"
		print ('/')


class Tree234:
	def __init__(self):
		self._pRoot = Node()

	def find(self, key):
		pCurNode = self._pRoot	#start at root
		while True:
			childNumber=pCurNode.findItem(key)
			if childNumber != -1:
				return childNumber	#found it
			elif pCurNode.isLeaf():
				return -1	#can't find it
			else:
				pCurNode = self.getNextChild(pCurNode, key)

	def insert(self, dValue):	#insert a DataItem
		pCurNode = self._pRoot
		pTempItem = DataItem(dValue)

		while True:
			if pCurNode.isFull():
				self.split(pCurNode)
				pCurNode = pCurNode.getParent()	#back up
					#search once
				pCurNode = self.getNextChild(pCurNode, dValue)

			elif pCurNode.isLeaf():
				break
			#node is not full, not a leaf; so go to lower level
			else:
				pCurNode = self.getNextChild(pCurNode, dValue)

		pCurNode.insertItem(pTempItem)

	def split(self, pThisNode):	
		#assumes node is full
		
		pItemC = pThisNode.removeItem()	#remove items from
		pItemB = pThisNode.removeItem()	#this node
		pChild2 = pThisNode.disconnectChild(2)	#remove children
		pChild3 = pThisNode.disconnectChild(3)	#from this node

		pNewRight = Node()	#make new node

		if pThisNode == self._pRoot:
			self._pRoot = Node()
			pParent = self._pRoot	#root is our parent
			self._pRoot.connectChild(0, pThisNode)	#connect to parent
		else:
			pParent = pThisNode.getParent()

		#deal with parent
		itemIndex = pParent.insertItem(pItemB)	#item B to parent
		n = pParent.getNumItems()	#total items?

		j = n-1#move parent's
		while j > itemIndex:	#connections
			pTemp = pParent.disconnectChild(j)	#one child
			pParent.connectChild(j+1, pTemp)	#to the right
			j -= 1
		#connect newRight to parent
		pParent.connectChild(itemIndex+1, pNewRight)

		#deal with newRight
		pNewRight.insertItem(pItemC)	#item C to newRight
		pNewRight.connectChild(0, pChild2)	#connect to 0 and 1
		pNewRight.connectChild(1, pChild3)	#on newRight


	def getNextChild(self, pNode, theValue):
		#assumes node is not empty, not full, not a leaf
		numItems = pNode.getNumItems()
		
		for j in range(numItems):	#for each item in node
			if theValue < pNode.getItem(j).dData:	#are we less?
				return pNode.getChild(j)	#return left child
		else:	#end for 	#we're greater, so
			return pNode.getChild(j + 1)	#return right child


	def displayTree(self):
		self.recDisplayTree(self._pRoot, 0, 0)

	def recDisplayTree(self, pThisNode, level, childNumber):
		print('level=', level, 'child=', childNumber)
		pThisNode.displayNode()

		numItems = pThisNode.getNumItems()
		for j in range(numItems+1):
			pNextNode = pThisNode.getChild(j)
			if pNextNode:
				self.recDisplayTree(pNextNode, level+1, j)
			else:
				return

	def run(self, key, searchValue): 

		d = Tree234()
		N = len(key)

		for i in key: 
			d.insert(i)

		result = d.find(searchValue)
		
		# if result == -1 or key[result] != searchValue: 
		if result == -1:	
			print("탐색오류")