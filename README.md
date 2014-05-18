NeedForCryptography
==========

A cryptographic library for python.

About NeedForCryptography
----------

NeedForCryptography is meant to be a cryptographic library. It will provide solutions for main problems in cryptography and many ciphers(some of them often used and other for educational purposes only). The project is inspired by the [Cryptography](http://www.fmi.uni-sofia.bg/algebra/cryptodescr.shtml) course at FMI.

==========

Here is a list of things that will be implemented in the library. All of them will have unit tests. 
These who have a suffix "(until June 2nd)" are predictions for "Milestone 1" task of the [Python](http://fmi.py-bg.net/) course at FMI:

* Common problems:
 * Generation of large primes (until June 2nd)
 * Decomposiotion of prime divisors (until June 2nd)
 * Pohlig-Hellman algorithm for finding discrete logarithm in Zn (until June 2nd)
 * Еlectronic signature (until June 2nd)
 * Generate a random bit
 * Secret sharing schemes

* Ciphers:
 * Playfair (until June 2nd)
 * Caeser (until June 2nd)
 * L. Hill (until June 2nd)
 * RC6 (until June 2nd)
 * DES
 * 3DES
 * Feistel
 * RSA
 * MacEliece
 * Diffie–Hellman

Undercover
==========

About Undercover
----------

Undercover will be a django web application(Crypto-Chat) which uses NeedForCryptography.
Users will be able to:

* Share their public keys
* Send encrypted messages
* Decrypt messages
* Enter their private key
* Have an unique identification using "Electronic signature".
