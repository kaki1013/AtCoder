N = int(input())
A = list(map(int, input().split()))

m_idx = A.index(max(A))
B = A[:m_idx] + A[m_idx+1:]
print(A.index(max(B))+1)
