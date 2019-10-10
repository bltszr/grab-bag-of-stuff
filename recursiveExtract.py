import os
import io
import tarfile

# courtesy of stackexchange and ya boi pseud/alpat. don't forget to study this code

def extract(filename):
    t = tarfile.open(name=filename)
    for f in t.getmembers():
        if f.name.endswith("tar"):
            new_filename = f.name
            t.extract(f)
        print(f)
    if not filename.endswith("20.tar"):
        os.remove("/" + filename)
        
    extract(os.path.join(os.getcwd() + "/" + new_filename))

extract(os.path.join(os.getcwd() + "/1000.tar"))