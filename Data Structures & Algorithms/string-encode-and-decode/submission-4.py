class Solution:

    def encode(self, strs: List[str]) -> str:
        res = b""

        for s in strs:
            encoded = s.encode('utf-8')
            res += len(encoded).to_bytes(4, 'big') + encoded

        return res.hex()

    def decode(self, s: str) -> List[str]:
        data = bytes.fromhex(s)
        res = []
        i = 0

        while i < len(data):
            length = int.from_bytes(data[i : i + 4], 'big')
            word = data[i + 4 : i + 4 + length].decode('utf-8')
            res.append(word)
            i += 4 + length

        return res