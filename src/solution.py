import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Loading network data from CSV file :
df = pd.read_csv("data/network_data.csv")

# Creating graph :
networkgraph = nx.Graph()
for _, row in df.iterrows():
    networkgraph.add_edge(row["source"], row["target"], weight=row["distance_km"])

# Find the shortest path :
# The algorithm minimizes total distance in km between the source and target node.
source_node = "Warehouse_Kadikoy"
target_node = "District_Maltepe"

shortest_path = nx.shortest_path(networkgraph, source=source_node, target=target_node, weight="weight")
shortest_distance = nx.shortest_path_length(networkgraph, source=source_node, target=target_node, weight="weight")

print(f"Shortest path: {' -> '.join(shortest_path)}")
print(f"Total distance: {shortest_distance:.2f} km")

# Visualizing the network :
# (Gray edges represent all connections, red edges highlight the optimal delivery route.)
plt.figure(figsize=(18, 12))
pos = nx.spring_layout(networkgraph, seed=42, k=4)

nx.draw_networkx_nodes(networkgraph, pos, node_color="steelblue", node_size=800)
nx.draw_networkx_edges(networkgraph, pos, edge_color="gray", width=1.5)

path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
nx.draw_networkx_edges(networkgraph, pos, edgelist=path_edges, edge_color="tomato", width=3)

edge_labels = nx.get_edge_attributes(networkgraph, "weight")
nx.draw_networkx_edge_labels(networkgraph, pos,
    edge_labels={k: f"{v} km" for k, v in edge_labels.items()},
    font_size=8,
    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=1.0))

label_pos = {node: (coords[0], coords[1] - 0.12) for node, coords in pos.items()}
nx.draw_networkx_labels(networkgraph, label_pos, font_size=9, font_color="black", font_weight="bold")

plt.title(f"Shortest Path: {source_node} → {target_node}\nTotal: {shortest_distance:.2f} km", fontsize=13)
plt.margins(0.2)
plt.tight_layout()
plt.savefig("results/network_visualization.png", dpi=150, bbox_inches="tight")
plt.show()

# Saving results to output file :
with open("results/solution_output.txt", "w") as f:
    f.write(f"Shortest path: {' -> '.join(shortest_path)}\n")
    f.write(f"Total distance: {shortest_distance:.2f} km\n")

print("Done. Results saved to results/")
