# -*- coding: UTF-8 -*-
import json
from collections import OrderedDict
from trieTree import Node

class Json2Tree(object):
    
    def convert(self, **args):
        '''
            if you wanna sort , you can use list
        '''
        if 'DICT' in args:
            json_input = args['DICT']
            if type(json_input) == file:
                try:
                    self.ordered_json = json.load(json_input,object_pairs_hook=OrderedDict)
                except:
                    print "some except occur, check your input"
            if type(json_input) == str:
                try:
                    self.ordered_json = json.loads(json_input,object_pairs_hook=OrderedDict)
                except:
                    print "maybe you can check or file() your input"
            if type(json_input) == unicode:
                json_input = json_input.encode("utf-8")
                try:
                    self.ordered_json = json.loads(json_input,object_pairs_hook=OrderedDict)
                except:
                    print "some except occur, check your input"
            if type(json_input) == dict:
                self.ordered_json = json.loads(json.dumps(json_input),object_pairs_hook=OrderedDict)  
        else:
            raise Exception('Can\'t convert NULL!')
        
        root = Node()
        return self.createTree(self.ordered_json, root)
      
    def createTree(self,iterStruct, pNode):
        
        def judge(entry):
            if isinstance(entry,unicode):
                return unicode(entry).encode("utf8")
            if isinstance(entry,int) or isinstance(entry,long) \
                or isinstance(entry, float) or isinstance(entry, bool):
                return str(entry)
            if None == entry:
                return ""           
            if isinstance(entry,dict) or isinstance(entry,list):
                if len(entry) == 0:
                    return ""
                else:
                    return entry
                
        def nodeCreater(entry):
            assert not (isinstance(entry,list) and isinstance(entry,dict))
            entrylist = entry.split(":::")
            if len(entrylist)==2:
                return Node(info=entrylist[0], attr = json.loads(entrylist[1]))
            return Node(info = entry)
        
        
        if isinstance(iterStruct,dict):
            for k in iterStruct:
                assert not (isinstance(k,list) and isinstance(k,dict))
                node = nodeCreater(judge(k))
                pNode.setChildrenNodes(node)
                v = judge(iterStruct[k])
                if isinstance(v,list) or isinstance(v,dict):
                    self.createTree(v, node)
                else:
                    cnode = nodeCreater(v)
                    node.setChildrenNodes(cnode)       
        elif isinstance(iterStruct,list):
            for entry in iterStruct:
                v = judge(entry)
                if isinstance(v,list) or isinstance(v,dict):
                    self.createTree(v, pNode)
                else:
                    cnode = nodeCreater(v)
                    pNode.setChildrenNodes(cnode)     
        else:
            raise Exception('sorry, Bonsai.Y can\' distinguish this type ')
        
        if pNode.getParentNode()  == None:
            return pNode
 
json2tree =  Json2Tree()               
         
