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

#

In this project, we wanted to create a large number of truly random numbers that could then by applied to procceses that need truly random numbers to work well, such as encrypting data.

To do this, we set up a 16 Qbit circuit, each of the bits in the circuit connected to a Hadamard gate. Each time we run the circuit, we measured the values from each Qbit. As we connected each Qbit to a Hadamard gate, they are forced to take a value of either 1 OR 0. Then, we can sequentialy add the binary value from each Qbit into a list.

By continously running the circuit, we can generate a list of truly random binary digits. 

But, we did not want random binary digits, but random numbers, prefrably from 0 to 1 so that we could efficently map them to any range of values we choose.

So, we created a fucntion that would seperate the list of binary digits into batches of 30 digits each, and turn the batch into 1 truly random decimal number between 0 and 1.

The function multiplied the first binary digit of the list by 0.5, the next by 0.25, the next by 0.125, and so on and add each of the returned values togethor to create the final real random number. So if we had a list [a, b, c, d, e], our final random number would be a/2 + b/4 + c/8 + d/16 + d/32 + e/64.

The whole above process would have to be repeated for each random number we wanted to make

#

In the .pynb file, we will go over the whole process in python to create 1000 true random numbers between 0 and 1
