import pandas as pd
import re

class DataProcessing:

  def __init__(self):
    self.df=pd.DataFrame()
    
    
  def load(self):
    dataset=pd.read_csv("wedding_info.csv")
    return dataset
   

  def imputing(self,dataset,lis:list):
    for i in lis:
      self.df=dataset.replace(i,'',regex=True)

    self.df=self.df.apply(lambda x:x.str.strip() if x.dtype == "object" else x)
    self.__fillers() 
  
  def __fillers(self):
    self.df.iloc[:,0:10]=self.df.iloc[:,0:10].fillna("None")
    self.df.iloc[:,10:20]=self.df.iloc[:,10:20].fillna('$0')
    self.__Estimate()

  def __Estimate(self):
    self.df['Estimate']=self.df['Estimate'].map(lambda x:x.lstrip('$').rstrip(' is the Estimated Wedding Cost')).astype(int)
    self.__strInt()
  
  def __strInt(self):
    for column in df.columns[11:20]:
      self.df[column]=self.df[column].map(lambda x:x.lstrip('$'))
      self.df[column]=self.df[column].astype(int)
      self.__Extract()
  
  def __Extract(self):

    df_new=pd.DataFrame()
    
    for i in range(0,980):
        extract=re.findall(r'\d+', df['Guest'][i])
        print(extract)
        if len(extract)==4:
        
          df_new= df_new.append(pd.DataFrame([extract], 
          columns=["Guest_number","range_start","range_end","Cost_per_person"]))
          
        elif len(extract)==3:     
        
          df_new= df_new.append(pd.DataFrame([extract], 
          columns=["Guest_number","range_end","Cost_per_person"]))
          df_new["range_start"] = '0'
        else:
          values=['0','0','0','0']
          df_new= df_new.append(pd.DataFrame([values], 
          columns=["Guest_number","range_start","range_end","Cost_per_person"]))

    for column in df_new.columns:
      df_new[column]=df_new[column].astype(int) 

    result=self.df.reset_index(drop=True).merge(df_new.reset_index(drop=True), left_index=True, right_index=True)
    self.__save(result)
  
  
  def __save(self,result):
    result.to_csv('processed_data.csv')

if __name__=="__main__":
  obj=DataProcessing()
  dataset= obj.load()
  obj.imputing(dataset,['\n','\t',','])
  