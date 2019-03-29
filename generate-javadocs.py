#!/usr/bin/env python

# Script to generate documentation javadocs using javasphinx
# This script assumes that javasphinx has been installed.

# Output of this script is to populate the "docs" folder. For each submodule
# in submodules.txt, a folder under docs will be created. The folder structure looks like:
# 
# .
# └── docs
#    ├── foo-lib
#    │    ├── com
#    │    │   └── foo
#    │    │       └── bar
#    │    │           ├── package-index.rst
#    │    │           ├── FooClass.rst
#    │    │           ├── BarClass.rst
#    │    │           └── FooBarClass.rst
#    │    └── packages.rst
#    └── bar-lib
#        ├── com
#        │   └── bar
#        │       └── foo
#        │           ├── package-index.rst
#        │           ├── FooClass.rst
#        │           ├── BarClass.rst
#        │           └── FooBarClass.rst
#        └── packages.rst

import argparse, os, suprocess

# useful constants
# how many spaces should we write before writing each repo name
REPOSITORY_INDENTATION_LEVEL = 3
# placeholder that will be substituted for the list of repositories
REPOSITORIES_PLACEHOLDER = "$QBIC_REPOSITORIES$"
# name of the master document
MASTER_DOCUMENT_NAME = "index.rst"
# directory where all git submodules reside
SUBMODULE_FOLDER = "modules"
# folder that has the source code, relative to each submodule folder
SOURCE_DIR = 'src/java/main'

# parses arguments
def main():
    parser = argparse.ArgumentParser(description='QBiC Javadoc Generator.', prog='generate-javadocs.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--submodules-file', required=True, default='submodules.txt',
        help='File containing a list of submodules. For each submodule, javadocs will be generated.')
    parser.add_argument('-t', '--template-file', required=True, default='.index.rst.template',
        help='Template file to generate index.rst.')
    parser.add_argument('-o', '--output-dir', required=True, default='docs',
        help='Folder on which the javadocs will be generated.')
    parser.add_argument('-b', '--branch', required=True, default='master',
        help='Branch from which javadocs will be generated for each submodule.')
    args = parser.parse_args()

    # read contents of the submodules file into a list
    submodules_list = parse_submodules_file(args.repositories_file)
    # for each repo, make sure that it has been added as a submodule, then
    # update each submodule and generate javadocs for it
    for submodule_name in submodules_list:
        update_submodule(submodule_name)
        generate_javadocs(args.output_dir, submodule_name)
    # update index.rst    
    update_master_file(args.output_dir, args.template_file, submodules_list)
    
# Parses the file found at the given path, returns
# a list where each element is a line in the file.
# Lines starting with '#' are ignored
def parse_submodules_file(submodules_file):
    submodule_names = []
    f = open(submodules_file, "r")
    for line in f:
        line = line.strip()
        # ignore comments
        if (line.startswith('#')):
            continue
        submodule_names.append(line)
    f.close()
    return submodule_names

# issues git commands to add/update a git submodule
# using the passed branch
def update_submodule(submodule_name, branch):
    # relative path to the submodule folder
    submodule_dir = get_submodule_dir(submodule_name)
    # force-add submodules
    execute(
        ["git", "submodule", "add", "--force", "-b", branch, '../{}'.format(submodule_name), submodule_dir],
        'Could not add submodule {}.'.format(submodule_name))    
    # update submodule
    execute(
        ["git", "submodule", "update", "--remote", submodule_dir], 
        'Could not update submodule {}.'.format(submodule_name))

# generates javadocs for the given submodule
def generate_javadocs(output_dir, submodule_name):
    # each submodule gets a directory under output_dir (e.g., docs/foo-lib, docs/bar-service)
    # make sure that the folder exists
    javadoc_output_dir = get_javadoc_output_dir(output_dir, submodule_name)
    src_dir = '{}/{}'.format(get_submodule_dir(submodule_name), SOURCE_DIR)
    if not (os.path.exists(javadoc_output_dir)):
        os.makedirs(javadoc_output_dir)
    execute(['javasphinx-apidoc', '-o', javadoc_output_dir, '-t', submodule_name])
    javasphinx-apidoc -o sample-lib -t sample-lib ~/Projects/QBiC/cookiecutter-templates-cli/generated/sample-cli/src/main/

def update_master_file(master_file, template_file, submodules_list):
    # be nice and list repos alphabetically in index.rst    
    sorted_submodules_list = submodules_list.sorted()

# given a submodule, returns the path of the folder, relative to the master repo
def get_submodule_dir(submodule_name):
    return '{}/{}'.format(SUBMODULE_FOLDER, submodule_name)

# given a submodule, returns the path of the corresponding javadoc output folder
def get_javadoc_output_dir(base_dir, submodule_name):
    return '{}/{}'.format(base_dir, submodule_name)

# executes an external command, raises an exception if the return code is not 0
def execute(command, error_message):
    completed_process = subprocess.run(command, capture_output=True)
    if (completed_process.returncode != 0):
        raise Exception('{}.\nExit code={}.\nStderr={}\nStdout{}'.format(
            error_message, completed_process.returncode, completed_process.stderr, completed_process.stdout))



if __name__ == "__main__":
    main()
