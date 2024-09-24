def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            print([j,j + i + 1])
            yield text[j:j + i + 1]

a = all_variants("ebc")
for i in a:
    print(i)