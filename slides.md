# Using debusine to automate your QA

.fx: title_slide

[`https://deb.li/debusine`](https://reimbursements.debian.net/)

Carles Pina i Estany <`cpina@debian.org`>,
Colin Watson <`cjwatson@debian.org`>,
Enrico Zini <`enrico@debian.org`>,
Stefano Rivera <`stefanor@debian.org`>

A [Freexian](https://www.freexian.com/) project, funded with the help of
the [Sovereign Tech Fund](https://www.sovereign.tech/programs/fund).

MiniDebConf Toulouse at Capitole du Libre, 16 November 2024

# Presenter Notes

Welcome.

We'll be rotating presenters. Introduce them all.

Let's talk about how you can use debusine to automate your Debian QA.

---

# Quick Introduction

.fx: introduction

* What is debusine
* Who we are
* State of the Project

# Presenter Notes

[5 minutes to whip through these]

Quick introduction, then we'll get onto a demo and really talk through
how things work.

---

# What is debusine:

* Potential future infrastructure for Debian
* Solving Freexian’s needs as a Debian derivative

    * Building packages
    * QA tasks and workflows
    * Package and secure boot signing
    * APT Repositories (future)

* Potential SAAS product for Freexian as a Debian Services Company

---

# Who are we:

* Debian Developers
* Freexian collaborators
* Paid to work on debusine
* Funded this year by STF

---

# State of the Project:

* Heavy development
* Core foundations in place
* Building out higher-level functionality
* Generally useable
* Public instance: debusine.debian.net

    * Used for testing the Python 3.13 transition recently.
    * And large-scale rebuilds around the Python ecosystem.

* In production for Freexian

---

# Example

# Presenter Notes

[2 minutes to run this]

See examples/README

Example of a source package upload and trigger the debian pipeline:
Prepare a source package
Maybe distro-info? It builds for multiple architectures and has autopkgtests.
debusine.client import-debian-artifact distro_info.dsc
debusine.client create-workflow workflow:debian-pipeline --data pipeline.yaml
Show pipeline yaml

---

# Debusine Concepts

.fx: introduction

* Artifacts
* Work Requests
* Collections
* Lookups
* Workflows

# Presenter Notes

[10 minutes for the concepts]

While we're waiting for the Demo to complete, let's talk about what's
happening in debusine.

---

# Artifacts

* E.g. `distro_info.dsc` becomes a `debian:source-package`
* Strongly typed objects with JSON metadata

    * Types: `debian:source-package`, `debian:binary-package`, `debian:upload`, `debian:package-build-log`, etc.

* Contain files
* Stored by hash in a blob store or on disk

# Presenter Notes

Look at our uploaded source package artifact.
Describe how artifacts work in general.

Blob store isn't implemented yet.

---

# Work Requests

* sbuild task
* Strongly typed with JSON metadata
* Inputs and outputs are artifacts
* Logs are artifacts
* Build happens on an external worker with no privileged access
* Build is sandboxed in an environment:

    * Unshare, Incus LXC, Incus VM, QEMU

* The environment also comes from an artifact

# Presenter Notes

Describe work requests, then look at the example work request that we're
running.

---

# Collections

* Strongly typed with defined semantics
* Hold a set of similar artifacts
* E.g. `debian:archive`, `debian:suite`, `debian:environments`.
* Can also hold bare-data JSON objects:

    * Configuration
    * Promises for to-be-created artifacts

# Presenter Notes

We skimmed over environments when we looked at the artifact.
Debusine has a collection of build environments, updated daily, that we
can use.

Describe collections.

---

# Lookups

* Finds one or many items in a collection by attributes
* Can be specified as a string:

    `bookworm@debian:suite/src2_2.0`

* Or dictionary:

    <pre><code>
    collection: debian/trixie
    child_type: artifact
    category: debian:binary-package
    data__package: libc6
    data__version: "2.37-15"
    </code></pre>

* Or even just bare artifact IDs.

# Presenter Notes

The environment was found using a lookup into the `debian` environments
collection for an `unstable` tarball. Under the hood, restrictions for a
tarball suitable for `unshare` would have been added.

Describe collections.

---

# Workflows

* One request triggers a tree of related work requests
* Automates common workflows using templates
* Currently driven by Python code in the server
* Has an internal collection for artifacts produced in the workflow.

---

# Using debusine to automate your QA

* Debian Developers can use [debusine.debian.net](https://debusine.debian.net/)
* Client configuration instructions are [in our docs](https://freexian-team.pages.debian.net/debusine/tutorials/getting-started-with-debusine.html#install-the-client-and-configure-it)
* Use one of [our workflows](https://freexian-team.pages.debian.net/debusine/reference/workflows/specs.html)

    * Low level work requests
    * Low level workflows: `sbuild`, `autopkgtest`, `lintian`, `piuparts`
    * High level workflows: `qa`, `debian_pipeline`

* For the brave: [debusine-rebuilds](https://salsa.debian.org/stefanor/debusine-rebuilds) can orchestrate large-scale rebuilds using debusine work requests.

# Presenter Notes

You've seen a demo. If you want to go home and do any of this, start
with our docs.

Here are some of the tools debusine provides that you can use to
automate Debian QA.

We have lower level building blocks that can run individual QA tasks,
but you probably want to use a higher level workflow like `qa`, or
`debian_pipeline`. `debian_pipeline` builds your package, runs all the
QA tests on it, and if they pass it can upload the result to Debian.

---

# What has been achieved in the last year

* STF funded milestones
* Approx 3 months each

# Presenter Notes

[5 minutes to whip through these]

---

# STF M1: QA Tasks

* Build out QA tasks (sbuild, autopkgtest, lintian, piuparts, blhc)
* Open dialogue with these QA teams
* Public debusine.debian.net instance
* SSO
* Web views for tasks
* Executor interface for sandboxing task and providing environments

# Presenter Notes

Before STF M1 we had artifacts and the basic sbuild task (using schroot).

---

# STF M2: Scheduled Tasks

* Workflows
* Collections

# Presenter Notes

These were both big complex tasks with

---

# STF M3: Buildd Network

* Replace Freexian’s buildd in production
* Talk to the Debian buildd team about requirements
* Sbuild workflow
* BD-Uninstallable waits
* Package upload workflow
* BinNMU, give-back
* Build log collections
* Task queue overviews

---

# STF M4: Security builds

* Talk to the Debian security team
* Implement private workspaces
* Workflow to copy from private workspace to a public one
* Secure boot signing (and HSMs)
* Review steps in workflows
* Debdiff task
* Reverse autopkgtest workflow

---

# Future of debusine

* Busy finishing M4
* About to start on M5
* 2025 STF Milestones

# Presenter Notes

[3 minutes]

---

# STF M5: Large Scale experiments and Cloud

* Record build resource statistics (build time, RAM + disk usage)
* Auto-spawn external build workers in the cloud
* Cloud storage for artifacts
* Custom workflows
* Web interface to monitor experiment results

---

# 2025 STF Milestones

* Increase debusine's adoption and maintainability
* Basic Package Repositories
* Advanced features for Package Repositories

    * Self-service repositories (PPAs)
    * Better UI
    * Copy packages

# Presenter Notes

[2 minutes]

No maintenance budget in 2024, STF features drove the schedule for the
year. We need to have some space for refactoring and misc work.

---

# Funding

* Freexian
* STF
* Other funding sources

# Presenter Notes

[2 minutes]

STF Funding made a big boost to development in 2024.

We expect less funding from STF in 2025, so we'll look at some other
sources too.

---

# Getting involved

* Open development on salsa

    * GPLv3, no CLA
    * Modern Python, Django, lots of type annotations, 100% branch coverage

* Bitesize tasks
* Backlogged tasks that don’t fit the funded roadmap

# Presenter Notes

[5 minutes]

---

# Questions?

# Presenter Notes

[5 minutes]
