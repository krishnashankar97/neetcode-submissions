class Twitter:

    def __init__(self):
        #self.count = 0
        self.tweets = []  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [userId, tweetId]
        self.tweets.append(tweet)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        n = len(self.tweets) - 1
        news = []
        while n >= 0 and len(news) < 10:
            t = self.tweets[n]
            uid, tid = t[0], t[1]
            if uid in self.followMap[userId] or uid == userId:
                news.append(tid)
            n -= 1
        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
