import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from([

    ('nap', {"color": "red"}),
    (5, {"color": "green"}),

])

G.add_edges_from(
    [('nap', 'vensuz'), ('nap', 'mars'), ('hold', 'merkur'), ('hold', 'vensuz'), ('merkur', 'nap'),
     ('merkur', 'hold'), ('merkur', 'vensuz'), ('merkur', 'mars'), ('merkur', 'mars'), ('mars', 'nap'),
     ('mars', 'merkur'), ('mars', 'nap'), ('mars', 'vensuz'), ('mars', 'mars')])

ket_iranyu_graf = [('nap', 'vensuz'), ('hold', 'merkur'), ('mars', 'merkur'), ('nap', 'mars'),
                   ('merkur', 'hold'), ('merkur', 'mars'), ('mars', 'nap')]

iranyitott_graf = [edge for edge in G.edges() if edge not in ket_iranyu_graf]

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)

nx.draw_networkx_labels(G, pos)
#
# nx.draw_networkx_edges(G, pos,
#                        edgelist=iranyitott_graf,
#                        edge_color='r', arrows=True)

nx.draw_networkx_edges(G, pos,
                       edgelist=ket_iranyu_graf,
                       arrows=False)
plt.show()
