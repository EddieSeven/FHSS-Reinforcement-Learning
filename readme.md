# Frequency Hopping Spread Spectrum(FHSS) Encryption with Reinforcement Learning

* Leif Skunberg, LeifTheDestroyer, Radio communication
* Charles Culpepper, EddieSeven, cryptography
* Michael Lyons, michaellyons786, Artificial Intelligence


This git is made for the final project of [CS440](http://www.cs.colostate.edu/~anderson/cs440/doku.php?id=schedule),
an artificial intelligence class taught by [Chuck Anderson](http://www.cs.colostate.edu/~anderson/wp/) at Colorado State University. 

This project is meant to explore encrypted wireless transmissions using FHSS techniques and reinforcement learning. 
Transmitted data through certain current technologies are prone to sniffing, man in the middle attacks and jamming.
We will be using reinforcement learning to scan through different ISM band frequencies to determine what frequency
would be best suited for data transmission. If a certain frequency is being jammed or has too much interference, 
a new frequency is found and transmission of message will resume. Reinforcement learning will be used to find the 
best possible channels for transmission of data.


## TODO:

### Radiowork:

* Finish radio top_block and packet handling

* interference detection

* FHSS selection and determination

### Cryptography:

* build a program/cli to input text data. Take the data and hash it with the recipient public key. write the data to message

* take the data from recievedmessage and decrypt it with the private key, display text to console

### Reinforcement Learning:

* take an array of values that represent interference levels, use a Q function to determine optimal or sub optimal interference levels

* create test data sets


This readme will be updated when more information is available to be dispersed.




CREDIT:

[GNUradio](https://www.gnuradio.org)

[Cryptography.io](https://cryptography.io/en/latest/)

[An Introduction to FHSS Data Communication Techniques](http://macs.citadel.edu/chenm/sigma_xi/Presentation_Skinner.pdf)

[Aaron Scher GNU radio companion collection](http://aaronscher.com/GNU_Radio_Companion_Collection/GNU_Radio_Companion.html)



