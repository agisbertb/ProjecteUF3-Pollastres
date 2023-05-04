def comprobar(files):
    get_files()
    fitxers_valids = []
    for file in files:
        if get_file_date(file) == ahir():
            file = open('noprocessats/'+file, 'r')
            lines = file.readlines()
            global total
            total = len(lines)
            global valid
            valid = 0
            global invalid
            invalid = 0
            global rangsino
            rangsino = 0
            global mitjana
            mitjana = 0
            global pesosvalids
            pesosvalids = []
            global lot
            lot = 0
            for line in lines:
                try:
                    float(line)
                    valid += 1
                    pesosvalids.append(float(line))
                    mitjana += float(line)
                    mitjana = mitjana/total
                    if float(line) < float(config_vars[3]) or float(line) > float(config_vars[4]):
                        rangsino += 1
                except ValueError:
                    invalid += 1

            valid = total - invalid
            valid = valid - rangsino

            mitjana = str(mitjana)
            mitjana = mitjana[0:7]
            mitjana = float(mitjana)
        else:
            print("No hi ha fitxers per processar")


def med():
    global mediana
    pesosvalids.sort()
    if len(pesosvalids) % 2 == 0:
        mediana = (pesosvalids[len(pesosvalids)//2] + pesosvalids[len(pesosvalids)//2-1])/2
    else:
        mediana = pesosvalids[len(pesosvalids)//2]

def desv():
    global sum
    global desviacio
    sum = 0
    for i in pesosvalids:
        sum += (i - mitjana)**2
    desviacio = math.sqrt(sum/total)
    desviacio = str(desviacio)
    desviacio = desviacio[0:7]
    desviacio = float(desviacio)
    return desviacio

