# Validation of random number generators

## Motivation

Random number generators are more accurately classified as pseudorandom in programming manuals. The reason for this prefix lies in the origin of its obtaining, which is generated from the truncation of some numerical calculation.

These numbers are essential for computer simulations of physical models, as in statistical mechanics, climatology, among others, because it is through them that physicists test their theoretical models.

It is possible that in small physical systems the pseudorandom numbers satisfy the requirement of the physicist/programmer, but as the system grows in size it will be possible to observe some patterns that can introduce undesired tendencies in the results, not because of the physical model, but in the random number to test it.

I propose to develop a methodology that tests the quality of the random number generator through python.


## Methodology 