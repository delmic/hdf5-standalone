import hdf5

das = hdf5.read_data("/home/piel/GDrive/Shared/Technology Development/Software/Test data/good-data/test_spectrum.h5")
print(das)
for da in das:
    print(da.metadata)
