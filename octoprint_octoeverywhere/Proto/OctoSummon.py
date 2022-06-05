# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Proto

import octoflatbuffers
from octoflatbuffers.compat import import_numpy
np = import_numpy()

class OctoSummon(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = octoflatbuffers.encode.Get(octoflatbuffers.packer.uoffset, buf, offset)
        x = OctoSummon()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsOctoSummon(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # OctoSummon
    def Init(self, buf, pos):
        self._tab = octoflatbuffers.table.Table(buf, pos)

    # OctoSummon
    def ServerConnectUrl(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # OctoSummon
    def SummonMethod(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 1

def Start(builder): builder.StartObject(2)
def OctoSummonStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddServerConnectUrl(builder, serverConnectUrl): builder.PrependUOffsetTRelativeSlot(0, octoflatbuffers.number_types.UOffsetTFlags.py_type(serverConnectUrl), 0)
def OctoSummonAddServerConnectUrl(builder, serverConnectUrl):
    """This method is deprecated. Please switch to AddServerConnectUrl."""
    return AddServerConnectUrl(builder, serverConnectUrl)
def AddSummonMethod(builder, summonMethod): builder.PrependInt8Slot(1, summonMethod, 1)
def OctoSummonAddSummonMethod(builder, summonMethod):
    """This method is deprecated. Please switch to AddSummonMethod."""
    return AddSummonMethod(builder, summonMethod)
def End(builder): return builder.EndObject()
def OctoSummonEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)