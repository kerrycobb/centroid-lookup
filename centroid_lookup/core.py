import sys
import os
import pandas as pd
import pkg_resources as pr

def parse_input_file(path):
    ext = os.path.splitext(path)[1]
    if ext == '.xlsx':
        xl = pd.ExcelFile(path)
        sheet = xl.sheet_names[0]
        df = xl.parse(sheet)
    elif ext == '.csv':
        df = pd.read_csv(path)
    else:
        sys.exit('{} not a valid file extension. Must be ".csv" or ".xlsx"'.format(ext))
    return(df)

def write_output_file(df, path):
    ext = os.path.splitext(path)[1]
    if ext == '.xlsx':
        writer = pd.ExcelWriter(path)
        df.to_excel(writer, 'Sheet1', index=False)
        writer.save()
    elif ext == '.csv':
        df.to_csv(path, index=False)

def lookup_from_file(input, headers, output=None):
    input_df = parse_input_file(input)
    out_df = lookup(input_df, headers)
    if output is None:
        input_dir = os.path.dirname(input)
        input_basename = os.path.basename(input)
        input_name, input_ext = os.path.splitext(input_basename)
        output_name = '{}-output{}'.format(input_name, input_ext)
        output = os.path.join(input_dir, output_name)
    write_output_file(out_df, output)

def lookup(input_df, headers):
    LVLS = ['adm0', 'adm1', 'adm2', 'adm3', 'adm4', 'adm5']
    lvl = len(headers) - 1
    lvls = LVLS[:lvl + 1]
    centroid_data = 'data/adm{}.csv'.format(lvl)
    centroid_data_path = pr.resource_filename('centroid_lookup', centroid_data)
    centroids = pd.read_csv(centroid_data_path)
    # TODO: Detect if adm0 is ISO format and use instead of full name
    centroids = centroids.drop(columns=['ISO'])
    input_df.rename(columns=dict(zip(headers, lvls)), inplace=True)
    out_df = pd.merge(centroids, input_df, how='right', on=lvls)
    out_df.rename(columns=dict(zip(lvls, headers)), inplace=True)
    return(out_df)
