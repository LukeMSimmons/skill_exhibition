from datetime import datetime

class a_simple_class(): 
    """A class is helpful for organizing the properties and methods you want to apply to different types of objects"""
    
    default_arg = "You haven't provided an argument when arguing with this simple class"
    
    
    def __init__(self, default_arg=default_arg): 
        """init runs whenever a class is instantiated, this is sometimes called a constructor."""
        
        self.default_argument = default_arg
        self.day_of_week = datetime.today().strftime('%A')
        print('Instance instantiated')
        return
        
        
    def say_hello(self, name='friend'): 
        """Methods can operate on an instance of a class.  This method just says hi."""
        
        print(f'Hello {name}!')
        return
        
        
    def argue(self, an_argument=False): 
        """Methods can take in positional or keyword arguements, just like normal functions."""
        
        response = f"Hmm... {an_argument}, interesting.. \nI guess there's no arguing with that" if an_argument else self.default_argument
        print(response, 'on this fine %s.' % self.day_of_week) 
        return
    