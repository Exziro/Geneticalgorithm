import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
'''
a = np.reshape(np.random.random_integers(0 ,1 , size= 100), (10, 10))
print("",a)
D = nx.DiGraph(a)

nx.draw(D, with_labels= True, font_weight = 'bold')
plt.axis('on')
plt.xticks([])
plt.yticks([])
plt.show()
'''
def random_martex_genetor(vex_num = 0):
    data_martex = []
    for i in range (vex_num):
        one_list = []
        for i in range(vex_num):
            one_list.append(random.randint(0, 1))
        data_martex.append(one_list)
    return data_martex
G = nx.Graph()
test = random_martex_genetor(10)
for i in range (len(test)):
    for j in range(len(test)):
        if(test[i][j] != 0):
            G.add_edge(i, j)
nx.draw(G)
plt.show()
#print("xxx",test)
#G = nx.dodecahedral_graph()
#nx.draw_shell(G, nlist = test)

#G.
#G.add_nodes_from(test)
#H = nx.path_graph(10)
#nx.draw(G, with_labels=True)
#plt.show()
