import math

ts1 = [3, 0, 2, 40, 1]


def anomaly_tst(ts, w, threshold):
    all_subseq = []
    distance = []
    cushion = w -1
    for i in range(len(ts)):
        if i < len(ts) - cushion:
            subseq = [ts[i]]
            while len(subseq) < w:
                subseq.append(ts[i + 1])
                i += 1
            all_subseq.append(subseq)
    for j in range(len(all_subseq)):
        if j < len(all_subseq) - 1:
            distance.append(math.dist(all_subseq[j], all_subseq[j + 1]))
            print(all_subseq[j], all_subseq[j + 1])
    print(distance)
    if max(distance) > threshold:
        return -1
    return distance.index(max(distance))


print(anomaly_tst(ts1, 2, 40))
print(anomaly_tst(ts1, 2, 100))
print(anomaly_tst([10, 10, 10, 10, 0, 0, 10], 2, 12))
print(anomaly_tst([10, 10, 10, 10, 10, 10, 10], 3, 12))
