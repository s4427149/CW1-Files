import custom_module

# open and append the report output file
rep_out =  open('report_output.txt', 'a', encoding="utf-8")

# open and read report 1
with open("report_1.txt", "r", encoding="utf-8") as file:
  for line in file:
    if 'Times' in file.read():
      print(line)

# open and read report 2
with open('report_2.txt', 'r', encoding="utf-8") as file:
 for line in file:
   if 'Times' in file.read():
      print(line)

# print(custom_module.w)