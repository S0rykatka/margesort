tab = [10,85,18,63,22,53,15,67]

def marge_sort(tab):
    if len(tab) > 1:
        s = len(tab) // 2
        left = tab[:s]
        right = tab[s:]
        marge_sort(left)
        marge_sort(right)
        marge(tab, left, right)

def marge(tab, left, right):
    i_l = 0
    i_p = 0
    i_tab = 0
    while i_l < len(left) and i_p < len(right):
        if left[i_l] < right[i_p]:
            tab[i_tab] = left[i_l]
            i_l += 1
        else:
            tab[i_tab] = right[i_p]
            i_p += 1
        i_tab += 1
    while i_l < len(left):
        tab[i_tab] = left[i_l]
        i_tab += 1
        i_l += 1
    while i_p < len(right):
        tab[i_tab] = right[i_p]
        i_tab += 1
        i_p += 1

marge_sort(tab)
print(tab)