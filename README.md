# BUNNY RAMDISK — Backup / Restore (Standalone CLI)

A12/A13 (iPhone XS–11 series, SE2) activation backup & restore scripts for the
BUNNY RAMDISK SSH ramdisk workflow. These are standalone CLI versions of the
GUI tool's backup/restore buttons — same logic, no GUI needed.

## Files

| File | Purpose |
|---|---|
| `bunny_backup.py` | Pull activation files from the SSH ramdisk → backup zip `0x<ECID>.zip` |
| `bunny_restore.py` | Restore activation files from a backup zip → reboot to normal iOS |

## Requirements

- A12/A13 device booted to the **BUNNY RAMDISK SSH ramdisk** (usbliter8 pwned DFU
  → iBEC → ramdisk → SSH up), filesystems mounted (`mount_ich`, `/mnt2` up)
- `python3` on the host
- macOS BUNNY RAMDISK install (scripts load `core.py` from the app bundle)

## Usage

### Backup

```bash
python3 bunny_backup.py
```

Pulls from the device (via SSH on port 2222, password `alpine`):

- `activation_record.plist` → System container `Library/activation_records/`
- `data_ark.plist` → System container `Library/internal/`
- `com.apple.commcenter.device_specific_nobackup.plist` → `wireless/Library/Preferences/`
- `IC-Info.sisv` → `mobile/Library/FairPlay/iTunes_Control/iTunes/`

Saves `owner_info.txt` (device/serial/ECID/phone) and zips everything to:

```
~/BUNNY RAMDISK/Backup/0x<ECID>.zip
```

Then reboots the device to normal iOS.

### Restore

```bash
python3 bunny_restore.py /path/to/0x<ECID>.zip
```

1. Extracts the backup zip
2. Stages files on the device (`/mnt2/root/Activation/`)
3. Runs `restore.sh` + `skip_setup.sh` + places SkipSetup markers
4. Verifies sizes (`act_rec` / `data_ark` / `IC`)
5. Reboots to normal iOS — setup skipped, no activation banner

## Notes

- Both scripts expect the device to already be in the SSH ramdisk with
  `/mnt2` mounted — run the ramdisk **Boot** first, then these scripts.
- The restore path expects the same zip layout the backup produces:
  `activation_record.plist`, `data_ark.plist`, `com.apple.commcenter.device_specific_nobackup.plist`,
  `FairPlay/iTunes_Control/iTunes/IC-Info.sisv`, `owner_info.txt`.

## ☕ Buy Me a Coffee

If this tool helped you, consider buying me a coffee:

- **Buy Me a Coffee:** https://www.buymeacoffee.com/bunnyciaa
- **PayPal:** https://www.paypal.com/paypalme/bunnyciaa
