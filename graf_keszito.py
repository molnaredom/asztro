import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

osszekottetesek = {'from': ['5', '3', '2', '1', '2', '5', '3', '2', '1', '2', '4'],
                'to':      ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','7'],
                  "fenyszog": ["konjukcio", "kvadrat", "trigon", "trigon", "egyuttallas",
                               "konjukcio", "kvadrat", "trigon", "trigon", "egyuttallas",
                               "konjukcio"]
                  }


fig, ax = plt.subplots(figsize=(10, 10))


relationships = pd.DataFrame(osszekottetesek)

# Create DF for node characteristics
carac = pd.DataFrame({'ID':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                      'type':['Személyjelölő','Személyjelölő', 'Személyjelölő', 'Személyjelölő','Személyjelölő',
                      'Sorsjelölő', 'Sorsjelölő',
                        'Transzcendens','Transzcendens', 'Transzcendens'
                              ]})

# Create graph object
G = nx.from_pandas_edgelist(relationships, 'from', 'to', create_using=nx.Graph())

# Make types into categories
carac = carac.set_index('ID')
carac = carac.reindex(G.nodes())

carac['type'] = pd.Categorical(carac['type'])
carac['type'].cat.codes

# Specify colors
cmap = matplotlib.colors.ListedColormap(['dodgerblue', 'lightgray', 'darkorange'])

edge_color = ['blue', 'red', 'green', 'red', 'blue']
borders = ['blue', 'red', 'green', 'red', 'blue']

# Set edge widths
edge_widths = [5, 4, 2, 3, 5]

# Draw graph
plt.subplot(1, 1, 1)
nx.draw(G, with_labels=True, node_color=carac['type'].cat.codes, cmap=cmap, node_size=4000,
        width=edge_widths, edge_color=edge_color, edgecolors = borders,
        )

plt.show()
