import pandas as pd
import numpy as np

def read_file(filename):#function read file
    file = pd.read_csv(filename,sep="\t",header=None)
    return file

file = read_file('file.wig')#reading file.wig
file.columns = ['chr','start','end','signal'] #assign column names file.wig
snp = read_file('snp.bed')  #read snp.bed
snp.columns = ['chr','rsid','position'] #assign columns of snp.bed

df = pd.merge(file,snp,on='chr') #merge two df on the basis of chr common column
print(df.shape)#print dimension of df
print(df.columns,"\n") #print df columns name
df.start,df.end = np.where(df.start > df.end, [df.end,df.start], [df.start,df.end]) #swap columns if start > end
df['enhancer'] = df.position.between(df.start,df.end,inclusive=True).map({True:'Yes',False:'No'}) #add new column if position is between start and end
df2=df[df.enhancer=='Yes'] #extract rows with overlapping enhancer region
df2 = df2[['chr','rsid','position','enhancer']] #extract specific columns
print(df2)
