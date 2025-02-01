
import collections

class Twitter:

    def __init__(self):
        """
        初始化数据结构。
        """
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        发布一条新推文。
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        # 将推文添加到用户列表中，并更新顺序值
        self.tweets[userId].append((self.order, tweetId))
        self.order -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        获取用户的最新十条推文。
        :type userId: int
        :rtype: List[int]
        """
        # 对用户关注的用户和自身发布的推文进行排序
        tweets = sorted(
            tweet for follower in self.following[userId] | {userId} 
            for tweet in self.tweets[follower]
        )[:10]

        # 提取推文ID
        return [tweet_id for _, tweet_id in tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        粉丝关注一个博主。如果操作无效，则应忽略。
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        粉丝取消关注一个博主。如果操作无效，则应忽略。
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
