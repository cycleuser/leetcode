
class Solution:
    # 定义一个类来解决寻找第n个超级丑数的问题

    def nthSuperUglyNumber(self, n: int, primes: list) -> int:
        # 初始化结果数组arr，包含第一个超级丑数1；primes是给定的素数列表；
        arr, heap, used = [1], primes[:], set()

        # 从第二个超级丑数开始计算直到第n个
        for i in range(1, n):
            # 取出堆中的最小值作为当前super-ugly number
            num = heapq.heappop(heap)
            
            # 将该值加入结果数组
            arr.append(num)

            # 生成新的super-ugly number并加入堆中，同时标记为已使用
            for p in primes:
                new_num = p * num
                if new_num not in used:
                    heapq.heappush(heap, new_num)
                    used.add(new_num)
        
        # 返回结果数组中的最后一个元素即第n个super-ugly number
        return arr[-1]
