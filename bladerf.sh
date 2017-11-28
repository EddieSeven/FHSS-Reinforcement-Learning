#!/bin/sh
#Author: Leif Skunberg
# purpose of this script is to set the next frequency on the radio for transmission of next data chunk


#First, set the frequency with with the first argument

frequencySet = $(bladeRF-cli -e 'set frequency rx $1')

echo " $frequencySet"

samplerateSet = $(bladeRF-cli -e 'set samplerate rx $2 M')

echo " $samplerateSet"

bandwidthSet = $(bladeRF-cli -e 'set bandwidth rx $3 M')

echo " $bandwidthSet"




