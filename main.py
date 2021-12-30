# #import statements
# # # import os
# # # import math
# #
# #
# # #constants
# #
# username = "kunab"
# print(username)


#loops
#if


# if (cond):
#     statement

# if (username.endswith("b")):
#     print("yes username ends with a")
# else:
#     print("No username doesn't ends with a")


# if (username.endswith("b")):
# #     print("yes username ends with b")
# # elif username.endswith("a"):
# #     print("yes username ends with a")
# # else:
# #     print("No username doesn't ends with a or b")


# multiple conditions

# if (username.endswith("b") and len(username) == 5):
#     print("both conditions are getting satisfied")


# if (username.endswith("b") or len(username) == 4):
#     print("both conditions are getting satisfied")

# #for loop
#
# username = "kunab"
# print(username)
#
#
# for each_element in username:
#     print(each_element)


# # for and if
#
email = "kunagmail.com"
#
# for each in email:
#     if each == "@":
#         print("its a valid email address")
# else:
#     print("its a invalid email address")

# continue and break

# email = "kunag@mail.com"

# for each in email:
#     print(each)
#     if (each == "@"):
#         break


# for each in email:
#     if (each == "@"):
#         continue
#     print(each)

# k = 10
#
# while (k > 5):
#     print("yes")
#     k -= 1  # k = k - 1


def each_gen(n):
    for element in n:
        yield element

k = each_gen(email)

print(k)

print(next(k))
print(next(k))


