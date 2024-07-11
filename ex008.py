import os 



def renamefiles(path,fextn):
    with os.scandir(path) as entries:
        fleno = 1
        for entry in entries:
            if entry.is_file() and entry.name.lower().endswith(f'.{fextn}'):                
                os.rename(path+"\\"+entry.name,path+"\\"+str(fleno)+"."+fextn)
                print(entry.name,"--->"+str(fleno)+"."+fextn)
                fleno +=1

renamefiles("E:\\AI_ER\\Python\\test\\",'txt')

                
       