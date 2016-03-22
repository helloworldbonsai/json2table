# -*-coding:UTF-8 -*-
from collections import deque

class Node(object):
    def __init__(self,upNode=None,downNode=None,childrenNodes=None,
                    parentNode=None,attr=None,info=None):
        self._upNode = upNode
        self._downNode = downNode
        self._childrenNodes = childrenNodes
        self._parentNode = parentNode
        self._attr = attr
        self._showline = None
        self._rowspan = None
        self._colspan = None
        self._info = info
        
    def showSelf(self):
        tag = "td" if self._isLeafNode() else "th"
        if "href" not in self.getAttr():
            return '''
                <%s colspan="%d" rowspan="%d" >%s</%s>
                    '''%(tag,self.getColspan(),self.getRowspan(),self.getInfo(),tag)
        else:
            if "fresh" in self.getAttr():
                return '''
                    <%s colspan="%d" rowspan="%d" >
		    <img  width=25px height=15px src="./static/resource/new.png"/>
                    <a %s>%s</a></%s>
                    '''%(tag,self.getColspan(),self.getRowspan(),
                         self.getAttr()["href"],self.getInfo(),tag)
             
            else:
                return '''
                    <%s colspan="%d" rowspan="%d" ><a %s>%s</a></%s>
                        '''%(tag,self.getColspan(),self.getRowspan(),
                             self.getAttr()["href"],self.getInfo(),tag)
    
    def register(self, bonsai):
        bonsai.luck(self)
        
    def getBFsearch(self):
        allChildNodes = []
        queue = deque([self])
        while len(queue)!=0:
            curNode = queue.popleft()
            allChildNodes.append(curNode)
            if not curNode._isLeafNode():
                for cNode in curNode._childrenNodes:
                    queue.append(cNode)
        if allChildNodes[0]._isRootNode():
            return allChildNodes[1:]
        return allChildNodes
            
    def getRowspan(self):
        self._rowspan = self._getLeafNodeNum()
        return self._rowspan
        
    def getColspan(self):
        if self._isLeafNode():
            this = self
            while this._parentNode:
                this = this._parentNode
            self._colspan = this._getMaxAfter()-self._getPre()
            return self._colspan
        else:
            self._colspan = 1
            return self._colspan
    
    #from 0
    def getShowline(self):
        if self._isRootNode(): 
            self._showline = -1
            return self._showline
        elif self._upNode==None:
            if self._parentNode._isRootNode():
                self._showline = 0
            else:    
                self._showline = self._parentNode.getShowline()
            return self._showline
        else:
            self._showline = self._upNode.getShowline()+self._upNode.getRowspan()
            return self._showline
    
    def getAttr(self):
        if self._attr:
            return self._attr
        else:
            return {}
    
    def getInfo(self):
        if self._info:
            return self._info
        else:
            return ""
    
    def setInfo(self, info):
        self._info = info
        
    def setAttr(self , attr):
        self._attr = attr
    
    def setChildrenNodes(self, nodeList):
        assert (type(nodeList) == list) or (type(nodeList) == Node) 
        if type(nodeList) == list:
            if self._childrenNodes == None:
                self._childrenNodes = nodeList
            else:
                self._childrenNodes.extend(nodeList)         
        else:
            if self._childrenNodes == None:
                self._childrenNodes = [nodeList]
            else:
                self._childrenNodes.append(nodeList)
                
        for i in range(0,len(self._childrenNodes)):
            self._childrenNodes[i]._setParentNode(self)
            if i<(len(self._childrenNodes)-1):
                self._childrenNodes[i]._setDownNode(self._childrenNodes[i+1])  
     
    def getParentNode(self):
        return self._parentNode
           
    # operation in tree            
    def _isLeafNode(self):
        return self._childrenNodes == None
    
    def _isRootNode(self):
        return self._parentNode == None
    
    
    def _setDownNode(self, node):
        assert type(node) == Node 
        self._downNode = node
        node._setUpNode(self)
    
    def _setUpNode(self, node):
        assert type(node) == Node 
        self._upNode = node      
    
    def _setParentNode(self , node):
        assert type(node) == Node 
        self._parentNode = node
    
    def _getLeafNodeNum(self):
        count = [0]
        def iter2(node):
            if node._isLeafNode():
                count[0] += 1
            else:
                for cn in node._childrenNodes:
                    iter2(cn)
        iter2(self)
        return count[0]    
    
    #get HTML table size  
    def _getPre(self):
        count = -1
        this = self
        while(this._parentNode):
            count+=1
            this = this._parentNode
        return count
    
    def _getMaxAfter(self):
        count = [0]
        def iter1(node ,deep):
            if node._childrenNodes == None:
                count[0] = deep if count[0]<deep else count[0]
            else:
                for cn in node._childrenNodes:
                    iter1(cn , deep+1)
        iter1(self, 0)
        return count[0]
    
