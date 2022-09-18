from unit.models import *


class CustomerTokenDTO(UnitDTO):
    @staticmethod
    def from_json_api(_id, _type, attributes, relationships):
        return CustomerTokenDTO(_id, _type, attributes_to_object(attributes), relationships)


class CustomerVerificationTokenDTO(UnitDTO):
    @staticmethod
    def from_json_api(_id, _type, attributes, relationships):
        return CustomerVerificationTokenDTO(_id, _type, attributes_to_object(attributes), relationships)


class CreateCustomerToken(UnitRequest):
    def __init__(self, customer_id: str, scope: str, verification_token: Optional[str] = None,
                 verification_code: Optional[str] = None, expires_in: Optional[int] = None,
                 jwt_subject: Optional[str] = None):
        self.customer_id = customer_id
        self.scope = scope
        self.verification_token = verification_token
        self.verification_code = verification_code
        self.expires_in = expires_in
        self.jwt_subject = jwt_subject

    def to_json_api(self) -> Dict:
        payload = {
            "data": {
                "type": "customerToken",
                "attributes": {
                    "scope": self.scope
                }
            }
        }

        if self.expires_in:
            payload["data"]["attributes"]["expiresIn"] = self.expires_in

        if self.verification_token:
            payload["data"]["attributes"]["verificationToken"] = self.verification_token

        if self.verification_code:
            payload["data"]["attributes"]["verificationCode"] = self.verification_code

        if self.jwt_subject:
            payload["data"]["attributes"]["jwtSubject"] = self.jwt_subject

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())


class CreateCustomerTokenVerification(UnitRequest):
    def __init__(self, customer_id: str, channel: str, phone: Optional[Phone] = None, app_hash: Optional[str] = None,
                 language: Optional[str] = None):
        self.customer_id = customer_id
        self.channel = channel
        self.phone = phone
        self.app_hash = app_hash
        self.language = language

    def to_json_api(self) -> Dict:
        payload = {
            "data": {
                "type": "customerTokenVerification",
                "attributes": {
                    "channel": self.channel
                }
            }
        }

        if self.phone:
            payload["data"]["attributes"]["phone"] = self.phone

        if self.app_hash:
            payload["data"]["attributes"]["appHash"] = self.app_hash

        if self.language:
            payload["data"]["attributes"]["language"] = self.language

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())

