S = "abcd"
indexes = [0, 2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
res = S

for i, val in enumerate(indexes):
    if S.find(sources[i], indexes[i], indexes[i] + len(sources[i])) != -1:
        res = res.replace(sources[i], targets[i])
