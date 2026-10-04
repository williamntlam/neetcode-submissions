import random
import string

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Delimiter \r [Random characters] \n
        # Think this should work.
        delimiter = "\r"
        for _ in range(5):
            random_letter = random.choice(string.ascii_letters)
            delimiter += random_letter

        delimiter += "\n"
        
        self.delimiter = delimiter
        # Perform run-length encoding.
        encoded_string = ""
        for word in strs:
            encoded_string += word + delimiter

        return encoded_string


    def decode(self, s: str) -> List[str]:
        return s.split(self.delimiter)[0:-1]