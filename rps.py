#created by Freddie Rice

#if this is the first round
if input == '' :
  output = random.choice( 'R', 'S', 'P' )
  rounds_played = 1
  player_list = [ input[:] ]
  comp_list = [ output[:] ]
else
  rounds_played += 1