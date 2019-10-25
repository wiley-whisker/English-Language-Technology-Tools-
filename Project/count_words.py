import string

DATA_DIR_STR = r'C:\Users\Wiley\Documents\Datasets\aclImdb\test\pos'


def remove_apostrophes(text: str) -> str:
    indeces_for_del = set()
    for i in range(len(text)):
        if text[i] == "'":
            for j in range(i, len(text)):
                if text[j] == ' ':
                    break
                indeces_for_del.add(j)
    new_text = ''
    for i in range(len(text)):
        if i not in indeces_for_del:
            new_text += text[i]
    return new_text


def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans('', '', string.punctuation))


def remove_capitalization(text: str) -> str:
    return text.lower()


def clean_text(text: str) -> str:
    text = remove_apostrophes(text)
    text = remove_punctuation(text)
    text = remove_capitalization(text)
    return text


def count_words(text, count={}):
    for word in text.split(' '):
        if word not in count.keys():
            count[word] = 1
        else:
            count[word] += 1
    return count


def main():
    text = """Hello"""
    d = {'hello': 1}
    text = clean_text(text)
    print(count_words(text, d))


if __name__ == '__main__':
    main()
