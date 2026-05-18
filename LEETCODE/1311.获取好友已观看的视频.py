class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        from collections import deque
        from collections import defaultdict
        vis = [-1]*len(friends)
        vis[id] = 0
        q = deque([id])

        friend_level = []
        while q:
            x = q.popleft()
            for y in friends[x]:
                if vis[y] < 0:
                    vis[y] = vis[x] + 1
                    if vis[y] == level:
                        friend_level.append(y)
                        continue
                    q.append(y)

        video_cnt = defaultdict(int)
        for friend in friend_level:
            for video in watchedVideos[friend]:
                video_cnt[video] += 1

        video_cnt = sorted(video_cnt.items(), key = lambda x: (x[1], x[0]))
        return [key[0] for key in video_cnt]

watchedVideos = [["A","B"],["C"],["B","C"],["D"]] 
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1
print(Solution().watchedVideosByFriends(watchedVideos, friends, id, level))