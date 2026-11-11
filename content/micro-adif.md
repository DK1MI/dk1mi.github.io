---
title: ADIF Syntax Highlighting for the Micro Editor
date: 2026-05-31
---

I recently fell in love with the [Micro Editor](https://micro-editor.github.io/) and switched to it from Vim after more than 25 years.
It is much more intuitive than Vim and I especially like the way how I can copy & paste text, that so many things are preconfigured
like i want it, the built-in plugin manager and many more. It was super easy to pick up without reading too much documentation.

Micro also comes with a large number of syntax highlighting definitions already built in - although not for the [Amateur Data Interchange Format (ADIF)](https://adif.org.uk), which was to be expected. Creating such a definition was the perfect opportunity for me to get to know this new (to me) editor better. The result was the following definition:

```
filetype: adif

detect:
  filename: "\\.adi$"

rules:
  # Matches the number inside the QSO field names that define the length
  # of the corresponding value
  - comment: ":[0-9]+>|:[0-9]+:.*>"

  # Color of all the possible QSO field names defined in the ADIF
  # specification under https://adif.org.uk/317/ADIF_317.htm#QSO_Fields
  - constant: "(?i)\\b(
    ADDRESS|ADDRESS_INTL|AGE|ALTITUDE|ANT_AZ|ANT_EL|ANT_PATH|ARRL_SECT|
    AWARD_GRANTED|AWARD_SUBMITTED|A_INDEX|BAND|BAND_RX|CALL|CHECK|CLASS|
    CLUBLOG_QSO_UPLOAD_DATE|CLUBLOG_QSO_UPLOAD_STATUS|CNTY|CNTY_ALT|COMMENT|
    COMMENT_INTL|CONT|CONTACTED_OP|CONTEST_ID|COUNTRY|COUNTRY_INTL|CQZ|
    CREDIT_SUBMITTED|CREDIT_GRANTED|DARC_DOK|DCL_QSLRDATE|DCL_QSLSDATE|
    DCL_QSL_RCVD|DCL_QSL_SENT|DISTANCE|DXCC|EMAIL|EQ_CALL|EQSL_AG|
    EQSL_QSLRDATE|EQSL_QSLSDATE|EQSL_QSL_RCVD|EQSL_QSL_SENT|FISTS|
    FISTS_CC|FORCE_INIT|FREQ|FREQ_RX|GRIDSQUARE|GRIDSQUARE_EXT|GUEST_OP|
    HAMLOGEU_QSO_UPLOAD_DATE|HAMLOGEU_QSO_UPLOAD_STATUS|HAMQTH_QSO_UPLOAD_DATE|
    HAMQTH_QSO_UPLOAD_STATUS|HRDLOG_QSO_UPLOAD_DATE|HRDLOG_QSO_UPLOAD_STATUS|
    IOTA|IOTA_ISLAND_ID|ITUZ|K_INDEX|LAT|LON|LOTW_QSLRDATE|LOTW_QSLSDATE|
    LOTW_QSL_RCVD|LOTW_QSL_SENT|MAX_BURSTS|MODE|MORSE_KEY_INFO|MORSE_KEY_TYPE|
    MS_SHOWER|MY_ALTITUDE|MY_ANTENNA|MY_ANTENNA_INTL|MY_ARRL_SECT|MY_CITY|
    MY_CITY_INTL|MY_CNTY|MY_CNTY_ALT|MY_COUNTRY|MY_COUNTRY_INTL|MY_CQ_ZONE|
    MY_DARC_DOK|MY_DXCC|MY_FISTS|MY_GRIDSQUARE|MY_GRIDSQUARE_EXT|MY_IOTA|
    MY_IOTA_ISLAND_ID|MY_ITU_ZONE|MY_LAT|MY_LON|MY_MORSE_KEY_INFO|MY_MORSE_KEY_TYPE|
    MY_NAME|MY_NAME_INTL|MY_POSTAL_CODE|MY_POSTAL_CODE_INTL|MY_POTA_REF|MY_RIG|
    MY_RIG_INTL|MY_SIG|MY_SIG_INTL|MY_SIG_INFO|MY_SIG_INFO_INTL|MY_SOTA_REF|
    MY_STATE|MY_STREET|MY_STREET_INTL|MY_USACA_COUNTIES|MY_VUCC_GRIDS|MY_WWFF_REF|
    NAME|NAME_INTL|NOTES|NOTES_INTL|NR_BURSTS|NR_PINGS|OPERATOR|OWNER_CALLSIGN|
    PFX|POTA_REF|PRECEDENCE|PROP_MODE|PUBLIC_KEY|QRZCOM_QSO_DOWNLOAD_DATE|
    QRZCOM_QSO_DOWNLOAD_STATUS|QRZCOM_QSO_UPLOAD_DATE|QRZCOM_QSO_UPLOAD_STATUS|
    QSLMSG|QSLMSG_INTL|QSLMSG_RCVD|QSLRDATE|QSLSDATE|QSL_RCVD|QSL_RCVD_VIA|
    QSL_SENT|QSL_SENT_VIA|QSL_VIA|QSO_COMPLETE|QSO_DATE|QSO_DATE_OFF|QSO_RANDOM|
    QTH|QTH_INTL|REGION|RIG|RIG_INTL|RST_RCVD|RST_SENT|RX_PWR|SAT_MODE|SAT_NAME|
    SFI|SIG|SIG_INTL|SIG_INFO|SIG_INFO_INTL|SILENT_KEY|SKCC|SOTA_REF|SRX|SRX_STRING|
    STATE|STATION_CALLSIGN|STX|STX_STRING|SUBMODE|SWL|TEN_TEN|TIME_OFF|TIME_ON|
    TX_PWR|UKSMG|USACA_COUNTIES|VE_PROV|VUCC_GRIDS|WEB|WWFF_REF
  )\\b"

  # Defines the color of EOH, EOR and the header fields described in
  # https://adif.org.uk/317/ADIF_317.htm#Header_Fields 
  - todo: "(?i)\\b(EOH|EOR|ADIF_VER|CREATED_TIMESTAMP|PROGRAMID|PROGRAMVERSION|USERDEF[0-9]+)\\b"

  # Defines the color of the < and > symbols around field names
  - error: "(<|>)"
```

Simply save the YAML file above to *~/.config/micro/syntax/adif.yaml* to enable syntax highlighting for ADIF files. The result will look like this:

![](/img/micro-adif-01.jpg)
