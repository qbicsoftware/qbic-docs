#!/usr/bin/env bash

# Positional arguments:
#   1. docs folder: directory on which all javadocs were generated
#
# The following environment variables are required:
#   - GITHUB_USERNAME 
#   - GITHUB_ACCESS_TOKEN: 
# This script will commit/push changes to GitHub, so a username and a personal access token are required.
 
# This script commits changes done to the docs folder. When changes are committed,
# ReadTheDocs.org will start a build and will update the published documentation.
git remote rm origin
git remote add origin https://$GITHUB_USERNAME:$GITHUB_ACCESS_TOKEN@github.com
git add $1
git commit -m "[skip travis] Automatic javadoc generation" -m "Travis build ID: $TRAVIS_BUILD_ID" -m "Travis build number: $TRAVIS_BUILD_NUMBER"