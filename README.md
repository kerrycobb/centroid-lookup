# Centroid Lookup
Lookup up administrative areas from csv or xlsx file and output centroids into copy of csv or xlsx. 

## Installation
```bash
pip install git+https://github.com/kerrycobb/centroid-lookup
```

## Usage
### Command Line Usage

View help menu showing all available commands `centroid-lookup --help`

```
Usage: centroid-lookup [OPTIONS] COMMAND [ARGS]...

  Look up centroid of GADM administrative areas in csv file or excel
  spreadsheet.

  INPUT can be csv or xlsx

Options:
  -h, --help  Show this message and exit.

Commands:
  adm0  Look up centroid of level 0 GADM administrative areas
  adm1  Look up centroid of level 1 GADM administrative areas
  adm2  Look up centroid of level 2 GADM administrative areas
  adm3  Look up centroid of level 3 GADM administrative areas
  adm4  Look up centroid of level 4 GADM administrative areas
  adm5  Look up centroid of level 5 GADM administrative areas
```

View help menu showing options for each command `centroid-lookup adm5 --help`

```
Usage: centroid-lookup adm5 [OPTIONS] INPUT

  Look up centroid of level 5 GADM administrative areas

Options:
  -0, --adm0 TEXT    Adm level 0 column header in input file
  -1, --adm1 TEXT    Adm level 1 column header in input file
  -2, --adm2 TEXT    Adm level 2 column header in input file
  -3, --adm3 TEXT    Adm level 3 column header in input file
  -4, --adm4 TEXT    Adm level 4 column header in input file
  -5, --adm5 TEXT    Adm level 5 column header in input file
  -o, --output TEXT  Path to output file. Defaults to centroid-lookup.out.csv
  -s, --sheet TEXT   sheet name if input is excel spreadsheet
  -h, --help         Show this message and exit.
```

## Util
`compute_gadm_centroids.py` is a script for downloading GADM data and computing centroids. This is how the data that are downloaded when installing centroid lookup were generated.

## Known issues
Alaska > Aleutians West centroid location way off
