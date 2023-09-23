from bs4 import BeautifulSoup
import csv
import os

filenames = os.listdir("Old")
allitems = []
x = 0
for filename in filenames:
    with open('Old/'+filename, 'rb') as raw_resuls:
        results = BeautifulSoup(raw_resuls, "xml")
    for i in results.find_all("m_TableData"):
        while(True):
            try:
                k = i.Array.data('data_'+str(x))[0]
                try:
                    print(k.m_Id['value'],k.m_Localized['value'])
                    allitems.append([k.m_Id['value'],k.m_Localized['value'].replace('\n','\x0A'), ""])
                    x+=1
                except:
                    x+=1
            except Exception as e:
                print(e)
                x = 0
                break

with open('translate/all.csv', 'w', encoding='utf8', newline='') as f:
    write = csv.writer(f)
    write.writerow(["ID", "EN", "TH"])
    write.writerows(allitems)

