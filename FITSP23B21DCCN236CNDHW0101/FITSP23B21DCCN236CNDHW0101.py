#Đặng Minh Đức
# B21DCCN236
# Lý thuyết thông tin
# Nhóm G05
# Bài 1


import pandas as pd
import openpyxl
import math
from collections import Counter
def calculate_probability(event, sum_event):
    for key in event.keys():
        event[key] /= sum_event
    return event
def calculate_entropy (probability):
    entropy = 0
    for v in probability.values():
        entropy += v * math.log2(v)
    return -entropy if entropy else 0
def calculate_IG (common_entropy, branch_entropy_list ,source_magnitude):
    result = common_entropy
    for entropy, magnitude in branch_entropy_list.items():
        result -= ((magnitude/source_magnitude)*entropy)
    return result

if __name__=="__main__":
    excel_file = 'Health Monitor Dataset.xlsx'
    csv_file = 'Health Monitor Dataset.csv'
    read_excel_file = pd.read_excel(excel_file)
    read_excel_sheet_2 = pd.read_excel(excel_file, sheet_name='Sheet2', index_col=None)
    read_excel_file.to_csv(csv_file, index=False)
    read_csv = pd.read_csv(csv_file)
    #1) Liệt kê danh sách các lựa chọn cho phân hoạch dữ liệu và hình thành cây quyết định
    headers = read_csv.columns[5:].to_list()

    # 2) Thực hiện xây dựng cây quyết định theo một thứ tự nào đó của danh sách các lựa chọn có được ở phần 1)
    causes_respiratory_imbalance_type_and_name = dict(zip(read_excel_sheet_2['Type'].to_list(), read_excel_sheet_2['Name'].to_list()))
    causes_respiratory_imbalance_name = list(causes_respiratory_imbalance_type_and_name.values())
    dataset = {}
    for header in headers:
        dataset.update({header:read_excel_file[header].to_list()})

    data_partition = {}
    event = {}
    for header in headers:
        data_partition.update({header: {}})
        event.update({header: {}})
        for type_, cause in causes_respiratory_imbalance_type_and_name.items():
            data_partition[header].update({type_: {cause:[]}})
            event[header].update({type_: {cause:[]}})
    # Ánh xạ data của các cột vào cac Causes Respiratory Imbalance
    for header in headers:
        if header != 'Causes Respiratory Imbalance' and header != 'Type':
            for i, (cause, type_) in enumerate(zip(dataset['Causes Respiratory Imbalance'], dataset['Type'])):
                data_partition[header][type_][cause].append(dataset[header][i])
                # print(data_partition[header][type_][cause])
    IG = []
    #3) Tính xác suất va entropy cua cac nhánh, và chung và tính IG
    for header in headers:
        source_count_event = Counter(dataset[header])
        source_probability = dict(calculate_probability(source_count_event, len(dataset[header])))
        source_entropy = calculate_entropy(source_probability)
        # print(probability_common, entropy_common)
        branch_entropy_list = []
        branch_magnitude_list = []
        for type_, cause in causes_respiratory_imbalance_type_and_name.items():
            branch_count_event = Counter(data_partition[header][type_][cause])
            branch_probability = dict(calculate_probability(branch_count_event, len(data_partition[header][type_][cause])))
            branch_entropy = calculate_entropy(branch_probability)
            branch_entropy_list.append(branch_entropy)
            branch_magnitude_list.append(len(data_partition[header][type_][cause]))
            event[header][type_][cause].extend([{f'{type_} {cause} Probability':branch_probability}, {f'{type_} {cause} Entropy': branch_entropy}])
        IG.append({header:calculate_IG(source_entropy, dict(zip(branch_entropy_list, branch_magnitude_list)),  len(dataset[header]))})

    #4) Hiển thị các thông tin hoặc lưu vào file
    with open('FITSP23B21DCCN236CNDHW0101.txt', 'w') as file:
        file.write("Danh sach lua chon:\n")
        for header in headers:
            if header != 'Type' or header !='Causes Respiratory Imbalance':
                file.write(header + ', ')
        file.write('\n\n{\n')
        for data in IG:
            check=0
            for k, v in data.items():
                if k == 'Type' or k=='Causes Respiratory Imbalance':
                    check=1
            if not check:
                file.write('\t'+ str(data)[1:len(data)-2] + '\n')
        file.write('}')