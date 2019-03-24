import os


if __name__ == '__main__':
    for root, dirs, files in os.walk('./'):
        for file in files:
            prefix=file.split('.')[0]
            suffix=file.split('.')[-1]
            if suffix=='md':
                cmd=rf'pandoc -s --toc --toc-depth=2 ./{file} -o ./{file}'
                os.system(cmd)
            # break
        break