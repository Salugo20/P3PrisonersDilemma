
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.'''
    
   
    if (their_history.count('c')>1) or (my_score > their_score):
        return 'c'
    else:
        return 'b'
        
          
    '''Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return ('b')
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: If you're winning or opponent has colluded more than betrayed the past three moves, collude. If neither, betray.
    if test_move(my_history='',
              their_history='bbb', 
              my_score=600,
              their_score=500,
              result='c'):
         print ('Test passed')
    if test_move(my_history='',
              their_history='cbc', 
              my_score=600,
              their_score=500,
              result='c'):
         print ('Test passed')
    if test_move(my_history='',
              their_history='cbc', 
              my_score=500,
              their_score=600,
              result='c'):
         print ('Test passed')
    if test_move(my_history='',
              their_history='bcb', 
              my_score=500,
              their_score=600,
              result='b'):
         print ('Test passed')
     