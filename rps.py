#RockSolid
#created by Freddie Rice

#------------------ Imports ------------------#
import random

#---------------- Check First ----------------#
if input == '' :
  output = random.choice( ['R', 'S', 'P'] )
  p_list = [ input[:] ]
  c_list = [ output[:] ]
  rounds_played = 1
elif rounds_played <= 5 :
  output = random.choice( ['R', 'S', 'P'] )
  p_list = p_list + [ input[:] ]
  c_list = c_list + [ output[:] ]
  rounds_played += 1
else
  #setup the round
  rounds_played += 1
  #print rounds_played
  p_list = p_list + [ input[:] ]
  
  
  
  output = random.choice( ['R', 'S', 'P'] )
  c_list = c_list + [ output[:] ]