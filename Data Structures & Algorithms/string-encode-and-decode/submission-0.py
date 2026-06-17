class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        for string in strs:
            encoded_str.append(str(len(string)) + "#" + string)
        return "".join(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded_str.append(word)

            i = j + 1 + length
        return decoded_str