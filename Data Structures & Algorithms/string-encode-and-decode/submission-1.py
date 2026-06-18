class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_strs = ""
        for s in strs:
            encoded_strs += (f"{s}:;")
        return encoded_strs
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        return s[:-2].split(":;")
        