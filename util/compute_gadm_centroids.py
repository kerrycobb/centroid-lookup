#!/usr/bin/env python

################################################################################
# Code use to build centroid database for centroid-lookup package

# TODO Known Issues:
# - Alaska > Aleutians West centroid location way off

################################################################################

import fiona
import geopandas
import pandas
import requests
import zipfile
import io
from os import path

GADM_WORLD_GDB_URL = 'https://biogeo.ucdavis.edu/data/gadm2.8/gadm28.gdb.zip'
GADM_WORLD_GDB_FILE = 'gadm28.gdb'
GADM_BASE_URL = 'https://biogeo.ucdavis.edu/data/gadm2.8/gdb/'
GADM_GDB_ZIP_SUFFIX = '_adm_gdb.zip'
GADM_GDB_FILE_SUFFIX = '_adm.gdb/'

def get_iso_list(path):
    '''Get ISO 3166-1 alpha-3 values from GADM whole world ESRI geodatabase'''
    gdb = geopandas.read_file(path, layer=1)
    iso3 = gdb['ISO3'].tolist()
    return(iso3)

def get_cols(lvl, df):
    '''Generate list of columns to copy over from GADM ESRI geodatabase'''
    cols = []
    cols.append('ISO')
    for i in list(range(lvl+1)):
        if lvl == 0:
            cols.append('NAME_ISO')
        else:
            cols.append('NAME_{}'.format(i))
    return(cols)

def fetch_gadm(url, gdb_file):
    '''Download country ESRI geodatabase from gadm.org'''
    request = requests.get(url)
    zip = zipfile.ZipFile(io.BytesIO(request.content))
    for file in zip.namelist():
        if file.startswith(gdb_file):
            zip.extract(file)

def compute_centroids():

    if not path.exists(GADM_WORLD_GDB_FILE):
        fetch_gadm(GADM_WORLD_GDB_URL, GADM_WORLD_GDB_FILE)

    countries = get_iso_list(GADM_WORLD_GDB_FILE)
    geo_dfs = [[], [], [], [], [], []]
    for iso in countries:
        gdb_file = iso + GADM_GDB_FILE_SUFFIX
        if not path.exists(gdb_file):
            url = GADM_BASE_URL + iso + GADM_GDB_ZIP_SUFFIX
            fetch_gadm(url, gdb_file)

        layers = range(len(fiona.listlayers(gdb_file)))
        for layer in layers:
            gdf = geopandas.read_file(gdb_file, layer=layer)
            centroids = gdf['geometry'].centroid
            gdf['cent_lon'] = centroids.x
            gdf['cent_lat'] = centroids.y
            cols = get_cols(layer, gdf)
            cols.append('cent_lon')
            cols.append('cent_lat')
            ndf = pandas.DataFrame(gdf[cols].values, columns=cols)
            geo_dfs[layer].append(ndf)

        print('{} complete'.format(iso))

    for i, df in enumerate(geo_dfs):
        try:
            concat_df = pandas.concat(df, ignore_index=True)
        except:
            print('No data for adm level {}'.format(i))
        concat_df.to_csv('adm{}.csv'.format(i), index=False)
    print('<br>Complete!<br>')

if __name__ == '__main__':
    compute_centroids()
