#lab8 Module 4
#Team 10 - M. Mariscal, C. Piwarski, W. Robleh


#This function increases the volume of a given sound sample by a factor of two
def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)
      
#Write a function called decreaseVolume that takes a sound object and reduces 
#the volume by half
def decreaseVolume(sound):
   for sample in range(0, getLength(sound)):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value * 0.5)
      
#Write a function called changeVolume that takes a sound object and changes 
#volume by a given factor
def changeVolume(sound, factor):
   for sample in range(0, getLength(sound)):
      value = getSampleValueAt(sound, sample)
      setSampleValueAt(sound, sample, value * factor)

#This function retrieves a file and creates a sound out of it
def picSound():
  return makeSound(pickAFile())
 
#Write a function called maxSample that finds the maximum sample value 
#in your sound
def maxSample(sound):
  maximum = -33000
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    maximum = max(value, maximum)
  return maximum

#Write a new function called maxVolume that increases the volume of each sample
#by the factor(factor=float(maxPossibleSampleValue)/largest) where largest is 
#the value returned by your maxSample function
def maxVolume(sound):
  factor = (float(127)/maxSample(sound))
  for sample in range(0, getLength(sound)):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(sound, sample, value * factor)
  return sound

#Write a new function called goToEleven, ths function should take a sound as a 
#parameterFor each sample, if the sample value is greater than 0, it should 
#set the sample value to the maximum possible value: 32767 for sound with 
#bit-depth 16. If the sample value is less than 0, it should set the sample 
#value to the minimum possible value: -32768.
def goToEleven(sound):
  max = 127
  min = -127
  for sample in range(0, getLength(sound)):
    value = getSampleValueAt(sound, sample)
    if value > 0:
      setSampleValueAt(sound, sample, max)
    elif value < 0:
      setSampleValueAt(sound, sample, min)
  return sound

