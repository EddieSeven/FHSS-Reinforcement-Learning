# Reinforcement Learning Algorithm Documentation (WORK IN PROGRESS)
## State
* *List* of (time t<sub>i</sub>, *list* of channels c<sub>1</sub>, (c<sub>2</sub>, ..., c<sub>n</sub>))
#### Example

## Time
* Discrete, arbitrary unit that increases by increments of 1.

## Channel
* [TODO] settle on representation of channel (especially interference value)
* Channel indices in the above mentioned state sublist should be static. For example, channel C is the same channel regardless if it is time 2 or time 3,000.

## Goal
* Final time t<sub>n</sub>

## Algorithm (based off of CSU CS 440 [lecture notes](https://nbviewer.jupyter.org/url/www.cs.colostate.edu/~anderson/cs440/notebooks/14%20Introduction%20to%20Reinforcement%20Learning.ipynb))

train(time)
Q = initialize(Q)

for t in time:
    if goal()
        update Qold with TD error (1 - Qold)
        start over
    else
        select next hop (greedy or random)
        update Qold with TD error (1 + Qnew - Qold)
        shift current state and action to old ones.
        apply action
