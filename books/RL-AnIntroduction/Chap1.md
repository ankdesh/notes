## Chapter 1 - Introduction

* __Value vs Reward__ The value of a state is the total amount of reward an agent can expect to accumulate over the future, starting from that state. Whereas rewards determine the immediate, intrinsic desirability of environmental states, values indicate the long-term desirability of states after taking into account the states that are likely to follow and the rewards available in those states.
* Comparision to other evolutionary learning methods
  * Solution methods such as _genetic algorithms, genetic programming, simulated annealing_, and other optimization methods never estimate value functions. These methods apply multiple static policies each interacting over an extended period of time with a separate instance of the environment.
  * If the space of policies is __sufficiently small__, or can be structured so that good policies are common or easy to find—or if a lot of time is available for the search—then evolutionary methods can be effective. 
  * In addition, evolutionary methods have __advantages__ on problems in which the _learning agent cannot sense the complete state_ of its environment.
