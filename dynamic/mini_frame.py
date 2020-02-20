import re

URL_PATHS = {}


def router(url):
    def set_func(func):
        URL_PATHS[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


def unique_email_nums():
    type_emails = []
    names = []
    count = 0
    with open("./dynamic/emails.txt", "r") as f:
        for email in f.readlines():
            is_valid = re.match(r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$", email)
            if is_valid:
                name = name_match(is_valid.group(1))
                type_email = is_valid.group(2)
                if type_email not in type_emails:
                    type_emails.append(type_email)
                    count += 1
                    names.append(name)
                elif name not in names:
                    names.append(name)
                    count += 1
            else:
                print("email address invalid")
    return count


def name_match(name):
    ans = ""
    if not name:
        return ans
    for char in name:
        if char != ".":
            if char == '+':
                return ans
            ans += char
    return ans


@router(r'/index.html')
def index(ret):
    content = ''
    try:
        f = open('./templates/index.html', 'r')
    except FileNotFoundError:
        raise FileNotFoundError("No such file")
    else:
        content = f.read()
        f.close()
        count = unique_email_nums()
        content = re.sub(r'{%values%}', str(count), content)
        return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['file_path']
    try:
        for url, func in URL_PATHS.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
            else:
                return "no such page-{}".format(file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        return str(env) + '-----404--->%s\n'
