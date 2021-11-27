import os
import sys

from invaultapi import RSAKey

def show_help():
    print("python3", os.path.basename(sys.argv[0]), "[-h | --keyfile-name <filename>]")

if "__main__" == __name__:
    if len(sys.argv) > 1 and "-h" == sys.argv[1]:
        show_help()
        sys.exit(0)
    rsa = RSAKey()
    public_key = rsa.public_key()
    private_key = rsa.private_key()
    if 1 == len(sys.argv):
        print("public key:", public_key)
        print("private key:", private_key)
        sys.exit(0)
    if 3 == len(sys.argv) and "--keyfile-name" == sys.argv[1]:
        public_key_file = sys.argv[2] + "_pub.pem"
        private_key_file = sys.argv[2] + ".pem"
        with open(public_key_file, "wb") as f:
            f.write(public_key)
        with open(private_key_file, "wb") as f:
            f.write(private_key)
        print("public key has been saved to file", public_key_file)
        print("private key has been saved to file", private_key_file)
        sys.exit(0)
    show_help()
    sys.exit(1)