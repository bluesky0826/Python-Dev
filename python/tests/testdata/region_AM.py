"""Auto-generated file, do not edit by hand. AM metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AM = PhoneMetadata(id='AM', country_code=374, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{7}', possible_number_pattern='\\d{5,8}', possible_length=(8,), possible_length_local_only=(5, 6)),
    fixed_line=PhoneNumberDesc(national_number_pattern='[1-9]\\d{7}', possible_number_pattern='\\d{5,8}', example_number='10123456', possible_length=(8,), possible_length_local_only=(5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='[1-9]\\d{7}', possible_number_pattern='\\d{5,8}', example_number='10123456', possible_length=(8,), possible_length_local_only=(5, 6)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='0',
    national_prefix_for_parsing='0')
