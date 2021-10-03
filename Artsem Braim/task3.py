import string


class Cipher:

    def __init__(self, keyword):
        keyword_without_duplicates = []
        self._alphabet_to_encode = list(string.ascii_lowercase)

        for i in keyword:
            if i not in keyword_without_duplicates:
                keyword_without_duplicates.append(i)
                self._alphabet_to_encode.remove(i)

        self._alphabet = string.ascii_lowercase
        self._alphabet_to_encode = "".join(keyword_without_duplicates + self._alphabet_to_encode)

    def encode(self, s):
        encode_s = []
        for ch in s:
            is_upper = ch.isupper()
            i = self._alphabet.find(ch.lower())
            if i == -1:
                encode_s.append(ch)
            elif is_upper:
                encode_s.append(self._alphabet_to_encode[i].upper())
            else:
                encode_s.append(self._alphabet_to_encode[i])

        return "".join(encode_s)

    def decode(self, s):
        decode_s = []
        for ch in s:
            is_upper = ch.isupper()
            i = self._alphabet_to_encode.find(ch.lower())
            if i == -1:
                decode_s.append(ch)
            elif is_upper:
                decode_s.append(self._alphabet[i].upper())
            else:
                decode_s.append(self._alphabet[i])

        return "".join(decode_s)


if __name__ == "__main__":
    cipher = Cipher("crypto")
    print(cipher.encode("Hello world"))
    print(cipher.decode("Fjedhc dn atidsn"))
