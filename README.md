[![Run on Ainize](https://ainize.ai/static/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=github.com/kmkwon94/ainized-karateclub)

# Ainized karateclub
# Find nodes that has probability of joining neigbors (Community Detection)

This repository provides ten community detection methods 
The using each methods is done in the following steps:
1. User types the argument which is composed of population, neighbors, probability, algorithm
2. User queries ainized server with previous step's arguments
3. ainized-karateclub which is ainized
4.  server returns a dictionary.

# How to deploy
ainized-karateclub server is dockerlized, so it can be built and run using docker commands.

## Docker build
```sh
$ docker build -t [your dockerhub id]/[your docker repo] .
```
## Docker run
```sh
$ docker run -p 80:80 -d [your dockerhub id]/[your docker repo]
```

Now the server is available at http://localhost. To learn how to query the server, see the next section

Note that the docker image can be deployed using any docker-based deploy platform [ainize.ai](https://ainize.ai/)

# How to query
```
http://localhost/?population=[input integer number]&neighbors=[input integer number]&probability=[input float number]&alogorithm=[input method] 
```
Note that 
1. population is enough larger than neighbors e.g population = 100 , neighbors = 20 
2. probability less than or equal to 1 
3. There are 10 methods walklets, deepWalk, splitter, edmot, danmf, mnmf, labelPropagation, graRep, graphWave, nnsed
4. In this paper, nnsed is superior method than other detection methods so I recommend using nnsed method first.

# How to run on ainize
1. Click Run on ainize 
   
    [![RunonAinize](./img/runonainize.png)](https://ainize.web.app/redirect?git_repo=github.com/kmkwon94/ainized-karateclub)
2. Click default

    <img src="./img/clickdefault.png" width="700" height="400">
3. Click Try it out and input the default value. Finally click execute

    <img src="./img/tryitout.png" width ="700" height="400">
    <img src="./img/execute.png" width="700" height="400">
4. Result

    <img src="./img/result.png" width="650" height="400">

# References
[Original code & paper](https://github.com/benedekrozemberczki/karateclub)


 ![Version](https://badge.fury.io/py/karateclub.svg?style=plastic)
 ![GitHub stars](https://img.shields.io/github/stars/benedekrozemberczki/karateclub.svg?style=plastic) ![GitHub forks](https://img.shields.io/github/forks/benedekrozemberczki/karateclub.svg?color=blue&style=plastic) ![License](https://img.shields.io/github/license/benedekrozemberczki/karateclub.svg?color=blue&style=plastic)

<p align="center">
  <img width="90%" src="https://github.com/benedekrozemberczki/karateclub/blob/master/karatelogo.jpg?sanitize=true" />
</p>

--------------------------------------------------------------------------------


**[Documentation](https://karateclub.readthedocs.io/)** | **[Paper](https://arxiv.org/abs/1802.03997)** 

*Karate Club* is an unsupervised machine learning extension library for [NetworkX](https://networkx.github.io/).


*Karate Club* consists of state-of-the-art methods to do unsupervised learning on graph structured data. To put it simply it is a Swiss Army knife for small-scale graph mining research. First, it provides network embedding techniques at the node and graph level. Second, it includes a variety of overlapping and non-overlapping commmunity detection methods. The package also includes methods that can deal with bipartite, temporal and heterogeneous graphs. Implemented methods cover a wide range of network science ([NetSci](https://netscisociety.net/home), [Complenet](https://complenet.weebly.com/)), data mining ([ICDM](http://icdm2019.bigke.org/), [CIKM](http://www.cikm2019.net/), [KDD](https://www.kdd.org/kdd2020/)), artificial intelligence ([AAAI](http://www.aaai.org/Conferences/conferences.php), [IJCAI](https://www.ijcai.org/)) and machine learning ([NeurIPS](https://nips.cc/), [ICML](https://icml.cc/), [ICLR](https://iclr.cc/)) conferences and pieces from prominent journals.  

--------------------------------------------------------------------------------

**Citing**

If you find *Karate Club* useful in your research, please consider citing the following paper:

>@misc{rozemberczki2020karateclub,    
       title = {Karate Club: A tool for unsupervised learning on graph structured data.},   
       author = {Benedek Rozemberczki and Rik Sarkar},   
       year = {2020}
       }

--------------------------------------------------------------------------------

**A simple example**

*Karate Club* makes the use of modern community detection tecniques quite easy (see [here](link_here) for the accompanying tutorial).
For example, this is all it takes to use on a Watts-Strogatz graph [Ego-splitting](https://www.eecs.yorku.ca/course_archive/2017-18/F/6412/reading/kdd17p145.pdf):

```python
import networkx as nx
from karateclub import EgoNetSplitter

g = nx.newman_watts_strogatz_graph(1000, 20, 0.05)

splitter = EgoNetSplitter(1.0)

splitter.fit(g)

print(splitter.overlapping_partitions)
```

--------------------------------------------------------------------------------

**Models included**

In detail, the following methods are currently implemented.

**Overlapping Community Detection**

* **[DANMF](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.community_detection.overlapping.danmf.DANMF)** from Ye *et al.*: [Deep Autoencoder-like Nonnegative Matrix Factorization for Community Detection](https://github.com/benedekrozemberczki/DANMF/blob/master/18DANMF.pdf) (CIKM 2018)

* **[M-NMF](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.community_detection.overlapping.mnmf.M_NMF)** from Wang *et al.*: [Community Preserving Network Embedding](https://aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/14589) (AAAI 2017)

* **[Ego-Splitting](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.community_detection.overlapping.ego_splitter.EgoNetSplitter)** from Epasto *et al.*: [Ego-splitting Framework: from Non-Overlapping to Overlapping Clusters](https://www.eecs.yorku.ca/course_archive/2017-18/F/6412/reading/kdd17p145.pdf) (KDD 2017)

* **[NNSED](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.community_detection.overlapping.nnsed.NNSED)** from Sun *et al.*: [A Non-negative Symmetric Encoder-Decoder Approach for Community Detection](http://www.bigdatalab.ac.cn/~shenhuawei/publications/2017/cikm-sun.pdf) (CIKM 2017)

* **[BigClam](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.community_detection.overlapping.bigclam.BigClam)** from Yang and Leskovec: [Overlapping Community Detection at Scale:A Nonnegative Matrix Factorization Approach](http://infolab.stanford.edu/~crucis/pubs/paper-nmfagm.pdf) (WSDM 2013)

**Non-Overlapping Community Detection**

* **[EdMot](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.community_detection.non_overlapping.edmot.EdMot)** from Li *et al.*: [EdMot: An Edge Enhancement Approach for Motif-aware Community Detection](https://arxiv.org/abs/1906.04560) (KDD 2019)

* **[Label Propagation](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.community_detection.non_overlapping.label_propagation.LabelPropagation)** from Raghavan *et al.*: [Near Linear Time Algorithm to Detect Community Structures in Large-Scale Networks](https://arxiv.org/abs/0709.2938) (Physics Review E 2007)

**Neighbourhood-Based Node Level Embedding**

* **[Walklets](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.node_embedding.neighbourhood.walklets.Walklets)** from Perozzi *et al.*: [Don't Walk, Skip! Online Learning of Multi-scale Network Embeddings](https://arxiv.org/abs/1605.02115) (ASONAM 2017)

* **[GraRep](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.node_embedding.neighbourhood.grarep.GraRep)** from Cao *et al.*: [GraRep: Learning Graph Representations with Global Structural Information](https://dl.acm.org/citation.cfm?id=2806512) (CIKM 2015)


* **[DeepWalk](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.node_embedding.neighbourhood.deepwalk.DeepWalk)** from Perozzi *et al.*: [DeepWalk: Online Learning of Social Representations](https://arxiv.org/abs/1403.6652) (KDD 2014)

**Structural Node Level Embedding**

* **[GraphWave](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.node_embedding.structural.graphwave.GraphWave)** from Donnat *et al.*: [Learning Structural Node Embeddings via Diffusion Wavelets](https://arxiv.org/abs/1710.10321) (KDD 2018)

**Attributed Node Level Embedding**

* **[BANE](https://karateclub.readthedocs.io/en/latest/modules/root.html#karateclub.node_embedding.attributed.bane.BANE)** from Yang *et al.*: [Binarized Attributed Network Embedding](https://ieeexplore.ieee.org/document/8626170) (ICDM 2018)

**Graph Level Embedding**

Head over to our [documentation](https://karateclub.readthedocs.io) to find out more about installation and data handling, a full list of implemented methods, and datasets.
For a quick start, check out our [examples](https://github.com/benedekrozemberczki/karateclub/tree/master/examples.py).

If you notice anything unexpected, please open an [issue](https://github.com/benedekrozemberczki/karateclub/issues) and let us know.
If you are missing a specific method, feel free to open a [feature request](https://github.com/benedekrozemberczki/karateclub/issues).
We are motivated to constantly make Karate Club even better.


--------------------------------------------------------------------------------

**Installation**

```sh
$ pip install karateclub
```

--------------------------------------------------------------------------------

**Running examples**

```
$ python examples.py
```
  

