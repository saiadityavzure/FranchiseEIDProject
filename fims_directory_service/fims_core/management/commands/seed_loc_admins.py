from django.core.management.base import BaseCommand
from fims_core.models import LocAdmin, Company, Location
from django.utils import timezone

LOCATION_ADMIN_DATA = [
    # FirstName, LastName, UID, LocCode, CompCode, CreatedBy
    ("Adam", "King", "aking101", "LAX01", "HSF1"),
    ("Bella", "Lopez", "blop419", "MIA01", "FFC2"),
    ("Caleb", "Martin", "cmart207", "ORD01", "HSF3"),
    ("Daisy", "Nash", "dnas093", "DFW01", "FFC4"),
    ("Evan", "Owens", "eowe255", "JFK01", "HSF5"),
    ("Faith", "Perez", "fper271", "LAX02", "HSF1"),
    ("Gavin", "Quinn", "gqui316", "MIA02", "FFC2"),
    ("Holly", "Reed", "hree848", "ORD02", "HSF3"),
    ("Ian", "Shaw", "ishaw562", "DFW02", "FFC4"),
    ("Jada", "Todd", "jtod114", "JFK02", "HSF5"),
    ("Kyle", "Vega", "kveg777", "LAX03", "HSF1"),
    ("Lily", "West", "lwes040", "MIA03", "FFC2"),
    ("Milo", "Xing", "mxi689", "ORD03", "HSF3"),
    ("Nora", "York", "nyor302", "DFW03", "FFC4"),
    ("Omar", "Zane", "ozan919", "JFK03", "HSF5"),
    ("Piper", "Allen", "pall503", "LAX04", "HSF1"),
    ("Quinn", "Boyd", "qboy445", "MIA04", "FFC2"),
    ("Ryan", "Carr", "rcar291", "ORD04", "HSF3"),
    ("Sara", "Dixon", "sdix806", "DFW04", "FFC4"),
    ("Trent", "Ellis", "telli628", "JFK04", "HSF5"),
    ("Uli", "Flynn", "ufly670", "LAX05", "HSF1"),
    ("Vera", "Grant", "vgra744", "MIA05", "FFC2"),
    ("Will", "Hale", "whal123", "ORD05", "HSF3"),
    ("Yael", "Ivey", "yive598", "DFW05", "FFC4"),
    ("Zoe", "Jones", "zjon330", "JFK05", "HSF5"),
    ("Alex", "Kane", "akan201", "LAX06", "HSF1"),
    ("Beth", "Lamb", "blam865", "MIA06", "FFC2"),
    ("Cody", "Mays", "cmay432", "ORD06", "HSF3"),
    ("Dawn", "Neal", "dnea178", "DFW06", "FFC4"),
    ("Eric", "Orr", "eorr641", "JFK06", "HSF5"),
    ("Finn", "Pace", "fpac909", "LAX07", "HSF1"),
    ("Gigi", "Rios", "grio717", "MIA07", "FFC2"),
    ("Hank", "Sears", "hsea284", "ORD07", "HSF3"),
    ("Ira", "Tate", "itat535", "DFW07", "FFC4"),
    ("Jeff", "Upton", "jup600", "JFK07", "HSF5"),
    ("Kira", "Voss", "kvos394", "LAX08", "HSF1"),
    ("Liam", "Ward", "lwar051", "MIA08", "FFC2"),
    ("Mia", "Xie", "mxi613", "ORD08", "HSF3"),
    ("Nico", "Yates", "nyat987", "DFW08", "FFC4"),
    ("Opal", "Zimm", "ozim346", "JFK08", "HSF5"),
    ("Pete", "Abel", "pabe829", "LAX09", "HSF1"),
    ("Quin", "Best", "qbes110", "MIA09", "FFC2"),
    ("Rose", "Cain", "rcai763", "ORD09", "HSF3"),
    ("Sam", "Drew", "sdr142", "DFW09", "FFC4"),
    ("Tia", "Ernst", "tern003", "JFK09", "HSF5"),
    ("Uma", "Felt", "ufel785", "LAX10", "HSF1"),
    ("Vic", "Gray", "vgra512", "MIA10", "FFC2"),
    ("Wynn", "Hill", "whil947", "ORD10", "HSF3"),
    ("Yuri", "Inge", "yin888", "DFW10", "FFC4"),
    ("Zane", "Jack", "zjac354", "JFK10", "HSF5"),
    ("Alvin", "Kerr", "aker199", "LAX11", "HSF1"),
    ("Becca", "Lane", "bla331", "MIA11", "FFC2"),
    ("Cole", "Mann", "cman572", "ORD11", "HSF3"),
    ("Demi", "Neff", "dn837", "DFW11", "FFC4"),
    ("Emil", "Otto", "eott666", "JFK11", "HSF5"),
    ("Faye", "Post", "fpos176", "LAX12", "HSF1"),
    ("Glen", "Quay", "gqua408", "MIA12", "FFC2"),
    ("Hope", "Ritz", "hrit952", "ORD12", "HSF3"),
    ("Ivan", "Sanz", "isan161", "DFW12", "FFC4"),
    ("June", "Troy", "jtro705", "JFK12", "HSF5"),
    ("Ken", "Vail", "kvai234", "LAX13", "HSF1"),
    ("Lana", "Wade", "lwa890", "MIA13", "FFC2"),
    ("Mark", "York", "myor182", "ORD13", "HSF3"),
    ("Nell", "Zink", "nzink500", "DFW13", "FFC4"),
    ("Otto", "Abb", "oabb713", "JFK13", "HSF5"),
]


class Command(BaseCommand):
    help = "Seeds the Location Admins table"

    def handle(self, *args, **kwargs):
        self.stdout.write("🔄 Seeding Location Admins...\n")

        created_count = 0
        skipped_count = 0

        for first, last, uid, loc_code, comp_code in LOCATION_ADMIN_DATA:
            try:
                company = Company.objects.get(comp_code=comp_code)
            except Company.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"❌ Missing Company: {comp_code}"))
                continue

            try:
                location = Location.objects.get(code=loc_code, company=company)
            except Location.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"❌ Missing Location: {loc_code} ({comp_code})"))
                continue

            # Check if exists
            if LocAdmin.objects.filter(first_name=first, last_name=last, company=company, location=location).exists():
                skipped_count += 1
                self.stdout.write(f"⏭ Skipped (exists): {first} {last} ({loc_code})")
                continue

            # Create
            LocAdmin.objects.create(
                first_name=first,
                last_name=last,
                email=f"{uid}@example.com",
                phone_number=None,
                company=company,
                location=location,
                created_by="system_admin",
                last_updated_by="system_admin",
            )

            created_count += 1
            self.stdout.write(self.style.SUCCESS(f"✔ Inserted: {first} {last} ({loc_code})"))

        self.stdout.write("\n🎉 Location Admin Seeding Complete!")
        self.stdout.write(f"   ✔ Created: {created_count}")
        self.stdout.write(f"   ⏭ Skipped: {skipped_count}")
