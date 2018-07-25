import click
import centroid_lookup as cl


global_options = [
    click.argument('input', type=click.Path(exists=True)),
    click.option('--output', '-o', default=None, help='Path to output file. Defaults to <input-path>/centroid-lookup.out.<input-file-ext>'),
]

lvl_options = [
    click.option('--adm0', '-0', default='adm0', help='Adm level 0 column header in input file'),
    click.option('--adm1', '-1', default='adm1', help='Adm level 1 column header in input file'),
    click.option('--adm2', '-2', default='adm2', help='Adm level 2 column header in input file'),
    click.option('--adm3', '-3', default='adm3', help='Adm level 3 column header in input file'),
    click.option('--adm4', '-4', default='adm4', help='Adm level 4 column header in input file'),
    click.option('--adm5', '-5', default='adm5', help='Adm level 5 column header in input file'),
]

def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return(func)
    return(_add_options)

@click.group(context_settings=dict(help_option_names=['-h', '--help']))
def cli():
    '''Docstring'''
    pass

################################################################################
# adm0 subcommand
@cli.command()
@add_options(lvl_options[:1])
@add_options(global_options)
def adm0(input, adm0, output):
    '''Docstring'''
    cl.lookup_from_file(input, [adm0], output=output)


################################################################################
# adm1 subcommand
@cli.command()
@add_options(lvl_options[:2])
@add_options(global_options)
def adm1(input, adm0, adm1, output):
    '''Docstring'''
    cl.lookup_from_file(input, [adm0, adm1], output=output)
#
#
################################################################################
# adm2 subcommand
@cli.command()
@add_options(lvl_options[:3])
@add_options(global_options)
def adm2(input, adm0, adm1, adm2, output):
    '''Docstring'''
    cl.lookup_from_file(input, [adm0, adm1, adm2], output=output)


################################################################################
# adm3 subcommand
@cli.command()
@add_options(lvl_options[:4])
@add_options(global_options)
def adm3(input, adm0, adm1, adm2, adm3, output):
    '''Docstring'''
    cl.lookup_from_file(input, [adm0, adm1, adm2, adm3], output=output)


################################################################################
# adm4 subcommand
@cli.command()
@add_options(lvl_options[:5])
@add_options(global_options)
def adm4(input, adm0, adm1, adm2, adm3, adm4, output):
    '''Docstring'''
    cl.lookup_from_file(input, [adm0, adm1, adm2, adm3, adm4], output=output)


################################################################################
# adm5 subcommand
@cli.command()
@add_options(lvl_options)
@add_options(global_options)
def adm5(input, adm0, adm1, adm2, adm3, adm4, adm5, output):
    '''Docstring'''
    cl.lookup_from_file(input, [adm0, adm1, adm2, adm3, adm4, adm5], output=output)
