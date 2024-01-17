import csv

path = "C:/Users/Thomas/Downloads/ENEDIS_R63_P_CdC_M05PVFR7_00001_20240116121524_1.json"
exit_path = "C:/Users/Thomas/Downloads/ENEDIS_R63_P_CdC_M05PVFR7_00001_20240116121524_1.csv"

def get_data(path):
    data = ""
    Exit_Data = [["Horodate","Valeur"]]
    with open(path, "r") as file:
        data = file.read()
    data = data.split('"points":')[1]
    data = data.replace("]}]}]}","]")
    data = data.replace("}, {","},{")
    data = data.replace("} ,{","},{")
    datas = data.split("},{")
    for i in range (len(datas)):
        ligne = []
        ligne = datas[i].split(",")
        ligne = ligne[:2]
        Exit_Data.append([ligne[1].split('"')[3],ligne[0].split('"')[3]])
    return Exit_Data

def translate_CSV(data,exit_path):
    with open(exit_path, 'w', newline='', encoding='utf-8') as fichier_csv:

        writer = csv.writer(fichier_csv,delimiter=';')
        writer.writerows(data)

translate_CSV(get_data(path),exit_path)
