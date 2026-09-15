class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for x in strs:
            encoded += f'{len(x)}#{x}'
        return encoded

    def decode(self, s: str) -> List[str]:
        start = 0
        end = 0
        
        pos = 0
        length = 0
        decoded = []

        while pos < len(s):
            while s[pos] != '#':
                pos += 1
            
            length = int(s[start:pos])

            start = pos + 1
            end = start + length

            decoded.append(s[start:end])

            pos = end
            start = end

            
            
        return decoded
        



