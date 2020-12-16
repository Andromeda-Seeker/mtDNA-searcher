import re,os,sys

def search_seq(seq_path,seq_1,seq_2):

    path = seq_path
    os.chdir('%s'%seq_path)

    txt_path = sys.path[0]

    full_txt = open('%s'%txt_path+'\\'+'full sequence result.txt',"a+")
    full_txt.truncate(0)
    final_txt = open('%s'%txt_path+'\\'+'sequence search result.txt',"a+")
    final_txt.truncate(0)

    i=1

    for file_name in os.listdir('%s'%seq_path):
        name = path + '\\' + file_name
        file = open(name,"a+",encoding='utf-8')

        file.seek(0)
        full_seq = re.sub('\n',"",file.read())
        full_txt.write('%d\t'%i + '%s\n\n'%full_seq)

        target_seq = re.findall(seq_1 + '(.+)' + seq_2,full_seq)
        if len(target_seq) != 0:
            final_txt.write('>sample-%d\n'%i + '%s\n'%target_seq[0])
        else:
            pass

        file.close()
        i+=1

    full_txt.close()
    final_txt.close()
    os.system('notepad %s\\sequence search result.txt'%txt_path)
    os.system('del /q %s\\sequence search result.txt'%txt_path)

def run():
    print('mtDNA Searcher V1.0.3(简易版)   by Ace\n\n该版本为简易版，为保证代码正常运行，请仅将所有seq文件放入同一文件夹中，按名称排序并做好备份。\n\n\n')
    seq_path = input('请输入序列文件夹目录：')
    seq_1 = input('请输入前端匹配序列：(建议：CTCTAGAGATT)\n')
    seq_2 = input('请输入后端匹配序列：(建议：AATCGTCGA)\n')
    search_seq(seq_path,seq_1,seq_2)
    sys.exit(0)


if __name__ == "__main__":
    run()