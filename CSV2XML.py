from bs4 import BeautifulSoup
import csv
import os
translatedfile = "all.csv"
filenames = os.listdir("Old")
translated = 'translate/all.csv'
with open(translated, encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    csv_dict = {}
    for row in csv_data:
        if row[0] not in csv_dict:
            csv_dict[row[0]] = {}
        csv_dict[row[0]][row[1]] = row[2]


for filename in filenames:
    x = 0
    with open("Old/"+filename, encoding='utf-8') as raw_resuls:
        results = BeautifulSoup(raw_resuls, 'xml')

    for i in results.find_all("m_TableData"):
        # fl = False
        while (True):
            try:
                k = i.Array.data('data_'+str(x))[0]
                try:
                    j_id = k.m_Id['value']
                    j_text = k.m_Localized['value']
                    if j_id in csv_dict and csv_dict[j_id][j_text] != "":
                        ttx = csv_dict[j_id][j_text]
                        ttx = ttx.replace('\n','x0A')
                        k.m_Localized['value'] = ttx
                        # fl = True
                    x += 1
                except:
                    x += 1
            except:
                print(k)
                print("Stopped-----------------------------------------------")
                x = 0
                break
        # if fl != True:
        #     fl = False

    with open("UnityEngine.Localization.Tables/"+filename, "w", encoding='utf-8') as outfile:
        outfile.write(str(results.prettify()))
