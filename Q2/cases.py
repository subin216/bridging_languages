import re
import urllib.request
import sys

#regexs
pascal_regex = r"(.*?)_([a-zA-Z])"
camel_regex = r"(.*?)_([a-zA-Z])"
snake_regex = r"(.+?)([A-Z])"
kebab_regex = r"(.*?)-([a-zA-Z])"


word = sys.argv[1]

def camel(match):
    # print(match.group(1))
    # print(match.group(2))

    return match.group(1) + match.group(2).upper()

def pascal(match):
    # print("wwwww")

    return match.group(1)[0].upper() + match.group(1)[1:] + match.group(2).upper()

def snake(match):
    # print("Asdfasdf")
    return match.group(1).lower() + "_" + match.group(2).lower()

def kebab(match):
    # print("eeeeeeee")
    return match.group(1) + match.group(2).upper()

functions = {"pascal": pascal, "camel": camel, "kebab": kebab, "snake":snake }

# print("word is", word)
# print("converting to:", sys.argv[2])

word = re.sub(camel_regex, functions[sys.argv[2]], word)

word = re.sub(pascal_regex, functions[sys.argv[2]], word)

word = re.sub(snake_regex, functions[sys.argv[2]], word)

word = re.sub(kebab_regex, functions[sys.argv[2]], word)

if(sys.argv[2] == "camel"):
    l = list(word)
    l[0] = l[0].lower()
    # print(l)
    word = "".join(l)
# print("after converting:", word)
sys.stdout.write(word)

