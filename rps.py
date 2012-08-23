#RockSolid
#created by Freddie Rice

#------------------ Imports ------------------#
import random

#---------------- Utility Defs ---------------#


#---------------- Check First ----------------#
if input == '' :
  output = random.choice( ['R', 'S', 'P'] )
  g_list = [ ]
  rounds_played = 1
elif rounds_played <= 5 :
  g_list.append( [ (input[:], output[:]) ] )
  output = random.choice( ['R', 'S', 'P'] )
  rounds_played += 1
else:
  g_list.append([(input[:], output[:])])
  #setup the round
  rounds_played += 1
  
  #get the last 4 games.
  last_list = glist[-4:]
  
  #save possibilities in list of ["GUESS", PATTERN_LENGTH]
  guess_list = []
  
  #iterate through the list to find patterns
  i = 0
  pattern_max = 4
  while pattern_max > 0 :
    while i < rounds_played - pattern_max :
      if glist[i:i+pattern_max+1] == last_list :
	    
	  i += 1
    pattern_max -= 1
  
  output = random.choice( ['R', 'S', 'P'] )
  