def zero_mat(n, p):
    """
    영 행열 생성
    입력값 : 생성하고자 할 영 행렬의 크기 n행, p열
    출력값: nxp 영 행열 Z
    """
    Z = []
    for i in range(0, n):
        row = []
        for j in range(0, p):
            row.append(0)
        Z.append(row)
    return (Z)

def deepcopy(A):
    """
    깊은 복사 (deepcopy) 구현
    입력값 : 깊은 복사를 하고자 하는 행렬 리스트 A
    출력값 : 깊은 복사 된 결과 행령 리스트 res
    """
    if type(A) == list:
        n = len(A)
        p = len(A[0])
        res = zero_mat(n, p)
        for i in range(0,n):
            for j in range(0,p):
                res[i][j]=A[i][j]
        return res
    else:
        n = len(A)
        res = []
        for i in range(0,n):
            res.append(A[i])
        return res

def v_add(u, v):
    """
    벡터의 덧셈
    입력값 : 더하고자 하는 벡터 u, v
    출력갑 : 벡터 u , v의 덥셈결과 w
    """
    w=[]
    n = len(u)
    for i in range(0, n):
        val = u[i] + v[i]
        w.append(val)
    return w

def v_subtract(u, v):
    """
    벡터의 뺄셈
    입력값 : 빼고자하는 벡터 u, v
    출력값 : 벡터의 뺄샘결과 w
    """
    w=[]
    n=len(u)
    for i in range(0, n):
        val = u[i] - v[i]
        w.append(val)
    return w

def scalar_v_mul(a, u):
    """
    벡터의 스칼라 곱
    입력값: 스칼라 a, 벡터 리스트 u
    출렵값: 스칼라 a와 벡터 리스트 u의 곱 결과 w
    """
    n = len(u)
    w = []
    for i in range(0, n):
        val = a * u[i]
        w.append(val)
    return w

def v_mul(u, v):
    """
    벡터의 원소 곱
    입력값: 벡터 리스트 u, v
    출력값: 벡터 리스트 u, v의 원소 곱 결과 w
    """
    w=[]
    n=len(u)
    for i in range(0, n):
        val = u[i] * v[i]
        w.append(w)
    return w

def v_biv(u,v):
    """
    벡터의 원소 나눗셈
    입력값: 곱하고자 하는 벡터 리스트 u, v
    출력값: 벡터 리스트 u, v의 원소 곱 결과 w
    """
    w=[]
    n = len(u)
    for i in range(0, n):
        val = u[i] / v[i]
        w.append(val)
    return w

def add(A, B):
    """
    행열 A와 B의 원소합
    입력갑: 행렬 A와 B
    출력갑: 행렬 A와 B의 원소합 결과 res
    """
    n = len(A)
    p = len(A[0])
    res =[]
    for i in range(0,n):
        row=[]
        for j in range(0,p):
            val = A[i][j] + B[i][j]
            row.append(val)
        res.append(row)
    return res

def subtract(A, B):
    """
    행열 A와 B의 뺄샘
    입력갑: 행렬 A와 B
    출력갑: 행렬 A와 B의 뺄샘
    """
    n = len(A)
    p = len(A[0])
    res =[]
    for i in range(0,n):
        row=[]
        for j in range(0,p):
            val = A[i][j] - B[i][j]
            row.append(val)
        res.append(row)
    return res

def scarla_mul(b, A):
    """
    행열의 스칼라 곱
    입력값: 스칼라 b, 행렬 A
    출력값: 자연수 b와 행렬 A의 곱
    """
    n = len(A)
    p = len(A[0])
    for i in range(0,n):
        row=[]
        for j in range(0, p):
            val = b * A[i][j]
            row.append(val)
    return row

def ele_product(A, B):
    """
    행렬의 원소 곱
    입력값: 곱할 행렬 A와 B
    출력값: 행렬곱의 결과 C
    """
    n = len(A)
    p = len(A[0])
    for i in range(0, n):
        C=[]
        for j in range(0, p):
            val = A[i][j] * B[i][j]
            C.append(val)
    return C

def matmul(A, B):
    """
    행렬의 행렬 곱
    입력값: 행렬 곱을 수행할 행렬 A, B
    출력값: 행렬 A와 B의 곱 결과인 행렬 res"""
    n = len(A)
    p1 = len(A[0])
    p2 = len(B[0])
    res=[]
    for i in range(0, n):
        row=[]
        for j in range(0, p2):
            val=0
            for k in range(0, p1):
                val += A[i][k] * B[k][j]
            row.append(val)
        res.append(row)
    return res

def transpose(A):
    """
    행렬의 전치 행렬
    입력값: 전치할 행렬 A
    출력값: 행렬 A의 전치행렬 B
    """
    C=[]
    n=len(A)
    p=len(A[0])
    for i in range(0, p):
        row=[]
        for j in range(0, n):
            val = A[j][i]
            row.append(val)
        C.append(row)
    return C