import numpy as np
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Set backend before importing pyplot
import matplotlib.pyplot as plt
import os

def is_safe_state(allocation, max_need, available):
    n = len(allocation)
    m = len(available) if allocation else 0

    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    work = available.copy()
    finish = [False] * n
    safe_sequence = []

    for _ in range(n):
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True
                break
        if not found:
            return (False, [])
    return (True, safe_sequence)

def detect_deadlock(allocation, request_matrix):
    n = len(allocation)
    m = len(allocation[0]) if n > 0 else 0
    
    total_resources = [sum(allocation[i][j] for i in range(n)) for j in range(m)]
    available = [total_resources[j] - sum(allocation[i][j] for i in range(n)) for j in range(m)]
    
    finish = [False] * n
    work = available.copy()
    
    while True:
        found = False
        for i in range(n):
            if not finish[i] and all(request <= work[j] for j, request in enumerate(request_matrix[i])):
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                found = True
                break
        if not found:
            break
    
    deadlocked = [i for i, f in enumerate(finish) if not f]
    return [f"P{i}" for i in deadlocked]

def draw_resource_graph(allocation, max_need, available):
    n = len(allocation)
    m = len(available) if allocation else 0

    G = nx.DiGraph()

    # Add nodes
    for i in range(n):
        G.add_node(f"P{i}", color='lightblue', type='process')
    for j in range(m):
        G.add_node(f"R{j}", color='lightgreen', type='resource')

    # Add edges
    for i in range(n):
        for j in range(m):
            # Allocation edges (resource to process)
            if allocation[i][j] > 0:
                G.add_edge(f"R{j}", f"P{i}", weight=allocation[i][j], color='blue', label=f'Alloc {allocation[i][j]}')
            
            # Request edges (process to resource)
            request = max_need[i][j] - allocation[i][j]
            if request > 0:
                G.add_edge(f"P{i}", f"R{j}", weight=request, color='red', style='dashed', label=f'Request {request}')

    # Create figure
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    
    # Draw nodes
    node_colors = [G.nodes[n]['color'] for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_size=2500, node_color=node_colors)
    
    # Draw edges
    edge_colors = [G.edges[e]['color'] for e in G.edges()]
    edge_styles = [G.edges[e].get('style', 'solid') for e in G.edges()]
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, style=edge_styles, width=2)
    
    # Draw labels
    labels = {n: n for n in G.nodes()}
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Save to file
    img_path = os.path.join('static', 'graph.png')
    plt.savefig(img_path)
    plt.close()
    
    return img_path