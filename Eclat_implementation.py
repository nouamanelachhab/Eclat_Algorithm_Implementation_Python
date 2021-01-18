from fim import eclat
import pandas as pd


data = pd.read_excel (r'D:\Accidents.xlsx') 

df = pd.DataFrame(data, columns= ["Date d'accident DAT_ACC","Heure d'accident HEU_ACC","Decoupage Geographique COD_PRV","Etat chaussée COD_ETA_CHA","Etat surface COD_ETA_SUR","Lumière COD_LUM","Lumière COD_LUM","Code Agglomeration COD_AGG","Localisation LOC","Type carrefours COD_TYP_CAR_AGG","Profils en long COD_PRO_LON","Type collision COD_TYP_COL","Obstacle heurtés COD_OBS_HRT","Point de choc initial COD_POI_CHO","manœuvre COD_MAN"])

##transformation de la dataframe en liste
freq_itemsets = df.values.tolist()

##Application de l'algorithme eclat
res= eclat(freq_itemsets, supp=10, zmin=10)

##transformer la liste en dataframe

to_df = pd.DataFrame(res, columns = ["Frequent Items" , "Support"])



##affichage du support sous forme de pourcentage
 
for index, row in to_df.iterrows():
    
   print (row['Frequent Items'],"\t\t", '%.2f' % (row['Support']/len(df)*100),"%")



    
 

