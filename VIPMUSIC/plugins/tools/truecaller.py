import phonenumbers
from phonenumbers import carrier, geocoder, phonenumberutil, timezone
from pyrogram import filters

from VIPMUSIC import app


@app.on_message(filters.command("tinfo"))
def phone_number_info(client, message):
    phone_number = message.text.split("/tinfo", 1)[1].strip()

    try:
        number = phonenumbers.parse(phone_number, None)
        country_code = phonenumbers.region_code_for_number(number)
        location = geocoder.description_for_number(number, "en")
        carrier_name = (
            carrier.name_for_number(number, "en")
            if carrier.name_for_number(number, "en")
            else "Unknown Carrier"
        )

        number_type = phonenumberutil.number_type(number)
        number_type_description = (
            "Mobile"
            if number_type == phonenumberutil.PhoneNumberType.MOBILE
            else (
                "Fixed-line"
                if number_type == phonenumberutil.PhoneNumberType.FIXED_LINE
                else (
                    "Toll-free"
                    if number_type == phonenumberutil.PhoneNumberType.TOLL_FREE
                    else (
                        "Premium rate"
                        if number_type == phonenumberutil.PhoneNumberType.PREMIUM_RATE
                        else (
                            "Shared cost"
                            if number_type
                            == phonenumberutil.PhoneNumberType.SHARED_COST
                            else (
                                "VOIP"
                                if number_type == phonenumberutil.PhoneNumberType.VOIP
                                else "Other"
                            )
                        )
                    )
                )
            )
        )

        validity = "Valid" if phonenumbers.is_valid_number(number) else "Invalid"
        formatted_number = phonenumbers.format_number(
            number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        possible_lengths = [
            len(str(number))
            for number in phonenumbers.PhoneNumberMatcher(phone_number, "ZZ")
        ]
        possible_lengths_description = (
            f"Possible lengths: {', '.join(str(length) for length in possible_lengths)}"
        )
        country_name = geocoder.country_name_for_number(number, "en")
        is_possible = (
            "Possible" if phonenumbers.is_possible_number(number) else "Not possible"
        )

        time_zones = timezone.time_zones_for_number(number)
        time_zones_description = (
            f"Time Zones: {', '.join(time_zones)}"
            if time_zones
            else "Time zone information not available"
        )

        national_number = phonenumbers.format_number(
            number, phonenumbers.PhoneNumberFormat.NATIONAL
        )
        extension = number.extension if number.extension else "No extension"

        latitude, longitude = None, None
        administrative_area = None
        possible_geocoding = None

        if location != "Unknown":
            info = geocoder.description_for_number(number, "en", region=None)
            location_info = info.split(", ")
            if len(location_info) >= 2:
                latitude_longitude = location_info[-1].split("/")
                if len(latitude_longitude) == 2:
                    latitude, longitude = latitude_longitude
                    administrative_area = location_info[-2]
                    possible_geocoding = geocoder.description_for_number(
                        number, "en", region="US"
                    )
                else:
                    latitude, longitude = None, None
                    administrative_area = None
                    possible_geocoding = None

        is_possible_emergency_number = (
            "Yes" if phonenumbers.is_possible_number_for_type(number, "001") else "No"
        )

        if hasattr(carrier, "name_for_number"):
            carrier_name = carrier.name_for_number(number, "en") or "Unknown Carrier"
        else:
            carrier_name = "Carrier information not available"

        valid_in_region = phonenumbers.is_valid_number_for_region(number, country_code)
        is_possible_number_type = (
            "Possible"
            if phonenumbers.is_possible_number_for_type(number, "MOBILE")
            else "Not possible"
        )
        is_possible_short_code = (
            "Possible"
            if phonenumbers.is_possible_short_number(number)
            else "Not possible"
        )
        is_valid_number_in_region = (
            "Valid"
            if phonenumbers.is_valid_number_for_region(number, country_code)
            else "Not valid"
        )

        time_zone_name = None
        if len(time_zones) > 0:
            time_zone_info = timezone.time_zones_for_number(number)
            if time_zone_info:
                time_zone_name = ", ".join(time_zone_info)

        possible_lengths = len(
            phonenumbers.PhoneNumberMatcher(phone_number, "ZZ").next().raw_string
        )
        national_significant_number = phonenumbers.national_significant_number(number)
        e164_format = phonenumbers.format_number(
            number, phonenumbers.PhoneNumberFormat.E164
        )
        rfc3966_format = phonenumbers.format_number(
            number, phonenumbers.PhoneNumberFormat.RFC3966
        )
        possible_types = str(number_type)

        details = {
            "Country Code": country_code,
            "Country Name": country_name,
            "Location": location,
            "Latitude": latitude,
            "Longitude": longitude,
            "Administrative Area": administrative_area,
            "Possible Geocoding (US)": possible_geocoding,
            "Sim Name": carrier_name,
            "Number Type": number_type_description,
            "Validity": validity,
            "Valid in Region": valid_in_region,
            "Formatted Number": formatted_number,
            "Possible Lengths": possible_lengths_description,
            "Is Possible Number": is_possible,
            "Time Zones": time_zones_description,
            "National Number": national_number,
            "Extension": extension,
            "Possible Emergency Number": is_possible_emergency_number,
            "Possible Mobile Number": is_possible_number_type,
            "Possible Short Code": is_possible_short_code,
            "Valid Number in Region": is_valid_number_in_region,
            "Time Zone Name": time_zone_name,
            "Possible Lengths": possible_lengths,
            "National Significant Number": national_significant_number,
            "E164 Format": e164_format,
            "RFC3966 Format": rfc3966_format,
            "Possible Types": possible_types,
        }

        details_str = "\n".join([f"{key}: {value}" for key, value in details.items()])

        message.reply_text("🌐 Phone Number Details 🌐:\n" + details_str)

    except phonenumbers.phonenumberutil.NumberParseException as e:
        message.reply_text("❌ Number could not be parsed: " + str(e))
