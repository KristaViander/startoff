# MODULE FOR ASKING QUESTIONS FROM CONSOLE AND CONVERTING ANSWERS TO VARIOUS DATA TYPES
# -------------------------------------------------------------------------------------

# LIBRARIES AND MODULES

# CLASS DEFINITIONS

class Question():
    """A class containning methods to ask questions on console 
        and converting answers to various datatypes
    ."""
    
    def __init__(self, question):
        self.question = question

    def ask_user_float(self, loop):
        """Ask a question from the user and converts answer to a floating point number

        Args:
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as float, error message, error code, detailed error
            """
        
        # If loop argument is true use while loop until user input 
        if loop == True:

            while True:
                answer_txt = input(self.question)

                # Let's try to convert input to numeric
                try:
                    answer = float(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break

                # if an error occurs tell the user to check
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))


        else:
            answer_txt = input(question)

        # Let's try to convert input to numeric
        try:
            answer = float(answer_txt)
            result = (answer, 'OK', 0, 'Conversion successful')

        # if an error occurs tell the user to check
        except Exception as e:
            print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
            result = (0, 'Error', 1, str(e))

        return result
    
    def ask_user_float(self, loop):
        """Ask a question from the user and converts answer to a floating point number

        Args:
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as float, error message, error code, detailed error
            """
        
        # If loop argument si true use while loop until user input 
        if loop == True:

            while True:
                answer_txt = int(self.question)

                # Let's try to convert input to numeric
                try:
                    answer = int(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break

                # if an error occurs tell the user to check
                except Exception as e:
                    print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
                    result = (0, 'Error', 1, str(e))
            
        
        else:
            answer_txt = input(self.question)

        # Let's try to convert input to numeric
        try:
            answer = int(answer_txt)
            result = (answer, 'OK', 0, 'Conversion successful')

        # if an error occurs tell the user to check
        except Exception as e:
            print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
            result = (0, 'Error', 1, str(e))

        return result

if __name__ == "__main__":
    
    question = Question('Kuinka vanha olet? ')
    answer_and_error = question.ask_user_float(True)
    print(answer_and_error)