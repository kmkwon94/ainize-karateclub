"""Example runs with Karate Club."""

import networkx as nx

from karateclub.community_detection.overlapping import EgoNetSplitter, NNSED, DANMF, MNMF
from karateclub.community_detection.non_overlapping import EdMot, LabelPropagation
from karateclub.node_embedding.neighbourhood import GraRep, DeepWalk, Walklets
from karateclub.node_embedding.structural import GraphWave

#population = int(input("input population which is bigger than b "))
#b = int(input("input number which is lower than population "))
#c = float(input("input number which is lower than 5 "))

#------------------------------------
# Walklets example
#------------------------------------
def walklets(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = Walklets()
    model.fit(g)
    emb = model.get_embedding()
    return [emb.shape]


#------------------------------------
# DeepWalk example
#------------------------------------
def deepWalk(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = DeepWalk()
    model.fit(g)
    return [model.get_embedding()]
#------------------------------------
# Splitter example
#------------------------------------

def splitter(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = EgoNetSplitter(1.0)
    model.fit(g)
    return [model.get_memberships()]

#------------------------------------
# Edmot example
#------------------------------------
def edmot(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = EdMot(3, 0.5)
    model.fit(g)
    return [model.get_memberships()]
#------------------------------------
# DANMF example
#------------------------------------
def danmf(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = DANMF()
    model.fit(g)
    print(model.get_embedding())
    return [model.get_memberships(), model.get_embedding()]

#------------------------------------
# M-NMF example
#------------------------------------
def mnmf(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = MNMF()
    model.fit(g)

    print(model.get_memberships())
    print(model.get_embedding())
    print(model.get_cluster_centers())
    return [model.get_memberships(),model.get_embedding(),model.get_cluster_centers()]
#------------------------------------
# Label Propagation example
#------------------------------------
def labelPropagation(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = LabelPropagation()
    model.fit(g)

    print(model.get_memberships())
    return [model.get_memberships()]
#------------------------------------
# GraRep example
#------------------------------------
def graRep(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = GraRep()
    model.fit(g)
    embedding = model.get_embedding()

    print(embedding)
    return [embedding]
#------------------------------------
# GraphWave example
#------------------------------------
def graphWave(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = GraphWave()
    model.fit(g)
    embedding = model.get_embedding()

    print(embedding)
    return [embedding]
#------------------------------------
# NNSED example
#------------------------------------
def nnsed(population, b, c):
    g = nx.newman_watts_strogatz_graph(population, b, c)
    model = NNSED()
    model.fit(g)
    embedding = model.get_embedding()

    print(embedding)

    memberships = model.get_memberships()
    print(memberships)
    
    return [embedding, memberships]

def allFunc(population, b, c):
    result = dict()
    result["walklets"] = walklets(population, b, c)
    result["deepWalk"] = deepWalk(population, b, c)
    result["splitter"] = splitter(population, b, c)
    result["edmot"] = edmot(population, b, c)
    result["danmf"] = danmf(population, b, c)
    result["mnmf"] = mnmf(population, b, c)
    result["labelPropagation"] = labelPropagation(population, b, c)
    result["graRep"] = graRep(population, b, c)
    result["graphWave"] = graphWave(population, b, c)
    result["nnsed"] = nnsed(population, b, c)
    return result
