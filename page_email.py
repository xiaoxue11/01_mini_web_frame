"""
Created on :  7:39 PM
Author : Xue Zhang
"""

import re


def unique_email_nums(emails):
    type_emails = []
    names = []
    count = 0
    for email in emails:
        is_valid = re.match(r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$", email)
        if is_valid:
            print(is_valid.group(1))
            name = name_match(is_valid.group(1))
            print(name)
            type_email = is_valid.group(2)
            if type_email not in type_emails:
                type_emails.append(type_email)
                count += 1
                names.append(name)
            elif name not in names:
                names.append(name)
                count += 1
        else:
            print("email address valid")
    print(names)
    print(type_emails)
    return count


def name_match(name):
    # ans = "A"
    ans = ""
    # result = re.match(r"([^\.^\+]+)(\.*)([^\+]*)(\+*)([0-9a-zA-Z_]*)$", name)
    for char in name:
        if char != ".":
            if char == '+':
                return ans
            ans += char
    print(ans)
    return ans


if __name__ == "__main__":
    emails_list = ["test.email@gmail.com", "test.email+spam@gmail.com", "testemail@gmail.com", "testemail@123.com",
                   "testemail+abcd@123.com", "+spam@gmail.com", "+spamabcd@gmail.com"]
    length = unique_email_nums(emails_list)
    print(length)

