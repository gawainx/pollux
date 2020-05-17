import os, sys
import typer
from pollux import inputer
from pollux.license import license_setup, license_text
import pollux.pip.utils as putils

main = typer.Typer()


@main.command()
def init(name: str):
    """
    Init a new pip project with given name
    :param name: Project name
    """
    setup_dict = dict()
    pwd = os.getcwd()
    project_path = os.path.join(pwd, name)
    typer.echo(f"Init Project {name} in {project_path}")
    if os.mkdir(project_path):
        os.chdir(project_path)  # cd {name}
        typer.echo("Collecting necessary information...")
        lic = inputer.select_license()
        if lic != 'n':
            whole_lic = license_text[lic]
            lic_setup = license_setup[lic]
            setup_dict['license'] = lic_setup
            with open('LICENSE', 'w') as lis:
                print(whole_lic, file=lis)
            print("LICENSE file created!")
        py_version = inputer.input_py_version()
        setup_dict['python'] = py_version
        setup_dict['author'] = input("Please input author name:\n")
        setup_py = putils.build_setup(name=name,
                                      lic=setup_dict['license'],
                                      author=setup_dict['author'])
        with open('setup.py', 'w') as spy:
            print(setup_py, file=spy)
        print("setup.py created!")
        with open('.gitignore', 'w') as ig:
            print(putils.gitignore, file=ig)
        print("Operation finished!")
    else:
        print(f"Directory {project_path} error!")


@main.command()
def build(cache: str = '.build',
          destination: str = 'dist'
          ):
    """
    Build wheel
    """
    # python setup.py sdist
