class Solution:
    MOD = 10 ** 9 + 7

    def matMul(self, A, B):
        MOD = self.MOD
        n = len(A)
        m = len(B[0])
        k = len(B)

        C = [[0] * m for _ in range(n)]

        for i in range(n):
            for t in range(k):
                if A[i][t] == 0:
                    continue
                x = A[i][t]
                for j in range(m):
                    C[i][j] = (C[i][j] + x * B[t][j]) % MOD
        return C

    def matPow(self, A, e):
        n = len(A)
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            res[i][i] = 1

        while e:
            if e & 1:
                res = self.matMul(res, A)
            A = self.matMul(A, A)
            e >>= 1
        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = self.MOD
        m = r - l + 1

        if n == 1:
            return m

        if n == 2:
            return m * (m - 1) % MOD

        size = 2 * m

        # Transition matrix
        T = [[0] * size for _ in range(size)]

        # up -> down
        for v in range(m):
            for x in range(v):
                T[m + x][v] = 1

        # down -> up
        for v in range(m):
            for x in range(v + 1, m):
                T[x][m + v] = 1

        # Initial state (length = 2)
        S = [[0] for _ in range(size)]
        for i in range(m):
            S[i][0] = i
            S[m + i][0] = m - 1 - i

        T = self.matPow(T, n - 2)
        ans = self.matMul(T, S)

        return sum(x[0] for x in ans) % MOD