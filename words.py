from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for lines in story:
    for words in lines.split():
        story_words.append(words.decode('utf-8'))
        
print(story_words)
story.close()
