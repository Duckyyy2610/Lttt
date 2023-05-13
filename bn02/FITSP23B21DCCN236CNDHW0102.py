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
        nodes.insert(0, parent)
    return nodes[0]


def generate_huffman_codes(node, code="", codes={}):
    if node.left is None and node.right is None:
        codes[node.symbol] = code
    else:
        generate_huffman_codes(node.left, code + "0", codes)
        generate_huffman_codes(node.right, code + "1", codes)
    return codes


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


def write_file(path, file_to_write, output):
    output_path = os.path.join(path, file_to_write)
    with open(output_path, 'w') as f:
        f.write(str(output))


def write_file_2(path, file_to_write, huffman_codes, probabilities):
    output_path = os.path.join(path, file_to_write)
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
    with open(output_path, 'w') as file:
        file.write('{\n')
        for k, v in output.items():
            file.write('\'' + str(k) + '\'' + ': ')
            file.write('\'' + str(v) + '\'' + '\n')
        file.write('}')


if __name__ == "__main__":
    huffman_codes_1 = {}  # phần 1
    huffman_codes_2 = {}  # phần 2
    decoded_string = ''

    # 1) Mã hóa biểu diễn nguồn theo phương pháp mã hóa Huffman
    symbol_probabilities = {
        'x_1': 0.125,
        'x_2': 0.25,
        'x_3': 0.125,
        'x_4': 0.5
    }

    root_node = build_huffman_tree(symbol_probabilities)
    # traverse(root_node)
    huffman_codes = generate_huffman_codes(root_node)
    huffman_codes_1 = huffman_codes.copy()
    huffman_codes.clear()

    # 2)Sử dụng hàm ở 1) thực hiện mã hóa một văn bản ký tự đọc vào từ file *.txt
    with open('C:\\hk2\\lttt\\btl\\bn02\input\\FITSP23B21DCCN236CNDHW0102.txt', 'r') as file:
        read_file = file.readlines()
        symbol_probabilities_2 = calculate_the_probability(read_file)
        root_node = build_huffman_tree(symbol_probabilities_2)
        huffman_codes = generate_huffman_codes(root_node)
        huffman_codes_2 = huffman_codes.copy()
        huffman_codes.clear()

    # 3) Giải mã cho một chuỗi mã cho trước được nhập từ bàn phím hoặc đọc từ file FITSP23B21DCCN236CNDHW0102 (decode).txt;
    # Sử dụng file FITSP23B21DCCN236CNDHW0102 (a-z character).txt để lấy ví dụ các kí tự sẽ được mã hóa như nào
    huffman_codes_from_atoz = {}
    with open('C:\\hk2\\lttt\\btl\\bn02\input\\FITSP23B21DCCN236CNDHW0102 (a-z, space, endline characters).txt',
              'r') as file:
        read_file = file.readlines()
        symbol_probabilities_3 = calculate_the_probability(read_file)
        root_node = build_huffman_tree(symbol_probabilities_3)
        huffman_codes_from_atoz = dict(sorted(generate_huffman_codes(root_node).items()))
        # print(huffman_codes_from_atoz)

    # Giải mã từ file FITSP23B21DCCN236CNDHW0102 (decode).txt
    with open('C:\\hk2\\lttt\\btl\\bn02\input\\FITSP23B21DCCN236CNDHW0102 (decode).txt', 'r') as file:
        read_file = file.readlines()
        code = read_file

        reverse_huffman_code = {v: k for k, v in huffman_codes_from_atoz.items()}

        # root_node = build_huffman_tree({k: 1 for k in huffman_codes_from_atoz.keys()})
        huffman_codes = generate_huffman_codes(root_node)

        for word in code:
            decoded_bit = ""
            for bit in word:
                decoded_bit += bit
                if decoded_bit in reverse_huffman_code:
                    decoded_string += reverse_huffman_code[decoded_bit]
                    decoded_bit = ""

        mapping_character_and_code = {}
        for x in decoded_string:
            mapping_character_and_code.update({x: huffman_codes_from_atoz[x]})
        symbol_probabilities_4 = calculate_the_probability(decoded_string)

    # 4, 5) Tính toán tham số, lưu vào file và hiển thị thông tin từ hảm write_file_2

    # Lưu vào file phần 1
    write_file_2('C:\\hk2\\lttt\\btl\\bn02\\output', 'FITSP23B21DCCN236CNDHW0102(output 1).txt', huffman_codes_1,
                 symbol_probabilities)

    # Lưu vào file phần 2
    write_file_2('C:\\hk2\\lttt\\btl\\bn02\\output', 'FITSP23B21DCCN236CNDHW0102(output 2).txt', huffman_codes_2,
                 symbol_probabilities_2)

    # Lưu vào file phần 3
    write_file('C:\\hk2\\lttt\\btl\\bn02\\output', 'FITSP23B21DCCN236CNDHW0102(output 3).txt', decoded_string)

    # Lưu vào file phần 3 khi đã giải mã
    write_file_2('C:\\hk2\\lttt\\btl\\bn02\\output', 'FITSP23B21DCCN236CNDHW0102(output 4).txt',
                 mapping_character_and_code, symbol_probabilities_4)
