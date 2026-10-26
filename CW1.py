import custom_module

# with open("report_output.txt", "w", encoding="utf-8") as rep_out:
#     for filename in ("report_1.txt", "report_2.txt"):
#         with open(filename, "r", encoding="utf-8") as file:
#             for line in file:
#                 if "Times" in line:
#                     print(line, end="")
#                     rep_out.write(line)
#                 if "COVID" in line:
#                     print (line, end="")
#                     rep_out.write(line)
#                     if "No COVID Issues" in line:
#                         print(False)

with open("report_output.txt", "w", encoding="utf-8") as rep_out:
    for filename in ("report_1.txt", "report_2.txt"):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                permitted_time = custom_module.permittedTime(line)
                covid_issues = custom_module.COVIDIssues(line)
                location = custom_module.COVIDIssues(line)
                
                if permitted_time is not None:
                    print(permitted_time, end="")
                    rep_out.write(permitted_time)

                if covid_issues is not None:
                    print(covid_issues, end="")
                    rep_out.write(covid_issues)
                    

#1.	What is the average permitted time length of maintenance? (Times:)
# 2.	Were there COVID issues, and what was the Location?
# 3.	What was the Possession Information of the report with the Ref: P2021/3322141?
# 4.	What were the Planned Works of the report with the Ref: P2021/3532144?
