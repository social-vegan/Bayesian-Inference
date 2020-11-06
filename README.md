# Bayesian-Inference
Bayesian network is a directed acyclic graphical representation of a set of variables and their conditional dependencies. Each variable is represented as a node in the graph and a directed edge between the nodes represents the parent-child relationship between the considered nodes. 
## Objective
Bayesian inference on the given data.
## Problem  
In this project we shall estimate the probability distributions or parameters of a given network based on user input. For this, we will make use of a user inputted dataset containing samples comprising of values observed for different variable.
## Input Format  
• Line 1: n : no. of variable or nodes (N1, N2, ...., Nn) \
• Line 2 to Line n + 1: Comma separated list of all possible values of variables N1 to Nn \
• Line n + 2 to Line 2n + 1: n × n matrix of 1’s and 0’s representing conditional dependencies or directed edges \
• Line 2n + 2: m : no. of samples \
• Line 2n + 3 to Line 2n + 2 + m: Comma separated values observed for all variables (N1, N2, ...., Nn) for each sample.
#### Input Explanation
```bash
3
TRUE, FALSE
TRUE, FALSE
TRUE, FALSE
0 0 1
0 0 1
0 0 0
100
TRUE, FALSE, TRUE
FALSE, TRUE, FALSE
.
.
.
.
```
In the above example, There are three binary variables (N1, N2, N3) in this Bayesian network, a value 1 at location (3,1) and (3,2) shows that N3 is conditionally dependent on N1 and N2. In other words, N1 and N2 are the parents of N3 or there is exists directed egdes from N1 to N3 and N2 to N3.

## Sample Input and Output
#### Sample Input 1
```bash
2
yes, no
yes, no
0 0
0 0
8
yes,no
yes,no
no,yes
no,no
yes,yes
yes,no
no,no
no,no
```
#### Sample Output 1
```bash
0.5000 0.5000 
0.2500 0.7500
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
