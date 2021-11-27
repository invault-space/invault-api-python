import base64
from typing import (
    Union,
)

from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5

from invaultapi._util import to_bytes


class RSAKey:
    def __init__(self, bits = 2048):
        self.__rsa = RSA.generate(bits, Random.new().read)

    @classmethod
    def import_key(cls, extern_key, passphrase = None):
        """Import an RSA key."""
        try:
            rsa = RSA.import_key(extern_key, passphrase)
        except ValueError:
            # Add Pre-Encapsulation Boundary and Post-Encapsulation Boundary
            extern_key = to_bytes(extern_key)
            extern_key = b"-----BEGIN KEY-----\n" + extern_key + b"\n-----END KEY-----"
            rsa = RSA.import_key(extern_key, passphrase)
        key = cls.__new__(cls)
        key.__rsa = rsa
        return key

    def public_key(self, format = "PEM") -> bytes:
        rsa = self.__rsa
        key = rsa.public_key().export_key(format)
        return key

    def private_key(self, format = "PEM", passphrase = None, pkcs = 8) -> bytes:
        rsa = self.__rsa
        key = rsa.export_key(format, passphrase = passphrase, pkcs = pkcs)
        return key

    def sign(self, data: Union[str, bytes, bytearray]) -> bytes:
        """Create the PKCS#1 v1.5 signature of a message."""
        if isinstance(data, str):
            message = data.encode()
        elif isinstance(data, bytes) or isinstance(data, bytearray):
            message = bytes(data)
        else:
            raise ValueError("invalid data type")
        rsa = self.__rsa
        signer = Signature_pkcs1_v1_5.new(rsa)
        digest = SHA256.new()
        digest.update(message)
        return signer.sign(digest)

    def verify(self, data: Union[str, bytes, bytearray], signature: Union[str, bytes, bytearray]) -> bool:
        """Check if the  PKCS#1 v1.5 signature over a message is valid.

        :parameter data:
            message data.
        :type data: string, byte string, or byte array

        :parameter signature:
            PKCS#1 v1.5 signature over message data.
        :type data: hex encoded string, base64 encoded string, byte string, or byte array.
        """
        if isinstance(data, str):
            message = data.encode()
        elif isinstance(data, bytes) or isinstance(data, bytearray):
            message = data
        else:
            raise ValueError("invalid data type")
        rsa = self.__rsa
        verifier = Signature_pkcs1_v1_5.new(rsa)
        digest = SHA256.new()
        digest.update(message)
        s = signature
        if isinstance(s, str):
            if s[:2] in ["0x", "0X"]:
                s = s[2:]
            try:
                s = bytes.fromhex(s)
            except:
                s = base64.b64decode(s)
        elif not isinstance(s, bytes) and not isinstance(s, bytearray):
            raise ValueError("invalid signature type")
        return verifier.verify(digest, s)
