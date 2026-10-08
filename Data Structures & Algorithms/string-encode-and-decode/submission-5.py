class Solution:
    def encode(self, strs: List[str]) -> str:
        length_encodings = ""
        encoding = ""

        for string in strs:
            length_encodings += str(len(string)) + "#"

            for char in string:
                encoding += chr((ord(char) + 2) % 256)

        return str(len(length_encodings)) + "#" + length_encodings + encoding

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        # Find the end of the length section size
        delimiter_index = s.index("#")
        num_encodings = int(s[:delimiter_index])

        # Collect all the string lengths
        length_start = delimiter_index + 1
        length_end = length_start + num_encodings

        collected_lengths = s[length_start:length_end]

        lengths = [
            int(length)
            for length in collected_lengths.split("#")
            if length != ""
        ]

        # Handle empty list
        if not lengths:
            return []

        # Compute starting positions
        start_positions = [length_end]

        for index in range(len(lengths) - 1):
            start_positions.append(
                start_positions[-1] + lengths[index]
            )

        # Decode the strings
        decodings = []

        for index in range(len(start_positions)):
            start_position = start_positions[index]
            encoding_length = lengths[index]

            decoded_string = ""

            for char_index in range(
                start_position,
                start_position + encoding_length
            ):
                decoded_string += chr(
                    (ord(s[char_index]) - 2) % 256
                )

            decodings.append(decoded_string)

        return decodings