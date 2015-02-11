# pi-qrng
Random Number Generation from Quantum Key

# Summary
In this program we're using random numbers generated from a quantum key distribution system, as detailed in [this paper](http://journals.aps.org/pra/abstract/10.1103/PhysRevA.90.062331). The basic principle is this: Alice generates two photons that are entangled, but whose state is unknown. She then applies one of two transformations randomly to one of them while sending the second to Bob. Bob also performs a transformation randomly. On the times that they perform the same transformation -- and assuming that no one has tried to evesdrop on the link -- the measurements they make will be correlated. 

In our case, we used photons that are correlated in the energy-time basis, meaning that _when_ the photons are created and what color they are is entangled. The two different measurements correspond to measuring the time of arrival of the phtotons, either with or without dispersion (color-dependent time delay) applied. 

As detailed in far more gory detail in the paper, Alice and Bob then compare these measurements, using the shared information of the time-correlations to generate a secret key shared by both of them, but never spoken of openly. They further improve this through the use of so-called privacy amplification which serves both to whiten the data and to ensure that, asymptotically, no information is leaked to an evesdropper.

As the correlations are truly random, at the quantum level, and we apply a verified whitening technique, this makes the protocol a fantastic source of random numbers. In this code, we make use of a base-256 key, assigning a number 0-255 to each of the participants in the drawing. We convert each of these to a three digit string (zero-padding where necessary) and find their first occurrance in the digits of pi. The occurance closest to the occurrance of 2012 is deemed the winner. 