#Đặng Minh Đức
# B21DCCN236
# Lý thuyết thông tin
# Nhóm G05
# Bài 3


import collections
import ast
def is_uniform_code(codes):
    x = len(codes[0])
    for code in codes:
        if len(code) != x:
            return False
    return True

def is_linearly_independent_code(codes):
    codeset = set(codes)
    return len(codeset) == len(codes)


def is_unique_decodable_code(codes):
    for i in codes:
        for j in codes:
            if i != j:
                if i in j or j in i:
                    return False
    return True


def is_prefix(code_1, code_2):
    len_1 = len(code_1)
    len_2 = len(code_2)
    min_len = min(len_1, len_2)
    for i in range(min_len):
        if code_1[i] != code_2[i]:
            return True
    return False
def is_prefix_code(codes):
    for i in codes:
        for j in codes:
            if i != j:
                if not is_prefix(i, j):
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

def is_linearly_independent(codes):
    m = len(codes)
    n = len(codes[0])
    matrix_int = [[int(x) for x in row] for row in codes]
    for i in range(m):
        for j in range(m):
            if i != j:
                vector_i = matrix_int[i]
                vector_j = matrix_int[j]
                result = [vector_i[k] - vector_j[k] for k in range(n)]
                if all(v == 0 for v in result):
                    return False
    return True


def is_basis_code(codes):
    if not is_uniform_code(codes) or not is_linearly_independent(codes):
        return False
    return True

def is_cyclic_code(codes):
    if not is_uniform_code(codes):
        return False
    codeset = set(codes)
    #dịch vòng bằng số từ mã trong bộ mã
    for i in range(len(codes)):
        new_code = ""
        new_code += codes[i][len(codes[i])-1]
        new_code += codes[i][0:len(codes[i])-1]
        if new_code not in codeset:
            return False
    return True

def is_permutation(code_1, code_2):
    code_1_freq = collections.Counter(code_1)
    code_2_freq = collections.Counter(code_2)
    if code_1_freq['0'] == code_2_freq['0'] and code_1_freq['1'] == code_2_freq['1'] and len(code_1_freq) == len(code_2_freq):
        return True
    return False

def is_permutation_code(codes):
    if not is_uniform_code(codes):
        return False
    for i in codes:
        for j in codes:
            if i != j:
                if not is_permutation(i, j):
                    return False
    return True

if __name__ == "__main__":
    code = {
        'codename': 'C',
        'codewords': ['1','01','001','000']
    }

    code_2 = {
        'codename': 'C2',
        'codewords':['001','100','010']
    }


    # with open('C:\\hk2\\lttt\\btl\\bn03\FITSP23B21DCCN236CNDHW0103(input).txt', 'r') as file:
    #     read_file = file.readlines()
    #     codename_list = []
    #     codewords_list = []
    #     test_file = []
    #     for data in read_file:
    #         if 'codewords' in data:
    #             codename_list.append("""{'codename':'C',""")
    #             codewords_item = ""
    #             new_data = data.strip()
    #             for char in new_data:
    #                 if ord(char) != 97 and char != 'n':
    #                     codewords_item += char
    #             codewords_item += "}"
    #             codewords_list.append(codewords_item)
    #
    #     for i in range(len(codename_list)):
    #         # print(codename_list[i] + codewords_list[i])
    #         test_file.append(ast.literal_eval(codename_list[i] + codewords_list[i]))
    #     cnt = 1
    # print(test_file)
    test = [
    {
        'codename': 'C',
        'codewords': ['1', '01', '001', '000']
    },
    {
        'codename': 'C',
        'codewords': ['000', '001', '100', '101']
    },
    {
        'codename': 'C',
        'codewords': ['01', '00', '110']
    },
    {
        'codename': 'C',
        'codewords': ['110', '011', '000', '101']
    },
    {
        'codename': 'C',
        'codewords': ['1100', '0011', '0001', '1011']
    },
    {
        'codename': 'C',
        'codewords': ['11010', '00111', '00011', '11011', '11111']
    },
    {
        'codename': 'C',
        'codewords': ['1', '01', '0001', '000']
    },
    {
        'codename': 'C',
        'codewords': ['001', '100', '010']
    },
    {
        'codename': 'C',
        'codewords': ['110110', '001111', '000111', '11011', '111111']
    },
    {
        'codename': 'C',
        'codewords': ['110100', '001111', '000110', '1100011', '111101', '0101011']
    }
    ]
    cnt = 1
    with open('FITSP23B21DCCN236CNDHW0103.txt', 'w') as file:
        for testcase in test:
            # 1) Cho biết các đặc tính cơ bản của bộ mã: đều/không đều,suy biến hay không suy biến,
            # minh họa suy biến (nếu có), giải mã duy nhất nhay không, minh họa giải mã không duy nhất (nếu có),
            # có tính prefix hay không, minh họa không prefix (nếu có)
            file.write("Test case " + str(cnt) +': \n')
            file.write('\tInput: '+str(testcase)+'\n' + '\tOutput:\n')
            if is_uniform_code(testcase['codewords']):
                file.write("\t\tBo ma la ma deu\n")
            else:
                file.write("\t\tBo ma khong phai la ma deu\n")

            if is_linearly_independent_code(testcase['codewords']):
                file.write("\t\tBo ma la ma khong suy bien\n")
            else:
                file.write("\t\tBo ma la ma suy bien\n")
            if is_unique_decodable_code(testcase['codewords']):
                file.write("\t\tBo ma la ma co kha nang giai ma duy nhat\n")
            else:
                file.write("\t\tBo ma khong phai la ma co kha nang giai ma duy nhat\n")

            if is_prefix_code(testcase['codewords']):
                file.write("\t\tBo ma la ma prefix\n")
            else:
                file.write("\t\tBo ma khong phai la ma prefix\n")

            # 2) Bộ mã có phải là mã khối tuyến tính?
            if is_linear_block_code(testcase['codewords']):
                file.write("\t\tBo ma la ma khoi tuyen tinh\n")
            else:
                file.write("\t\tBo ma khong phai la ma khoi tuyen tinh\n")

            # 3) Tập các véc-tơ mã đã cho có phải là hệ cơ sở
            if is_basis_code(testcase['codewords']):
                file.write("\t\tBo ma la mot he co so\n")
            else:
                file.write("\t\tBo ma khong phai la mot he co so\n")

            # 4) Bộ mã đã cho có phải mã vòng (mã cyclic) tuyến tính?
            if is_cyclic_code(testcase['codewords']):
                file.write("\t\tBo ma la ma vong (ma cyclic)\n")
            else:
                file.write("\t\tBo ma khong phai la ma vong (ma cyclic)\n")

            # 5) Với hai bộ mã, chúng có phải là một (là hoán vị của nhau)
            if is_permutation_code(testcase['codewords']):
                file.write("\t\tVoi 2 bo ma bat ky chung la hoan vi cua nhau\n")
            else:
                file.write("\t\tVoi 2 bo ma bat ky chung khong phai la hoan vi cua nhau\n\n")
            cnt+=1







