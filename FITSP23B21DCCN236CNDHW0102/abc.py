# 3) Giải mã cho một chuỗi mã cho trước được nhập từ bàn phím hoặc đọc từ file FITSP23B21DCCN236CNDHW0102 (decode).txt;
    # Sử dụng file FITSP23B21DCCN236CNDHW0102 (a-z character).txt để lấy ví dụ các kí tự sẽ được mã hóa như nào
    huffman_codes_from_atoz = {}
    with open('FITSP23B21DCCN236CNDHW0102 (a-z, space, endline characters).txt',
              'r') as file:
        read_file = file.readlines()
        symbol_probabilities_3 = calculate_the_probability(read_file)
        root_node = build_huffman_tree(symbol_probabilities_3)
        huffman_codes_from_atoz = dict(sorted(generate_huffman_codes(root_node).items()))
        # print(huffman_codes_from_atoz)