new_list=[]
url_list=['dsvxvvds/sdfs/dsf/catalog/vcd','scsdc/sdcv/xczxc/xz','zxczc/dfs/catalog/df']
for i in url_list:
    if 'catalog' in i.split('/'):
         new_list.append(i)
print(new_list)


