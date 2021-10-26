# LPG development environment

## Overview

The purpose of this project is to set up the LPG development environment as quickly as possible. It achieves this by utilising a Python script which pulls each individual repository down, subsequently building them. This script will also include QoL features such as validating the correct versions of Java/Node are installed on the developers machine.

After the script has finished building all of the applications, `docker-compose` can then be used to run the applications (using their local Dockerfiles)

## Script.py

### Script Requirements

- Python 3
- GitHub access to https://github.com/Civil-Service-Human-Resources
- Node 16.4 installed
- Java 1.8 installed

### Step 1: Validation

The script will first validate that the correct versions of `Node` and `Java` are installed correctly. These are currently versions `16.4` and `1.8`, respectively.

### Step 2: Git clone

During the next step, the script will attmept to pull down the relevant git repositories from the [CSHR GitHub](https://github.com/Civil-Service-Human-Resources). This will use terminal commands, so please ensure you are authenticated against the organisation's GitHub with a valid SSH key/username login before running.

The branch `idt-feature-LC-XXX-local-development` will be checked out to automatically; this branch contains the specific quirks that each project requires to run smoothly in a local environment (i.e missing flyway migrations for the Java applications).

### Step 3: Build

The script will then loop through the applications it has cloned and attempt to build them using their respective build commands. This step is required as the Dockerfiles are set up to expect a pre-built application (i.e JAR/compiled TS app) to build correctly.

After this step completes, the applications will be ready for copying into their Docker containers via `docker-compose`.

## rebuild_app.py