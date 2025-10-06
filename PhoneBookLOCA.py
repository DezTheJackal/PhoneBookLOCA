#!/usr/bin/env python3
"""
PhoneBookLOCA v1.0 - Phone Number Location Lookup Tool
OSINT tool for educational purposes only
"""

import sys
import json
import argparse
import csv
import re
from typing import Dict, Optional, Tuple, List
from datetime import datetime
from pathlib import Path

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except ImportError:
    print("\n[!] Error: 'phonenumbers' module not found")
    print("[*] Install with: pip3 install phonenumbers\n")
    sys.exit(1)


class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


class PhoneIntel:
    """Main intelligence gathering class"""
    
    def __init__(self):
        self.results_cache = []
        
    def print_banner(self):
        """Display the tool banner"""
        print("\n" + "="*50)
        print("  PhoneBookLOCA v1.0 - OSINT Phone Lookup")
        print("  DEV: DEZTHEJACKAL")
        print("="*50 + "\n")

    def validate_phone_number(self, number: str) -> Tuple[bool, Optional[phonenumbers.PhoneNumber], Optional[str]]:
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

    def get_number_type(self, parsed: phonenumbers.PhoneNumber) -> str:
        """Determine the type of phone number"""
        number_type = phonenumbers.number_type(parsed)
        type_mapping = {
            phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
            phonenumbers.PhoneNumberType.MOBILE: "Mobile",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Toll Free",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
            phonenumbers.PhoneNumberType.SHARED_COST: "Shared Cost",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
            phonenumbers.PhoneNumberType.PAGER: "Pager",
            phonenumbers.PhoneNumberType.UAN: "UAN",
            phonenumbers.PhoneNumberType.VOICEMAIL: "Voicemail",
            phonenumbers.PhoneNumberType.UNKNOWN: "Unknown"
        }
        return type_mapping.get(number_type, "Unknown")

    def format_number_variants(self, parsed: phonenumbers.PhoneNumber) -> Dict[str, str]:
        """Generate different format variants of the number"""
        return {
            "E164": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164),
            "International": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "National": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL),
            "RFC3966": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.RFC3966)
        }

    def get_regional_info(self, parsed: phonenumbers.PhoneNumber) -> Dict[str, str]:
        """Get regional information"""
        region_code = phonenumbers.region_code_for_number(parsed)
        return {
            "region_code": region_code or "Unknown",
            "country_name": geocoder.country_name_for_number(parsed, "en") or "Unknown"
        }

    def extract_numbers_from_text(self, text: str, default_region: str = "US") -> List[str]:
        """
        Extract phone numbers from free-form text
        
        Args:
            text: Text containing potential phone numbers
            default_region: Default country code for parsing
            
        Returns:
            List of extracted phone numbers
        """
        numbers = []
        for match in phonenumbers.PhoneNumberMatcher(text, default_region):
            numbers.append(phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))
        return list(set(numbers))

    def generate_number_variants(self, parsed: phonenumbers.PhoneNumber) -> List[str]:
        """
        Generate common formatting variants
        
        Args:
            parsed: Parsed phone number object
            
        Returns:
            List of number format variants
        """
        variants = []
        
        e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        national = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        
        variants.extend([
            e164,
            e164.replace('+', ''),
            national,
            national.replace(' ', ''),
            national.replace('-', ''),
            national.replace('(', '').replace(')', ''),
            f"00{e164[1:]}"
        ])
        
        return list(set(variants))

    def lookup_phone_number(self, number: str, verbose: bool = False, 
                          json_output: bool = False, show_variants: bool = False) -> Optional[Dict]:
        """
        Perform comprehensive phone number lookup
        
        Args:
            number (str): Phone number to lookup
        """
        if not json_output:
            print(f"[*] Target: {number}")
            print(f"[*] Initiating trace...\n")
        
        is_valid, parsed, error = self.validate_phone_number(number)
        
        if not is_valid:
            if not json_output:
                print(f"[!] Error: {error}")
                print("[!] Trace failed\n")
            return None
        
        location = geocoder.description_for_number(parsed, "en")
        if not location:
            location = "Unknown"
        
        carrier_name = carrier.name_for_number(parsed, "en")
        if not carrier_name:
            carrier_name = "Unknown"
        
        timezones = timezone.time_zones_for_number(parsed)
        if not timezones:
            timezones = ["Unknown"]
        
        country_code = f"+{parsed.country_code}"
        number_type = self.get_number_type(parsed)
        formats = self.format_number_variants(parsed)
        regional_info = self.get_regional_info(parsed)
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "input": number,
            "valid": True,
            "country_code": country_code,
            "region_code": regional_info["region_code"],
            "country_name": regional_info["country_name"],
            "location": location,
            "carrier": carrier_name,
            "type": number_type,
            "timezones": timezones,
            "formats": formats
        }
        
        if show_variants:
            results["common_variants"] = self.generate_number_variants(parsed)
        
        self.results_cache.append(results)
        
        if json_output:
            return results
        
        print("[+] Results:")
        print(f"    Country Code: {country_code}")
        print(f"    Country: {regional_info['country_name']}")
        print(f"    Region: {regional_info['region_code']}")
        print(f"    Location: {location}")
        print(f"    Carrier: {carrier_name}")
        print(f"    Type: {number_type}")
        print(f"    Timezone(s): {', '.join(timezones)}")
        print(f"    Valid: Yes")
        
        if verbose:
            print(f"\n[*] Format Variants:")
            for fmt_name, fmt_value in formats.items():
                print(f"    {fmt_name}: {fmt_value}")
        
        if show_variants:
            print(f"\n[*] Common Format Variants:")
            for variant in self.generate_number_variants(parsed):
                print(f"    • {variant}")
        
        print("\n[+] Trace Complete\n")
        return results

    def batch_lookup(self, filename: str, output_file: Optional[str] = None, 
                    output_format: str = 'json', show_progress: bool = True):
        """Process multiple phone numbers from a file"""
        print(f"\n[*] Batch mode: Processing {filename}\n")
        
        try:
            with open(filename, 'r') as f:
                numbers = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            results = []
            successful = 0
            failed = 0
            
            for i, number in enumerate(numbers, 1):
                if show_progress:
                    print(f"[{i}/{len(numbers)}] Processing: {number}")
                
                result = self.lookup_phone_number(number, json_output=True)
                if result:
                    results.append(result)
                    successful += 1
                    if show_progress:
                        print("✓ Success\n")
                else:
                    failed += 1
                    if show_progress:
                        print("✗ Failed\n")
            
            if output_file and results:
                self.export_results(results, output_file, output_format)
            
            print(f"[+] Batch Complete")
            print(f"    Total: {len(numbers)} | Success: {successful} | Failed: {failed}\n")
            
        except FileNotFoundError:
            print(f"[!] Error: File '{filename}' not found\n")
        except Exception as e:
            print(f"[!] Error: {str(e)}\n")

    def export_results(self, results: List[Dict], output_file: str, format_type: str = 'json'):
        """
        Export results in various formats
        
        Args:
            results: List of result dictionaries
            output_file: Output filename
            format_type: Export format (json, csv, txt)
        """
        try:
            if format_type == 'json':
                with open(output_file, 'w') as f:
                    json.dump(results, f, indent=2)
                print(f"[+] JSON results saved to: {output_file}\n")
                
            elif format_type == 'csv':
                if not results:
                    return
                
                csv_data = []
                for r in results:
                    flat = {
                        'timestamp': r['timestamp'],
                        'input': r['input'],
                        'valid': r['valid'],
                        'country_code': r['country_code'],
                        'country_name': r.get('country_name', 'N/A'),
                        'region_code': r.get('region_code', 'N/A'),
                        'location': r['location'],
                        'carrier': r['carrier'],
                        'type': r['type'],
                        'timezones': ', '.join(r['timezones']),
                        'e164': r['formats']['E164']
                    }
                    csv_data.append(flat)
                
                with open(output_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
                    writer.writeheader()
                    writer.writerows(csv_data)
                print(f"[+] CSV results saved to: {output_file}\n")
                
            elif format_type == 'txt':
                with open(output_file, 'w') as f:
                    f.write("PhoneBookLOCA v1.0 - OSINT Results\n")
                    f.write("=" * 50 + "\n\n")
                    for r in results:
                        f.write(f"Target: {r['input']}\n")
                        f.write(f"Timestamp: {r['timestamp']}\n")
                        f.write(f"Country: {r.get('country_name', 'N/A')} ({r['country_code']})\n")
                        f.write(f"Location: {r['location']}\n")
                        f.write(f"Carrier: {r['carrier']}\n")
                        f.write(f"Type: {r['type']}\n")
                        f.write(f"Timezones: {', '.join(r['timezones'])}\n")
                        f.write("-" * 50 + "\n\n")
                print(f"[+] TXT results saved to: {output_file}\n")
                
        except Exception as e:
            print(f"[!] Export error: {str(e)}\n")

    def scan_text_file(self, filename: str, output_file: Optional[str] = None):
        """Scan a text file and extract all phone numbers"""
        print(f"\n[*] Scanning file for phone numbers: {filename}\n")
        
        try:
            with open(filename, 'r') as f:
                text = f.read()
            
            numbers = self.extract_numbers_from_text(text)
            
            if not numbers:
                print(f"[!] No phone numbers found in file\n")
                return
            
            print(f"[+] Found {len(numbers)} phone number(s):")
            for num in numbers:
                print(f"    • {num}")
            
            if output_file:
                with open(output_file, 'w') as f:
                    for num in numbers:
                        f.write(f"{num}\n")
                print(f"\n[+] Extracted numbers saved to: {output_file}\n")
            else:
                print()
            
        except FileNotFoundError:
            print(f"[!] Error: File '{filename}' not found\n")
        except Exception as e:
            print(f"[!] Error: {str(e)}\n")

    def interactive_mode(self, verbose: bool = False):
        """Run the tool in interactive mode"""
        self.print_banner()
        print("Enter phone numbers to lookup (with country code, e.g., +1234567890)")
        print("Type 'quit' or 'exit' to stop, 'help' for commands\n")
        
        while True:
            try:
                user_input = input("Enter phone number: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\n[*] Exiting PhoneBookLOCA. Goodbye!\n")
                    break
                
                if user_input.lower() == 'help':
                    print("\nAvailable Commands:")
                    print("  • Enter a phone number (e.g., +14155552671)")
                    print("  • 'stats' - Show session statistics")
                    print("  • 'export' - Export session results")
                    print("  • 'clear' - Clear session cache")
                    print("  • 'help' - Show this message")
                    print("  • 'quit' or 'exit' - Exit the tool\n")
                    continue
                
                if user_input.lower() == 'stats':
                    self.show_statistics()
                    continue
                
                if user_input.lower() == 'export':
                    filename = input("Export filename (default: results.json): ").strip() or "results.json"
                    if self.results_cache:
                        self.export_results(self.results_cache, filename, 'json')
                    else:
                        print("[!] No results to export\n")
                    continue
                
                if user_input.lower() == 'clear':
                    self.results_cache.clear()
                    print("[+] Session cache cleared\n")
                    continue
                
                if not user_input:
                    print("[!] Please enter a phone number\n")
                    continue
                
                print()
                self.lookup_phone_number(user_input, verbose=verbose)
                
            except KeyboardInterrupt:
                print("\n\n[*] Interrupted. Exiting...\n")
                break
            except Exception as e:
                print(f"\n[!] Unexpected error: {str(e)}\n")

    def show_statistics(self):
        """Display session statistics"""
        if not self.results_cache:
            print("\n[!] No lookups performed this session\n")
            return
        
        print("\n[*] Session Statistics:")
        print(f"    Total Lookups: {len(self.results_cache)}")
        
        countries = {}
        carriers = {}
        types = {}
        
        for result in self.results_cache:
            country = result.get('country_name', 'Unknown')
            countries[country] = countries.get(country, 0) + 1
            
            carrier = result.get('carrier', 'Unknown')
            carriers[carrier] = carriers.get(carrier, 0) + 1
            
            num_type = result.get('type', 'Unknown')
            types[num_type] = types.get(num_type, 0) + 1
        
        print(f"\n    Top Countries:")
        for country, count in sorted(countries.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"      • {country}: {count}")
        
        print(f"\n    Top Carriers:")
        for carrier, count in sorted(carriers.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"      • {carrier}: {count}")
        
        print(f"\n    Number Types:")
        for num_type, count in types.items():
            print(f"      • {num_type}: {count}")
        
        print()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='PhoneBookLOCA v1.0 - Phone Number Location Lookup Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s +14155552671                      # Single lookup
  %(prog)s +442071838750 -v                  # Verbose mode
  %(prog)s +14155552671 --variants           # Show format variants
  %(prog)s -b numbers.txt                    # Batch processing
  %(prog)s -b numbers.txt -o results.csv -f csv  # Batch with CSV export
  %(prog)s --scan document.txt               # Extract numbers from file
  %(prog)s --scan data.txt -o found.txt      # Extract and save
  %(prog)s                                   # Interactive mode
        """
    )
    
    parser.add_argument('number', nargs='?', help='Phone number to lookup')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed information')
    parser.add_argument('-j', '--json', action='store_true', help='Output in JSON format')
    parser.add_argument('-b', '--batch', metavar='FILE', help='Process numbers from file (one per line)')
    parser.add_argument('-o', '--output', metavar='FILE', help='Save results to file')
    parser.add_argument('-f', '--format', choices=['json', 'csv', 'txt'], default='json',
                       help='Output format (default: json)')
    parser.add_argument('--variants', action='store_true', help='Show common number format variants')
    parser.add_argument('--scan', metavar='FILE', help='Scan text file and extract phone numbers')
    parser.add_argument('--quiet', action='store_true', help='Suppress progress output in batch mode')
    
    args = parser.parse_args()
    
    intel = PhoneIntel()
    
    if args.scan:
        intel.scan_text_file(args.scan, args.output)
        return
    
    if args.batch:
        intel.batch_lookup(args.batch, args.output, args.format, not args.quiet)
        return
    
    if args.number:
        intel.print_banner()
        result = intel.lookup_phone_number(args.number, verbose=args.verbose, 
                                          json_output=args.json, show_variants=args.variants)
        if args.json and result:
            print(json.dumps(result, indent=2))
        return
    
    intel.interactive_mode(verbose=args.verbose)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Exiting...\n")
        sys.exit(0)
