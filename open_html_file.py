import webbrowser

browser = webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s')
name_html_file = "C:\\Users\\inxtc\\Documents\\その他\\Python開発\\10_rakus\\index.html"

browser.open(name_html_file)

print("Open Page := {}".format(name_html_file))