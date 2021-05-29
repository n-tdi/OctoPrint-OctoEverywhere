# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Proto

import octoflatbuffers
from octoflatbuffers.compat import import_numpy
np = import_numpy()

class HandshakeSyn(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = octoflatbuffers.encode.Get(octoflatbuffers.packer.uoffset, buf, offset)
        x = HandshakeSyn()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsHandshakeSyn(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # HandshakeSyn
    def Init(self, buf, pos):
        self._tab = octoflatbuffers.table.Table(buf, pos)

    # HandshakeSyn
    def PrinterId(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HandshakeSyn
    def IsPrimaryConnection(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(octoflatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # HandshakeSyn
    def PluginVersion(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HandshakeSyn
    def LocalDeviceIp(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # HandshakeSyn
    def LocalHttpProxyPort(self):
        o = octoflatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(octoflatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(5)
def HandshakeSynStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddPrinterId(builder, printerId): builder.PrependUOffsetTRelativeSlot(0, octoflatbuffers.number_types.UOffsetTFlags.py_type(printerId), 0)
def HandshakeSynAddPrinterId(builder, printerId):
    """This method is deprecated. Please switch to AddPrinterId."""
    return AddPrinterId(builder, printerId)
def AddIsPrimaryConnection(builder, isPrimaryConnection): builder.PrependBoolSlot(1, isPrimaryConnection, 0)
def HandshakeSynAddIsPrimaryConnection(builder, isPrimaryConnection):
    """This method is deprecated. Please switch to AddIsPrimaryConnection."""
    return AddIsPrimaryConnection(builder, isPrimaryConnection)
def AddPluginVersion(builder, pluginVersion): builder.PrependUOffsetTRelativeSlot(2, octoflatbuffers.number_types.UOffsetTFlags.py_type(pluginVersion), 0)
def HandshakeSynAddPluginVersion(builder, pluginVersion):
    """This method is deprecated. Please switch to AddPluginVersion."""
    return AddPluginVersion(builder, pluginVersion)
def AddLocalDeviceIp(builder, localDeviceIp): builder.PrependUOffsetTRelativeSlot(3, octoflatbuffers.number_types.UOffsetTFlags.py_type(localDeviceIp), 0)
def HandshakeSynAddLocalDeviceIp(builder, localDeviceIp):
    """This method is deprecated. Please switch to AddLocalDeviceIp."""
    return AddLocalDeviceIp(builder, localDeviceIp)
def AddLocalHttpProxyPort(builder, localHttpProxyPort): builder.PrependUint32Slot(4, localHttpProxyPort, 0)
def HandshakeSynAddLocalHttpProxyPort(builder, localHttpProxyPort):
    """This method is deprecated. Please switch to AddLocalHttpProxyPort."""
    return AddLocalHttpProxyPort(builder, localHttpProxyPort)
def End(builder): return builder.EndObject()
def HandshakeSynEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)