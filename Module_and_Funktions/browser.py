import webbrowser

# webbrowser.open("https://www.python.org/", new=1)
# webbrowser.open("https://docs.python.org/3.8/library/webbrowser")
# help(webbrowser)

# for i in range(10):
#     print(i, i * i, i * 3, sep=": ", end=' ')

chrome = webbrowser.get(using='google-chrome')
chrome.open_new("https://docs.python.org/3.8/library/webbrowser")

