"""Example runs with Karate Club."""

import networkx as nx

from karateclub.community_detection.overlapping import EgoNetSplitter, NNSED, DANMF, MNMF
from karateclub.community_detection.non_overlapping import EdMot, LabelPropagation
from karateclub.node_embedding.neighbourhood import GraRep, DeepWalk, Walklets
from karateclub.node_embedding.structural import GraphWave

#population = int(input("input population which is bigger than b "))
#neighbors = int(input("input number which is lower than population ")), each node is joined with 'b' nearest neighbors in a ring topology
#probability = float(input("input number which is lower than 5 ")) mean the probability of adding a new edge for each node

#------------------------------------
# Walklets example
#------------------------------------
def walklets(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = Walklets()
    model.fit(g)
    emb = model.get_embedding()
    #print(emb.shape)
    return [emb.shape]


#------------------------------------
# DeepWalk example
#------------------------------------
def deepWalk(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = DeepWalk()
    model.fit(g)
    #print(model.get_embedding())
    return [model.get_embedding()]
#------------------------------------
# Splitter example
#------------------------------------

def splitter(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = EgoNetSplitter(1.0)
    model.fit(g)
    #print(model.get_memberships())
    return [model.get_memberships()]

#------------------------------------
# Edmot example
#------------------------------------
def edmot(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = EdMot(3, 0.5)
    model.fit(g)
    #print(model.get_memberships())
    return [model.get_memberships()]
#------------------------------------
# DANMF example
#------------------------------------
def danmf(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = DANMF()
    model.fit(g)
    #print(model.get_embedding())
    return [model.get_memberships(), model.get_embedding()]

#------------------------------------
# M-NMF example
#------------------------------------
def mnmf(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = MNMF()
    model.fit(g)

    #print(model.get_memberships())
    #print(model.get_embedding())
    #print(model.get_cluster_centers())
    return [model.get_memberships(),model.get_embedding(),model.get_cluster_centers()]
#------------------------------------
# Label Propagation example
#------------------------------------
def labelPropagation(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = LabelPropagation()
    model.fit(g)

    #print(model.get_memberships())
    return [model.get_memberships()]
#------------------------------------
# GraRep example
#------------------------------------
def graRep(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = GraRep()
    model.fit(g)
    embedding = model.get_embedding()

    #print(embedding)
    return [embedding]
#------------------------------------
# GraphWave example
#------------------------------------
def graphWave(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = GraphWave()
    model.fit(g)
    embedding = model.get_embedding()

    #print(embedding)
    return [embedding]
#------------------------------------
# NNSED example
#------------------------------------
def nnsed(population, neighbors, probability):
    g = nx.newman_watts_strogatz_graph(population, neighbors, probability)
    model = NNSED()
    model.fit(g)
    embedding = model.get_embedding()

    #print(embedding)

    memberships = model.get_memberships()
    #print(memberships)
    
    return [memberships]

def allFunc(population, neighbors, probability):
    result = dict()
    result["walklets"] = walklets(population, neighbors, probability)
    result["deepWalk"] = deepWalk(population, neighbors, probability)
    result["splitter"] = splitter(population, neighbors, probability)
    result["edmot"] = edmot(population, neighbors, probability)
    result["danmf"] = danmf(population, neighbors, probability)
    result["mnmf"] = mnmf(population, neighbors, probability)
    result["labelPropagation"] = labelPropagation(population, neighbors, probability)
    result["graRep"] = graRep(population, neighbors, probability)
    result["graphWave"] = graphWave(population, neighbors, probability)
    result["nnsed"] = nnsed(population, neighbors, probability)
    return result
