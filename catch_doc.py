import os


def main():
    root_dir = '../PythonProject'
    save_file = open('export.txt', 'w', encoding='utf-8')
    find_all_annotation_text(root_dir, save_file)
    save_file.close()


def find_all_annotation_text(root_dir, save_file):
    for parent, dirNames, fileNames, in os.walk(root_dir):
        if 'demo' in dirNames:
            continue
        for fileName in fileNames:  # 输出文件信息
            if parent != 'demo':
                print("parent is:" + parent)
                print("filename is:" + fileName)
                print("the full name of the file is:" + os.path.join(parent, fileName))
                try:
                    file = open(os.path.join(parent, fileName), encoding='utf-8')
                    file_list = file.readlines()
                    for line in file_list:
                        if line.startswith("#"):
                            save_file.writelines(line)
                            print(line)
                except UnicodeDecodeError:
                    print("e")


main()
