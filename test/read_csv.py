import csv

comision = 0
with open('CDATS_agosto.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['PROMOTOR'] == 'TARAZONA TARAZONA JOHANNA MARCELA':
            date = row['V_TITULO'].replace(".0", "")
            if int(date) > 50000 and int(date) < 170000000:
                value = int(date) / 1000000
                comision += 6000 * value
            if int(date) > 170000000 and int(date) < 370000000:
                value = int(date) / 1000000
                comision += 8000 * value
            if int(date) > 370000000:
                value = int(date) / 1000000
                comision += 10000 * value
            print(f"{row['PROMOTOR']} - {row['V_TITULO']}")
    print(comision)