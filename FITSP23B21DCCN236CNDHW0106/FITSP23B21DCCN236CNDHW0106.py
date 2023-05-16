#Đặng Minh Đức
# B21DCCN236
# Lý thuyết thông tin
# Nhóm G05
# Bài 6


from sympy import *
from sympy import symbols, Poly, gcd, div
import random
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
def check_polynomial_simplification(polynomial):
    x = symbols('x')
    poly = Poly(polynomial, x)
    gcd_poly = gcd(poly, poly.diff(x))
    return gcd_poly.is_one

def factorize_polynomial(n):
    x = symbols('x')
    polynomial = x**n + 1
    factors = factor(polynomial, modulus=2)
    return factors

def check_divisibility(polynomial1, polynomial2):
    if not polynomial1 or not polynomial2:
        return False
    x = symbols('x')
    _, remainder = div(polynomial1, polynomial2, domain='GF(2)')
    return remainder == 0

if __name__ == '__main__':

    x = symbols('x')
    # 1)Liệt kê tất cả các đa thức bất khả quy
    poly = []
    bit_repr = []
    test_1 = []
    with open('input/FITSP23B21DCCN236CNDHW0106(input 1).txt', 'r') as file:
        file = file.readlines()
        for testcase in file:
            digit = ''
            for i in range(len(testcase)-1, 0, -1):
                if testcase[i].isdigit():
                    digit = testcase[i] + digit
                if testcase[i] == ' ':
                    break
            test_1.append(digit)

        for i, testcase in enumerate(test_1):
            poly_ = []
            bit_repr_ = []
            for deg in range(int(testcase)+1, int(testcase)+2):
                for c in range(2**deg):
                    p = Poly([int(d)for d in bin(c)[2:].zfill(deg)], x, domain='GF(2)')
                    if not p.is_irreducible:
                        continue
                    if p.as_expr():
                        bit_repr_.append(str(p.all_coeffs()))
                        poly_.append(str(p.as_expr()))

            poly.append(poly_)
            bit_repr.append(bit_repr_)
    # print(len(test))
    with open('output/FITSP23B21DCCN236CNDHW0106(output 1).txt', 'w') as file:
        file.write('1) Liet ke tat ca cac da thuc bat kha quy\n')
        for i in range(len(test_1)):
            file.write(f'\nTest case {i+1}:')
            file.write(f'\n\n \tInput: Da thu bat kha quy bac {test_1[i]}\n\tOutput: \n\t isReverse = 0')
            for p, b in zip(poly[i], bit_repr[i]) :
                file.write(f'\n\t ({p}) : {b}')
            file.write('\n')

    # 2)Kiểm tra một đa thức cho trước có phải tối giản hay không
    test_2 = []
    s = set()
    for _ in range(5):
        random_number = random.randint(1, 10)
        s.add(random_number)
    for i in s:
        test_2.extend(binary_generate(i))
    # print(test_2)
    poly_transform = []
    for testcase in test_2:
        poly_transform.append(Poly(testcase, x, domain='GF(2)').as_expr())
    with open('input/FITSP23B21DCCN236CNDHW0106(input 2).txt', 'w') as file:
        for i in range(len(test_2)):
            file.write(f'Test case {i + 1} : {test_2[i]}\n')

    with open('output/FITSP23B21DCCN236CNDHW0106(output 2).txt', 'w') as file:
        file.write('2) Kiem tra mot da thuc cho truoc co phai toi gian hay khong\n')
        for i in range(len(test_2)):
            file.write(f'\nTest case {i + 1}:')
            check = check_polynomial_simplification(poly_transform[i])
            msg = 'Da thuc nay la da thuc toi gian' if check else 'Da thuc nay khong phai la da thuc toi gian'
            file.write(f'\n\n \tInput: {poly_transform[i]}\n\tOutput: {msg}\n')

    # 3) Phân tích x^n+1 thành các nhân tử tối giản

    test_3 = []
    with open('input/FITSP23B21DCCN236CNDHW0106(input 3).txt','r') as file:
        file = file.readlines()
        for testcase in file:
            digit = ''
            for i in range(len(testcase)-1, 0, -1):
                if testcase[i].isdigit():
                    digit = testcase[i] + digit
                if testcase[i] == ' ':
                    break
            test_3.append(digit)
    with open('output/FITSP23B21DCCN236CNDHW0106(output 3).txt', 'w') as file:
        file.write('2) Phan tich x^n + 1 thanh cac nhan tu toi gian \n')
        for i in range(len(test_3)):
            file.write(f'\nTest case {i + 1}:')
            file.write(f'\n\n \tInput: x^{test_3[i]} + 1\n\tOutput: {factorize_polynomial(int(test_3[i]))}\n')

    #4) Liệt kê tất cả các nhân tử (ước số) phân biệt của x^n+1
    test_4 = []
    poly_2 = []
    bit_repr_2 = []
    with open('input/FITSP23B21DCCN236CNDHW0106(input 4).txt', 'r') as file:
        file = file.readlines()
        for testcase in file:
            digit = ''
            for i in range(len(testcase)-1, 0, -1):
                if testcase[i].isdigit():
                    digit = testcase[i] + digit
                if testcase[i] == ' ':
                    break
            test_4.append(digit)
        for i, testcase in enumerate(test_4):
            poly_ = []
            bit_repr_ = []
            for deg in range(int(testcase)+1, int(testcase)+2):
                for c in range(2**deg):
                    p = Poly([int(d)for d in bin(c)[2:].zfill(deg)], x, domain='GF(2)')
                    if not p.is_irreducible:
                        continue
                    if p.as_expr():
                        # bit_repr_.append(str(p.all_coeffs()))
                        poly_.append(str(p.as_expr()))

            poly_2.append(poly_)
            # bit_repr_2.append(bit_repr_)
    max_digit = 0
    bin_poly = set()
    for i in range(len(test_4)):
        max_digit = max(max_digit, int(test_4[i]))
    for i in range(1, max_digit+2):
        binary = binary_generate(i)
        for code in binary:
            code_ = ""
            for bit in code:
                code_ += str(bit)
            bin_poly.add(code_)
    bin_poly_sort = sorted(bin_poly)
    # print(bin_poly_sort)
    poly_transform = set()
    for bin_ in bin_poly_sort:
        poly_transform.add(Poly([int(poly) for poly in bin_], x, domain='GF(2)'))
    poly_transform_sort = sorted(poly_transform,key=lambda poly: poly.degree())
    with open('output/FITSP23B21DCCN236CNDHW0106(output 4).txt', 'w') as file:
        file.write('4) Liet ke tat ca cac nhan tu uoc so phan biet cua x^n + 1')
        for i in range(len(test_4)):
            poly_root = Poly(x**(int(test_4[i])) + 1,x)
            file.write(f'\nTest case {i+1}:')
            file.write(f'\n\n \tInput: Da thuc {poly_root.as_expr()}\n\tOutput: \n\t isReverse = 0')
            p_ = []
            for p in poly_transform :
                if check_divisibility(poly_root, p):
                    p_.append(p)
            p_sort = sorted(p_ , key=lambda poly: poly.degree())
            for p_ in p_sort:
                file.write(f'\n\t ({p_.as_expr()})')
            file.write('\n')
