import heapq


class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = {}
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId] = [(self.ts, tweetId)] + self.posts.get(userId, [])
        self.ts += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        h = []
        res = []

        if userId not in self.following:
            self.following[userId] = {userId}
        else:
            s = self.following[userId]
            s.add(userId)
            self.following[userId] = s

        for user in self.following[userId]:
            if user in self.posts:
                ind = 0
                ts, pid = self.posts[user][ind]
                h.append((ts, pid, user, ind + 1))
        heapq.heapify_max(h)
        while h and len(res) < 10:
            ts, pid, user, ind = heapq.heappop_max(h)
            res.append(pid)
            if ind < len(self.posts[user]):
                ts, pid = self.posts[user][ind]
                heapq.heappush_max(h, (ts, pid, user, ind + 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = {followeeId}
        else:
            s = self.following[followerId]
            s.add(followeeId)
            self.following[followerId] = s

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
