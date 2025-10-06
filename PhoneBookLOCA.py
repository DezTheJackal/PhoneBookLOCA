#!/usr/bin/env python3
"""
PhoneBookLOCA v1.0 - Phone Number Location Lookup Tool
OSINT tool for educational purposes only
"""

import sys
import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def print_banner():
    """Display the tool banner"""
    print("\n" + "="*50)
    print("  PhoneBookLOCA v1.0 - OSINT Phone Lookup")
    print("  DEV: DEZTHEJACKAL")
    print("="*50 + "\n")


def validate_phone_number(number):
    """
    Validate and parse phone number
    
    Args:
        number (str): Phone number to validate
        
    Returns:
        tuple: (is_valid, parsed_number, error_message)
    """
    try:
        parsed = phonenumbers.parse(number, None)
        if phonenumbers.is_valid_number(parsed):
            return True, parsed, None
        else:
            return False, None, "Invalid phone number format"
    except phonenumbers.NumberParseException as e:
        return False, None, f"Parse error: {str(e)}"


def lookup_phone_number(number):
    """
    Perform comprehensive phone number lookup
    
    Args:
        number (str): Phone number to lookup
    """
    print(f"[*] Target: {number}")
    print(f"[*] Initiating trace...\n")
    
    # Validate number
    is_valid, parsed, error = validate_phone_number(number)
    
    if not is_valid:
        print(f"[!] Error: {error}")
        print("[!] Trace failed\n")
        return False
    
    # Get location
    location = geocoder.description_for_number(parsed, "en")
    if not location:
        location = "Unknown"
    
    # Get carrier
    carrier_name = carrier.name_for_number(parsed, "en")
    if not carrier_name:
        carrier_name = "Unknown"
    
    # Get timezone
    timezones = timezone.time_zones_for_number(parsed)
    if not timezones:
        timezones = ["Unknown"]
    
    # Get country code
    country_code = f"+{parsed.country_code}"
    
    # Display results
    print("[+] Results:")
    print(f"    Country Code: {country_code}")
    print(f"    Location: {location}")
    print(f"    Carrier: {carrier_name}")
    print(f"    Timezone(s): {', '.join(timezones)}")
    print(f"    Valid: Yes")
    print("\n[+] Trace Complete\n")
    
    return True


def interactive_mode():
    """Run the tool in interactive mode"""
    print_banner()
    print("Enter phone numbers to lookup (with country code, e.g., +1234567890)")
    print("Type 'quit' or 'exit' to stop\n")
    
    while True:
        try:
            number = input("Enter phone number: ").strip()
            
            if number.lower() in ['quit', 'exit', 'q']:
                print("\n[*] Exiting PhoneBookLOCA. Goodbye!\n")
                break
            
            if not number:
                print("[!] Please enter a phone number\n")
                continue
            
            print()
            lookup_phone_number(number)
            
        except KeyboardInterrupt:
            print("\n\n[*] Interrupted. Exiting...\n")
            break
        except Exception as e:
            print(f"\n[!] Unexpected error: {str(e)}\n")


def main():
    """Main entry point"""
    # Check if number provided as argument
    if len(sys.argv) > 1:
        print_banner()
        number = sys.argv[1]
        lookup_phone_number(number)
    else:
        # Run in interactive mode
        interactive_mode()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Exiting...\n")
        sys.exit(0)
