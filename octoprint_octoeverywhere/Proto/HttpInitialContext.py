# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Proto

import octoflatbuffers
from octoflatbuffers.compat import import_numpy
np = import_numpy()

class HttpInitialContext(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = octoflatbuffers.encode.Get(octoflatbuffers.packer.uoffset, buf, offset)
        x = HttpInitialContext()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsHttpInitialContext(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # HttpInitialContext
    def Init(self, buf, pos):
        self._tab = octoflatbuffers.table.Table(buf, pos)

    # HttpInitialContext
    def Path(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HttpInitialContext
    def PathType(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 1

    # HttpInitialContext
    def Method(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HttpInitialContext
    def OctoHost(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HttpInitialContext
    def Headers(self, j):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += octoflatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from octoprint_octoeverywhere.Proto.HttpHeader import HttpHeader
            obj = HttpHeader()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # HttpInitialContext
    def HeadersLength(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # HttpInitialContext
    def HeadersIsNone(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # HttpInitialContext
    def UseOctoeverywhereAuth(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(6)
def HttpInitialContextStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddPath(builder, path): builder.PrependUOffsetTRelativeSlot(0, octoflatbuffers.number_types.UOffsetTFlags.py_type(path), 0)
def HttpInitialContextAddPath(builder, path):
    """This method is deprecated. Please switch to AddPath."""
    return AddPath(builder, path)
def AddPathType(builder, pathType): builder.PrependInt8Slot(1, pathType, 1)
def HttpInitialContextAddPathType(builder, pathType):
    """This method is deprecated. Please switch to AddPathType."""
    return AddPathType(builder, pathType)
def AddMethod(builder, method): builder.PrependUOffsetTRelativeSlot(2, octoflatbuffers.number_types.UOffsetTFlags.py_type(method), 0)
def HttpInitialContextAddMethod(builder, method):
    """This method is deprecated. Please switch to AddMethod."""
    return AddMethod(builder, method)
def AddOctoHost(builder, octoHost): builder.PrependUOffsetTRelativeSlot(3, octoflatbuffers.number_types.UOffsetTFlags.py_type(octoHost), 0)
def HttpInitialContextAddOctoHost(builder, octoHost):
    """This method is deprecated. Please switch to AddOctoHost."""
    return AddOctoHost(builder, octoHost)
def AddHeaders(builder, headers): builder.PrependUOffsetTRelativeSlot(4, octoflatbuffers.number_types.UOffsetTFlags.py_type(headers), 0)
def HttpInitialContextAddHeaders(builder, headers):
    """This method is deprecated. Please switch to AddHeaders."""
    return AddHeaders(builder, headers)
def StartHeadersVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def HttpInitialContextStartHeadersVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartHeadersVector(builder, numElems)
def AddUseOctoeverywhereAuth(builder, useOctoeverywhereAuth): builder.PrependInt8Slot(5, useOctoeverywhereAuth, 0)
def HttpInitialContextAddUseOctoeverywhereAuth(builder, useOctoeverywhereAuth):
    """This method is deprecated. Please switch to AddUseOctoeverywhereAuth."""
    return AddUseOctoeverywhereAuth(builder, useOctoeverywhereAuth)
def End(builder): return builder.EndObject()
def HttpInitialContextEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)