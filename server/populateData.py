import csv
from dataTables.models import ERG

with open('test_erg_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            temp = ERG(manual_id=row[0],contact_name=row[1],contact_email=row[2],company_name=row[3],city_name=row[4],industry=row[5],post_date=row[6],identification=row[7])
            temp.save()


import code
code.interact(local=locals())

