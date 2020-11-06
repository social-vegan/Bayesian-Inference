# Bayesian-Inference
Bayesian network is a directed acyclic graphical representation of a set of variables and their conditional dependencies.\
Each variable is represented as a node in the graph and a directed edge between the nodes represents the parent-child relationship between the considered nodes.

Note: To transform the directed bayesian model into an undirected model, the dependency matrix should be made symmetrical.
## Objective
To find the Bayesian inference on the given data.
## Problem  
In this project, we shall estimate the probability distributions or parameters of a given bayesian network based on user input. For this, we will make use of a user inputted dataset containing samples that comprise of values observed for all the different variables in the network.
- - - -
## Input
##### Input Format
• Line 1: n - Number of variable or nodes (N1, N2, ...., Nn) \
• Line 2 to Line n + 1: Comma separated list of all possible values of variables N1 to Nn \
• Line n + 2 to Line 2n + 1: n × n boolean matrix (1 or 0 only) representing conditional dependencies or directed edges \
• Line 2n + 2: m - Denoting the number of samples to be inputted or in other words, the size of the dataset \
• Line 2n + 3 to Line 2n + 2 + m: Comma separated values observed for all variables (N1, N2, ...., Nn) for each sample.
##### Input Explanation
```bash
3
TRUE, FALSE
TRUE, FALSE
TRUE, FALSE
0 0 1
0 0 1
0 0 0
100
FALSE,FALSE,TRUE
FALSE,FALSE,TRUE
FALSE,FALSE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,FALSE
FALSE,TRUE,FALSE
FALSE,FALSE,TRUE
FALSE,FALSE,TRUE
FALSE,FALSE,TRUE
FALSE,TRUE,FALSE
FALSE,FALSE,FALSE
FALSE,TRUE,FALSE
FALSE,TRUE,FALSE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
FALSE,TRUE,TRUE
TRUE,TRUE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,FALSE
TRUE,FALSE,TRUE
FALSE,TRUE,TRUE
FALSE,FALSE,FALSE
FALSE,TRUE,FALSE
TRUE,FALSE,FALSE
FALSE,FALSE,TRUE
FALSE,TRUE,TRUE
TRUE,TRUE,FALSE
FALSE,FALSE,TRUE
FALSE,TRUE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,FALSE
TRUE,TRUE,FALSE
FALSE,TRUE,FALSE
FALSE,FALSE,TRUE
FALSE,TRUE,FALSE
FALSE,FALSE,FALSE
FALSE,TRUE,FALSE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
TRUE,TRUE,FALSE
FALSE,FALSE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
TRUE,FALSE,TRUE
FALSE,TRUE,TRUE
FALSE,TRUE,TRUE
FALSE,TRUE,FALSE
TRUE,FALSE,TRUE
TRUE,FALSE,TRUE
FALSE,TRUE,FALSE
FALSE,FALSE,TRUE
FALSE,TRUE,FALSE
TRUE,TRUE,FALSE
FALSE,TRUE,FALSE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
TRUE,FALSE,FALSE
FALSE,FALSE,FALSE
FALSE,FALSE,FALSE
FALSE,TRUE,FALSE
TRUE,TRUE,FALSE
FALSE,TRUE,FALSE
FALSE,TRUE,FALSE
FALSE,TRUE,FALSE
FALSE,FALSE,FALSE
FALSE,TRUE,TRUE
TRUE,TRUE,FALSE
FALSE,FALSE,TRUE
FALSE,FALSE,TRUE
TRUE,TRUE,FALSE
FALSE,TRUE,FALSE
TRUE,FALSE,FALSE
TRUE,TRUE,FALSE
FALSE,TRUE,TRUE
TRUE,FALSE,FALSE
TRUE,FALSE,FALSE
FALSE,TRUE,FALSE
FALSE,FALSE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,FALSE
TRUE,FALSE,FALSE
TRUE,TRUE,TRUE
FALSE,FALSE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
FALSE,FALSE,FALSE
FALSE,FALSE,TRUE
FALSE,TRUE,FALSE
FALSE,TRUE,FALSE
FALSE,TRUE,TRUE
FALSE,FALSE,TRUE
FALSE,TRUE,FALSE
FALSE,FALSE,FALSE
```
In the above example, There are three binary variables (N1, N2, N3) in this Bayesian network, a value 1 at location (3,1) and (3,2) shows that N3 is conditionally dependent on N1 and N2. In other words, N1 and N2 are the parents of N3 or there is exists directed egdes from N1 to N3 and N2 to N3.

Also,
The dataset has 100 samples and we shall find the probability distribution for each of the variables based on the given dataset. 
- - - -
## Output
Program will learn the parameters (probability distributions of each variable) of the given network and return them in the following format.
##### Output Format
Print n lines where for each i from 1 to n, Line i contains the probability distribution of variable Ni i.e., Line 1 will contain probability distribution of variable N1 and so on. The probability values are rounded off to 4 decimal places.

For 1<=i<=n,\
• Line i: probability distribution of variable Ni 
##### Output Explanation
The output for the sample input under input explanation is:
```bash
0.2 0.8
0.4 0.6
0.2 0.4 0.3 0.5 0.8 0.6 0.7 0.5
```
This implies P(N1=TRUE) = 0.2, and P(N1=FALSE) = 0.8.\
Similarly P(N2=TRUE) = 0.4, and P(N2=FALSE) = 0.6.\
Further, P(N3=TRUE|N1=TRUE, N2=TRUE) = 0.2, P(N3=TRUE|N1=TRUE, N2=FALSE) = 0.4, P(N3=TRUE|N1=FALSE, N2=TRUE) = 0.3 and so on.
- - - -

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
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

