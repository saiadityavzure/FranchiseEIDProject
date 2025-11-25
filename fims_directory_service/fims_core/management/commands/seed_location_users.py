from django.core.management.base import BaseCommand
from fims_core.models import Company, Location, LocationUser


class Command(BaseCommand):
    help = "Seed example Location Users (5 users only)."

    def handle(self, *args, **kwargs):
        self.stdout.write("🔄 Seeding Location Users...")

        # Company + Location mapping
        try:
            company = Company.objects.get(comp_code="HSF1")
        except Company.DoesNotExist:
            self.stdout.write(self.style.ERROR("❌ Company HSF1 not found. Create it first."))
            return

        try:
            location = Location.objects.get(code="LAX01")
        except Location.DoesNotExist:
            self.stdout.write(self.style.ERROR("❌ Location LAX01 not found. Create it first."))
            return

        seed_users = [
            ("Julia",  "Ray",   "jray@example.com",   "555-1101"),
            ("Robert", "Lane",  "rlane002@example.com", "555-1102"),
            ("Emily",  "Chen",  "echen003@example.com", "555-1103"),
            ("Marcus", "Diaz",  "mdiaz004@example.com", "555-1104"),
            ("Tina",   "Holt",  "tholt005@example.com", "555-1105"),
        ]

        created = 0
        skipped = 0

        for first_name, last_name, email, phone in seed_users:
            # Check if this user already exists by email + location
            exists = LocationUser.objects.filter(
                first_name=first_name,
                last_name=last_name,
                company=company,
                location=location,
            ).first()

            if exists:
                skipped += 1
                self.stdout.write(f"⏭ Skipped (exists): {first_name} {last_name}")
                continue

            LocationUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone,
                company=company,
                location=location,
                created_by="system_admin",
                last_updated_by="system_admin",
            )

            created += 1
            self.stdout.write(f"✔ Inserted: {first_name} {last_name}")

        self.stdout.write("\n🎉 Location User Seeding Complete!")
        self.stdout.write(f"   ✔ Created: {created}")
        self.stdout.write(f"   ⏭ Skipped: {skipped}")
