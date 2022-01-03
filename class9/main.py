import re

# sentence = 'TextView mVisiblity.getValue doesn\'t is false'
# sentence2 = "TextView: mVisiblity.getValue is doesn't false"

# result = re.findall("pattern", string)

# ^starting $end  \s \n \t

# result = re.findall("^T.", sentence) # start with T and next char
#
# print(result)

# result = re.findall("^T.{3}", sentence) # start with T and next char
#
# print(result)

# result = re.findall("^T.*", sentence) #
#
# print(result)

# result = re.findall("^T.*\.", sentence) #
#
# print(result)

# result = re.findall("^T.*\s", sentence) #
# #
# # print(result)


# result = re.findall("^T\w+\s", sentence) #
#
# print(result)

# # [a-zA-Z1-9@:;/<>]
# result = re.findall("[a-e]", "happy new bc") #
#
# print(result)


# result = re.findall("[^a-e\s]", "happy new bc") #
#
# print(result)


# sed, wc -lv '":;  assignment


sentence = "03-17 16:13:38.875  2227  2227 D textview: visible is system.call.count gt 0"

compiler = re.compile("(\d{2}:\d{2}:\d{2}\.\d{3}).*(\s.*:)")

result = compiler.findall(sentence)

print(result)


# assignment




