# PPN Invoice Narration Module

This Odoo module adds a standardized PPN (Value Added Tax) narration text to invoice reports based on PMK 131/2024 regulations.

## Features

- Adds automatic PPN 11% narration text to invoice reports
- Implements PMK Nomor 131 Tahun 2024 compliance text
- Inherits and extends standard Odoo invoice report template

## Technical Details

The module extends `account.report_invoice_document` template by adding a fixed narration text before the existing narration field
created by Dino Herlambang
