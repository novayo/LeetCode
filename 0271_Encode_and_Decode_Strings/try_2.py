class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        string = ''
        for s in strs:
            length = len(s)
            prefix = str(length).zfill(4)
            string += prefix + s
        return string

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        ret = []
        i = 0
        while i < len(s):
            prefix = s[i:i+4]
            i += 4
            
            length = int(prefix)
            ret.append(s[i:i+length])
            i += length
        
        return ret


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
