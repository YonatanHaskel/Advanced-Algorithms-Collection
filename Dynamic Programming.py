def DP_min_edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert = dp[i][j - 1]
                delete = dp[i - 1][j]
                replace = dp[i - 1][j - 1]
                dp[i][j] = min(insert, delete, replace) + 1
    return dp[m][n]


s1, s2 = "yonatan", "shira"

min_dist = DP_min_edit_distance(s1, s2)

print(f'minimum operations to turn {s1} to {s2}: {min_dist}')

def DP_min_palindrom_cuts(s):
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                is_pal[i][j] = True
    dp = n * [0]
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            dp[i] = min(dp[j - 1] + 1 for j in range(1, i + 1) if is_pal[j][i])
    return dp[-1]

s = "yonatan"
min_cut = DP_min_palindrom_cuts(s)
print(f'minimum amount of cuts to divide {s} into palindroms: {min_cut}')


def DP_longest_bitonic_subsequence(arr):
    dp_inc = [1] * len(arr)
    parent_inc = [-1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and dp_inc[j] + 1 > dp_inc[i]:
                dp_inc[i] = dp_inc[j] + 1
                parent_inc[i] = j
    dp_dec = [1] * len(arr)
    parent_dec = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[i] and dp_dec[j] + 1 > dp_dec[i]:
                dp_dec[i] = dp_dec[j] + 1
                parent_dec[i] = j
    max_len, max_i = 0, 0
    for i in range(len(arr)):
        if dp_inc[i] + dp_dec[i] - 1 > max_len:
            max_len = dp_inc[i] + dp_dec[i] - 1
            max_i = i
    inc_seq = []
    i = max_i
    while i != -1:
        inc_seq.append(arr[i])
        i = parent_inc[i]
    inc_seq.reverse()
    dec_seq = []
    i = parent_dec[max_i]
    while i != -1:
        dec_seq.append(arr[i])
        i = parent_dec[i]
    bitonic_seq = inc_seq + dec_seq
    return f'longest bitonic subsequence is {bitonic_seq} and its length is {max_len}'

try_arr = [1, 3, 11, 7, 9, 0, 4, 2]
print(DP_longest_bitonic_subsequence(try_arr))


def DP_longest_zigzag_subsequence(arr):
    up = [1] * len(arr)
    down = [1] * len(arr)
    prev_up = [-1] * len(arr)
    prev_down = [-1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                if down[j] + 1 > up[i]:
                    up[i] = down[j] + 1
                    prev_up[i] = j
            elif arr[j] > arr[i]:
                if up[j] + 1 > down[i]:
                    down[i] = up[j] + 1
                    prev_down[i] = j
    if max(up) > max(down):
        length = max(up)
        i = up.index(max(up))
        use_up = True
    else:
        length = max(down)
        i = down.index(max(down))
        use_up = False
    zigzag_seq = []
    while i != -1:
        zigzag_seq.append(arr[i])
        if use_up:
            i = prev_up[i]
            use_up = False
        else:
            i = prev_down[i]
            use_up = True
    zigzag_seq.reverse()
    return f'The longest zigzag subsequence in the array is {zigzag_seq} and its length is {length}'


try_arr2 = [1, 14, 19, 2, 0, 6, 8, 3, 15, 16, 9]
print(DP_longest_zigzag_subsequence(try_arr2))


def DP_fibonacci_sequence(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    dp = [0, 1] + [-1] * (n - 2)
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp


n = 20
print(f'first {n} numbers in the fibonacci sequence: {DP_fibonacci_sequence(n)}')


def DP_burst_baloons_max_coins(baloons):
    baloons = [1] + baloons + [1]
    n = len(baloons)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for i in range(left + 1, right):
                coins = dp[left][i] + (baloons[left] * baloons[i] * baloons[right]) + dp[i][right]
                dp[left][right] = max(dp[left][right], coins)
    return dp[0][n - 1]


baloons = [14, 6, 27, 13, 2, 22, 33, 9]
print(f'maximum amount of coins that can be earned in the burst baloons game for this group of baloons: {DP_burst_baloons_max_coins(baloons)}')


def DP_counting_distinct_subsequences(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]


S1, S2 = "blubblub", "blub"
print(f"There are {DP_counting_distinct_subsequences(S1, S2)} ways to create {S2} from {S1}'s subsequences")


def DP_weighted_interval_scheduling(tasks):
    n = len(tasks)
    sorted_tasks = sorted(tasks, key=lambda x: x["end"])
    dp = [0] * n
    parent = [-1] * n
    def last_legal_task(i):
        for j in range(i - 1, -1, -1):
            if sorted_tasks[j]["end"] <= sorted_tasks[i]["start"]:
                return j
        return -1
    for i in range(n):
        incl_weight = sorted_tasks[i]["weight"]
        j = last_legal_task(i)
        if j != -1:
            incl_weight += dp[j]
        if i > 0:
            if incl_weight > dp[i - 1]:
                dp[i] = incl_weight
                parent[i] = j
            else:
                dp[i] = dp[i - 1]
                parent[i] = parent[i - 1]
        else:
            dp[i] = incl_weight
            parent[i] = j
    selected_tasks = []
    i = n - 1
    while i >= 0:
        j = parent[i]
        if j == -1 or dp[i] != dp[j]:
            selected_tasks.append(sorted_tasks[i])
            i = j
        else:
            i -= 1
    selected_tasks.reverse()
    return f'The maximum profit from Non-overlapping tasks avilable is {dp[-1]} and the tasks are {selected_tasks}'


tasks = [{"task": "developing", "start": 9, "end": 12, "weight": 2500},
         {"task": "Debugging", "start": 14, "end": 15, "weight": 1400},
         {"task": "Code Review", "start": 10, "end": 11, "weight": 900},
         {"task": "Test", "start": 17, "end": 19, "weight": 1800}]

print(DP_weighted_interval_scheduling(tasks))