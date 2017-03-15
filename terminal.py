from chatterbot.adapters.input import InputAdapter
from chatterbot.conversation import Statement
from chatterbot.utils.read_input import input_function


class TerminalAdapter(InputAdapter):
    """
    A simple adapter that allows ChatterBot to
    communicate through the terminal.
    """

    def process_input(self,take_question):
        """
        Read the user's input from the terminal.
        """
         
        file = open("D:/bots/flask/testfile.txt", "r") 
        readf=file.read()
        if readf=='':
            user_input = "What is nab"
            
        else:
            user_input = readf
            print("user input is",user_input)
        return Statement(user_input)
