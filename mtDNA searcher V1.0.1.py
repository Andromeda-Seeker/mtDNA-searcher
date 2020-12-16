import re,os,sys

def search_seq(seq_path):

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

        target_seq = re.findall('CTCTAGAGATT(.+)AATCGTCGA',full_seq)
        if len(target_seq) != 0:
            final_txt.write('%d\t'%i + '%s\n'%target_seq[0])
        else:
            pass

        file.close()
        i+=1

    full_txt.close()
    final_txt.close()

def run():
    print('mtDNA Searcher V1.0.1简易版)   by Ace\n\n该代码为简易版本，为保证代码正常运行，请仅将所有seq文件放入同一文件夹中，按名称排序并做好备份。\n\n\n')
    seq_path = input('请输入序列文件夹目录：')
    search_seq(seq_path)
    sys.exit(0)


if __name__ == "__main__":
    run()