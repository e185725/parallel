'''FaceEditedフォルダにある画像の２割をテストフォルダに移行するプログラム。
'''
import shutil
import random
import glob
import os

import sys
import time
#members = ["松本潤","二宮和也","相葉雅紀","櫻井翔","大野智"]



def main(member):

    name = member

    in_dir = "./FaceEdited2/"+name+"/face/*"
    in_jpg=glob.glob(in_dir)
    img_file_name_list=os.listdir("./FaceEdited/"+name+"/")
    #img_file_name_listをシャッフル、そのうち2割をtestフォルダに入れる。
    random.shuffle(in_jpg)
    os.makedirs('./Test/' + name, exist_ok=True)
    for t in range(len(in_jpg)//5):
        shutil.move(str(in_jpg[t]), "./Test/"+name)


if __name__ == "__main__":
    
    _,member = sys.argv
    main(member)
    """
    member = ["二宮和也","櫻井翔","相葉雅紀","大野智","松本潤"]
    start = time.time()
    for i in range(5):
        main(member[i])
    end = time.time()
    print("Finished in {} seconds.".format(end-start))
    """
    
    
