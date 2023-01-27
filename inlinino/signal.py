from pyqtgraph import QtCore


class InstrumentSignals(QtCore.QObject):
    status_update = QtCore.pyqtSignal()
    packet_received = QtCore.pyqtSignal()
    packet_corrupted = QtCore.pyqtSignal()
    packet_logged = QtCore.pyqtSignal()
    new_ts_data = QtCore.pyqtSignal(object, float)
    new_spectrum_data = QtCore.pyqtSignal(list)
    new_aux_data = QtCore.pyqtSignal(list)
    new_meta_data = QtCore.pyqtSignal(list)
    alarm = QtCore.pyqtSignal(bool)


class HyperNavSignals(InstrumentSignals):
    toggle_command_mode = QtCore.pyqtSignal(bool)
    new_frame = QtCore.pyqtSignal(object)


class InterfaceSignals(QtCore.QObject):
    read = QtCore.pyqtSignal(bytes)
    write = QtCore.pyqtSignal(bytes)
