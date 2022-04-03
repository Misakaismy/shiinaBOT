# import pygsheets


# gc = pygsheets.authorize('client_secret.json')
# sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1eIRcSbwYb0fpvvdBeVZfBlkMDhZV8x7S-KV-Z8wKS5U/')

# wks_list = sht.worksheets()
# print(wks_list)

# wks = sht.worksheet_by_title("剪刀石頭布")

# # for row_num in range(999):
# #     if wks.get_row(row_num+1, include_tailing_empty=False) == []:
# #         wks.update_row(row_num+1, [f'{row_num}', '222677011917832202', ""])
# #         break
# list1 = wks.get_all_values(include_tailing_empty = False, include_tailing_empty_rows = False)
# print(list1)

# list1 = [[123, 0, 123, 0], [456, 1, 456, 1]]
# for index in range(len(list1)):
#     if list1[index][1] == 1 and list1[index][3] == 1:
#         list1.remove(list1[index])

# print(list1)
# print("Len:"+str(len(list1)))
import random

list1 = [1,2,3,4,5,6]

# for index in range(len(list1)):
#     print(list1[index])

print(random.choice(range(1,6)))