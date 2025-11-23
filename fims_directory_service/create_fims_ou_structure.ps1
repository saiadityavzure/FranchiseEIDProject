# ============================================
# FIMS DIRECTORY OU STRUCTURE CREATION SCRIPT
# ============================================

Write-Host "Starting creation of FIMS Directory OU structure..." -ForegroundColor Cyan

# Root domain DN
$domainDN = "DC=adtest,DC=local"

# Create root OU
$fimsRootOU = "OU=FIMS_Directory,$domainDN"

if (-not (Get-ADOrganizationalUnit -Filter "Name -eq 'FIMS_Directory'" -SearchBase $domainDN -ErrorAction SilentlyContinue)) {
    New-ADOrganizationalUnit -Name "FIMS_Directory" -Path $domainDN
    Write-Host "Created OU: FIMS_Directory" -ForegroundColor Green
} else {
    Write-Host "OU 'FIMS_Directory' already exists." -ForegroundColor Yellow
}

# Sub OUs under FIMS_Directory
$subOUs = @(
    "CorpAdmins",
    "LocAdmins",
    "LocationUsers"
)

foreach ($ou in $subOUs) {
    $ouPath = "OU=$ou,$fimsRootOU"

    if (-not (Get-ADOrganizationalUnit -Filter "Name -eq '$ou'" -SearchBase $fimsRootOU -ErrorAction SilentlyContinue)) {
        New-ADOrganizationalUnit -Name $ou -Path $fimsRootOU
        Write-Host "Created OU: $ou" -ForegroundColor Green
    }
    else {
        Write-Host "OU '$ou' already exists." -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "============================================"
Write-Host "FIMS Directory OU structure created successfully."
Write-Host "============================================"
Write-Host ""
Write-Host "Hierarchy:"
Write-Host "OU=FIMS_Directory,$domainDN"
Write-Host "    ├── OU=CorpAdmins"
Write-Host "    ├── OU=LocAdmins"
Write-Host "    └── OU=LocationUsers"
Write-Host "" -ForegroundColor Cyan
