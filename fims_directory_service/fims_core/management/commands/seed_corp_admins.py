from django.core.management.base import BaseCommand
from django.db import transaction
from fims_core.models import CorpAdmin, Company


class Command(BaseCommand):
    help = "Seed Corporate Admin users."

    # ------------------------------------------------------------------
    # Corporate Admin Seed Data:
    # (first_name, last_name, uid, comp_code)
    # ------------------------------------------------------------------
    SEED_DATA = [
        ("Ursula", "Vance", "uvanc387", "HSF1"),
        ("Victor", "Stone", "vston812", "FFC2"),
        ("Wendy", "Ross", "wross504", "HSF3"),
        ("Xavier", "Price", "xpric931", "FFC4"),
        ("Yara", "Nguyen", "ynguy675", "HSF5"),
        ("Zack", "Fisher", "zfish228", "FFC1"),
        ("Anna", "Brooks", "abroo149", "HSF1"),
        ("Ben", "Reed", "breed760", "FFC2"),
        ("Cathy", "Morgan", "cmorg336", "HSF3"),
        ("Dan", "Hayes", "dhaye088", "FFC4"),
        ("Elsa", "Jenkins", "ejenk455", "HSF5"),
        ("Fred", "Cook", "fcook117", "FFC1"),
        ("Gina", "Patel", "gpate602", "HSF1"),
        ("Henry", "Wood", "hwood874", "FFC2"),
        ("Ivy", "Ramirez", "irami059", "HSF3"),
        ("Jack", "Hughes", "jhugh247", "FFC4"),
        ("Kara", "Coleman", "kcole793", "HSF5"),
        ("Leo", "Perry", "lperr365", "FFC1"),
        ("Mia", "Bell", "mbell101", "HSF1"),
        ("Noel", "Foster", "nfost553", "FFC2"),
        ("Owen", "Ortiz", "oorti918", "HSF3"),
        ("Pia", "Murphy", "pmurp642", "FFC4"),
        ("Quinn", "Soto", "qsoto005", "HSF5"),
        ("Rick", "Gibson", "rgibt277", "FFC1"),
        ("Sara", "Ellis", "selli496", "HSF1"),
        ("Tom", "Marsh", "tmars850", "FFC2"),
        ("Uma", "Chung", "uchun133", "HSF3"),
        ("Vince", "Kelly", "vkel482", "FFC4"),
        ("Willa", "Fox", "wfox410", "HSF5"),
    ]

    def handle(self, *args, **kwargs):
        self.stdout.write("\n🔄 Seeding Corporate Admins...\n")

        # Build comp_code → company_id mapping
        company_map = {c.comp_code: c.id for c in Company.objects.all()}

        missing = [
            entry[3] for entry in self.SEED_DATA
            if entry[3] not in company_map
        ]
        if missing:
            self.stdout.write(self.style.ERROR(f"❌ Missing companies for comp_codes: {missing}"))
            return

        created_count = 0
        skipped_count = 0

        for first, last, uid, comp_code in self.SEED_DATA:

            company_id = company_map[comp_code]

            # Idempotent check to avoid duplicates
            if CorpAdmin.objects.filter(
                first_name=first,
                last_name=last,
                company_id=company_id
            ).exists():
                self.stdout.write(f"⏭ Skipped (exists): {first} {last} ({comp_code})")
                skipped_count += 1
                continue

            with transaction.atomic():
                CorpAdmin.objects.create(
                    first_name=first,
                    last_name=last,
                    email=None,              # Email intentionally EMPTY
                    phone_number=None,       # Optional
                    company_id=company_id,
                    status="ENABLED",
                    created_by="system_admin",
                    last_updated_by="system_admin",
                )

            self.stdout.write(self.style.SUCCESS(
                f"✔ Inserted: {first} {last} ({comp_code})"
            ))
            created_count += 1

        self.stdout.write("\n🎉 Corporate Admin Seeding Complete!")
        self.stdout.write(self.style.SUCCESS(f"   ✔ Created: {created_count}"))
        self.stdout.write(self.style.WARNING(f"   ⏭ Skipped: {skipped_count}\n"))
