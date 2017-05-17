import requests, re, sys
'''
selenium can be used here; sometimes resp.text doesn't load what we want,
although it should. We can exploit selenium's WebDriverWait functionality.
'''
rank_patt = r'(#[\d,]+) in Books'
isbn_patt = r'([^\d]+) (\d+)'

with open('fav_books.txt', 'r') as f:
    for eachLine in f:
        book = re.search(isbn_patt, eachLine)
        try:
            if len(sys.argv) == 2 and sys.argv[1] == 'html':
                print '<p>',
            print book.group(1),
            amazon_page = requests.get('http://www.amazon.com/dp/'+book.group(2))
            rank = re.search(rank_patt, amazon_page.text).group(1)
            print ":", rank,
            if len(sys.argv) == 2 and sys.argv[1] == 'html':
                print '</p>',
        except:
            print ": Failed to load rank",
            if len(sys.argv) == 2 and sys.argv[1] == 'html':
                print '</p>',
        print
