
import gzip
import shutil

with open('fic23.txt', 'rb') as f_in:
    with gzip.open('fic23_com.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
