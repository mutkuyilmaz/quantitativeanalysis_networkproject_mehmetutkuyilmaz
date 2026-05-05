### Istanbul E-Commerce Delivery Network Optimization

# 1. Real World Problem Context : 
E-commerce companies in Istanbul deal with a real problem: getting orders from warehouses to customers as efficiently as possible. Route choice directly affects 
fuel costs and delivery speed. This project solves that problem using network optimization.

# 2. Problem Definition :
The aim is to find the shortest delivery path from Warehouse_Kadikoy to District_Maltepe across a network of warehouses, hubs, and districts in Istanbul. 
The problem is modeled as a shortest path problem where edge weights represent distances in kilometers.

# 3. Network Model :
The network is represented as an undirected weighted graph. Nodes represent physical locations such as warehouses, distribution hubs, and customer districts. 
Edges represent road connections between these locations, with weights indicating the distance in kilometers.

# 4. Nodes and Edges
The network consists of 7 nodes and 10 edges.

Nodes: Warehouse_Kadikoy, Hub_Uskudar, Hub_Besiktas, District_Umraniye, District_Maltepe, District_Sisli, District_Kagithane.

Edges (Selected):
| Source            | Target           | Distance (km) |
| Warehouse_Kadikoy | Hub_Uskudar      | 4.2           |
| Hub_Uskudar       | District_Maltepe | 7.3           |
| Hub_Besiktas      | District_Sisli   | 3.8           |
| District_Umraniye | District_Maltepe | 9.2           |

Full dataset : data/network_data.csv

# 5. Selected Algorithm :
I used the Dijkstra's algorithm (The Shortest Path algorithm) which is the default method in NetworkX. 
This algorithm finds the path with the minimum total weight between two nodes by exploring the least costly connections first. 

# 6. Python Implementation :
The solution is implemented in `src/solution.py` using the following libraries:
- NetworkX : graph creation and shortest path calculation
- Matplotlib : network visualization
- Pandas : loading and processing the CSV dataset

The graph is created as an undirected weighted graph. Each row in the CSV file is added as an edge with its distance as the weight attribute.

# 7. Results :
Shortest Path: Warehouse_Kadikoy -> Hub_Uskudar -> District_Maltepe  
Total Distance: 11.50 km

The network visualization shows all connections in gray, with the optimal route highlighted in red.

Visualized network : results/network_visualization.png

# 8. Managerial Interpretation :
The results show the fact that routing deliveries through Hub_Uskudar is the most efficient option for reaching District_Maltepe from Warehouse_Kadıköy.
Alternative routes are longer or they require passing through more intermediate points. 
A real e-commerce company would minimize fuel costs and delivery time through this model.

# 9. How to Run the Code : 
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the solution: `python src/solution.py`

Output files will be saved in the `results/` folder.

# 10. References :
- NetworkX Documentation: https://networkx.org/documentation/stable/
- Dijkstra, E. W. (1959). A note on two problems in connexion with graphs. Numerische Mathematik, 1, 269–271.
- Taylor, B. W. (2019). Introduction to Management Science. Pearson.
