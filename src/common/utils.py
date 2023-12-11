import os
from pprint import pprint
from typing import List


def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print(filename)  ## foo.txt
    print(os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
    print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt

def find_conflicting_files(dir1, dir2):
  # create a dict of all files in dir1 (full path starting at repo name)
  fname_1 = create_dir_traversal_list(dir1)
  set_1 = set(fname_1)
  # traverse dir2 and check if file exists in
  fname_2 = create_dir_traversal_list(dir2)
  set_2 = set(fname_2)
  print("conflicting files are:")
  intersection = set_1.intersection(set_2)
  for item in sorted(intersection):
    print(item)

def should_exclude_file(f, root):
  return "__pycache__" in root or ".git" in root or ".idea" in root or ".pytest_cache" in root or "__init__" in f

def create_dir_traversal_list(d) -> List[str]:
  fname = []
  for root, d_names, f_names in os.walk(d):
    for f in f_names:
      if should_exclude_file(f, root):
        continue
      else:
        relative_root = root.replace(d, '')
        fname.append(os.path.join(relative_root, f))
  # print("fname = %s" % fname)
  return fname

dir1="/Users/lfinkels/repos/repo_merge_trial/old_repo1/"
dir2="/Users/lfinkels/repos/repo_merge_trial/old_repo2/"
find_conflicting_files(dir1, dir2)

dir1="/Users/lfinkels/repos/genesys/language-model-builder-data-aggregation/"
dir2="/Users/lfinkels/repos/genesys/language-model-finetuning/"
find_conflicting_files(dir1, dir2)