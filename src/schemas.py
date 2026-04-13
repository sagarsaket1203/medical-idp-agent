from pydantic import BaseModel


class ContactInfo(BaseModel):
    phone_number: str
    email: str


class Address(BaseModel):
    street_address: str
    city: str
    state: str
    postal_code: str


class MedicalSpecialties(BaseModel):
    specialties: list[str]


class FacilityCapabilities(BaseModel):
    capabilities: list[str]


class MedicalFacility(BaseModel):
    name: str
    contact_info: ContactInfo
    address: Address
    specialties: MedicalSpecialties
    capabilities: FacilityCapabilities


class ExtractionResult(BaseModel):
    data: dict
    success: bool


class SynthesisResult(BaseModel):
    summary: str
    confidence: float


class PlanningAction(BaseModel):
    action: str
    parameters: dict