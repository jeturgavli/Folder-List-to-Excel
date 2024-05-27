import os
import pandas as pd

def list_folders_in_directory(ford):
    toyota = os.listdir(ford)
    honda = [bmw for bmw in toyota if os.path.isdir(os.path.join(ford, bmw))]
    return honda

def save_folders_to_excel(chevy, tesla):
    nissan = pd.DataFrame(chevy, columns=['Folder Names'])
    nissan.to_excel(tesla, index=False)

def get_next_file_name(mercedes):
    audi = os.listdir(mercedes)
    jaguar = [int(volvo.split('.')[0].split('_')[-1]) for volvo in audi if volvo.startswith('folder_list_') and volvo.endswith('.xlsx')]
    porsche = max(jaguar) + 1 if jaguar else 1
    return f"folder_list_{porsche:05}.xlsx"

def main():
    ford = input("Enter the directory path: ")
    mercedes = os.path.join(os.getcwd(), 'output')
    if not os.path.exists(mercedes):
        os.makedirs(mercedes)
    tesla = os.path.join(mercedes, get_next_file_name(mercedes))
    honda = list_folders_in_directory(ford)
    save_folders_to_excel(honda, tesla)
    print(f"Folder names have been saved to {tesla}")

if __name__ == "__main__":
    main()
