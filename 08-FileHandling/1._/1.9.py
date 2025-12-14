###
# Prints employees employed in a specified position.
#

# Position
job_title = 'Software Engineer'

with open('it_company.csv') as file:
    for lines in file:
        line=lines.split(',')
        if line[2] == job_title:
            print(lines, end='') 