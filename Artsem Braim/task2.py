import re


def most_common_words(filepath, number_of_words=3):
    with open(filepath) as file:
        text = file.read().lower()
        words = re.split(r"\.|,|\s+", text)
        frequency = dict()
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        frequency.pop("", None)
        sorted_frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}
        most_common = []
        i = 0
        for k, v in sorted_frequency.items():
            most_common.append(k)
            i += 1
            if i == number_of_words:
                break

        return most_common


if __name__ == "__main__":
    print(most_common_words("../data/lorem_ipsum.txt", number_of_words=500))
