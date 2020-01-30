# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""Python interface to libmraa"""


from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')
def swig_import_helper():
    import importlib
    pkg = __name__.rpartition('.')[0]
    mname = '.'.join((pkg, '_mraa')).lstrip('.')
    try:
        return importlib.import_module(mname)
    except ImportError:
        return importlib.import_module('_mraa')
_mraa = swig_import_helper()
del swig_import_helper
del _swig_python_version_info

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class uint8Array(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, uint8Array, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, uint8Array, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _mraa.new_uint8Array(nelements)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mraa.delete_uint8Array
    def __del__(self):
        return None

    def __getitem__(self, index):
        return _mraa.uint8Array___getitem__(self, index)

    def __setitem__(self, index, value):
        return _mraa.uint8Array___setitem__(self, index, value)

    def cast(self):
        return _mraa.uint8Array_cast(self)
    if _newclass:
        frompointer = staticmethod(_mraa.uint8Array_frompointer)
    else:
        frompointer = _mraa.uint8Array_frompointer

# Register uint8Array in _mraa:
_mraa.uint8Array_swigregister(uint8Array)

def uint8Array_frompointer(t):
    return _mraa.uint8Array_frompointer(t)
uint8Array_frompointer = _mraa.uint8Array_frompointer

INTEL_GALILEO_GEN1 = _mraa.INTEL_GALILEO_GEN1
INTEL_GALILEO_GEN2 = _mraa.INTEL_GALILEO_GEN2
INTEL_EDISON_FAB_C = _mraa.INTEL_EDISON_FAB_C
INTEL_DE3815 = _mraa.INTEL_DE3815
INTEL_MINNOWBOARD_MAX = _mraa.INTEL_MINNOWBOARD_MAX
RASPBERRY_PI = _mraa.RASPBERRY_PI
BEAGLEBONE = _mraa.BEAGLEBONE
BANANA = _mraa.BANANA
INTEL_NUC5 = _mraa.INTEL_NUC5
A96BOARDS = _mraa.A96BOARDS
INTEL_SOFIA_3GR = _mraa.INTEL_SOFIA_3GR
INTEL_CHERRYHILLS = _mraa.INTEL_CHERRYHILLS
INTEL_UP = _mraa.INTEL_UP
INTEL_JOULE_EXPANSION = _mraa.INTEL_JOULE_EXPANSION
PHYBOARD_WEGA = _mraa.PHYBOARD_WEGA
DE_NANO_SOC = _mraa.DE_NANO_SOC
INTEL_UP2 = _mraa.INTEL_UP2
MTK_LINKIT = _mraa.MTK_LINKIT
MTK_OMEGA2 = _mraa.MTK_OMEGA2
IEI_TANK = _mraa.IEI_TANK
FTDI_FT4222 = _mraa.FTDI_FT4222
GROVEPI = _mraa.GROVEPI
GENERIC_FIRMATA = _mraa.GENERIC_FIRMATA
ANDROID_PERIPHERALMANAGER = _mraa.ANDROID_PERIPHERALMANAGER
MOCK_PLATFORM = _mraa.MOCK_PLATFORM
NULL_PLATFORM = _mraa.NULL_PLATFORM
UNKNOWN_PLATFORM = _mraa.UNKNOWN_PLATFORM
INTEL_EDISON_MINIBOARD_J17_1 = _mraa.INTEL_EDISON_MINIBOARD_J17_1
INTEL_EDISON_MINIBOARD_J17_5 = _mraa.INTEL_EDISON_MINIBOARD_J17_5
INTEL_EDISON_MINIBOARD_J17_7 = _mraa.INTEL_EDISON_MINIBOARD_J17_7
INTEL_EDISON_MINIBOARD_J17_8 = _mraa.INTEL_EDISON_MINIBOARD_J17_8
INTEL_EDISON_MINIBOARD_J17_9 = _mraa.INTEL_EDISON_MINIBOARD_J17_9
INTEL_EDISON_MINIBOARD_J17_10 = _mraa.INTEL_EDISON_MINIBOARD_J17_10
INTEL_EDISON_MINIBOARD_J17_11 = _mraa.INTEL_EDISON_MINIBOARD_J17_11
INTEL_EDISON_MINIBOARD_J17_12 = _mraa.INTEL_EDISON_MINIBOARD_J17_12
INTEL_EDISON_MINIBOARD_J17_14 = _mraa.INTEL_EDISON_MINIBOARD_J17_14
INTEL_EDISON_MINIBOARD_J18_1 = _mraa.INTEL_EDISON_MINIBOARD_J18_1
INTEL_EDISON_MINIBOARD_J18_2 = _mraa.INTEL_EDISON_MINIBOARD_J18_2
INTEL_EDISON_MINIBOARD_J18_6 = _mraa.INTEL_EDISON_MINIBOARD_J18_6
INTEL_EDISON_MINIBOARD_J18_7 = _mraa.INTEL_EDISON_MINIBOARD_J18_7
INTEL_EDISON_MINIBOARD_J18_8 = _mraa.INTEL_EDISON_MINIBOARD_J18_8
INTEL_EDISON_MINIBOARD_J18_10 = _mraa.INTEL_EDISON_MINIBOARD_J18_10
INTEL_EDISON_MINIBOARD_J18_11 = _mraa.INTEL_EDISON_MINIBOARD_J18_11
INTEL_EDISON_MINIBOARD_J18_12 = _mraa.INTEL_EDISON_MINIBOARD_J18_12
INTEL_EDISON_MINIBOARD_J18_13 = _mraa.INTEL_EDISON_MINIBOARD_J18_13
INTEL_EDISON_MINIBOARD_J19_4 = _mraa.INTEL_EDISON_MINIBOARD_J19_4
INTEL_EDISON_MINIBOARD_J19_5 = _mraa.INTEL_EDISON_MINIBOARD_J19_5
INTEL_EDISON_MINIBOARD_J19_6 = _mraa.INTEL_EDISON_MINIBOARD_J19_6
INTEL_EDISON_MINIBOARD_J19_8 = _mraa.INTEL_EDISON_MINIBOARD_J19_8
INTEL_EDISON_MINIBOARD_J19_9 = _mraa.INTEL_EDISON_MINIBOARD_J19_9
INTEL_EDISON_MINIBOARD_J19_10 = _mraa.INTEL_EDISON_MINIBOARD_J19_10
INTEL_EDISON_MINIBOARD_J19_11 = _mraa.INTEL_EDISON_MINIBOARD_J19_11
INTEL_EDISON_MINIBOARD_J19_12 = _mraa.INTEL_EDISON_MINIBOARD_J19_12
INTEL_EDISON_MINIBOARD_J19_13 = _mraa.INTEL_EDISON_MINIBOARD_J19_13
INTEL_EDISON_MINIBOARD_J19_14 = _mraa.INTEL_EDISON_MINIBOARD_J19_14
INTEL_EDISON_MINIBOARD_J20_3 = _mraa.INTEL_EDISON_MINIBOARD_J20_3
INTEL_EDISON_MINIBOARD_J20_4 = _mraa.INTEL_EDISON_MINIBOARD_J20_4
INTEL_EDISON_MINIBOARD_J20_5 = _mraa.INTEL_EDISON_MINIBOARD_J20_5
INTEL_EDISON_MINIBOARD_J20_6 = _mraa.INTEL_EDISON_MINIBOARD_J20_6
INTEL_EDISON_MINIBOARD_J20_7 = _mraa.INTEL_EDISON_MINIBOARD_J20_7
INTEL_EDISON_MINIBOARD_J20_8 = _mraa.INTEL_EDISON_MINIBOARD_J20_8
INTEL_EDISON_MINIBOARD_J20_9 = _mraa.INTEL_EDISON_MINIBOARD_J20_9
INTEL_EDISON_MINIBOARD_J20_10 = _mraa.INTEL_EDISON_MINIBOARD_J20_10
INTEL_EDISON_MINIBOARD_J20_11 = _mraa.INTEL_EDISON_MINIBOARD_J20_11
INTEL_EDISON_MINIBOARD_J20_12 = _mraa.INTEL_EDISON_MINIBOARD_J20_12
INTEL_EDISON_MINIBOARD_J20_13 = _mraa.INTEL_EDISON_MINIBOARD_J20_13
INTEL_EDISON_MINIBOARD_J20_14 = _mraa.INTEL_EDISON_MINIBOARD_J20_14
INTEL_EDISON_GP182 = _mraa.INTEL_EDISON_GP182
INTEL_EDISON_GP135 = _mraa.INTEL_EDISON_GP135
INTEL_EDISON_GP27 = _mraa.INTEL_EDISON_GP27
INTEL_EDISON_GP20 = _mraa.INTEL_EDISON_GP20
INTEL_EDISON_GP28 = _mraa.INTEL_EDISON_GP28
INTEL_EDISON_GP111 = _mraa.INTEL_EDISON_GP111
INTEL_EDISON_GP109 = _mraa.INTEL_EDISON_GP109
INTEL_EDISON_GP115 = _mraa.INTEL_EDISON_GP115
INTEL_EDISON_GP128 = _mraa.INTEL_EDISON_GP128
INTEL_EDISON_GP13 = _mraa.INTEL_EDISON_GP13
INTEL_EDISON_GP165 = _mraa.INTEL_EDISON_GP165
INTEL_EDISON_GP19 = _mraa.INTEL_EDISON_GP19
INTEL_EDISON_GP12 = _mraa.INTEL_EDISON_GP12
INTEL_EDISON_GP183 = _mraa.INTEL_EDISON_GP183
INTEL_EDISON_GP110 = _mraa.INTEL_EDISON_GP110
INTEL_EDISON_GP114 = _mraa.INTEL_EDISON_GP114
INTEL_EDISON_GP129 = _mraa.INTEL_EDISON_GP129
INTEL_EDISON_GP130 = _mraa.INTEL_EDISON_GP130
INTEL_EDISON_GP44 = _mraa.INTEL_EDISON_GP44
INTEL_EDISON_GP46 = _mraa.INTEL_EDISON_GP46
INTEL_EDISON_GP48 = _mraa.INTEL_EDISON_GP48
INTEL_EDISON_GP131 = _mraa.INTEL_EDISON_GP131
INTEL_EDISON_GP14 = _mraa.INTEL_EDISON_GP14
INTEL_EDISON_GP40 = _mraa.INTEL_EDISON_GP40
INTEL_EDISON_GP43 = _mraa.INTEL_EDISON_GP43
INTEL_EDISON_GP77 = _mraa.INTEL_EDISON_GP77
INTEL_EDISON_GP82 = _mraa.INTEL_EDISON_GP82
INTEL_EDISON_GP83 = _mraa.INTEL_EDISON_GP83
INTEL_EDISON_GP134 = _mraa.INTEL_EDISON_GP134
INTEL_EDISON_GP45 = _mraa.INTEL_EDISON_GP45
INTEL_EDISON_GP47 = _mraa.INTEL_EDISON_GP47
INTEL_EDISON_GP49 = _mraa.INTEL_EDISON_GP49
INTEL_EDISON_GP15 = _mraa.INTEL_EDISON_GP15
INTEL_EDISON_GP84 = _mraa.INTEL_EDISON_GP84
INTEL_EDISON_GP42 = _mraa.INTEL_EDISON_GP42
INTEL_EDISON_GP41 = _mraa.INTEL_EDISON_GP41
INTEL_EDISON_GP78 = _mraa.INTEL_EDISON_GP78
INTEL_EDISON_GP79 = _mraa.INTEL_EDISON_GP79
INTEL_EDISON_GP80 = _mraa.INTEL_EDISON_GP80
INTEL_EDISON_GP81 = _mraa.INTEL_EDISON_GP81
RASPBERRY_WIRING_PIN8 = _mraa.RASPBERRY_WIRING_PIN8
RASPBERRY_WIRING_PIN9 = _mraa.RASPBERRY_WIRING_PIN9
RASPBERRY_WIRING_PIN7 = _mraa.RASPBERRY_WIRING_PIN7
RASPBERRY_WIRING_PIN15 = _mraa.RASPBERRY_WIRING_PIN15
RASPBERRY_WIRING_PIN16 = _mraa.RASPBERRY_WIRING_PIN16
RASPBERRY_WIRING_PIN0 = _mraa.RASPBERRY_WIRING_PIN0
RASPBERRY_WIRING_PIN1 = _mraa.RASPBERRY_WIRING_PIN1
RASPBERRY_WIRING_PIN2 = _mraa.RASPBERRY_WIRING_PIN2
RASPBERRY_WIRING_PIN3 = _mraa.RASPBERRY_WIRING_PIN3
RASPBERRY_WIRING_PIN4 = _mraa.RASPBERRY_WIRING_PIN4
RASPBERRY_WIRING_PIN5 = _mraa.RASPBERRY_WIRING_PIN5
RASPBERRY_WIRING_PIN12 = _mraa.RASPBERRY_WIRING_PIN12
RASPBERRY_WIRING_PIN13 = _mraa.RASPBERRY_WIRING_PIN13
RASPBERRY_WIRING_PIN6 = _mraa.RASPBERRY_WIRING_PIN6
RASPBERRY_WIRING_PIN14 = _mraa.RASPBERRY_WIRING_PIN14
RASPBERRY_WIRING_PIN10 = _mraa.RASPBERRY_WIRING_PIN10
RASPBERRY_WIRING_PIN11 = _mraa.RASPBERRY_WIRING_PIN11
RASPBERRY_WIRING_PIN17 = _mraa.RASPBERRY_WIRING_PIN17
RASPBERRY_WIRING_PIN21 = _mraa.RASPBERRY_WIRING_PIN21
RASPBERRY_WIRING_PIN18 = _mraa.RASPBERRY_WIRING_PIN18
RASPBERRY_WIRING_PIN19 = _mraa.RASPBERRY_WIRING_PIN19
RASPBERRY_WIRING_PIN22 = _mraa.RASPBERRY_WIRING_PIN22
RASPBERRY_WIRING_PIN20 = _mraa.RASPBERRY_WIRING_PIN20
RASPBERRY_WIRING_PIN26 = _mraa.RASPBERRY_WIRING_PIN26
RASPBERRY_WIRING_PIN23 = _mraa.RASPBERRY_WIRING_PIN23
RASPBERRY_WIRING_PIN24 = _mraa.RASPBERRY_WIRING_PIN24
RASPBERRY_WIRING_PIN27 = _mraa.RASPBERRY_WIRING_PIN27
RASPBERRY_WIRING_PIN25 = _mraa.RASPBERRY_WIRING_PIN25
RASPBERRY_WIRING_PIN28 = _mraa.RASPBERRY_WIRING_PIN28
RASPBERRY_WIRING_PIN29 = _mraa.RASPBERRY_WIRING_PIN29
SUCCESS = _mraa.SUCCESS
ERROR_FEATURE_NOT_IMPLEMENTED = _mraa.ERROR_FEATURE_NOT_IMPLEMENTED
ERROR_FEATURE_NOT_SUPPORTED = _mraa.ERROR_FEATURE_NOT_SUPPORTED
ERROR_INVALID_VERBOSITY_LEVEL = _mraa.ERROR_INVALID_VERBOSITY_LEVEL
ERROR_INVALID_PARAMETER = _mraa.ERROR_INVALID_PARAMETER
ERROR_INVALID_HANDLE = _mraa.ERROR_INVALID_HANDLE
ERROR_NO_RESOURCES = _mraa.ERROR_NO_RESOURCES
ERROR_INVALID_RESOURCE = _mraa.ERROR_INVALID_RESOURCE
ERROR_INVALID_QUEUE_TYPE = _mraa.ERROR_INVALID_QUEUE_TYPE
ERROR_NO_DATA_AVAILABLE = _mraa.ERROR_NO_DATA_AVAILABLE
ERROR_INVALID_PLATFORM = _mraa.ERROR_INVALID_PLATFORM
ERROR_PLATFORM_NOT_INITIALISED = _mraa.ERROR_PLATFORM_NOT_INITIALISED
ERROR_UART_OW_SHORTED = _mraa.ERROR_UART_OW_SHORTED
ERROR_UART_OW_NO_DEVICES = _mraa.ERROR_UART_OW_NO_DEVICES
ERROR_UART_OW_DATA_ERROR = _mraa.ERROR_UART_OW_DATA_ERROR
ERROR_UNSPECIFIED = _mraa.ERROR_UNSPECIFIED
PIN_VALID = _mraa.PIN_VALID
PIN_GPIO = _mraa.PIN_GPIO
PIN_PWM = _mraa.PIN_PWM
PIN_FAST_GPIO = _mraa.PIN_FAST_GPIO
PIN_SPI = _mraa.PIN_SPI
PIN_I2C = _mraa.PIN_I2C
PIN_AIO = _mraa.PIN_AIO
PIN_UART = _mraa.PIN_UART
I2C_STD = _mraa.I2C_STD
I2C_FAST = _mraa.I2C_FAST
I2C_HIGH = _mraa.I2C_HIGH
UART_PARITY_NONE = _mraa.UART_PARITY_NONE
UART_PARITY_EVEN = _mraa.UART_PARITY_EVEN
UART_PARITY_ODD = _mraa.UART_PARITY_ODD
UART_PARITY_MARK = _mraa.UART_PARITY_MARK
UART_PARITY_SPACE = _mraa.UART_PARITY_SPACE

def init():
    return _mraa.init()
init = _mraa.init

def getVersion():
    return _mraa.getVersion()
getVersion = _mraa.getVersion

def setPriority(priority):
    return _mraa.setPriority(priority)
setPriority = _mraa.setPriority

def getPlatformType():
    return _mraa.getPlatformType()
getPlatformType = _mraa.getPlatformType

def printError(result):
    return _mraa.printError(result)
printError = _mraa.printError

def pinModeTest(pin, mode):
    return _mraa.pinModeTest(pin, mode)
pinModeTest = _mraa.pinModeTest

def adcRawBits():
    return _mraa.adcRawBits()
adcRawBits = _mraa.adcRawBits

def adcSupportedBits():
    return _mraa.adcSupportedBits()
adcSupportedBits = _mraa.adcSupportedBits

def getPlatformName():
    return _mraa.getPlatformName()
getPlatformName = _mraa.getPlatformName

def getPlatformVersion(*args):
    return _mraa.getPlatformVersion(*args)
getPlatformVersion = _mraa.getPlatformVersion

def getPinCount():
    return _mraa.getPinCount()
getPinCount = _mraa.getPinCount

def getUartCount():
    return _mraa.getUartCount()
getUartCount = _mraa.getUartCount

def getI2cBusCount():
    return _mraa.getI2cBusCount()
getI2cBusCount = _mraa.getI2cBusCount

def getI2cBusId(i2c_bus):
    return _mraa.getI2cBusId(i2c_bus)
getI2cBusId = _mraa.getI2cBusId

def getPinName(pin):
    return _mraa.getPinName(pin)
getPinName = _mraa.getPinName

def getGpioLookup(pin_name):
    return _mraa.getGpioLookup(pin_name)
getGpioLookup = _mraa.getGpioLookup

def getI2cLookup(i2c_name):
    return _mraa.getI2cLookup(i2c_name)
getI2cLookup = _mraa.getI2cLookup

def getSpiLookup(spi_name):
    return _mraa.getSpiLookup(spi_name)
getSpiLookup = _mraa.getSpiLookup

def getPwmLookup(pwm_name):
    return _mraa.getPwmLookup(pwm_name)
getPwmLookup = _mraa.getPwmLookup

def getUartLookup(uart_name):
    return _mraa.getUartLookup(uart_name)
getUartLookup = _mraa.getUartLookup

def setLogLevel(level):
    return _mraa.setLogLevel(level)
setLogLevel = _mraa.setLogLevel

def hasSubPlatform():
    return _mraa.hasSubPlatform()
hasSubPlatform = _mraa.hasSubPlatform

def isSubPlatformId(pin_or_bus_id):
    return _mraa.isSubPlatformId(pin_or_bus_id)
isSubPlatformId = _mraa.isSubPlatformId

def getSubPlatformId(pin_or_bus_index):
    return _mraa.getSubPlatformId(pin_or_bus_index)
getSubPlatformId = _mraa.getSubPlatformId

def getSubPlatformIndex(pin_or_bus_id):
    return _mraa.getSubPlatformIndex(pin_or_bus_id)
getSubPlatformIndex = _mraa.getSubPlatformIndex

def getDefaultI2cBus(*args):
    return _mraa.getDefaultI2cBus(*args)
getDefaultI2cBus = _mraa.getDefaultI2cBus

def addSubplatform(subplatformtype, dev):
    return _mraa.addSubplatform(subplatformtype, dev)
addSubplatform = _mraa.addSubplatform

def removeSubplatform(subplatformtype):
    return _mraa.removeSubplatform(subplatformtype)
removeSubplatform = _mraa.removeSubplatform

def initJsonPlatform(path):
    return _mraa.initJsonPlatform(path)
initJsonPlatform = _mraa.initJsonPlatform

def gpioFromDesc(desc):
    return _mraa.gpioFromDesc(desc)
gpioFromDesc = _mraa.gpioFromDesc

def aioFromDesc(desc):
    return _mraa.aioFromDesc(desc)
aioFromDesc = _mraa.aioFromDesc

def uartFromDesc(desc):
    return _mraa.uartFromDesc(desc)
uartFromDesc = _mraa.uartFromDesc

def spiFromDesc(desc):
    return _mraa.spiFromDesc(desc)
spiFromDesc = _mraa.spiFromDesc

def i2cFromDesc(desc):
    return _mraa.i2cFromDesc(desc)
i2cFromDesc = _mraa.i2cFromDesc

def pwmFromDesc(desc):
    return _mraa.pwmFromDesc(desc)
pwmFromDesc = _mraa.pwmFromDesc

def ledFromDesc(desc):
    return _mraa.ledFromDesc(desc)
ledFromDesc = _mraa.ledFromDesc
MODE_STRONG = _mraa.MODE_STRONG
MODE_PULLUP = _mraa.MODE_PULLUP
MODE_PULLDOWN = _mraa.MODE_PULLDOWN
MODE_HIZ = _mraa.MODE_HIZ
DIR_OUT = _mraa.DIR_OUT
DIR_IN = _mraa.DIR_IN
DIR_OUT_HIGH = _mraa.DIR_OUT_HIGH
DIR_OUT_LOW = _mraa.DIR_OUT_LOW
EDGE_NONE = _mraa.EDGE_NONE
EDGE_BOTH = _mraa.EDGE_BOTH
EDGE_RISING = _mraa.EDGE_RISING
EDGE_FALLING = _mraa.EDGE_FALLING
MODE_IN_ACTIVE_HIGH = _mraa.MODE_IN_ACTIVE_HIGH
MODE_IN_ACTIVE_LOW = _mraa.MODE_IN_ACTIVE_LOW
MODE_OUT_OPEN_DRAIN = _mraa.MODE_OUT_OPEN_DRAIN
MODE_OUT_PUSH_PULL = _mraa.MODE_OUT_PUSH_PULL
class Gpio(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Gpio, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Gpio, name)
    __repr__ = _swig_repr

    def __init__(self, pin, owner=True, raw=False):
        this = _mraa.new_Gpio(pin, owner, raw)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mraa.delete_Gpio
    def __del__(self):
        return None

    def edge(self, mode):
        return _mraa.Gpio_edge(self, mode)

    def isr(self, mode, pyfunc, args):
        return _mraa.Gpio_isr(self, mode, pyfunc, args)

    def isrExit(self):
        return _mraa.Gpio_isrExit(self)

    def mode(self, mode):
        return _mraa.Gpio_mode(self, mode)

    def dir(self, dir):
        return _mraa.Gpio_dir(self, dir)

    def readDir(self):
        return _mraa.Gpio_readDir(self)

    def read(self):
        return _mraa.Gpio_read(self)

    def write(self, value):
        return _mraa.Gpio_write(self, value)

    def useMmap(self, enable):
        return _mraa.Gpio_useMmap(self, enable)

    def getPin(self, raw=False):
        return _mraa.Gpio_getPin(self, raw)

    def inputMode(self, mode):
        return _mraa.Gpio_inputMode(self, mode)

    def outputMode(self, mode):
        return _mraa.Gpio_outputMode(self, mode)

# Register Gpio in _mraa:
_mraa.Gpio_swigregister(Gpio)

class I2c(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, I2c, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, I2c, name)
    __repr__ = _swig_repr

    def __init__(self, bus, raw=False):
        this = _mraa.new_I2c(bus, raw)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mraa.delete_I2c
    def __del__(self):
        return None

    def frequency(self, mode):
        return _mraa.I2c_frequency(self, mode)

    def address(self, address):
        return _mraa.I2c_address(self, address)

    def readByte(self):
        return _mraa.I2c_readByte(self)

    def read(self, data):
        return _mraa.I2c_read(self, data)

    def readReg(self, reg):
        return _mraa.I2c_readReg(self, reg)

    def readWordReg(self, reg):
        return _mraa.I2c_readWordReg(self, reg)

    def readBytesReg(self, reg, data):
        return _mraa.I2c_readBytesReg(self, reg, data)

    def writeByte(self, data):
        return _mraa.I2c_writeByte(self, data)

    def write(self, data):
        return _mraa.I2c_write(self, data)

    def writeReg(self, reg, data):
        return _mraa.I2c_writeReg(self, reg, data)

    def writeWordReg(self, reg, data):
        return _mraa.I2c_writeWordReg(self, reg, data)

# Register I2c in _mraa:
_mraa.I2c_swigregister(I2c)

class Pwm(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Pwm, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Pwm, name)
    __repr__ = _swig_repr

    def __init__(self, pin, owner=True, chipid=-1):
        this = _mraa.new_Pwm(pin, owner, chipid)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mraa.delete_Pwm
    def __del__(self):
        return None

    def write(self, percentage):
        return _mraa.Pwm_write(self, percentage)

    def read(self):
        return _mraa.Pwm_read(self)

    def period(self, period):
        return _mraa.Pwm_period(self, period)

    def period_ms(self, ms):
        return _mraa.Pwm_period_ms(self, ms)

    def period_us(self, us):
        return _mraa.Pwm_period_us(self, us)

    def pulsewidth(self, seconds):
        return _mraa.Pwm_pulsewidth(self, seconds)

    def pulsewidth_ms(self, ms):
        return _mraa.Pwm_pulsewidth_ms(self, ms)

    def pulsewidth_us(self, us):
        return _mraa.Pwm_pulsewidth_us(self, us)

    def enable(self, enable):
        return _mraa.Pwm_enable(self, enable)

    def max_period(self):
        return _mraa.Pwm_max_period(self)

    def min_period(self):
        return _mraa.Pwm_min_period(self)

# Register Pwm in _mraa:
_mraa.Pwm_swigregister(Pwm)

SPI_MODE0 = _mraa.SPI_MODE0
SPI_MODE1 = _mraa.SPI_MODE1
SPI_MODE2 = _mraa.SPI_MODE2
SPI_MODE3 = _mraa.SPI_MODE3
class Spi(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Spi, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Spi, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _mraa.new_Spi(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mraa.delete_Spi
    def __del__(self):
        return None

    def mode(self, mode):
        return _mraa.Spi_mode(self, mode)

    def frequency(self, hz):
        return _mraa.Spi_frequency(self, hz)

    def writeByte(self, data):
        return _mraa.Spi_writeByte(self, data)

    def writeWord(self, data):
        return _mraa.Spi_writeWord(self, data)

    def write(self, txBuf):
        return _mraa.Spi_write(self, txBuf)

    def lsbmode(self, lsb):
        return _mraa.Spi_lsbmode(self, lsb)

    def bitPerWord(self, bits):
        return _mraa.Spi_bitPerWord(self, bits)

# Register Spi in _mraa:
_mraa.Spi_swigregister(Spi)

class Aio(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Aio, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Aio, name)
    __repr__ = _swig_repr

    def __init__(self, pin):
        this = _mraa.new_Aio(pin)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mraa.delete_Aio
    def __del__(self):
        return None

    def read(self):
        return _mraa.Aio_read(self)

    def readFloat(self):
        return _mraa.Aio_readFloat(self)

    def setBit(self, bits):
        return _mraa.Aio_setBit(self, bits)

    def getBit(self):
        return _mraa.Aio_getBit(self)

# Register Aio in _mraa:
_mraa.Aio_swigregister(Aio)

class Uart(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Uart, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Uart, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _mraa.new_Uart(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mraa.delete_Uart
    def __del__(self):
        return None

    def getDevicePath(self):
        return _mraa.Uart_getDevicePath(self)

    def read(self, data):
        return _mraa.Uart_read(self, data)

    def write(self, data):
        return _mraa.Uart_write(self, data)

    def readStr(self, length):
        return _mraa.Uart_readStr(self, length)

    def writeStr(self, data):
        return _mraa.Uart_writeStr(self, data)

    def dataAvailable(self, millis=0):
        return _mraa.Uart_dataAvailable(self, millis)

    def flush(self):
        return _mraa.Uart_flush(self)

    def sendBreak(self, duration):
        return _mraa.Uart_sendBreak(self, duration)

    def setBaudRate(self, baud):
        return _mraa.Uart_setBaudRate(self, baud)

    def setMode(self, bytesize, parity, stopbits):
        return _mraa.Uart_setMode(self, bytesize, parity, stopbits)

    def setFlowcontrol(self, xonxoff, rtscts):
        return _mraa.Uart_setFlowcontrol(self, xonxoff, rtscts)

    def setTimeout(self, read, write, interchar):
        return _mraa.Uart_setTimeout(self, read, write, interchar)

    def setNonBlocking(self, nonblock):
        return _mraa.Uart_setNonBlocking(self, nonblock)

# Register Uart in _mraa:
_mraa.Uart_swigregister(Uart)

class Led(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Led, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Led, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _mraa.new_Led(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _mraa.delete_Led
    def __del__(self):
        return None

    def setBrightness(self, value):
        return _mraa.Led_setBrightness(self, value)

    def readBrightness(self):
        return _mraa.Led_readBrightness(self)

    def readMaxBrightness(self):
        return _mraa.Led_readMaxBrightness(self)

    def trigger(self, trigger):
        return _mraa.Led_trigger(self, trigger)

    def clearTrigger(self):
        return _mraa.Led_clearTrigger(self)

# Register Led in _mraa:
_mraa.Led_swigregister(Led)

# This file is compatible with both classic and new-style classes.


