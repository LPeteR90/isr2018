
import networkx
import copy

q = 0.15

class Node:
    incoming = []
    outgoing = []
    rank = 0

    def __init__(self, incoming, outgoing):
        self.incoming = incoming
        self.outgoing = outgoing
        self.rank = 1/12


def sum_function(loc_graph, in_indices):
    curr_sum = 0
    for ind in in_indices:
        #print("Add:", loc_graph[ind - 1].rank, "/", len(loc_graph[ind - 1].outgoing))
        curr_sum += loc_graph[ind - 1].rank / len(loc_graph[ind - 1].outgoing)
    #print(curr_sum)
    return curr_sum


def normalize(loc_graph):
    c = 1 / sum(n.rank for n in loc_graph)

    for ix, n in enumerate(loc_graph):
        n.rank *= c
        print("D" + str(ix + 1) + ":", loc_graph[ix].rank)


graph = [Node([], [7]), Node([], [7]), Node([], [7]), Node([], [8, 9, 10]), Node([], [8, 9, 10]), Node([], [8, 9]),
         Node([1, 2, 3], [11]), Node([4, 5, 6], []), Node([4, 5, 6], [12]), Node([4, 5], []), Node([7], []),
         Node([9], [])]

print("--------Iteration", 0, "--------")
for counter in range(len(graph)):
    print(str(counter + 1) + ":", graph[counter].rank)

for counter in range(3):
    print("--------Iteration", counter + 1, "--------")
    helper_graph = copy.deepcopy(graph)
    for idx, node in enumerate(graph):
        #print("INIT:", node.rank)
        helper_graph[idx].rank = q/len(graph)

        #if len(node.outgoing) > 0:
        helper_graph[idx].rank += (1.0 - q) * sum_function(graph, node.incoming)
        print("D" + str(idx + 1) + ":", helper_graph[idx].rank)
    print("----normalized---")
    normalize(helper_graph)

    graph = copy.deepcopy(helper_graph)

#print(sum(node.rank for node in graph))




