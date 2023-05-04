resultat = open('resultat.xml', 'w')

#Añadir etiquetas al xml
resultat.write("<pesades>\n")
resultat.write("    <pesada>\n")
resultat.write ("       <lot>"+str(lot)+"</lot>\n")
resultat.write ("       <num_pesada>"+str(total)+"</num_pesada>\n") 
resultat.write ("       <errors>"+str(invalid)+"</errors>\n")
resultat.write ("       <fora_rang>"+str(rangsino)+"</fora_rang>\n")

resultat.write ("       <dades_animals>\n")
resultat.write ("           <num_animals>"+str(valid)+"</num_animals>\n")
resultat.write ("           <mitjana>"+str(mitjana)+"</mitjana>\n")
resultat.write ("           <mediana>"+str(mediana)+"</mediana>\n")
resultat.write ("           <desviacio_tipica>"+str(sum)+"</desviacio_tipica>\n")
resultat.write ("       </dades_animals>\n")
resultat.write("    </pesada>\n")
resultat.write("</pesades>\n")
resultat.close()