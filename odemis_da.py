import numpy

class DataArray(numpy.ndarray):
    """
    Array of data (a numpy nd.array) + metadata.
    It is the main object returned by a dataflow.
    It can be created either explicitly:
     DataArray([2,3,1,0], metadata={"key": 2})
    or via a view:
     x = numpy.array([2,3,1,0])
     x.view(DataArray)
    """

    # see http://docs.scipy.org/doc/numpy/user/basics.subclassing.html
    def __new__(cls, input_array, metadata=None):
        """
        input_array: array from which to initialise the data
        metadata (dict str-> value): a dict of (standard) names to their values
        """
        obj = numpy.asarray(input_array).view(cls)
        if metadata is None:
            metadata = {}
        obj.metadata = metadata
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return

        if hasattr(obj, 'metadata'):
            # Create a shallow copy of the meta data, otherwise when the array
            # gets copied, both will use the same meta data dictionary.
            self.metadata = obj.metadata.copy()
        else:
            self.metadata = {}

    # Used to send the DataArray over Pyro (over ZMQ, we use an optimised way)
    def __reduce__(self):
        # take the normal output (need to convert to list to modify it)
        ret = list(numpy.ndarray.__reduce__(self))
        # add to the state our additional state
        ret[2] = (ret[2], self.metadata)
        return tuple(ret)

    def __setstate__(self, state):
        nd_state, md = state
        numpy.ndarray.__setstate__(self, nd_state)
        self.metadata = md

