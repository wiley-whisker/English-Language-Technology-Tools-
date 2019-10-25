import os
from language_check import LanguageTool
from count_words import count_words, clean_text
import matplotlib.pyplot as plt


DATA_DIR_STR = r'C:\Users\Wiley\Documents\Datasets\aclImdb\test\pos'

def main():
    lt = LanguageTool('en-US')

    dir = os.fsencode(DATA_DIR_STR)
    count = {}

    for file in os.listdir(dir)[:10]:
        filename = os.fsdecode(file)
        path = os.path.join(dir, file)
        print(path)
        with open(path) as f:
            for line in f.readlines():
                print(line)
                cleaned_line = clean_text(line)
                count = count_words(cleaned_line, count)
                # matches = lt.check(line)
                # for match in matches:
                #     print(match)
        #print(os.path.join(os.fsdecode(dir), filename))
    words = sorted(count.items(), key=lambda x : x[1], reverse=True)
    for item in words:
        print(item)
    x = [i for i in range(1, len(words)+1)]
    y = [num[1] for num in words]
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
