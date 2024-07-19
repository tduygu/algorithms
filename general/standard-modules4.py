import webbrowser

user_term = input("Enter a search term: ").replace(" ","+")

webbrowser.open("https://google.com?q="+user_term)