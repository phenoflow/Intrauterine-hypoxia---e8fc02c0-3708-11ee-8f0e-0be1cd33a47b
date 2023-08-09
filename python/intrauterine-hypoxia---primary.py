# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"Q21..00","system":"readv2"},{"code":"101103.0","system":"med"},{"code":"102969.0","system":"med"},{"code":"11693.0","system":"med"},{"code":"13276.0","system":"med"},{"code":"16097.0","system":"med"},{"code":"22597.0","system":"med"},{"code":"23009.0","system":"med"},{"code":"24243.0","system":"med"},{"code":"26401.0","system":"med"},{"code":"26837.0","system":"med"},{"code":"34132.0","system":"med"},{"code":"35054.0","system":"med"},{"code":"3620.0","system":"med"},{"code":"36694.0","system":"med"},{"code":"39759.0","system":"med"},{"code":"41102.0","system":"med"},{"code":"41296.0","system":"med"},{"code":"42131.0","system":"med"},{"code":"42322.0","system":"med"},{"code":"44828.0","system":"med"},{"code":"46502.0","system":"med"},{"code":"46514.0","system":"med"},{"code":"48274.0","system":"med"},{"code":"49485.0","system":"med"},{"code":"50281.0","system":"med"},{"code":"52151.0","system":"med"},{"code":"53241.0","system":"med"},{"code":"53863.0","system":"med"},{"code":"5479.0","system":"med"},{"code":"64335.0","system":"med"},{"code":"64732.0","system":"med"},{"code":"68431.0","system":"med"},{"code":"70850.0","system":"med"},{"code":"73394.0","system":"med"},{"code":"94759.0","system":"med"},{"code":"95649.0","system":"med"},{"code":"96821.0","system":"med"},{"code":"97471.0","system":"med"},{"code":"98422.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('intrauterine-hypoxia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["intrauterine-hypoxia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["intrauterine-hypoxia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["intrauterine-hypoxia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
