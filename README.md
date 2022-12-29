you're walking up the empire state building and you're playing a game with a friend.

You throw a dice one hundred times.
If it's 1 or 2 you'll go one step down.
If it's 3, 4, or 5, you'll go one step up.
If you throw a 6, you'll throw the dice again and will walk up the resulting number of steps.

Of course, you can not go lower than step number 0.

And also, you admit that you're a bit clumsy and have a chance of 0.1% of falling down the stairs when you make a move.
Falling down means that you have to start again from step 0.

With all of this in mind, you bet with your friend that you'll reach 60 steps high.

How to solve?
What is the chance that you will win this bet? It's a complex assignment. One way to solve it would be to calculate the chance analytically using equations. Another possible approach, is to simulate this process thousands of times, and see in what fraction of the simulations that you will reach 60 steps. This is a form of -hacker statistics-. As you can probably guess, we're going to opt for the second approach.

what is the chance that you'll reach 60 steps high? Each random walk will end up on a different step. If you simulate this walk thousands of times, you will end up with thousands of final steps.

To calculate the chance that this end point is greater than or equal to 60, you can count the number of walks with ending that are greater than or equal to 60 and divide that number by the total number of simulations.
