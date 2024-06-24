This is standalone version of the Odemis HDF5 loader. Originally the file also supported writing HDF5 files, but this doesn't works anymore (as a trade-off to simplicity). Adding back write support wouldn't be so hard, but needs a bit more work.

The way it should installed is that you'll copy the files ``hdf5.py`` + all the ``odemis_*.py`` from the folder into where ever you need them. The hdf5_read_test.py is not needed, it's only to show how to use (import) the other files.

Example usage::

    import hdf5

    das = hdf5.read_data("my_odemis_acquisition.h5")
    # das contains a list of "DataArrays", which are numpy arrays, with a .metadata dict
    print(das)

    for da in das:
        print(da.shape)
        print(da.metadata)

    # You can use the metadata keys using model.MD_*. See odemis_metadata for the complete list
    import odemis_model as model
    print(da[0].metadata[model.MD_POS])


