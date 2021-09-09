from checksumdir import dirhash
import os
import hashlib


def build_checksum_of_directory(dir: str, ex_files: list = [], ex_ext: list = [], hash_func: str = 'sha256'):
    """
    Builds a checksum of the given directory to check for changes. Uses https://pypi.org/project/checksumdir/

    Parameters
    ----------
    dir: str
        directory to create hash of
    ex_files: list
        list of files to be excluded of the hash creation
    ex_ext:
        list of file extensions to be excluded from the hash creation
    hash_func: str
        method of hash algorithm

    Returns
    -------
    hash: str
        hash string of given directory
    """
    allowed_hash_functions = ['md5', 'sha1', 'sha256']  # fast, but "insecure" --> slow but more secure

    if os.path.exists(dir) and hash_func in allowed_hash_functions:
        hash = dirhash(dir, hash_func, excluded_files=ex_files, excluded_extensions=ex_ext)
        return hash
    else:
        return None


def build_hash_of_file(filepath: str, hash_func: str = 'sha256'):
    """
    Returns a hash string of given file with hashlib

    Parameters
    ----------
    filepath: str
        path to file to be hashed
    hash_func: str
        indicator for hash function to be used. one of ['md5', 'sha1', 'sha256']

    Returns
    -------
    hash: str
        hexdigest of created file hash as string
    """
    allowed_hash_functions = ['md5', 'sha1', 'sha256']  # fast, but "insecure" --> slow but more secure
    buf_size = 65536

    if os.path.exists(filepath) and os.path.isfile(filepath) and hash_func in allowed_hash_functions:
        hash = eval("hashlib." + hash_func + "()")
        with open(filepath, 'rb') as f:
            while True:
                data = f.read(buf_size)
                if not data:
                    break
                hash.update(data)
        return hash.hexdigest()
    else:
        return None


if __name__ == "__main__":
    # testing build_checksum_of_directory
    directory = './test_directory'
    dir_hash = build_checksum_of_directory(dir=directory)
    print(f"Hash of dir: {dir_hash}")
    dir_hash = build_checksum_of_directory(dir=directory, ex_files=['package.json'])
    print(f"Hash of dir without package.json: {dir_hash}")
    dir_hash = build_checksum_of_directory(dir=directory, ex_ext=['txt'])
    print(f"Hash of dir without txt files: {dir_hash}")

    # testing build_hash_of_file
    print()
    filepath = './test_directory/package.json'
    file_hash1 = build_hash_of_file(filepath=filepath)
    print(f"Hash file 1: {file_hash1}")
    filepath = './test_directory/test2.txt'
    file_hash2 = build_hash_of_file(filepath=filepath)
    print(f"Hash file 2: {file_hash2}")
    print(f"Files are equal: {file_hash1 == file_hash2}")

    # Reading and Writing files
    # https://realpython.com/read-write-files-python/#reading-and-writing-opened-files
    filepath_txt = './test_directory/test1.txt'
    with open(filepath_txt, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

    lines.append("New line :) \n")
    with open(filepath_txt, 'w') as f:
        f.writelines(lines)
