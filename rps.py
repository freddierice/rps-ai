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
  pattern_max = 4
  pattern_min = 2
  while pattern_max >= pattern_min :
    i = 0
    while i < rounds_played - pattern_max - 2 : #don't look at the very last one
      if glist[i:i+pattern_max+1] == last_list :
	    guess_list.append( [glist[i+pattern_max+1][0], pattern_max] )
	  i += 1
	if glist[i:i+pattern_max+1] == last_list :  #very last case: depends on input
	  guess_list.append( input, pattern_max] )
    pattern_max -= 1
  
  output = random.choice( ['R', 'S', 'P'] )
  