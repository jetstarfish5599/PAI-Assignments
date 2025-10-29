#Q2 GulPhone PR info
#sample data
allPosts = [
    {'id': 1, 'text': 'I LOVE THE NEW #GULPHONE! BATERRY LIFE IS AMAZING.'},
    {'id': 2, 'text': 'MY #GULPHHONE IS A TOTAL DISASTER.THE SCREEN IS ALREADY BROKEN!'},
    {'id': 3, 'text': 'WORST CUSTOMER SERVICE EVER FROM @gulphonesupport.AVOID THIS.'},
    {'id': 4, 'text': 'THE @gulphonesupport team was helpful and resolved my issue. great service!'},
]

#keyword sets and punctuation list
PUNCTUATION_CHARS = '!@#$^&()_+{|}:"<>?/[]\''
STOPWORDS_SET = {'i','me','my','a','an','the','is','am','are','was','were','and','but','if','or','and','to','of','at','by','for','with','this','that'}
POSITIVE_WORDS_SET = {'love','amazing','great','helpful','resolved'}
NEGATIVE_WORDS_SET = {'disaster','broken','worst','avoid'}

#removes punct and stopwords
def preprocesstext(text, punctuationList, stopwordsSet):
    for ch in punctuationList:
        text = text.replace(ch, '')
    words = text.split()
    filtered = [w for w in words if w not in stopwordsSet]
    return filtered


#posts pos=+1 negg=-1
def analyzeposts(postsList, punctuation, stopwords, positive, negative):
    def score_post(post):
        words = preprocesstext(post['text'], punctuation, stopwords)
        score = sum([(1 if w in positive else -1 if w in negative else 0) for w in words])
        return {'id': post['id'], 'text': post['text'], 'score': score}
    return list(map(lambda p: score_post(p), postsList))


#get neg posts
def getflaggedposts(scoredPosts, negComments=-1):
    return [p for p in scoredPosts if p['score'] <= negComments]


#counts hashtags #,@ in neg posts
def findnegativetopics(flaggedPosts):
    topics = {}
    for post in flaggedPosts:
        words = post['text'].split()
        for w in words:
            if w.startswith('#') or w.startswith('@'):
                topics[w] = topics.get(w, 0) + 1
    return topics

#main 
scored = analyzeposts(allPosts, PUNCTUATION_CHARS, STOPWORDS_SET, POSITIVE_WORDS_SET, NEGATIVE_WORDS_SET)
flagged = getflaggedposts(scored)
topics = findnegativetopics(flagged)

#output
print("all posts with emotional scores:")
for p in scored:
    print(f"post {p['id']}: score = {p['score']}")

print("\nflagged negative posts:")
for p in flagged:
    print(f"post {p['id']}: {p['text']}")

print("\ntrending negative topics:")
print(topics)
