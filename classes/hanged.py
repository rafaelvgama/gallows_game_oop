# Hanged class deals with how the drawings will be shown during the game match.
#
class Hanged():

    # Constructor
    #
    def __init__(self):
        self.body_draw = ['''
     __________   
    | /      |   
    |/        
    |         
    |          
    |        
    |         
    |
    ================''', '''
    __________   
    | /      |   
    |/       O 
    |         
    |          
    |        
    |         
    |
    ================''', '''
    __________   
    | /      |   
    |/       O 
    |        ^  
    |          
    |        
    |         
    |
    ================''', '''
    __________   
    | /      |   
    |/       O 
    |        ^  
    |      / | \  
    |        
    |         
    |
    ================''', '''
    __________   
    | /      |   
    |/       O 
    |        ^  
    |      / | \   
    |        ^
    |         
    |
    ================''', '''
    __________   
    | /      |   
    |/       O 
    |        ^  
    |      / | \   
    |        ^
    |      /   \  
    |
    ================''']

    # Prints the gallows drawing based on the number of player's wrong guesses.
    #
    #  @param position: Number of player's wrong guesses.
    #
    def draw_gallows(self, position):
        print(self.body_draw[position])

    # Defines the player's wrong guesses limit.
    #
    #  @return Wrong guesses limit.
    #
    def get_error_limit(self):
        return len(self.body_draw) - 1
