# GeneratingPosets
A quick implementation of the poset generating algorithm described on "Algorithm of the Bimonth:Generating Posets" by  Harley Flanders

Url of the paper: http://www.jstor.org/stable/pdf/2686806.pdf ( paywalled)


# Posets
A poset (X,<) is a pair where X is a nonempty set and < is a "strict" partial order on X.
This means that < is a relation on X(= a subset of X^2) that has the two following properties:

1. There is no x \in X s.t. x < x
2. if x<y and y<z then x<z (Transitivity)


Clearly we can then uniquely associate for each poset X an nxn(where n= |X|)  matrix A defined as:
    A[i,j]= x_i < x_j

Note: the matrix is a Boolean entried matrix


#The algorithm

The idea of this algorithm is to start with a set X and a set of generating relations.

These are then mapped into the associated matrix B, according to the bijection defined earlier.

Then the algorithm takes as input B and it tell us if the relations are inconsistent or it gives out
a new matrix A representing the poset, where all the remaining relations are deduced by Transitivity.

---
So for example, if take the set X ={a,b} with relations: {a<b , b<a} , the algorithm will print "Inconsistent"

If instead X = {a,b,c} with relations: {a<b,b<c} then by tranisitivity we can deduce a<c and the matrix A is:
[False, True, True]
[False, False, True]
[False, False, False]

The interesgting thing about this algorithm  [due to S.
 Warshall, Jour. ACM 9 (1962)] is that despite what a naive analysis my suggest, it manages to solve the problem in O(n^3)
