import re

#regexs
camel_pascal_regex = r"(.*?)_([a-zA-Z])"
snake_regex = r"(.+?)([A-Z])"
kebab_regex = r"(.*?)-([a-zA-Z])"


def camel(match):
    return match.group(1) + match.group(2).upper()

def pascal(match):
    return match.group(1)[0].upper() + match.group(1)[1:] + match.group(2).upper()

def snake(match):
    return match.group(1).lower() + "_" + match.group(2).lower()

def kebab(match):
    return match.group(1) + match.group(2).upper()

snake_words = """add
matrix_add
diagonal_matrix_add
pseudo_inverse""".splitlines()

results = [re.sub(camel_pascal_regex, camel, w, 0) for w in snake_words]
print("snake_to_camel: ")
print(results)


pascal_words = """MyClass
MyClassFactory
MyClassFactoryBuilder
MyClassFactoryBuilderImpl
myInstance
myInstance2
abc
patternMatcher""".splitlines()

results = [re.sub(camel_pascal_regex, snake, w, 0) for w in pascal_words]
print("pascal_to_snake: ")
print(results)


kebab_words = """paul-add
matrix-add
diagonal-matrix-add
pseudo-inverse""".splitlines()

results = [re.sub(kebab_regex, pascal, w, 0) for w in kebab_words]
print("kebab_to_pascal: ")
print(results)


