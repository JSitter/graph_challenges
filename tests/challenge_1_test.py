from challenge_1 import Graph

def test_intance():
    assert Graph()
    
def test_build_new_graph():
    g = Graph()
    g.build_new_graph('graph.txt')
    assert g.graph['1']
    assert len(g.graph['1']) == 2