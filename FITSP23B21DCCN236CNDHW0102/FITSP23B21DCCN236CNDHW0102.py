import os
from functools import cmp_to_key
import math


class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.probability < other.probability


def build_huffman_tree(symbol_probabilities):
    nodes = [Node(symbol, probability) for symbol, probability in symbol_probabilities.items()]
    while len(nodes) > 1:
        if len(nodes) > 2:
            nodes.sort()
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(symbol_probabilities, left.probability + right.probability)
        parent.left = left
        parent.right = right
        if len(nodes) > 2:
            nodes.append(parent)
        else:
            nodes.insert(0, parent)  # do chỉ còn 2 phần tử nên cần giữ đúng thứ tự k sắp xếp
    return nodes[0]


def generate_huffman_codes(node, code="", codes={}):
    if node.left is None and node.right is None:
        codes[node.symbol] = code
    else:
        generate_huffman_codes(node.left, code + "0", codes)
        generate_huffman_codes(node.right, code + "1", codes)
    return codes

def build_huffman(symbol_probabilities):
    root_node = build_huffman_tree(symbol_probabilities)
    huffman_codes = generate_huffman_codes(root_node)
    return huffman_codes

def traverse(node):
    if node is None:
        return
    traverse(node.left)
    print(node.symbol, node.probability, end='\n')
    traverse(node.right)


def calculate_the_probability(words):
    characters = 0
    symbol_probabilities = {}
    for word in words:
        # xử lý kí tự xuống dòng của file
        word_1 = list(word)
        end = len(word) - 1
        if word_1[end] == 'n' and ord(word_1[end - 1]) == 97:
            x = word_1.pop(end - 1)
            y = word_1.pop(end - 1)
            x += y
            characters += 1
            if x in symbol_probabilities:
                symbol_probabilities[x] += 1
            else:
                symbol_probabilities[x] = 1

        for char in word_1:
            if char in symbol_probabilities:
                symbol_probabilities[char] += 1
            else:
                symbol_probabilities[char] = 1
            characters += 1
    for key in symbol_probabilities.keys():
        symbol_probabilities[key] /= characters
    return symbol_probabilities


def calculate_average_code_length(probabilities, codewords):
    avg_length = 0
    for p, c in zip(probabilities, codewords):
        avg_length += p * len(c)
    return avg_length


def calculate_variance(avg_length, probabilities, codewords):
    variance = 0
    for p, c in zip(probabilities, codewords):
        variance += p * ((len(c) - avg_length) ** 2)
    return variance


def write_file(file_to_write, mode, part, testcase, input, output):
    output_path = file_to_write
    with open(output_path, mode) as file:
        file.write(part)
        file.write(testcase)
        file.write(f'\n\tInput: {input} \tOutput: {output}\n')


def write_file_2(file_to_write, mode, part, testcase, input, huffman_codes, probabilities):
    output_path = file_to_write
    elsym = list(probabilities.keys())
    elprob = [float(round(x, 5)) for x in probabilities.values()]
    elcodeword = list(dict(sorted(huffman_codes.items(), key=lambda x: x[0])).values())
    avg_l = calculate_average_code_length(elprob, elcodeword)
    sigma_l_2 = calculate_variance(avg_l, elprob, elcodeword)
    output = {}
    output.update({'source': 'X',
                   'elsym': elsym,
                   'elprob': elprob,
                   'elcodeword': elcodeword,
                   'avg_l': avg_l,
                   'sigma_l_2': sigma_l_2,
                   'isNewLess': 1,
                   'isLeftBranchZero': 1,
                   })
    with open(output_path, mode) as file:
        file.write(part)
        file.write(testcase)
        file.write(f'\n\tInput:\n\t{input} \n\tOutput:')
        file.write('\n\t{\n')
        for k, v in output.items():
            file.write('\t\t\'' + str(k) + '\'' + ': ')
            file.write('\'' + str(v) + '\'' + '\n')
        file.write('\t}\n')


if __name__ == "__main__":
    # 1) Mã hóa biểu diễn nguồn theo phương pháp mã hóa Huffman
    symbol_probabilities = {
        'x_1': 0.125,
        'x_2': 0.25,
        'x_3': 0.125,
        'x_4': 0.5
    }

    huffman_code = build_huffman(symbol_probabilities)
    huffman_code_1 = huffman_code.copy()
    # Lưu vào file phần 1
    write_file_2('FITSP23B21DCCN236CNDHW0102(output).txt',
                 'w',
                 '1) Ma hoa bieu dien nguon theo phuong phap ma hoa huffman\n',
                 '',
                 str(symbol_probabilities),
                 build_huffman(symbol_probabilities),
                 symbol_probabilities)
    huffman_code.clear()

    # 2)Sử dụng hàm ở 1) thực hiện mã hóa một văn bản ký tự đọc vào từ file *.txt
    test_list_2 = []
    symbol_probabilities_list = []
    huffman_codes_list = []
    pos = 0
    with open('FITSP23B21DCCN236CNDHW0102(input).txt', 'r') as file:
        read_file = file.readlines()
        # Tách các test
        read_ = ""
        for i, read in enumerate(read_file):
            if 'Test case' in read and read_:
                test_list_2.append(read_)
                read_ = ""
            elif '3)' in read:
                test_list_2.append(read_)
                pos = i
                break
            elif '2)' not in read and 'Test case' not in read:
                read_ += '\t' + read


        for test in test_list_2:
            # print(test)
            symbol_probabilities = calculate_the_probability(test)
            symbol_probabilities_list.append(symbol_probabilities)
            huffman_codes_list.append(build_huffman(symbol_probabilities))

    # Lưu vào file phần 2
    for i,test in enumerate(test_list_2):
        part = ""
        if i==0:
            part += '\n2) Su dung ham o 1) ma hoa 1 van ban doc tu file\n'
        write_file_2('FITSP23B21DCCN236CNDHW0102(output).txt',
                    'a',
                     part,
                    f'\nTest case {i+1}:\n',
                     test,
                     huffman_codes_list[i],
                     symbol_probabilities_list[i])

    #3) Giải mã dãy bit
    huffman_code = {'\n': '1010000', ' ': '001', 'a': '1011', 'b': '1100', 'c': '1111', 'd': '0001',
                    'e': '011011', 'f': '0101', 'g': '01100', 'h': '011100', 'i': '1010001', 'j': '101001',
                    'k': '011110', 'l': '011111', 'm': '11011', 'n': '00000', 'o': '10101', 'p': '1110',
                    'q': '011010', 'r': '11010', 's': '1000', 't': '010001', 'u': '010010', 'v': '1001',
                    'w': '010011', 'x': '00001', 'y': '011101', 'z': '010000'}
    # print(huffman_code)
    with open('FITSP23B21DCCN236CNDHW0102(input).txt', 'r') as file:
        read_file = file.readlines()
        test_list_3 = []
        read = ""
        for i in range(pos+1, len(read_file)):
            # print(read_file[i])
            if 'Test case' in read_file[i] and read_file[i]:
                test_list_3.append(read)
                read = ""
            else:
                read += read_file[i]
            if i == len(read_file)-1:
                test_list_3.append(read)
                break
        reverse_huffman_code = {v: k for k, v in huffman_code.items()}
        # root_node = build_huffman_tree({k: 1 for k in huffman_code.keys()})
        # huffman_codes = generate_huffman_codes(root_node)
        # print(huffman_codes)
        decoded_string_list = []
        for test in test_list_3:
            if test:
                decoded_string = ""
                # print(test[0:len(test)-1])
                decoded_bit = ""
                for word in test:
                    decoded_bit += word
                    # print(decoded_bit,end='')
                    if decoded_bit in reverse_huffman_code:
                        decoded_string += reverse_huffman_code[decoded_bit]
                        decoded_bit = ""
                # print(decoded_string)
                decoded_string_list.append(decoded_string)
        # print(decoded_string_list)

    # Lưu vào file phần 3
    for i, decode in enumerate(decoded_string_list):
        part = ""
        if not i:
            part += '\n3) Giai ma tu file\n'
        write_file('FITSP23B21DCCN236CNDHW0102(output).txt',
                   'a',
                   part,
                   f'\nTest case {i+1}:\n',
                   test_list_3[i+1],
                   decode)

