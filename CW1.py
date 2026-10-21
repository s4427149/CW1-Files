# import custom_module

# # open and append the report output file
# rep_out =  open('report_output.txt', 'a')

# # open and read report 1
# with open("report_1.txt", "r") as file:
#   for line in file:
#     if 'Times' in file.read():
#       print(line)

# # open and read report 2
# #with open('report_2.txt', 'r') as file:
#  # for line in file:
#    # if 'Times' in file.read():
#       #print(line)

# print(custom_module.w)

# open and read report 1
with open("report_1.txt", "r") as file:
   content = file.read()
   print(content)