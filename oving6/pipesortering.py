def quick_sort(liste, lo, hi):
    p = partition(liste, lo, hi)
    quick_sort(liste, lo, p - 1)
    quick_sort(liste, p + 1, hi)

def partition(liste, lo, hi):
    pivot = liste[hi]
    i = lo
    for j in range(lo, hi):
        if liste[j] <= pivot:
            liste[i], liste[j] = liste[j], liste[i]
            i += 1
    liste[i], liste[hi] = liste[hi], liste[i]
    return i

def merge_sort(m):
    if len(m) <= 1:
        return m
    n = merge
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(n(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result


def binary_search(liste, value, find_lower):
    low = 0
    high = len(liste)-1
    while low <= high:
        mid = (low + high) // 2
        if liste[mid] > value:
            high = mid-1
        elif liste[mid] < value:
            low = mid+1
        else:
            return liste[mid]
    if find_lower:
        if low != 0:
            return liste[low - 1]
        else:
            return liste[low]
    else:
        if high != len(liste) - 1:
            return liste[high + 1]
        else:
            return liste[high]

def finn(liste, nedre, ovre):
    return [binary_search(liste, nedre, True), binary_search(liste, ovre, False)]


def main():
    from sys import stdin
    liste = []
    for x in stdin.readline().split():
        liste.append(int(x)) #  Kanskje mulig aa gjore dette raskere?

    #quick_sort(liste, 0, len(liste) - 1)
    liste = merge_sort(liste)
    f = finn
    for linje in stdin:
        ord = linje.split()
        resultat = f(liste, int(ord[0]), int(ord[1]))
        print str(resultat[0]) + " " + str(resultat[1])

main()