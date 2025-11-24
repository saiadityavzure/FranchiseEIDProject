from django.core.management.base import BaseCommand
from fims_core.models.company import Company
from fims_core.models.country import Country


class Command(BaseCommand):
    help = "Seeds initial sample companies into the database."

    SAMPLE_COMPANIES = [
        {
            "name": "StarLight Resorts",
            "address": "100 Hollywood Blvd",
            "city": "Los Angeles",
            "state": "CA",
            "comp_code": "HSF1",
            "country_code": "US",
        },
        {
            "name": "BurgerBlitz",
            "address": "450 Ocean Drive",
            "city": "Miami",
            "state": "FL",
            "comp_code": "FFC2",
            "country_code": "US",
        },
        {
            "name": "The Grand Hotel",
            "address": "224 Michigan Ave",
            "city": "Chicago",
            "state": "IL",
            "comp_code": "HSF3",
            "country_code": "US",
        },
        {
            "name": "Pizza Planet",
            "address": "880 Commerce St",
            "city": "Dallas",
            "state": "TX",
            "comp_code": "FFC4",
            "country_code": "US",
        },
    ]

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("🔄 Seeding companies...\n"))

        inserted_count = 0

        for company_data in self.SAMPLE_COMPANIES:
            comp_code = company_data["comp_code"]

            # Skip if already exists
            if Company.objects.filter(comp_code=comp_code).exists():
                self.stdout.write(self.style.NOTICE(f"⏭ Skipped (exists): {comp_code}"))
                continue

            # Find the related country by its code
            try:
                country = Country.objects.get(code=company_data["country_code"])
            except Country.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"❌ Country with code '{company_data['country_code']}' not found.")
                )
                continue

            Company.objects.create(
                name=company_data["name"],
                address=company_data["address"],
                city=company_data["city"],
                state=company_data["state"],
                comp_code=company_data["comp_code"],
                country=country,
                status="ENABLED",
            )

            inserted_count += 1
            self.stdout.write(self.style.SUCCESS(f"✔ Inserted: {company_data['name']}"))

        self.stdout.write(self.style.SUCCESS(f"\n🎉 Done. {inserted_count} companies inserted."))
