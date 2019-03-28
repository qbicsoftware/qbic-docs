#!/usr/bin/env python

# Script to generate documentation javadocs using javasphinx
# This script assumes that javasphinx has been installed.

# Output of this script is to populate the "docs" folder. For each repository
# in repositories.txt, a folder will be created. The folder structure looks like:
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

import argparse, shutil, os, distutils
from distutils import dir_util

# useful constants
# how many spaces should we write before writing each repo name
REPOSITORY_INDENTATION_LEVEL = 3
# placeholder that will be substituted for the list of repositories
REPOSITORIES_PLACEHOLDER = "$QBIC_REPOSITORIES$"
# name of the master document
MASTER_DOCUMENT_NAME = "index.rst"

# parses arguments
def main():
    parser = argparse.ArgumentParser(description='QBiC Javadoc Generator.', prog='generate-javadocs.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-r', '--repositories-file', required=True, default='repositories.txt',
        help='File containing a list of repositories. For each of these repositories, javadocs will be generated.')
    parser.add_argument('-t', '--template-file', required=True, default='.index.rst.template',
        help='Template file to generate index.rst.')
    parser.add_argument('-o', '--output-dir', required=True, default='docs',
        help='Folder on which the javadocs will be generated.')
    args = parser.parse_args()

    # read contents of the repos file into a list
    repos_list = parse_repos_file(args.repositories_file)
    # generate javadocs for each repo
    for repo_name in repos_list:
        generate_javadocs(args.output_dir, repo_name)
    # update index.rst    
    update_master_file(args.output_dir, args.template_file, repos_list)
    
def parse_repos_file(repositories_file):
    repo_names = []
    f = open(repositories_file, "r")
    for line in f:
        line = line.strip()
        # ignore comments
        if (line.startswith('#')):
            continue
        repo_names.append(line)
    f.close()

def generate_javadocs(output_dir, repo_name):

def update_master_file(master_file, template_file, repos_list):
    # be nice and list repos alphabetically in index.rst    
    sorted_repos_list = repos_list.sorted()
    

if __name__ == "__main__":
    main()
