# https://github.com/meer-khan/Art-Gallery-App-Flutter/commits/main


import requests, re
url = "https://github.com/ZhangGongjie/thesis/commits/master"
# url = "https://github.com/ZhangGongjie/ZhangGongjie.github.io/commits/master"
text = requests.get(url=url).text

print(text)

pattern = re.compile(r"\w+\s+\d{1,2},\s+\d{3,4}", re.I|re.M)
print(pattern)
match = pattern.findall(text)
print(match)
# Commits on Mar 31, 2022