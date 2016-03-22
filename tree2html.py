class Tree2Html(object):
    def __init__(self):
        self._nodes = []
        self._bowel = ""
        
    def clear(self):
        self._nodes =[]
        self._bowel =""
    
    def empty(self):
        self._eat()
        return self._bowel
            
    def love(self, node):
        self._nodes.append(node)
        
    def load(self ,nodes):
        self._nodes.extend(nodes)
        
    def _eat(self):
        self._bowel = ""
        self._bowel +="<table border=1>"  
        for i in range(0, self._nodes[-1].getRowspan()):
            self._bowel += "<tr>"
            for node in self._nodes:
                if node.getShowline() == i:
                    self._bowel += node.showSelf().decode('utf8')
            self._bowel += "</tr>"
        self._bowel += "</table>"
        
tree2html = Tree2Html()