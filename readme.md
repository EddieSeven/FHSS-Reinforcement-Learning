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

* integrate BladeRF with top_block/ create copy without throttle

* interference detection 
    * use bladeRF to capture 10 second samples on 10(?) different frequencies
        * set frequency rx 2400.00M

* FHSS selection and determination

   * frequency hop with a system call to the bladerf.sh script(3 args, 1 is frequency, 2nd is samplerate, 3rd is bandwidth). 
  
  
   

### Cryptography:

* build a program/cli to input text data. Take the data and hash it with the recipient public key. write the data to message

* take the data from recievedmessage and decrypt it with the private key, display text to console

### Reinforcement Learning:

* take an array of tuples that represent interference levels and their associated frequency, use a Q function to determine optimal or sub optimal interference levels

* create test data sets

* Michael Look at me --- http://ieeexplore.ieee.org/document/7772036/


This readme will be updated when more information is available to be dispersed.




CREDIT:

[GNUradio](https://www.gnuradio.org)

[Cryptography.io](https://cryptography.io/en/latest/)

[An Introduction to FHSS Data Communication Techniques, Jason S. Skinner](http://macs.citadel.edu/chenm/sigma_xi/Presentation_Skinner.pdf)

[Aaron Scher GNU radio companion collection](http://aaronscher.com/GNU_Radio_Companion_Collection/GNU_Radio_Companion.html)



