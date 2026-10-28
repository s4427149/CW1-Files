def permittedTime(line, reportOutput):
    if "Times" in line:
        reportOutput.write(line)

def COVIDIssues(line, reportOutput):
    if "COVID" in line:
        reportOutput.write(line)
        # if "No COVID" in line:
        #     location(line, reportOutput)

def location(line, reportOutput):
    if "Location" in line:
        reportOutput.write(line)

def possessionInformation(line, reportOutput):
    if "Ref: P2021/3322141" in line:
        if "Possession Information" in line:
            reportOutput.write(line)

def plannedWorks(line, reportOutput):
    if "Ref: P2021/3532144" in line:
        if "Planned Works" in line:
            reportOutput.write(line)

def search(file, reportOutput):
    for line in file:
        permittedTime(line, reportOutput)
        COVIDIssues(line, reportOutput)
        location(line, reportOutput)
        possessionInformation(line, reportOutput)
        plannedWorks(line, reportOutput)
