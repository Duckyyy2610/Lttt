import numpy as np
import collections
def is_uniform_code(codes):
    x = len(codes[0])
    for code in codes:
        if len(code) != x:
            return False
    return True

def is_linear_block_code(codes):
    if not is_uniform_code(codes):
        return False
    check = 0
    for i in range(len(codes)):
        counter = collections.Counter(codes[i])
        if counter['0'] and not counter['1']:
            check = 1
    if not check:
        return False
    codeset = set(codes)
    for code_1 in codes:
        for code_2 in codes:
            if code_1 != code_2:
                code = ""
                for i in range(len(code_1)):
                    code += str(int(code_1[i])^int(code_2[i]))
                if code not in codeset:
                    return False
    return True

def binary_generate(n):
    end = 0
    binary = []
    a = [0] * n
    binary.append(a)
    cnt=0
    while not end:
        i = n - 1
        while i>=0 and a[i] == 1:
            a[i] = 0
            i-=1
        if i>=0:
            a[i] = 1
            binary.append(a.copy())
            # print(binary[cnt])
            cnt+=1
        else:
            end=1
    return binary
def HtoP(H):
    n = np.shape(H)[1]
    k = n - np.shape(H)[0]
    PK = H[:, n - k:n]
    P = np.transpose(PK)
    return P.astype(int)

def HtoG(H):
    n = np.shape(H)[1]
    k = n - np.shape(H)[0]
    P = HtoP(H)
    Ik = np.eye(k)
    G = np.concatenate((P, Ik), axis=1)
    return G.astype(int)
def matrix_multiply(a, b):
    m = len(a)
    n = len(b[0])
    result = [[0] * n ] *m
    for i in range(m):
        for j in range(n):
            for k in range(len(b)):
                result[i][j] ^= (a[i][k] * b[k][j])
    return result

def check_valid_code(c, H):
    H_t = [list(x) for x in zip(*H)]
    if len(c[0]) != len(H_t):
        return False
    result = matrix_multiply(c, H_t)
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j]:
                return False
    return True
def hamming_distance(c):
    hamming_distance_ = 1000000000
    for code_1 in c:
        for code_2 in c:
            if code_1 != code_2:
                code = ""
                for i in range(len(code_1)):
                    code += str(int(code_1[i]) ^ int(code_2[i]))
                counter = collections.Counter(code)
                hamming_distance_ = min(hamming_distance_, counter['1'])
    return hamming_distance_

if __name__=='__main__':
    H = np.array([[1,0,1,1,1,0,0],
                  [0,1,0,1,1,1,0],
                  [0,0,1,0,1,1,1]])


    #1) Tìm dmin dựa theo số cột của ma trận kiểm tra H


    test = binary_generate(7)

    for i in range(len(H[0])):
        H[0][i] ^= H[2][i]
    G = HtoG(H)
    m = binary_generate(4)
    c = []
    for i in range(len(m)):
        a = []
        a.append(m[i])
        result = matrix_multiply(a, G)
        codeword = ''
        for i in range(len(result[0])):
            codeword += str(result[0][i])
        c.append(codeword)
    # print(c)

    cnt = 1
    with open('FITSP23B21DCCN236CNDHW0104.txt', 'w') as file:
        # 3) Liệt kê các từ mã cho bộ mã
        file.write('3) Cac tu ma cua bo ma la:\n')
        for i in range(len(c)):
            for j in range(len(c[0])):
                file.write(c[i][j] + ' ')
            file.write('\n')

        #4)Tìm dmin theo định nghĩa
        file.write('4) dmin theo dinh nghia: '+ str(hamming_distance(c))+'\n')

        # 5) Tìm dmin theo tính chất của mã khối tuyến tính
        if is_linear_block_code(c):
            hd = 1000000000
            for i in range(len(c)):
                counter = collections.Counter(c[i])
                if counter['1']:
                    hd = min(hd, counter['1'])
            file.write('5) dmin theo tinh chat: ' + str(hamming_distance(c)) + '\n')
        else:
            file.write('5) dmin theo dinh nghia: ' + str(hamming_distance(c)) + '\n')
        #2) Kiểm tra một vec-tơ cho trước có phải là một vec-tơ mã hợp lệ
        file.write('2) Kiem tra mot vec-to cho truoc co phai la 1 vecto ma hop le\n')
        for testcase in test:
            a = []
            file.write('Test case ' + str(cnt) + ':' + '\n\tInput: ' + str(testcase) + '\n' + '\tOutput: ')
            a.append(testcase)
            if check_valid_code(a, H):
                file.write("La tu ma hop le\n")
            else:
                file.write("Khong la tu ma hop le\n")
            cnt += 1

