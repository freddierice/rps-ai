#RockSolid
#created by Freddie Rice

#------------------ Imports ------------------#
import random

#---------------- Check First ----------------#
if input == '' :
  output = random.choice( ['R', 'S', 'P'] )
  g_list = [ (input[:], output[:]) ]
  rounds_played = 1
elif rounds_played <= 5 :
  output = random.choice( ['R', 'S', 'P'] )
  g_list = g_list + [ (input[:], output[:]) ]
  rounds_played += 1
else
  #setup the round
  rounds_played += 1
  
  #get the last 4 games.
  last_list = glist[-4:]
  
  #save possibilities in list of ["GUESS", PATTERN_LENGTH]
  
  #iterate through the list to find patterns
  i = 0
  pattern_max = 4
  while pattern_max > 0 :
    while i < rounds_played - pattern_max :
      if glist[i:i+pattern_max+1] == last_list :
	    
	  
  pattern_max -= 1
  
  output = random.choice( ['R', 'S', 'P'] )
  g_list = g_list + [ (input[:], output[:]) ]