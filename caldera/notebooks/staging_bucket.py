import fsspec
import s3fs
import os
import re

def return_dailys(file_list, product_match, year):
    prune_list=[]
    expression = '.*' + product_match + str(year) + '[0-9][0-9][0-9].tif$'
    for tif in file_list:
        match = re.match(expression, tif)
        if match:
            prune_list.append(tif)
    return prune_list

def stage_file_obj(the_files, year):
    for file_obj in the_files:
        tile_id = file_obj.split('/')[2]
        print(tile_id)
        path2 = f'ws-out/stage_caldera/netet/{tile_id}/{year}/{os.path.basename(file_obj)}'
        print (path2)
        fs.cp(file_obj, path2)

fs = fsspec.filesystem('s3', anon=False, requester_pays=True)
fs = s3fs.S3FileSystem()

dirs = fs.ls('ws-enduser/CONUS')
my_tiles = [ x for x in dirs if "conus_mos" not in x ]
years = ['2003','2004','2005','2006','2007','2008','2009',
         '2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

#year = '2002'
for year in years:
    for tile in my_tiles:
        pth = f'{tile}/{year}'
        print(pth)
        all_files = fs.ls(pth)
        netet_files = [ x for x in all_files if "netet_"  in x ]
        netet_files = return_dailys(netet_files, 'netet_', year)
        #print('\n'.join(netet_files))
        stage_file_obj(netet_files, year)
        
        
        
        
