#Лабораторная работа 3, список
def find_missing_nums(nums):
    n = len(nums)
    u = []
    m = False
    for p in range (1,n+1):
        for q in range (0,n):
            if p == nums[q]:
                m = True
                continue
        if not m:
            u.append(i)
        m = False
    return u
