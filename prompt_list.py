from typing import List

class PromptList:
    """
    List of prompts data structure
    """
    def __init__(self, prompts=[]) -> None:
        self._prompts = prompts.copy()

    def unwrap_copy(self) -> List[str]:
        """
        generate a copy of all prompts\n
        return all prompts in the copy
        """
        return self._prompts.copy()

    def unwrap_same(self) -> List[str]:
        """
        return original object
        """
        return self._prompts
    
    def add_var_prompt(self, var_name, prompt) -> None:
        """
        create a prompt for initializing a variable
        """
        # self.add_prompt([f"Differentiate between heat and temperature", 0])
        self.add_prompt([f"Let {var_name} be {prompt}", 1])

    def add_rulebook_prompt(self, prompt) -> None:
        """
        create a prompt for creating a rulebook\n
        remember to tweak to your liking
        """
        #self.add_prompt([f"Create a rulebook to analyze a speech for effective argument: {prompt}", 0])
        self.add_prompt([f"Give a summary and rule-book for defective arguments according to {prompt}", 0])
    
    
    def add_argument_prompt(self, var_name, reference_var) -> None:
        """
        create a prompt for evaluation of var_name based on reference_var using arguments
        """

        self.add_prompt([f"Critique {var_name} for the defects in its arguments according to {reference_var}", 0])

    def add_rhetoric_prompt(self, var_name, reference_var) -> None:
        """
        create a prompt for evaluation of var_name based on reference_var using rhetoric
        """
        self.add_prompt([f"Critique {var_name} for the defects in its rhetoric according to {reference_var}", 0])
        
    
    def add_rating_prompt(self, var_name, reference_var) -> None:
        """
        create a prompt for rating of var_name based on reference_var from 1 through 100
        """
        self.add_prompt([f"Using {reference_var} give a rating for how defective the arguments are in {var_name} from 1 to 100. Give justifications for the ratings from {reference_var}, take it step by step.", 0])
    
    def add_reference_comparison(self, var1, var2, ref_var) -> None:
        self.add_prompt([f"Using {ref_var} compare {var1} and {var2} and tell me which is worse", 0])
    
    def add_prompt(self, prompt) -> None:
        """
        add your own custom prompt
        """
        self._prompts.append(prompt)
    
    def clear(self) -> None:
        """
        clear all prompts
        """
        self._prompts.clear()
    
    def remove_prompt(self, prompt) -> None:
        """
        remove prompt using the prompt
        """
        self._prompts.remove(prompt)
    
    def remove_prompt(self, index) -> int:
        """
        remove prompt using the index
        """
        try:
            del self._prompts[index]
            return 0
        except:
            IndexError("Prompt at index does not exist")
            return -1
    
    def pop_prompt(self, index) -> str:
        """
        simulataneously get and remove a prompt based on its index
        """
        return self._prompts.pop(index)

    def first(self) -> str:
        """
        get the first prompt
        """
        try:
            return self._prompts[0]
        except:
            LookupError("No first prompt")
    
    def last(self) -> str:
        """
        get the last prompt
        """
        try:
            return self._prompts[-1]
        except:
            LookupError("No last prompt")
    
    def __str__(self) -> str:        
        rv = "[\n"

        for arr, num in self._prompts:
            rv += "|"+str(arr) + f" {num}|" + ","
        
        return rv + "\n]"