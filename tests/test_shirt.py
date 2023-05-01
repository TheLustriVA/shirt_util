import os
import tempfile
import shutil
from shirt import replace_strings_in_filenames

def test_basic_renaming():
    with tempfile.TemporaryDirectory() as tempdir:
        original_file = os.path.join(tempdir, 'test_old.txt')
        expected_file = os.path.join(tempdir, 'test_new.txt')
        with open(original_file, 'w') as f:
            f.write('test')
        replace_strings_in_filenames(['old'], ['new'], file_pattern=os.path.join(tempdir, '*'))
        assert not os.path.exists(original_file)
        assert os.path.exists(expected_file)

def test_recursive_renaming():
    with tempfile.TemporaryDirectory() as tempdir:
        subdir = os.path.join(tempdir, 'subdir')
        os.makedirs(subdir)
        original_file = os.path.join(subdir, 'test_old.txt')
        expected_file = os.path.join(subdir, 'test_new.txt')
        with open(original_file, 'w') as f:
            f.write('test')
        replace_strings_in_filenames(['old'], ['new'], file_pattern='*', recursive=True)
        assert not os.path.exists(original_file)
        assert os.path.exists(expected_file)

def test_invert_match_renaming():
    with tempfile.TemporaryDirectory() as tempdir:
        original_file1 = os.path.join(tempdir, 'test_old.txt')
        original_file2 = os.path.join(tempdir, 'test_another.txt')
        expected_file1 = os.path.join(tempdir, 'test_new.txt')
        with open(original_file1, 'w') as f:
            f.write('test1')
        with open(original_file2, 'w') as f:
            f.write('test2')
        replace_strings_in_filenames(['old'], ['new'], file_pattern=os.path.join(tempdir, '*'), invert_match=True)
        assert not os.path.exists(original_file1)
        assert os.path.exists(expected_file1)
        assert os.path.exists(original_file2)

def test_dry_run():
    with tempfile.TemporaryDirectory() as tempdir:
        original_file = os.path.join(tempdir, 'test_old.txt')
        with open(original_file, 'w') as f:
            f.write('test')
        renamed_files = replace_strings_in_filenames(['old'], ['new'], file_pattern=os.path.join(tempdir, '*'), dry_run=True)
        assert os.path.exists(original_file)
        assert len(renamed_files) == 1
        assert renamed_files[0][0] == original_file
        assert renamed_files[0][1] == os.path.join(tempdir, 'test_new.txt')
