"""Auto-generated file, do not edit by hand. AO metadata"""
from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AO = PhoneMetadata(id='AO', country_code=244, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[29]\\d{8}', possible_number_pattern='\\d{9}', possible_length=(9,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2\\d(?:[26-9]\\d|\\d[26-9])\\d{5}', example_number='222123456', possible_length=(9,)),
    mobile=PhoneNumberDesc(national_number_pattern='9[1-3]\\d{7}', example_number='923123456', possible_length=(9,)),
    toll_free=PhoneNumberDesc(),
    premium_rate=PhoneNumberDesc(),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='0~0',
    national_prefix_for_parsing='0~0',
    number_format=[NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3')])
