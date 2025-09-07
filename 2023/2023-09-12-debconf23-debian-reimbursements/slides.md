# Debian Reimbursements

.fx: title_slide

[`https://reimbursements.debian.net/`](https://reimbursements.debian.net/)

Stefano Rivera <`stefanor@debian.org`>

Funded by [Freexian](https://www.freexian.com/) Debian Project Funding

DebConf 23 — September 2023

# Presenter Notes

Who am I?

Past DebConf organizer and current committee, serving as the treasurer
for DebConf23.
Experience spending Debian's money, and working with the Debian
Treasurer team.

Built most of the infrastructure behind the DebConf website.
Experience building Django apps in Debian.

We'll talk about:

How Debian currently pays for things and the reimbursement web interface
I've been working on since DebConf 22.

---

# Introduction

---

# Money in Debian

* Sponsors donate to support us
* We need to spend this money
* Assets are held by Trusted Organizations:
    * SPI (US)
    * Debian France (EU)
    * Debian.ch (Switzerland, EEA? FIXME)

# Presenter Notes

Sponsors give us money to support us.

Debian's money doesn't do much good unless we spend it.

Debian isn't a legal entity, but rather has spawned several entities
that hold assets for us (and other projects).

We may add a Debian entity in the near future.

---

# What do we spend it on?

* Annual conferences
    * Our main fundraising activity
    * Usually makes a profit
* Development sprints
* Bug Squashing Parties
* Infrastructure (Servers)
* Hardware for developers

# Presenter Notes

DebConf is the main financial activity in Debian for the year.
But also Debian's main fundraising.

Sprints typically get some local (in-kind) sponsorship and co-locate
with an event to save costs. But usually require travel, food, and
accommodation sponsorship.

BSPs: Sponsor pizza

Infrastructure used to be mostly sponsored, but more recently DSA has
purchased servers (typically with discounts).

Developers can request funding to buy hardware to assist them in Debian.

Probably others...

---

# How do we spend it?

* DPL authorizes all spending
* DPL can delegate a budget to DebConf's treasurer
* TO contracts and is invoiced, directly
* Developer pays out of pocket and is reimbursed
* TO pays on behalf of a developer

# Presenter Notes

Debian's constitution delegates some powers, but most rest with the DPL,
including finance.

The DPL authorizes most expenses but can delegate an entire budget of
expenses (typically to DebConf's treasurer, every year).

If we have contracts to sign, typically a Trusted Organization will
sign them, and be invoiced directly.

For smaller expenses, a Developer pays out of pocket and is reimbursed.
That's what we're addressing in this project.

Where a Developer cannot afford to pay an expense out of pocket, a
Trusted Organization can pay on their behalf.

---

# How do reimbursements currently work?

* File RT pre-approval ticket (DPL & TO)
* Get Approved
* Spend money
* Compile Expense Report (XE Travel Calculator)
* Print to PDF
* Manually fix multi-page rendering bugs
* Prepare SPI Bank Details form
* Bundle together PDFs
* Copy-paste a statement into an email
* Submit to reimbursement ticket

# Presenter Notes

This is the current e-mail based flow for spending Debian's money at the
moment.

Don't worry too much about the details, I'll show you an example in a
second.

The point is that it's e-mail centric, requires creating multiple RT
tickets, and CCing the right people. Basically you have to refer to the
wiki page whenever you do it, even if you do it a lot.

The tools used are painful and buggy, there are gaps in the system, and
reimbursements often stall for years.

---

# Example!

# Presenter Notes

This is a fairly typical example from people who have done this before
several times. They (should) know what they're doing.

I picked this example because it was recent and I remembered it going
smoothly. Only when I was writing the talk did I how many things had
gone wrong.

Some I can explain. Some are just emails that fell through the cracks.

---

.fx: full_email long_email

    From: Louis-Philippe Véronneau <pollo@debian.org>
    Subject: Debian RT: Budget Request - DebConf Videoteam sprint, July 20th-23rd, Paris, France
    To: debian-sprints@lists.debian.org, DPL <leader@debian.org>
    Cc: Stefano Rivera <stefanor@debian.org>, Wouter Verhelst <wouter@debian.org>, Kyle Robbertze
            <paddatrapper@debian.org>, Nicolas Dandrimont <olasd@debian.org>,
            treasurer@debian.org, treasurer@rt.spi-inc.org, tresorier@france.debian.net
    Date: Sat, 17 Jun 2023 01:12:58 -0400

    Dear DPL,

    The following is a budget request for the upcoming Deconf Videoteam sprint,
    that will take place in Paris, France, from July 20th to July 23rd 2023.

    In total, we're asking for 6,365 USD. Here's the budget breakdown:

    # | Name            | Travel      | Accommodation  | Meals and incidentals  | TOTAL       | TO         |
    --|-----------------|-------------|----------------|------------------------|-------------|------------|
    1 | Louis-Philippe  | N/A         | N/A            | 456 USD                | 456 USD     | SPI        |
    2 | Kyle            | 850 USD     | 550 USD        | 250 USD                | 1,650 USD   | SPI        |
    3 | Wouter          | 1,100 EUR   | 500 EUR        | 230 EUR                | 1,830 EUR   | Debian Fr  |
    4 | Stefano         | 1,200 USD   | 550 USD        | 250 USD                | 2,000 USD   | SPI        |
    5 | Nicolas         | N/A         | N/A            | 230 EUR                | 230 EUR     | Debian Fr  |
    --------------------------------------------------------------------------------------------------------
    TOTAL: 4,106 USD + 2,060 EUR ~= 6,365 USD

    I'm the only remote participant who's asking for M&I, and my request is based on
    data provided by the US government [1].

    Since people will be reimbursed in two different currencies (USD and EUR) by
    two different TOs (SPI and Debian France), I've taken the liberty of only
    converting the total. If you need me to convert everything to a single currency
    anyway, I'll be happy to.

    Cheers,

    [1]: https://www.gsa.gov/travel/plan-book/per-diem-rates/per-diem-rates-lookup

# Presenter Notes

Things to note here:

* The To and CC lists are complex
* There's a budget
* In 2 currencies
* There are multiple Trusted Organizations involved in reimbursement.
* This is filing a new ticket in the SPI RT system, but only the sender
  gets the reply with the new subject.
* For the pedants: Magical Debian RT cookie

---

.fx: full_email medium_email

    From: Jonathan Carter <jcc@debian.org>
    Subject: Debian RT: Budget Request - DebConf Videoteam sprint, July
        20th-23rd, Paris, France
    To: debian-sprints@lists.debian.org, Debian Project Leader <leader@debian.org>,
        "treasurer@rt.spi-inc.orgtreasurer@debian.org >> Debian treasurer team"
        <treasurer@debian.org>
    Cc: Stefano Rivera <stefanor@debian.org>, Wouter Verhelst
        <wouter@debian.org>, Kyle Robbertze <paddatrapper@debian.org>,
        Nicolas Dandrimont <olasd@debian.org>
    Date: Wed, 5 Jul 2023 20:23:44 +0200

    Hi Pollo

    > The following is a budget request for the upcoming Deconf Videoteam sprint,
    > that will take place in Paris, France, from July 20th to July 23rd 2023.
    >
    > In total, we're asking for 6,365 USD. Here's the budget breakdown:

    Expenses approved for the above sprint.

    -Jonathan

# Presenter Notes

Things to note:

* DPL reads the budget but probably wants to review just one currency.
* DPL didn't get the RT subject, so his reply would have created a new SPI ticket.
* Except, something went wrong in the email address, and it went into a black hole.

---

    From: Martin Michlmayr via RT <treasurer@rt.spi-inc.org>
    Subject: [TREASURER #6567] Debian RT: Budget Request - DebConf
        Videoteam sprint, July 20th-23rd, Paris, France
    To: pollo@debian.org
    CC: leader@debian.org, olasd@debian.org, paddatrapper@debian.org,
        stefanor@debian.org, treasurer@debian.org, wouter@debian.org
    Date: Mon, 24 Jul 2023 06:13:39 -0400

    Did this get approved?

    I never saw a reply to this email.

    Martin

.notes: Proactive TO!

---

.fx: full_email medium_email

    From: Jonathan Carter <jcc@debian.org>
    Subject: Re: [TREASURER #6567] Debian RT: Budget Request - DebConf
        Videoteam sprint, July 20th-23rd, Paris, France
    To: treasurer@rt.spi-inc.org, pollo@debian.org
    Cc: leader@debian.org, olasd@debian.org, paddatrapper@debian.org,
        stefanor@debian.org, treasurer@debian.org, wouter@debian.org
    Date: Mon, 24 Jul 2023 13:47:25 +0200
    
    Hi Martin
    
    On 2023/07/24 12:13, Martin Michlmayr via RT wrote:
    > Did this get approved?
    >
    > I never saw a reply to this email.
    
    It got approved on 2023-07-05,
    Message-ID: <ebbd461a-0c54-b5fe-2981-7c72230c2924@debian.org>
    
    Did you receive that mail? Otherwise I'll re-send.
    
    -Jonathan

---

.fx: full_email medium_email

    From: "tbm@spi-inc.org via RT" <treasurer@rt.spi-inc.org>
    Subject: Re: [TREASURER #6567] Debian RT: Budget Request - DebConf
        Videoteam sprint, July 20th-23rd, Paris, France
    To: pollo@debian.org
    CC: leader@debian.org, olasd@debian.org, paddatrapper@debian.org,
        stefanor@debian.org, treasurer@debian.org, wouter@debian.org
    Date: Mon, 24 Jul 2023 07:57:18 -0400
    
    * Jonathan Carter via RT <treasurer@rt.spi-inc.org> [2023-07-24 07:47]:
    > It got approved on 2023-07-05,
    > Message-ID: <ebbd461a-0c54-b5fe-2981-7c72230c2924@debian.org>
    >
    > Did you receive that mail? Otherwise I'll re-send.
    
    I didn't receive it.
    
    --
    Martin Michlmayr
    Contractor, Software in the Public Interest, Inc.

---

.fx: full_email medium_email

    From: Martin Michlmayr via RT <treasurer@rt.spi-inc.org>
    Subject: [TREASURER #6567] Debian RT: Budget Request - DebConf
        Videoteam sprint, July 20th-23rd, Paris, France
    To: jcc@debian.org, pollo@debian.org
    CC: leader@debian.org, olasd@debian.org, paddatrapper@debian.org,
        stefanor@debian.org, treasurer@debian.org, wouter@debian.org
    Date: Thu, 03 Aug 2023 03:10:38 -0400
    
    So if I'm reading this correctly, the following people will get
    reimbursed by SPI:
    
    * Louis-Philippe
    * Kyle
    * Stefano
    
    I'll trim the CC list accordingly.
    
    Kyle and Stefano: please follow
    https://www.spi-inc.org/treasurer/reimbursement-form/ and submit a
    ticket (mention RT#6567 as approval). You know the drill :)
    
    Martin

---

.fx: full_email long_email

    From: Kyle Robbertze <paddatrapper@debian.org>
    Subject: Re: [TREASURER #6567] Debian RT: Budget Request - DebConf
        Videoteam sprint, July 20th-23rd, Paris, France
    To: treasurer@rt.spi-inc.org, jcc@debian.org, pollo@debian.org
    Cc: leader@debian.org, olasd@debian.org, stefanor@debian.org,
        treasurer@debian.org, wouter@debian.org
    Date: Thu, 3 Aug 2023 15:40:38 +0100
    
    Hi,
    
    On 2023/08/03 08:10, Martin Michlmayr via RT wrote:
    > So if I'm reading this correctly, the following people will get reimbursed by SPI:
    >
    > * Louis-Philippe
    > * Kyle
    > * Stefano
    >
    > I'll trim the CC list accordingly.
    >
    > Kyle and Stefano: please follow
    > https://www.spi-inc.org/treasurer/reimbursement-form/ and submit a
    > ticket (mention RT#6567 as approval). You know the drill :)
    
    I was unable to attend due to visa issues, so I will not be requesting a
    reimbursement.
    
    Cheers
    Kyle

---

.fx: full_email

    From: Wouter Verhelst via RT <treasurer@rt.spi-inc.org>
    Subject: Re: [TREASURER #6567] Debian RT: Budget Request - DebConf
        Videoteam sprint, July 20th-23rd, Paris, France
    To: jcc@debian.org, pollo@debian.org
    CC: leader@debian.org, paddatrapper@debian.org, stefanor@debian.org, treasurer@debian.org

    Date: Tue, 08 Aug 2023 19:36:15 -0400
    
    Hi all,
    
    What's the status on this one? I had counted on it being in my bank
    account by now, there's some payments now that are bouncing...
    
    Thanks,

---

    From: Martin Michlmayr via RT <treasurer@rt.spi-inc.org>
    Subject: [TREASURER #6567] Debian RT: Budget Request - DebConf
        Videoteam sprint, July 20th-23rd, Paris, France
    To: jcc@debian.org, pollo@debian.org
    CC: leader@debian.org, paddatrapper@debian.org, stefanor@debian.org, treasurer@debian.org
    Date: Tue, 08 Aug 2023 20:33:56 -0400
    
    Wouter,
    
    According to the approvals table, your request is handled by Debian
    France, not SPI.  Did you submit your reimbursement request there?
    
    Anyway, I'll forward your email to Debian France.
    
    3 | Wouter | 1,100 EUR | 500 EUR | 230 EUR | 1,830 EUR | Debian Fr |
    
    Martin

---

.fx: full_email long_email

    From: Jonathan Carter <jcc@debian.org>
    Subject: Re: Debian RT: Budget Request - DebConf Videoteam sprint,
        July 20th-23rd, Paris, France
    To: treasurer@rt.spi-inc.org, treasurer@debian.org, treasurer-debianfr@rt.debian.org,
        Louis-Philippe Véronneau <pollo@debian.org>
    Cc: Wouter Verhelst <wouter@debian.org>, Pierre-Elliott Bécue <tresorier@france.debian.net>,
        Debian Project Leader <leader@debian.org>
    Date: Wed, 16 Aug 2023 16:14:41 +0200
    
    Dear all
    
    (minus sprints@ and some video team members)
    
    It seems that Debian France was omitted in the original process, where Wouter
    is now claiming reimbursement from.
    
    On 2023/07/24 14:16, Jonathan Carter wrote:
    > > The following is a budget request for the upcoming Deconf Videoteam
    > > sprint, that will take place in Paris, France, from July 20th to July
    > > 23rd 2023.
    > >
    > > In total, we're asking for 6,365 USD. Here's the budget breakdown:
    >
    > Expenses approved for the above sprint.
    >
    > -Jonathan
    
    Budget for that video sprint is on the wiki:
    https://wiki.debian.org/Sprints/2023/DebConfVideoteam
    
    Wouter's total approval amount was for a total of €1830, although if his
    invoices add up to more, we can give some leeway if needed.
    
    So, for the avoidance of any doubt, Wouter's expenses has approval for €1830.
    
    -Jonathan

---

    From: Stefano Rivera <stefanor@debian.org>
    Subject: Reimbursement Request for DebConf Video Sprint - Stefano
    To: treasurer@rt.spi-inc.org
    Date: Fri, 4 Aug 2023 09:30:04 +0000
    
    Approved in RT#6567, here is my reimbursement request.
    
    By submitting this reimbursement request, I declare:
      - that I have prepared an SPI Reimbursement Request Form including
        bank account details,
      - that I have prepared an Expense Report using Expensify,
      - that I have attached sufficient documentation substantiating my request,
      - that I seek reimbursement of expenses that are compliant with
        SPI and applicable Associate Project policies, and
      - that I have not sought nor will seek reimbursement of these
        expenses from any other source.
    
    Stefano

---

    From: Martin Michlmayr via RT <treasurer@rt.spi-inc.org>
    Subject: [TREASURER #6671] Reimbursement Request for DebConf Video Sprint - Stefano
    To: stefanor@debian.org
    Date: Mon, 07 Aug 2023 01:40:45 -0400
    
    This request looks complete. It's slightly above the approved budget
    but Debian allows 5% grace so this is fine anyway.

---

# We can do better

* Web interface to guide you
* Log for each request that everyone involved can see
* Automated exchange rate conversion
* Automated budget sums
* You still need to get receipts
* You still need to scan receipts
    * We *could* build in cellphone camera scans (future)
* Still need to fill in bank details
    * We can remember these for your next request
* TO still needs to manually copy and paste bank details
    * We can hopefully pre-fill these for Wise and SEPA payments

---

# New Flow

* Log into reimbursement web-interface
* Describe your request with a high-level budget
* Click submit. Goes to DPL for approval
* Spend money
* Upload receipts
* Fill in bank details (if not already known)
* Click submit

---

# Goals

* Encourage Debian Developers to spend Debian's money by making it easy
* Provide common flows between Trusted Organizations
* Track spending in Debian with reporting across Trusted Organizations
* Avoid confusion between Trusted Organizations
* Avoid having to complete the same reimbursement forms every time
* Help Trusted Organizations to automate their reimbursement flows

---

# Freexian Funding

* I contract to Freexian as a collaborator
* Freexian provides Debian Services including Debian LTS and ELTS
* Collaborators may spend 20% of funded time on Debian projects
* Freexian also directly funds projects to improve Debian:
  [https://salsa.debian.org/freexian-team/project-funding/](https://salsa.debian.org/freexian-team/project-funding/)
* This project was funded for 3 full-time week milestones

---

# Current Status

* In the MVP phase right now.
* Currency and exchange rate handling is complete and published as a separate Django app.
* The most basic core flows are complete, but not all corner cases are handled.
* Production instance running on a `debian.net` hosted VM.
* Ready to be used for some DebConf reimbursements.
* Still light test coverage.

---

# Next Steps

* Test at DebConf
* Complete IRC notifications
* Better bank detail forms
* Sub-requests (e.g. 3 attendees at a sprint)
* Expand test coverage
* Automated TO selection
* Build out exports and GDPR compliance cleanups
* Show spending statistics
* Announce general availability
* Iterate development based on feedback

---

# Questions?
