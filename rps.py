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
  
  #initialize new weights each turn
  s_count = 0
  r_count = 0
  p_count = 0
  
  #while statement that adds to the weights 
  #based on patterns.
  
  output = random.choice( ['R', 'S', 'P'] )
  g_list = g_list + [ (input[:], output[:]) ]