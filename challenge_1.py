import sys

class Graph:

    def __init__(self, graph_file=None):
        ''' 
        Instantiate new Graph Object

            all_edges: [ Tuple(link_to_node:int, weight:int(optional)), 
                         Tuple(link_to_other_node:int, weight:int(optional))
                        ...
                       ]

            graph Object
            {
                node: [index1, index2]
            }

        '''
        self.graph = {}
        self.all_edges = []
        self.nodes = []
        self.edges = []

        if graph_file:
            self.build_new_graph(graph_file)

    def build_new_graph(self, filename):
        '''
        Build Graph from File
        '''
        self.file_lines = self.read_graph_file(filename)
        nodes = self.file_lines[1].split(',')
        edges = self.file_lines[2::]

        if self.file_lines[0] == 'G':
            # Build Undirected Graph
            self.build_undirected_graph(nodes, edges)

        elif self.file_lines[0] == 'D':
            # Build Directed Graph
            self.build_directed_graph(nodes, edges)
        
        else:
            raise Exception("Cannot determine Graph Type")

    def read_graph_file(self, graph_file):
        '''
        Read graph file and return as array
        '''
        lines = 0
        with open(graph_file) as file:
            lines = file.read()
        return lines.split('\n')

    def build_directed_graph(self, nodes, edges):
        '''
        Build Directed Graph

            nodes: [node:Int]
            edges: [Edges:Tuple(from_node:Int, to_node:Int, weight:Int)]

            Insertion Time O(v+e)
        '''
        
        self.nodes = nodes # Save References to Nodes and Edges
        self.edges = edges

        for node in nodes:
            self.graph[node] = []

        for edge in edges:
            # Convert String to list
            # Get rid of Parens
            edge = edge.split(',')
            edge[0] = edge[0][1:]
            edge[-1] = edge[-1][:-1]
            edge_tuple = ()
            if len(edge) == 3:
                # Edge Includes Weight
                edge_tuple = (edge[0], edge[1])

            elif len(edge) == 2:
                # Edge does not include weight
                edge_tuple = (edge[0],) 

            else:
                raise Exception("Wrong number of parameters for edge on node {}: Expected 3 got {}".format(edge[0], len(edge)))
    
            # Store Edge tuple in list and save index
            edge_id = len(self.all_edges)
            self.all_edges.append(edge_tuple)

            # Add Edge to Vertex in Graph
            if self.graph[edge[0]]:
                # print(self.graph)
                # print("looking for: {}".format(edge[0]))
                self.graph[edge[0]].append(edge_id)
            else:
                self.graph[edge[0]] = [edge_id]

    def build_undirected_graph(self, nodes, edges):
        '''
        Build Undirected Graph
        
            nodes: [node:Int]
            edges: [Edges:Tuple(to_node:Int, weight:Int)]

        Insertion Time: O(v+2e) => O(v+e)
        '''
        self.nodes = nodes # Save References to Nodes and Edges
        self.edges = edges

        for node in nodes:
            self.graph[node] = []

        for edge in edges:
            # Convert String to list
            # Get rid of Parens
            edge = edge.split(',')
            edge[0] = edge[0][1:]
            edge[-1] = edge[-1][:-1]

            if len(edge) == 3:
                # Edge Includes Weight
                this_edge_tuple = (edge[2], edge[3])
                other_edge_tuple = (edge[1], edge[3])
            elif len(edge == 2):
                # Edge does not include weight
                this_edge_tuple = (edge[2],)
                other_edge_tuple = (edge[1],)

            else:
                raise Exception("Wrong number of parameters for edge on vertex {}: Expected 3 got {}".format(edge[0], len(edge)))
    
            # Store edge Tuple in list and save index
            # Link to Other Vertex
            this_edge_id = len(self.all_edges)
            # Link from Other Vertex to this one
            other_edge_id = this_edge_id + 1

            self.all_edges.append(this_edge_tuple)
            self.all_edges.append(other_edge_tuple)

            # Add Edge to Current Vertex in Graph
            if self.graph[edge[0]]:
                self.graph[edge[0]].append(this_edge_id)
            else:
                self.graph[edge[0]] = [this_edge_id]
            
            # Add Link back from Other Vertex
            if self.graph[edge[0]]:
                self.graph[edge[0]].append(other_edge_id)
            else:
                self.graph[edge[0]] = [other_edge_id]
    
    def print_graph_info(self):
        '''
        Display Graph Information
        '''
        print('# Vertices: {}'.format(len(self.graph.keys())))
        print('# Edges: {}'.format(len(self.nodes)))
        print('Edge List')
        for edge in self.edges:
            print(edge)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        graph_file_name = sys.argv[1]
        g = Graph(graph_file_name)
        g.print_graph_info()

    else:
        raise Exception("Graph file not specified. Please provide path to load graph from.")
