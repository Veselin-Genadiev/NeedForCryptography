NeedForCryptography
==========

To use "NeedForCryptography" please install numpy:

    sudo pip install numpy
    
Here is an example on how to use a cipher:

    from Symmetric.playfair import Playfair
    cipher = Playfair('qazwsxedcrfvtgbyhnujmiklo')
    print(cipher.encrypt('dumb message')  #outputs encrypted message
    print(cipher.decrypt(cipher.encrypt('dumb message'))  #outputs original message
