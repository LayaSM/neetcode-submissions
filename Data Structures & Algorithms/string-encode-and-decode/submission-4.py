class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            start_of_str = j + 1
            end_of_str = start_of_str + length

            result.append(s[start_of_str : end_of_str])

            i = end_of_str

        return result


