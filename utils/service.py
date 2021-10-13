import base64
import hashlib
import hmac
CLIENT_SECRET='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'


class Utils:
    # def verify_webhook(data, hmac_header):
    #     """Verify Shopify webhook."""
    #     digest = hmac.new(CLIENT_SECRET, data, hashlib.sha256).digest()
    #     computed_hmac = base64.b64encode(digest)
    #     return hmac.compare_digest(computed_hmac, hmac_header.encode('utf-8'))


    def verify_webhook(data, hmac_header):
        digest = hmac.new(CLIENT_SECRET.encode('utf-8'),data,hashlib.sha256).digest()
        computed_hmac = base64.b64encode(digest)
        return hmac.compare_digest(computed_hmac, hmac_header.encode('utf-8'))


utils=Utils()