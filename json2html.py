#-*- coding:utf-8- *-
from tree2html import tree2html
from json2tree import json2tree
class JSON2Html():
    
    def convert(self , arg):
        tree2html.clear()
        rootNode = json2tree.convert(DICT=arg)
        allNodes = rootNode.getBFsearch()
        tree2html.load(allNodes)
        tree2html.love(rootNode)
        return tree2html.empty()

json2html=JSON2Html()