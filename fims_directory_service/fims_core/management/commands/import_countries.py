import json
from django.core.management.base import BaseCommand
from fims_core.models import Continent, Country


# Mapping continent code → continent_id (from your DB)
CONTINENT_MAP = {
    "AF": 2,  # Africa
    "AS": 3,  # Asia
    "AU": 4,  # Australia
    "EU": 5,  # Europe
    "NA": 1,  # North America
    "SA": 6,  # South America
    "AN": 7,  # Antarctica
}


# List of all countries with ISO2 codes + assigned CONTINENT_CODE
COUNTRIES = [
    {"name": "Afghanistan", "code": "AF", "continent": "AS"},
    {"name": "Albania", "code": "AL", "continent": "EU"},
    {"name": "Algeria", "code": "DZ", "continent": "AF"},
    {"name": "American Samoa", "code": "AS", "continent": "AU"},
    {"name": "Andorra", "code": "AD", "continent": "EU"},
    {"name": "Angola", "code": "AO", "continent": "AF"},
    {"name": "Anguilla", "code": "AI", "continent": "NA"},
    {"name": "Antarctica", "code": "AQ", "continent": "AN"},
    {"name": "Antigua and Barbuda", "code": "AG", "continent": "NA"},
    {"name": "Argentina", "code": "AR", "continent": "SA"},
    {"name": "Armenia", "code": "AM", "continent": "AS"},
    {"name": "Aruba", "code": "AW", "continent": "NA"},
    {"name": "Australia", "code": "AU", "continent": "AU"},
    {"name": "Austria", "code": "AT", "continent": "EU"},
    {"name": "Azerbaijan", "code": "AZ", "continent": "AS"},
    {"name": "Bahamas", "code": "BS", "continent": "NA"},
    {"name": "Bahrain", "code": "BH", "continent": "AS"},
    {"name": "Bangladesh", "code": "BD", "continent": "AS"},
    {"name": "Barbados", "code": "BB", "continent": "NA"},
    {"name": "Belarus", "code": "BY", "continent": "EU"},
    {"name": "Belgium", "code": "BE", "continent": "EU"},
    {"name": "Belize", "code": "BZ", "continent": "NA"},
    {"name": "Benin", "code": "BJ", "continent": "AF"},
    {"name": "Bermuda", "code": "BM", "continent": "NA"},
    {"name": "Bhutan", "code": "BT", "continent": "AS"},
    {"name": "Bolivia", "code": "BO", "continent": "SA"},
    {"name": "Bosnia and Herzegovina", "code": "BA", "continent": "EU"},
    {"name": "Botswana", "code": "BW", "continent": "AF"},
    {"name": "Brazil", "code": "BR", "continent": "SA"},
    {"name": "Brunei Darussalam", "code": "BN", "continent": "AS"},
    {"name": "Bulgaria", "code": "BG", "continent": "EU"},
    {"name": "Burkina Faso", "code": "BF", "continent": "AF"},
    {"name": "Burundi", "code": "BI", "continent": "AF"},
    {"name": "Cambodia", "code": "KH", "continent": "AS"},
    {"name": "Cameroon", "code": "CM", "continent": "AF"},
    {"name": "Canada", "code": "CA", "continent": "NA"},
    {"name": "Cape Verde", "code": "CV", "continent": "AF"},
    {"name": "Central African Republic", "code": "CF", "continent": "AF"},
    {"name": "Chad", "code": "TD", "continent": "AF"},
    {"name": "Chile", "code": "CL", "continent": "SA"},
    {"name": "China", "code": "CN", "continent": "AS"},
    {"name": "Colombia", "code": "CO", "continent": "SA"},
    {"name": "Comoros", "code": "KM", "continent": "AF"},
    {"name": "Congo", "code": "CG", "continent": "AF"},
    {"name": "Costa Rica", "code": "CR", "continent": "NA"},
    {"name": "Croatia", "code": "HR", "continent": "EU"},
    {"name": "Cuba", "code": "CU", "continent": "NA"},
    {"name": "Cyprus", "code": "CY", "continent": "EU"},
    {"name": "Czech Republic", "code": "CZ", "continent": "EU"},
    {"name": "Denmark", "code": "DK", "continent": "EU"},
    {"name": "Djibouti", "code": "DJ", "continent": "AF"},
    {"name": "Dominican Republic", "code": "DO", "continent": "NA"},
    {"name": "Ecuador", "code": "EC", "continent": "SA"},
    {"name": "Egypt", "code": "EG", "continent": "AF"},
    {"name": "El Salvador", "code": "SV", "continent": "NA"},
    {"name": "Estonia", "code": "EE", "continent": "EU"},
    {"name": "Ethiopia", "code": "ET", "continent": "AF"},
    {"name": "Fiji", "code": "FJ", "continent": "AU"},
    {"name": "Finland", "code": "FI", "continent": "EU"},
    {"name": "France", "code": "FR", "continent": "EU"},
    {"name": "Gabon", "code": "GA", "continent": "AF"},
    {"name": "Gambia", "code": "GM", "continent": "AF"},
    {"name": "Georgia", "code": "GE", "continent": "AS"},
    {"name": "Germany", "code": "DE", "continent": "EU"},
    {"name": "Ghana", "code": "GH", "continent": "AF"},
    {"name": "Greece", "code": "GR", "continent": "EU"},
    {"name": "Grenada", "code": "GD", "continent": "NA"},
    {"name": "Guatemala", "code": "GT", "continent": "NA"},
    {"name": "Guinea", "code": "GN", "continent": "AF"},
    {"name": "Guyana", "code": "GY", "continent": "SA"},
    {"name": "Haiti", "code": "HT", "continent": "NA"},
    {"name": "Honduras", "code": "HN", "continent": "NA"},
    {"name": "Hong Kong", "code": "HK", "continent": "AS"},
    {"name": "Hungary", "code": "HU", "continent": "EU"},
    {"name": "Iceland", "code": "IS", "continent": "EU"},
    {"name": "India", "code": "IN", "continent": "AS"},
    {"name": "Indonesia", "code": "ID", "continent": "AS"},
    {"name": "Iran", "code": "IR", "continent": "AS"},
    {"name": "Iraq", "code": "IQ", "continent": "AS"},
    {"name": "Ireland", "code": "IE", "continent": "EU"},
    {"name": "Israel", "code": "IL", "continent": "AS"},
    {"name": "Italy", "code": "IT", "continent": "EU"},
    {"name": "Jamaica", "code": "JM", "continent": "NA"},
    {"name": "Japan", "code": "JP", "continent": "AS"},
    {"name": "Jordan", "code": "JO", "continent": "AS"},
    {"name": "Kenya", "code": "KE", "continent": "AF"},
    {"name": "Korea, Republic of", "code": "KR", "continent": "AS"},
    {"name": "Kuwait", "code": "KW", "continent": "AS"},
    {"name": "Kyrgyzstan", "code": "KG", "continent": "AS"},
    {"name": "Latvia", "code": "LV", "continent": "EU"},
    {"name": "Lebanon", "code": "LB", "continent": "AS"},
    {"name": "Liberia", "code": "LR", "continent": "AF"},
    {"name": "Libya", "code": "LY", "continent": "AF"},
    {"name": "Lithuania", "code": "LT", "continent": "EU"},
    {"name": "Luxembourg", "code": "LU", "continent": "EU"},
    {"name": "Macao", "code": "MO", "continent": "AS"},
    {"name": "Madagascar", "code": "MG", "continent": "AF"},
    {"name": "Malawi", "code": "MW", "continent": "AF"},
    {"name": "Malaysia", "code": "MY", "continent": "AS"},
    {"name": "Maldives", "code": "MV", "continent": "AS"},
    {"name": "Mali", "code": "ML", "continent": "AF"},
    {"name": "Malta", "code": "MT", "continent": "EU"},
    {"name": "Mauritania", "code": "MR", "continent": "AF"},
    {"name": "Mauritius", "code": "MU", "continent": "AF"},
    {"name": "Mexico", "code": "MX", "continent": "NA"},
    {"name": "Moldova", "code": "MD", "continent": "EU"},
    {"name": "Monaco", "code": "MC", "continent": "EU"},
    {"name": "Mongolia", "code": "MN", "continent": "AS"},
    {"name": "Montenegro", "code": "ME", "continent": "EU"},
    {"name": "Morocco", "code": "MA", "continent": "AF"},
    {"name": "Mozambique", "code": "MZ", "continent": "AF"},
    {"name": "Myanmar", "code": "MM", "continent": "AS"},
    {"name": "Namibia", "code": "NA", "continent": "AF"},
    {"name": "Nepal", "code": "NP", "continent": "AS"},
    {"name": "Netherlands", "code": "NL", "continent": "EU"},
    {"name": "New Zealand", "code": "NZ", "continent": "AU"},
    {"name": "Nicaragua", "code": "NI", "continent": "NA"},
    {"name": "Niger", "code": "NE", "continent": "AF"},
    {"name": "Nigeria", "code": "NG", "continent": "AF"},
    {"name": "Norway", "code": "NO", "continent": "EU"},
    {"name": "Oman", "code": "OM", "continent": "AS"},
    {"name": "Pakistan", "code": "PK", "continent": "AS"},
    {"name": "Palau", "code": "PW", "continent": "AU"},
    {"name": "Panama", "code": "PA", "continent": "NA"},
    {"name": "Papua New Guinea", "code": "PG", "continent": "AU"},
    {"name": "Paraguay", "code": "PY", "continent": "SA"},
    {"name": "Peru", "code": "PE", "continent": "SA"},
    {"name": "Philippines", "code": "PH", "continent": "AS"},
    {"name": "Poland", "code": "PL", "continent": "EU"},
    {"name": "Portugal", "code": "PT", "continent": "EU"},
    {"name": "Qatar", "code": "QA", "continent": "AS"},
    {"name": "Romania", "code": "RO", "continent": "EU"},
    {"name": "Russian Federation", "code": "RU", "continent": "EU"},
    {"name": "Rwanda", "code": "RW", "continent": "AF"},
    {"name": "Saudi Arabia", "code": "SA", "continent": "AS"},
    {"name": "Senegal", "code": "SN", "continent": "AF"},
    {"name": "Serbia", "code": "RS", "continent": "EU"},
    {"name": "Seychelles", "code": "SC", "continent": "AF"},
    {"name": "Sierra Leone", "code": "SL", "continent": "AF"},
    {"name": "Singapore", "code": "SG", "continent": "AS"},
    {"name": "Slovakia", "code": "SK", "continent": "EU"},
    {"name": "Slovenia", "code": "SI", "continent": "EU"},
    {"name": "Somalia", "code": "SO", "continent": "AF"},
    {"name": "South Africa", "code": "ZA", "continent": "AF"},
    {"name": "South Sudan", "code": "SS", "continent": "AF"},
    {"name": "Spain", "code": "ES", "continent": "EU"},
    {"name": "Sri Lanka", "code": "LK", "continent": "AS"},
    {"name": "Sudan", "code": "SD", "continent": "AF"},
    {"name": "Suriname", "code": "SR", "continent": "SA"},
    {"name": "Sweden", "code": "SE", "continent": "EU"},
    {"name": "Switzerland", "code": "CH", "continent": "EU"},
    {"name": "Syrian Arab Republic", "code": "SY", "continent": "AS"},
    {"name": "Taiwan", "code": "TW", "continent": "AS"},
    {"name": "Tajikistan", "code": "TJ", "continent": "AS"},
    {"name": "Tanzania", "code": "TZ", "continent": "AF"},
    {"name": "Thailand", "code": "TH", "continent": "AS"},
    {"name": "Timor-Leste", "code": "TL", "continent": "AS"},
    {"name": "Togo", "code": "TG", "continent": "AF"},
    {"name": "Tonga", "code": "TO", "continent": "AU"},
    {"name": "Trinidad and Tobago", "code": "TT", "continent": "NA"},
    {"name": "Tunisia", "code": "TN", "continent": "AF"},
    {"name": "Turkey", "code": "TR", "continent": "AS"},
    {"name": "Turkmenistan", "code": "TM", "continent": "AS"},
    {"name": "Uganda", "code": "UG", "continent": "AF"},
    {"name": "Ukraine", "code": "UA", "continent": "EU"},
    {"name": "United Arab Emirates", "code": "AE", "continent": "AS"},
    {"name": "United Kingdom", "code": "GB", "continent": "EU"},
    {"name": "United States", "code": "US", "continent": "NA"},
    {"name": "Uruguay", "code": "UY", "continent": "SA"},
    {"name": "Uzbekistan", "code": "UZ", "continent": "AS"},
    {"name": "Vanuatu", "code": "VU", "continent": "AU"},
    {"name": "Venezuela", "code": "VE", "continent": "SA"},
    {"name": "Viet Nam", "code": "VN", "continent": "AS"},
    {"name": "Yemen", "code": "YE", "continent": "AS"},
    {"name": "Zambia", "code": "ZM", "continent": "AF"},
    {"name": "Zimbabwe", "code": "ZW", "continent": "AF"},
]


class Command(BaseCommand):
    help = "Imports all countries and maps them to the correct continent."

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("Importing countries..."))

        created = 0
        updated = 0

        for entry in COUNTRIES:
            continent_code = entry["continent"]
            continent_id = CONTINENT_MAP.get(continent_code)

            if not continent_id:
                self.stdout.write(self.style.WARNING(
                    f"Skipping {entry['name']} — invalid continent {continent_code}"
                ))
                continue

            country, is_created = Country.objects.update_or_create(
                code=entry["code"],
                defaults={
                    "name": entry["name"],
                    "continent_id": continent_id
                }
            )

            if is_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Done! Countries created: {created}, updated: {updated}"
        ))
