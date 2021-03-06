import csv
def fileGenator(filename,column, dir):
    with open('csv/student.csv', mode='w') as student_file:
        student_writer = csv.writer(student_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        column = ['CIE L', 'CIE a*', 'CIE b*', 'CHOMA', 'HUE', 'R', 'G', 'B']
        listInfo = [39, 48, 39, 52, 29, 70, 10, 348]

        for order in listInfo:
            student_writer.writerow(str(order))
        else:
            print('Writing has been completed')
