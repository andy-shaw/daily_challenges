'''
Andy Shaw
11/24/2014

Web scraper challenge to determine mood of comments in a youtube post.

http://www.reddit.com/r/dailyprogrammer/comments/2nauiv/20141124_challenge_190_easy_webscraping_sentiments/

'''
import urllib
import sys
import re

from pprint import pprint

YOUTUBE_BASE_URL = 'https://www.youtube.com/all_comments?v='

comment_div = re.compile(r'<div class="comment-text-content">(.*)</div>.*')

def pluralize(num):
    if num > 1: return 's'
    return ''

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 1:
        print 'USAGE: python mood_youtube_comment_scraper.py URL'

    #pull out just the video bit
    s = re.split('[&|?]', args[0])
    video_url = ''
    for t in s:
        if 'v=' == t[:2]:
            video_url = t[2:]

    opener = urllib.FancyURLopener({})
    page = opener.open(YOUTUBE_BASE_URL + video_url).read()

    lines = page.split('\n')
    
    comments = []
    for line in lines:
        r = comment_div.match(line)
        if r:
            comments.append(r.group(1))

    happy = ['love','loved','like','liked','awesome','amazing','good','great','excellent']
    sad = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst'] 

    num_happy = 0
    num_sad = 0

    for comment in comments:
        for word in happy: num_happy += 1 if word in comment else 0
        for word in sad: num_sad += 1 if word in comment else 0

    print 'From a sample size of {0} comments, the responses to this video are mostly {1}.'.format(len(comments), ('happy' if num_happy > num_sad else 'sad'))
    print 'It contained {happy} happy keyword{plural_happy} and {sad} sad keyword{plural_sad}.'.format(happy=num_happy, plural_happy=pluralize(num_happy), sad=num_sad, plural_sad=pluralize(num_sad))