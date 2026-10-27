# def permittedTime(line):
#     if "Times" in line:
#         return line
#     return None

# def COVIDIssues(line):
#     if "COVID" in line:
#         return line
#     return None

# def location(line):
#     if "location" in line:
#         return line
#     return None

# def possessionInformation():

# def plannedWorks():

def permittedTime(line, reportOutput):
    if "Times" in line:
        reportOutput.write(line)

# def COVIDIssues(line):
#     if "COVID" in line:
#         return line
#     return None

# def location(line):
#     if "location" in line:
#         return line
#     return None

def search(file, reportOutput):
    for line in file:
        permittedTime(line, reportOutput)
        # COVIDIssues(line)
        # location(line)

        # permitted_time = permittedTime(line)
        # covid_issues = COVIDIssues(line)
        # location = location(line)
        
        # if permitted_time is not None:
        #     print(permitted_time, end="")
        #     rep_out.write(permitted_time)

        # if covid_issues is not None:
        #     print(covid_issues, end="")
        #     rep_out.write(covid_issues)
        