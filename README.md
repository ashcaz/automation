# Lab:19 - Automation

## Overview

A colleague has abruptly left the team to pursue a career as a novelist.

This colleague’s last days (and weeks) on the job were a mixed bag in terms of productivity.

Looking through the documents left behind there is some important contact info in the form of email addresses and phone numbers.

Unfortunately it’s mixed in with a bunch of useless notes.

Your job is to find the needles in the haystack.

## Feature Tasks and Requirements

- Given a document potential-contacts, find and collect all email addresses and phone numbers.
- Phone numbers may be in various formats.
  - (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
  - phone numbers with missing area code should presume 206
  - phone numbers should be stored in xxx-yyy-zzzz format.
- Once emails and phone numbers are found they should be stored in two separate documents.
- The information should be sorted in ascending order.
- Duplicate entries are not allowed.

### User Acceptance Tests

The ‘phone_numbers.txt’ and ‘emails.txt’ files will be verified by an automated system. So make sure to match the naming/formatting requirements exactly.

## Configuration

- Find potential-contacts.txt and existing-contacts.txt in folder assets for today’s class in course repo.

Use `poetry` to create `automation` project.

```Bash
> $ poetry new automation
```

Use the folder created by Poetry as the root of your project’s git repository.

**Phone number Regualr expression used from https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html**

**Email regualr expresion used from**
