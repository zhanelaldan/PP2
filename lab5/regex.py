import re
# ex1
x1 = re.match("a*b", "abbb")
print(x1)
# ex2
x2 = re.match("ab{2}|b{3}", "abbb")
print(x2)
# ex3
print(re.findall(".+_+.+", "zhanel_aldan"))
# ex4
print(re.findall("[A-Z]{1}[a-z]+", "Zhanel"))
# ex5
print(re.match("^a.*b$", "afdsfb"))
# ex6
txt = "a r,.n"
txt = txt.replace(".", ":").replace(",", ":").replace(" ", ":")
print(txt)
# ex7
txt = "zhanel_aldan"
txt = txt.title().replace("_", "")
print(txt)
# ex8
txt = "uniVEErsity"
print(re.split("[A-Z]", txt))
# ex9
txt = "ZHanel"
print(re.sub(r"(\w)([A-Z])", r"\1 \2", txt))
# ex10
txt = "zhanelAldan"
string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt).lower()
print(string)