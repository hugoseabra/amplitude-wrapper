from dataclasses import dataclass, asdict
from typing import *


@dataclass
class AmplitudeEventProperties:
    # Required Fields
    event_type: str
    user_id: str

    # Recommended Fields
    event_id: Optional[str] = None
    device_id: Optional[str] = None
    session_id: Optional[str] = None
    platform: Optional[str] = None
    version_name: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    city: Optional[str] = None
    dma: Optional[str] = None
    language: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    productId: Optional[str] = None
    revenue: Optional[float] = None
    eventType: Optional[str] = None
    location_lat: Optional[float] = None
    location_lng: Optional[float] = None
    ip: Optional[str] = None
    idfa: Optional[str] = None
    idfv: Optional[str] = None
    adid: Optional[str] = None
    android_id: Optional[str] = None
    event_properties: Optional[dict] = None
    user_properties: Optional[dict] = None
    app_version: Optional[str] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    device_brand: Optional[str] = None
    device_manufacturer: Optional[str] = None
    device_model: Optional[str] = None
    carrier: Optional[str] = None
    library: Optional[str] = None
    uuid: Optional[str] = None
    event_time: Optional[int] = None
    revenue_type: Optional[str] = None
    data: Optional[dict] = None
    groups: Optional[dict] = None
    paying: Optional[bool] = None
    start_version: Optional[str] = None
    limit_ad_tracking: Optional[bool] = None
    session_num: Optional[int] = None
    dma_mapping: Optional[str] = None
    ltv_amount: Optional[float] = None
    ltv_sale_amount: Optional[float] = None
    ltv_transaction_id: Optional[str] = None
    ltv_receipt: Optional[str] = None
    ltv_purchase_id: Optional[str] = None
    ltv_sku: Optional[str] = None
    ltv_currency: Optional[str] = None
    ltv_quantity: Optional[int] = None
    ltv_receipt_signature: Optional[str] = None
    ltv_payment_provider: Optional[str] = None
    ltv_subscription_id: Optional[str] = None
    ltv_google_play_purchase_token: Optional[str] = None
    ltv_ios_original_transaction_id: Optional[str] = None
    ltv_user_agent: Optional[str] = None
    ltv_ip: Optional[str] = None
    ltv_event_properties: Optional[dict] = None
    ltv_user_properties: Optional[dict] = None
    ltv_device_id: Optional[str] = None
    ltv_idfa: Optional[str] = None
    ltv_idfv: Optional[str] = None
    ltv_adid: Optional[str] = None
    ltv_android_id: Optional[str] = None

    def dict(self) -> Dict[str, Any]:
        return asdict(self)
