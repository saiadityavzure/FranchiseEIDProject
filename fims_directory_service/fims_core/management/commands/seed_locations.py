from django.core.management.base import BaseCommand
from fims_core.models.location import Location
from fims_core.models.company import Company


class Command(BaseCommand):
    help = "Seeds sample locations for all companies."

    SAMPLE_LOCATIONS = [
        # HSF1 - StarLight Resorts
        ("LAX01", "Pacific Grand Hotel", "HSF1"),
        ("LAX02", "Pacific Grand Hotel", "HSF1"),
        ("LAX03", "Pacific Grand Hotel", "HSF1"),
        ("LAX04", "Pacific Grand Hotel", "HSF1"),
        ("LAX05", "Pacific Grand Hotel", "HSF1"),
        ("LAX06", "Pacific Grand Hotel", "HSF1"),
        ("LAX07", "Pacific Grand Hotel", "HSF1"),
        ("LAX08", "Pacific Grand Hotel", "HSF1"),
        ("LAX09", "Pacific Grand Hotel", "HSF1"),
        ("LAX10", "Pacific Grand Hotel", "HSF1"),
        ("LAX11", "Pacific Grand Hotel", "HSF1"),
        ("LAX12", "Pacific Grand Hotel", "HSF1"),
        ("LAX13", "Pacific Grand Hotel", "HSF1"),

        # FFC2 - BurgerBlitz
        ("MIA01", "The South Beach Inn", "FFC2"),
        ("MIA02", "The South Beach Inn", "FFC2"),
        ("MIA03", "The South Beach Inn", "FFC2"),
        ("MIA04", "The South Beach Inn", "FFC2"),
        ("MIA05", "The South Beach Inn", "FFC2"),
        ("MIA06", "The South Beach Inn", "FFC2"),
        ("MIA07", "The South Beach Inn", "FFC2"),
        ("MIA08", "The South Beach Inn", "FFC2"),
        ("MIA09", "The South Beach Inn", "FFC2"),
        ("MIA10", "The South Beach Inn", "FFC2"),
        ("MIA11", "The South Beach Inn", "FFC2"),
        ("MIA12", "The South Beach Inn", "FFC2"),
        ("MIA13", "The South Beach Inn", "FFC2"),

        # HSF3 - The Grand Hotel
        ("ORD01", "Midwest Executive Suites", "HSF3"),
        ("ORD02", "Midwest Executive Suites", "HSF3"),
        ("ORD03", "Midwest Executive Suites", "HSF3"),
        ("ORD04", "Midwest Executive Suites", "HSF3"),
        ("ORD05", "Midwest Executive Suites", "HSF3"),
        ("ORD06", "Midwest Executive Suites", "HSF3"),
        ("ORD07", "Midwest Executive Suites", "HSF3"),
        ("ORD08", "Midwest Executive Suites", "HSF3"),
        ("ORD09", "Midwest Executive Suites", "HSF3"),
        ("ORD10", "Midwest Executive Suites", "HSF3"),
        ("ORD11", "Midwest Executive Suites", "HSF3"),
        ("ORD12", "Midwest Executive Suites", "HSF3"),
        ("ORD13", "Midwest Executive Suites", "HSF3"),

        # FFC4 - Pizza Planet
        ("DFW01", "Lone Star Conference Center", "FFC4"),
        ("DFW02", "Lone Star Conference Center", "FFC4"),
        ("DFW03", "Lone Star Conference Center", "FFC4"),
        ("DFW04", "Lone Star Conference Center", "FFC4"),
        ("DFW05", "Lone Star Conference Center", "FFC4"),
        ("DFW06", "Lone Star Conference Center", "FFC4"),
        ("DFW07", "Lone Star Conference Center", "FFC4"),
        ("DFW08", "Lone Star Conference Center", "FFC4"),
        ("DFW09", "Lone Star Conference Center", "FFC4"),
        ("DFW10", "Lone Star Conference Center", "FFC4"),
        ("DFW11", "Lone Star Conference Center", "FFC4"),
        ("DFW12", "Lone Star Conference Center", "FFC4"),
        ("DFW13", "Lone Star Conference Center", "FFC4"),

        # HSF5 - Coastal Suites
        ("JFK01", "New York Harbor View", "HSF5"),
        ("JFK02", "New York Harbor View", "HSF5"),
        ("JFK03", "New York Harbor View", "HSF5"),
        ("JFK04", "New York Harbor View", "HSF5"),
        ("JFK05", "New York Harbor View", "HSF5"),
        ("JFK06", "New York Harbor View", "HSF5"),
        ("JFK07", "New York Harbor View", "HSF5"),
        ("JFK08", "New York Harbor View", "HSF5"),
        ("JFK09", "New York Harbor View", "HSF5"),
        ("JFK10", "New York Harbor View", "HSF5"),
        ("JFK11", "New York Harbor View", "HSF5"),
        ("JFK12", "New York Harbor View", "HSF5"),
        ("JFK13", "New York Harbor View", "HSF5"),
    ]

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("🔄 Seeding locations...\n"))

        inserted = 0

        for code, name, comp_code in self.SAMPLE_LOCATIONS:

            # Get company by comp_code
            try:
                company = Company.objects.get(comp_code=comp_code)
            except Company.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"❌ Company with comp_code '{comp_code}' not found. Skipping {code}."
                ))
                continue

            # Skip if already exists
            if Location.objects.filter(code=code, company=company).exists():
                self.stdout.write(self.style.NOTICE(f"⏭ Skipped (exists): {code}"))
                continue

            Location.objects.create(
                code=code,
                name=name,
                company=company,
                status="ENABLED",
            )

            inserted += 1
            self.stdout.write(self.style.SUCCESS(f"✔ Inserted: {code}"))

        self.stdout.write(self.style.SUCCESS(
            f"\n🎉 Done. {inserted} locations inserted successfully."
        ))
