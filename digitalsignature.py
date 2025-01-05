from rsa import RSA

class DigitalSignature:
    asymmetricEncryption = RSA()

    def sign(self, private_key, document):
        document = str(document)
        signature = DigitalSignature.asymmetricEncryption.encrypt(document, private_key)
        return signature
    
    def verify(self, public_key, document, signature):
        document = str(document)
        signature_content = DigitalSignature.asymmetricEncryption.decrypt(signature, public_key)
        for c in signature_content:
            if not c.isalnum():
                raise ValueError(f"Verify signature of document={document} : Signature is wrong")
        return document == signature_content
