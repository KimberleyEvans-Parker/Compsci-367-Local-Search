import pandas as pd
import openpyxl

# def extract_number(line)

with open("hill climbing data 100 samples.txt", "r") as f:
    columns = ['hill climbing', 'sideways', 'restart']
    index = []
    expanded = []
    time = []
    prob = []
    for i in range(31):
        tmp = f.readline().split()[1]
        # print("N", tmp)
        # if tmp == "":
        #     break
        index.append(tmp)
        expanded_row = []
        time_row = []
        prob_row = []
        for i in range(3):
            tmp = f.readline().split()[1]
            # print("expanded:", tmp)
            expanded_row.append(tmp)
            tmp = f.readline().split()[1]
            # print("time:", tmp)
            time_row.append(tmp)
            tmp = f.readline().split()[1]
            # print("prob:", tmp)
            prob_row.append(tmp)
        expanded.append(expanded_row)
        time.append(time_row)
        prob.append(prob_row)
        f.readline()

expanded_df = pd.DataFrame(expanded, index=index, columns=columns)
time_df = pd.DataFrame(time, index=index, columns=columns)
prob_df = pd.DataFrame(prob, index=index, columns=columns)

with pd.ExcelWriter('data.xlsx') as writer:
    expanded_df.to_excel(writer, sheet_name='expanded')
    time_df.to_excel(writer, sheet_name='time')
    prob_df.to_excel(writer, sheet_name='prob')
