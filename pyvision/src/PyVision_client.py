##################################################
# file: PyVision_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/bin/wsdl2py ./wsdl/binding.wsdl
# 
##################################################


import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

# Locator
class PyVisionServiceLocator:
    PyVision_address = "http://127.0.0.1:8080/pyvision.py"
    def getPyVisionAddress(self):
        return PyVisionServiceLocator.PyVision_address
    def getPyVision(self, url=None, **kw):
        return BindingSOAP(url or PyVisionServiceLocator.PyVision_address, **kw)

# Methods
class BindingSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: echo
    def echo(self, request, **kw):
        if isinstance(request, EchoRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="urn:PyVision#echo", encodingStyle="http://schemas.xmlsoap.org/soap/encoding/", **kw)
        # no output wsaction
        typecode = Struct(pname=None, ofwhat=EchoResponse.typecode.ofwhat, pyclass=EchoResponse.typecode.pyclass)
        response = self.binding.Receive(typecode)
        return response

    # op: add
    def add(self, request, **kw):
        if isinstance(request, AddRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="urn:PyVision#add", encodingStyle="http://schemas.xmlsoap.org/soap/encoding/", **kw)
        # no output wsaction
        typecode = Struct(pname=None, ofwhat=AddResponse.typecode.ofwhat, pyclass=AddResponse.typecode.pyclass)
        response = self.binding.Receive(typecode)
        return response

    # op: send
    def send(self, request, **kw):
        if isinstance(request, SendRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="urn:PyVision#send", encodingStyle="http://schemas.xmlsoap.org/soap/encoding/", **kw)
        # no output wsaction
        typecode = Struct(pname=None, ofwhat=SendResponse.typecode.ofwhat, pyclass=SendResponse.typecode.pyclass)
        response = self.binding.Receive(typecode)
        return response

class EchoRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        Message -- part Message
        """
        self._Message =  kw.get("Message")
EchoRequest.typecode = Struct(pname=("urn:PyVision","echo"), ofwhat=[ZSI.TC.String(pname="Message", aname="_Message", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=EchoRequest, encoded="urn:PyVision")

class EchoResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        Message -- part Message
        """
        self._Message =  kw.get("Message")
EchoResponse.typecode = Struct(pname=("urn:PyVision","echoResponse"), ofwhat=[ZSI.TC.String(pname="Message", aname="_Message", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=EchoResponse, encoded="urn:PyVision")

class AddRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        One -- part One
        Two -- part Two
        """
        self._One =  kw.get("One")
        self._Two =  kw.get("Two")
AddRequest.typecode = Struct(pname=("urn:PyVision","add"), ofwhat=[ZSI.TC.AnyType(pname="One", aname="_One", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.AnyType(pname="Two", aname="_Two", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=AddRequest, encoded="urn:PyVision")

class AddResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        Result -- part Result
        """
        self._Result =  kw.get("Result")
AddResponse.typecode = Struct(pname=("urn:PyVision","addResponse"), ofwhat=[ZSI.TC.AnyType(pname="Result", aname="_Result", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=AddResponse, encoded="urn:PyVision")

class SendRequest:
    def __init__(self, **kw):
        """Keyword parameters:
        Date -- part Date
        Sender -- part Sender
        Reference -- part Reference
        Message -- part Message
        Priority -- part Priority
        """
        self._Date =  kw.get("Date")
        self._Sender =  kw.get("Sender")
        self._Reference =  kw.get("Reference")
        self._Message =  kw.get("Message")
        self._Priority =  kw.get("Priority")
SendRequest.typecode = Struct(pname=("urn:PyVision","send"), ofwhat=[ZSI.TC.String(pname="Date", aname="_Date", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.String(pname="Sender", aname="_Sender", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.String(pname="Reference", aname="_Reference", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.String(pname="Message", aname="_Message", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True), ZSI.TC.AnyType(pname="Priority", aname="_Priority", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=SendRequest, encoded="urn:PyVision")

class SendResponse:
    def __init__(self, **kw):
        """Keyword parameters:
        Message -- part Message
        """
        self._Message =  kw.get("Message")
SendResponse.typecode = Struct(pname=("urn:PyVision","sendResponse"), ofwhat=[ZSI.TC.String(pname="Message", aname="_Message", typed=False, encoded=None, minOccurs=1, maxOccurs=1, nillable=True)], pyclass=SendResponse, encoded="urn:PyVision")
