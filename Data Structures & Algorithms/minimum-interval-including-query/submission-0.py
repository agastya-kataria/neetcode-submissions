class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedQueries = sorted(queries)

        heap = []
        res = {}
        i = 0

        for q in sortedQueries:

            # Add every interval that has started
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            # Remove intervals that ended before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Smallest remaining interval contains q
            if heap:
                res[q] = heap[0][0]
            else:
                res[q] = -1

        return [res[q] for q in queries]