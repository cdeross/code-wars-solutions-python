'''
Extract the domain name from a URL

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
'''

#im noob,dont judge too harshly
def domain_name(url):
    per_ind = 0
    i = 0
    url_str = ""
    if url[0] == "h":
        while i < len(url):
            if str(url[0] + url[1]) == "//":
                break
            else:
                url = url[1:]
        url = url[2:]
        if str(url[0] + url[1] + url[2] + url[3]) == "www.":
            url = url[4:]
        for i in url:
            if i == ".":
                return url_str
            else:
                url_str = url_str + i
    elif str(url[0] + url[1] + url[2] + url[3]) == "www.":
        url = url[4:]
        for i in url:
            if i == ".":
                return url_str
            else:
                url_str = url_str + i
    else:
        for i in url:
            if i == ".":
                return url_str
            else:
                url_str += i