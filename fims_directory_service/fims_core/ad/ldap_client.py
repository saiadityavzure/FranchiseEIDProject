from ldap3 import Server, Connection, ALL, NTLM, MODIFY_REPLACE

class ADClient:
    DOMAIN = "adtest.local"

    OU_MAP = {
        "corp_admin": "OU=CorpAdmins,OU=FIMS_Directory,DC=adtest,DC=local",
        "loc_admin": "OU=LocAdmins,OU=FIMS_Directory,DC=adtest,DC=local",
        "location_user": "OU=LocationUsers,OU=FIMS_Directory,DC=adtest,DC=local",
    }

    def __init__(
        self,
        server_uri="ldap://10.3.1.45:389",
        user_dn="Administrator@adtest.local",
        password="P@ssw0rd!23",
    ):
        self.server = Server(server_uri, get_info=ALL)
        self.user_dn = user_dn
        self.password = password
        self.conn = None

    def connect(self):
        self.conn = Connection(
            self.server,
            user=self.user_dn,
            password=self.password,
            authentication=NTLM,
            auto_bind=True,
        )
        return self.conn.bound

    def get_user_ou(self, employee_type: str) -> str:
        return self.OU_MAP.get(employee_type)

    def create_user(
        self,
        employee_type: str,
        eid: str,
        first_name: str,
        last_name: str,
        email: str,
        password: str = "TempPass@123",
    ) -> dict:

        if not self.conn:
            raise Exception("AD connection not established")

        ou_dn = self.get_user_ou(employee_type)
        if not ou_dn:
            raise Exception(f"No OU mapped for employee type: {employee_type}")

        cn = f"CN={first_name} {last_name}"
        user_dn = f"{cn},{ou_dn}"

        attributes = {
            "sAMAccountName": eid,
            "userPrincipalName": f"{eid}@{self.DOMAIN}",
            "givenName": first_name,
            "sn": last_name,
            "mail": email,
            "displayName": f"{first_name} {last_name}",
            "userAccountControl": 544,  # Normal account
        }

        self.conn.add(user_dn, ["top", "person", "organizationalPerson", "user"], attributes)

        if self.conn.result["description"] != "success":
            raise Exception(f"Failed to create user: {self.conn.result}")

        # Set password
        self.conn.extend.microsoft.modify_password(user_dn, password)

        # Enable user
        self.conn.modify(
            user_dn,
            {"userAccountControl": [(MODIFY_REPLACE, [512])]},
        )

        # Lookup GUID
        self.conn.search(
            search_base=user_dn,
            search_filter="(objectClass=user)",
            attributes=["objectGUID"],
        )

        guid = None
        if self.conn.entries:
            guid = self.conn.entries[0]["objectGUID"].value

        return {
            "dn": user_dn,
            "guid": guid,
        }
