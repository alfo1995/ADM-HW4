# AMD-HW4
This is the last project we did during the course **Algorithm of data mining** where we practiced on dealing with networks.

The data we had available concerned the publications made by the computer scientists, so we had to create a computer scientists Network and carry out some informations from this one. 

The file *modules.py* contains the code.

We decided to split it in a four parts:

* Introduction
* first point
* second point
* third point

## Introduction
In the introduction what we did is quite simple.

We import data from a Json file saving it in a variable called **data**, we start to observe the data (their structure) and wondering how to approach on it? are there any missing data? 

At this point, once we decided how to store, manipulate and parse the data, we start creating a dictionary which contains for each *computer scientists* all the publications that he did.

## First point
In this first part, after importing the library *Networkxx*, we implemented the code to create our Graph.

once studied the structure of our json file:
where :

+ keys are the ‘authors’ and the values are lists of dictionaries containing the authors name and id whose participated in the same publication.

the other keys of the dictionary are:

* the title of the publication
* the id of the publication
* the id of the conference.

Before creating the graph we defined the **jaccard** function, which calculated the distance, precisely of **jaccard**, between two authors, on the basis of their publications.

* Jaccard distance: $\frac{|A \bigcup B| - |A \bigcap B|}{|A \bigcup B|}$

So if two authors have made the same publications, or rather have always collaborated together, their distance of **jaccard** will be 0.

Then we built up our graph adding as nodes all the authors and the edges are between the computer scientist who collaborated for the same publications with weight equal to the distance of jaccard between them.

## Second point

In the second part after creating the network of computer scientists, we create a function called ‘searchConfid’ that wants in input a conference id and returns all the authors who participated in it.
So with this function we are now able to draw a subgraph of authors from the entire graph.

Up until now we carried out informations from the subgraph we’ve generated previously with some statistics technique; so we calculate:

+ *Degree*
+ *Betweenness centrality*
+ *Closeness centrality*

of nodes.
The function named *most_important* return the nodes in the subgraph with high betweenness centrality.
At the same time the function called *get_top_keys* returns the nodes with highest closeness centrality.

This second part also deals with **HOP DISTANCE**.
We created a function called [hopDistance](https://www.lifewire.com/what-are-hops-hop-counts-2625905) which wants in input a source (author-id) and an integer ‘d’.
the function first of all computes the shortest path from a node source to all the nodes in the graph and we assign the length of this path to a variable named ‘edge’.
In each iteration if edge is at most equal to the integer d, keep it and append it in an empty list.
At the end we will have all node with the required skills and we plotted them and visualize the graph.

## Third point

This third point concerns the last part of the homework.
First we implemented the Dijkstra algorithm as it was the key to resolving the two points that followed.

![Alt Text](https://media.giphy.com/media/ZkIkk3Y8E6hgc/giphy.gif)

We have implemented two functions that calculated the shortest path from a source node to a destination node.
During the execution we realized that the first function that we implemented had a fairly high computation complexity and therefore took a long time, and in most cases when we compared two quite distant nodes it gave as *maximum depth recursion error*.

We know that:
the running time of Dijkstra's algorithm depends on the combination of the underlying data structure and the graph shape (edges and vertices).
For example, using a linked list would require $O(V^²)$ time, i.e. it only depends on the number of vertices. 

Using a heap would require $O((V + E) \cdot log V)$, i.e. it depends on both the number of vertices and the number of edges.
For this reason, also documenting on the web, we have seen that using the heap algorithm becomes more efficient.


