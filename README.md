# Quantum_Random_Number_Generator
#### This project uses Qiskit in the IBM Q Experience Environment to create Truly Random Numbers
#

Before entering the .pynb file, please create an IBM Q Experience account at : https://quantum-computing.ibm.com

If you do not have an IBMid yet, you can make one at https://www.ibm.com/account/reg/ca-en/signup?formid=urx-30292

#

Computers are logical machines. This makes them efficient for performing tasks where instructions (codes) and rules have to be followed rigorously and repetitively. This attribute makes them inefficient at performing operations where we seek randomness rather than following instructions.

You cannot code randomness. It means classical computers are ill-suited to generating a perfect set of “random” numbers and is a limitation of classical computers.

Classical computers can generate pseudo-random numbers that come close to being random but are not perfectly random. Pseudo-random number generators (PRNG) are based on mathematical algorithms that need a starting seed state. This seed state can then be used to quickly generate a set of random numbers. These numbers are not truly random as they are deterministic. Why?

If we restart with the same seed state (or if 2 people share the same seed state) we can recreate the same set of numbers making them no longer truly random. These numbers are also periodic over a very long time. These limitations aside, such pseudo-random numbers are still very useful and are used in a range of applications including simulation and modeling of processes. But these are too deterministic to be used for applications such as data encryption.

Such applications require truly random numbers. For this, we rely on processes that are non-algorithmic and cannot be predicted perfectly. Instead, we can only determine the probability of their occurrences. What could such processes be?

Governed by the probabilistic nature of quantum mechanics, it makes quantum computers adept at performing random operations.

Every quantum particle is characterized by a wave function. And the probability of obtaining any possible measurement outcome for its position, momentum, angular momentum is equal to the square of the corresponding amplitude. Until then, these values exist in superposition states and only the act of measurement collapses the wave function to discrete values.

In classical computers, information is stored in bits that have discrete values – either 0 or 1 but not both at the same time. These values are represented by voltage levels inside a computer processor (such as On or Off). In quantum computers, information is stored in quantum bits or qubits. These can take values 0 and 1 and can also exist as a superposition of these states.

Superposition is the possibility of a quantum system to exist in multiple states (say up and down, horizontal and vertical, 0 and 1) at the same time. These states are physically implemented by subatomic particles such as electrons and photons that can have binary states such as spin up and spin down of an electron, or horizontal and vertical polarisation of a photon. As quantum computers do not have to reduce their operations to 0s and 1s, it allows them to perform specific calculations much faster than classical computers.


Measuring states of quantum particles that are in a “superposition” have unpredictable results. The very act of measurement collapses the probability wave – forcing these particles to choose a state – randomly and with equal probability. This property can easily be used to generate random numbers in 4 simple steps.

Take a qubit represented by a subatomic particle with a predefined state (either |0> or |1> vector).
Force the qubit into superposition – by application of the Hadamard Gate that combines the 2 states a|0> + b|1> (where a and b are complex numbers)
Measure the state of the qubit to collapse its superposition (the wave function)
Obtain the random value of |0> or |1> that should occur with equal probability. Use these values to generate a larger set of random numbers.

We have now performed the equivalent of a quantum coin flip using the probabilistic nature of subatomic particles. The random numbers so generated cannot be replicated.

Unbelievable as it may sound, it is relatively simple to write a code that invokes the quantum nature of a subatomic particle to generate a set of random numbers. The difficult part is to engineer and build quantum computers that can harness the quantum effects and reduce noise that might impact the probability distribution of generated random numbers.




Some of the most common Quantum Logic Gates are:

Pauli-X gate: Acts on a single qubit. It is the quantum equivalent of the NOT gate for classical computers along the z-direction.  The reversal of direction along the Z-axis happens because of rotation around the X-axis of the Bloch sphere by pi radians.

It maps |0> to |1> and  |1> to |0>

Pauli-Y gate: Acts on a single qubit. It equates to a rotation around the Y-axis of the Bloch sphere by pi radians.

It maps |0> to i|1> and|1> to -i|0> 

Pauli-Z gate: Acts on a single qubit. It equates to a rotation around the Z-axis of the Bloch sphere by pi radians bringing a phase shift.

It maps |0> to |0> (unchanged)and|1> to  –|1> 

Hadamard (H) Gate: Acts on a single qubit. A very important gate and is used to create a superposition of basis states. It is the combination of two rotations, pi about the Z-axis followed by pi /2 about the Y-axis.

To create the Quantum Maze Runner Game we applied the Hadamard Gates to each of the 4 qubits and then carried out the measurement. The Hadamard Gates (H) created the superposition of the basis states |0> and |1> while the act of Measurement (M) collapsed the superposition of states to either |0> or|1>.


To create the maze we figured we would need 2000 random numbers.  To create each random number, the quantum circuit is run 5 times. Since the computer uses 4 qubits, each time it generates 4 binary digits (1s and 0s). At the end of 5 runs, 20 binary digits are created.


Randomly Generated Points using 4 Qubit Rigetti Quantum Computer (by Artash Nath)
A function is then applied to these 20 binary digits to create a random decimal number between 0 and 1.  The function used was built on geometric series. The first random binary digit was halved and added to the quarter of the second random binary number and then added to the eighth of the third random binary number and so on, until 2 to the power of 20  of the twentieth random binary number was added.

Function to Generate Random Decimal number between 0 and 1:

A/2 + B/4 + C/8 + D/16 …….. + T/ 2^20 

where A, B, C, D… T are 20 random numbers generated by the quantum computer

The above process was repeated 2000 times to create 2000 random decimal numbers between 0 and 1. To create coordinates, we divide these numbers into two lists of 1000 each: X-axis and Y-axis.


K-means Clustering on Randomly Generated Points (done by Amardeep Singh)
A scatter plot was created using these numbers. To generate a maze (or obstacles) for gaming purposes, we applied K-means clustering to find denser areas in the scatter plot. The centers of each of these clusters transformed into the centers of the obstacles to create the maze.

We realized that if we use too many coordinates, then the perfect nature of random numbers would mean that the numbers would start getting distributed more equally making the maze more uniform and less challenging. Interestingly (and as expected) no 2 mazes generated by quantum computers were the same!

maze 2
Maze Generated through running the Quantum Circuit on 4 Qubit Rigetti Quantum Computer at the Quantum Futures Hackathon at the Fields Institute
maze 1
Probabilistic nature of quantum mechanics means that no two mazes generated are the same
Presentation of the Project at the Quantum Futures Hackathon

At the end of 48 hours of hacking, the presentations started at 7 pm on October 20, 2019. While there was normal attrition in teams and team members (as it happens in all hackathons), it was encouraging to note that there were 7 teams who completed their projects and gave presentations.

Each of the presentations lasted 15 minutes followed by questions and answers and feedback by the organizers. You can download our presentation from here. QuantumMazeRunner

present1

Presenting the Quantum Maze Runner at the Fields Institute on 20th October 2019

We really enjoyed the hackathon. We would like to thank the organizers Tomas and Mark (and late Peter Wittek) for their efforts and resources to put in, to organize this hackathon. We also thank teammates Chris and Amardeep as it was a wonderful team effort.

More Pictures

saturday.jpg
Relaxed Saturday at the Hackathon at the Fields Institute learning about Quantum Logic Gates and Quantum Circuits
 

present3
Presenting the Quantum Maze Runner at the Fields Institute on 20th October 2019
 

blackboard.jpg
Figuring out Pauli-Quantum gates and their impact on binary states
