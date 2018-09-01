# CSL622-assignment2
This code contains a function "updated_pagerank" which is supposedly an updated version of the pagerank function in the previous assignment.
The dataset is the same. We use an algorithm described at http://www.cs.princeton.edu/~chazelle/courses/BIB/pagerank.htm
This python file prints the output of this algorithm, and the output of the built-in pagerank algorithm in networkx. We compare the results
and try to estimate the "error" as the sum of absolute differences in pagerank for each node scaled by the total number of nodes present.
