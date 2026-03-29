def longest_palindromic_sequence(s):
    def chars_editor(s):
        t = ""
        for char in s:
            t += "#" + char
        t += "#"
        return t
    t = chars_editor(s)
    n = len(t)
    p = [0] * n
    center, right = 0, 0
    for i in range(n):
        mirror = center * 2 - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while i - (p[i] + 1) >= 0 and i + (p[i] + 1) < n and t[i - (p[i] + 1)] == t[i + (p[i] + 1)]:
            p[i] += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
    max_len, max_center = 0, 0
    for i in range(n):
        if p[i] > max_len:
            max_len = p[i]
            max_center = i
    start = (max_center - max_len) // 2
    lcs = s[start:start + max_len]
    return f'The longest palindromic sequence in the string is {lcs} and its length is {max_len}'

print(longest_palindromic_sequence("yonatan"))


def prefix_match_length(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r - i] == s[r]:
                r += 1
                z[i] = r - i
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                z[i] = r - i + 1
            while r + 1 < n and s[r + 1 - i] == s[r + 1]:
                r += 1
                z[i] = r - i + 1
    return f'longest prefix match length per index in {s} is {z}'


print(prefix_match_length("aabxcaahaabxgaab"))


def all_pattern_positions(t, p):
    m, n = len(p), len(t)
    def lps_array(p):
        i, j = 1, 0
        lps = [0] * m
        while i < m:
            if p[i] == p[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j - 1]
        return lps
    lps = lps_array(p)
    i, j = 0, 0
    matches = []
    while i < n:
        if t[i] == p[j]:
            i += 1
            j += 1
            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
    return f"The pattern appearances' positions in the text are {matches}"


print(all_pattern_positions("abbaaaxdabaabx", "ab"))


def lexicographicly_min_spin(s):
    t = s + s
    i, j = 0, 1
    off_set = 0
    while i < len(s) and j < len(s) and off_set < len(s):
        if t[i + off_set] == t[j + off_set]:
            off_set += 1
            continue
        elif t[i + off_set] > t[j + off_set]:
            i = i + off_set + 1
            if i == j:
                i += 1
        else:
            j = j + off_set + 1
            if i == j:
                j += 1
        off_set = 0
    k = min(i, j)
    return f'The lexicographicly minimal spin of the string is {s[k:] + s[:k]}'


print(lexicographicly_min_spin("aabbabaxaxb"))


def lyndons_factorization(s):
    i, n = 0, len(s)
    factors = []
    while i < n:
        j = i + 1
        k = i
        while j < n and s[k] <= s[j]:
            if s[k] < s[j]:
                k = i
            else:
                k += 1
            j += 1
        l = j - k
        while i <= k:
            factors.append(s[i:i + l])
            i += l
    return f'all lyndon factors in {s}: {factors}'


print(lyndons_factorization("abababa"))


def longest_unique_characters_strings_set(strings):
    def string_to_mask(s):
        mask = 0
        for c in s:
            bit = ord(c) - ord('a')
            if mask & (1 << bit):
                return 0
            mask |= (1 << bit)
        return mask

    masks = [(string_to_mask(s), s) for s in strings]
    valid_strings = [(s, m) for m, s in masks if m != 0]
    dp = {0: []}
    for string, string_mask in valid_strings:
        new_dp = dp.copy()
        for mask, string_list in dp.items():
            if mask & string_mask == 0:
                new_mask = mask | string_mask
                new_dp[new_mask] = string_list + [string]
        dp = new_dp
    max_mask = max(dp.keys(), key=lambda m: bin(m).count('1'))
    subset_strings = dp[max_mask]
    return f'The longest unique characters strings set is {subset_strings}'


strings = ['aabxdfg', 'fjdaaxb', 'opbxaftgd', 'lkcn']
print(longest_unique_characters_strings_set(strings))