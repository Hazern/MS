from pathlib import Path
import os
import shutil
from zipfile import ZipFile

from colorama import Fore, Style
from colorama import init
init()

def first_file_count(Mod_list):
    file_count = []
    first_file_path = Path(__file__).parent / Mod_list
    for counter in first_file_path.iterdir():
        file_count.append(counter)
    print(Fore.YELLOW + f'{Fore.GREEN + str(len(file_count)) + Fore.YELLOW} file ready to sorting and extracting')

def extract(file_path, latestpath):
    with ZipFile(file_path, "r") as zobj:
        zobj.extractall(path=latestpath)

def extract_allfile(filepath):
    for latest in filepath.glob("*.zip"):
        extract(latest, filepath)

def Sorting(Mod_list_path, Mod_Sorter_path):
    mod_list_path = Path(__file__).parent / Mod_list_path
    mod_sorter_path = Path(__file__).parent / Mod_Sorter_path
    folder_name = ["N", "R", "SR_", "SSR"]
    
    for Mod_name in mod_list_path.glob("*.zip"):
        Mod_name_str = str(Mod_name.name)
        
        if Mod_name_str[0] == folder_name[0]:
            print(Fore.YELLOW + f"{Mod_name_str} :", Fore.GREEN + "moving to sorter folder complete..." + Fore.WHITE)
            for sorter_path in mod_sorter_path.glob(folder_name[0]):
                shutil.move(Mod_name, sorter_path)
                extract_allfile(sorter_path)
                for delete in sorter_path.glob("*.zip"):
                    os.remove(delete)

        elif Mod_name_str[0] == folder_name[1]:
            print(Fore.YELLOW + f"{Mod_name_str} :", Fore.GREEN + "moving to sorter folder complete..." + Fore.WHITE)
            for sorter_path in mod_sorter_path.glob(folder_name[1]):
                shutil.move(Mod_name, sorter_path)
                extract_allfile(sorter_path)
                for delete in sorter_path.glob("*.zip"):
                    os.remove(delete)

        elif Mod_name_str[0:3] == folder_name[2]:
            print(Fore.YELLOW + f"{Mod_name_str} :", Fore.GREEN + "moving to sorter folder complete..." + Fore.WHITE)
            for sorter_path in mod_sorter_path.glob(folder_name[2]):
                shutil.move(Mod_name, sorter_path)
                extract_allfile(sorter_path)
                for delete in sorter_path.glob("*.zip"):
                    os.remove(delete)
                
        elif Mod_name_str[0:3] == folder_name[3]:
            print(Fore.YELLOW + f"{Mod_name_str} :", Fore.GREEN + "moving to sorter folder complete..." + Fore.WHITE)
            for sorter_path in mod_sorter_path.glob(folder_name[3]):
                shutil.move(Mod_name, sorter_path)
                extract_allfile(sorter_path)
                for delete in sorter_path.glob("*.zip"):
                    os.remove(delete)
        else:
            print(Fore.YELLOW + f"{Mod_name_str} :", Fore.RED + "moving to sorter folder failed..." + Fore.WHITE)
            print(Fore.CYAN + "Please checking your first Charater of file name in this format. \nN | R | SR_ | SSR" + Fore.WHITE)

def last_file_count(Mod_Sorter_path):
    count = []
    mod_sorter_path = Path(__file__).parent / Mod_Sorter_path
    for all_class in mod_sorter_path.iterdir():
        for file in all_class.iterdir():
            count.append(file.name)
    print(Fore.YELLOW + f'hooray! {Fore.GREEN + str(len(count)) + Fore.YELLOW} mod is already sorting and extracting yet.')

first_file_count("Mod_list")
Sorting("Mod_list", "Mod_Sorter_by_SwimSuit_Rarity")
last_file_count("Mod_Sorter_by_SwimSuit_Rarity")