# LPG development environment

## Overview

This project is intended to allow any developer to pull down and spin up the LPG development environment as quickly as possible. This is achieved via various python scripts which will validate tool versions, clone relevant repositories and build JARs/Javascript assets (if desired).

It is designed to work with the `idt-feature-LC-XXX-local-development` branch on the various LPG projects. This branch was created to fix some of the quirks found in the projects which prevent them from being easily run in a development environment (Such as databse migrations being missing from some of the Java apps).

## Requirements

### Azure account

An Azure account is needed to be provided by the Apps Team.

Once you have an account, you'll need to authorise Azure. To do this:

1. [Install the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) for your OS. This may take a few minutes.

2. In your terminal, run `az acr login --name lpgregistry`. This will log you in to the LPG Azure registry by opening a page in the browser.

### Host entries

- There is a **hard requirement** to put the relevant host entries in your hosts file before accessing the site locally. This is because Docker-compose networking is used for the frontend applications. The required hosts can be found in `supporting_files/required_hosts.txt`.

#### On a Mac

On a Mac, open the Terminal, head to the root of this repository and paste the following command to update the hosts:

```sh
sudo zsh -c "cat supporting_files/required_hosts.txt >> /etc/hosts"
```
(This will most probably ask for your password as it's a `sudo` command).

## build_dev_env.py

This is the main entry point for the development environment. This script will clone all of the relevant projects and checkout to the relevant branches. It will also build JARs/JS projects, if desired, however this is not necessary to running the development environment (It is necessary if you want to use the base `Dockerfile` for each project).

### Script Requirements

- Python 3.7
- GitHub access to https://github.com/Civil-Service-Human-Resources
- If using the build flag:
    - Node 16.4 installed
    - Java 1.8 installed

### Step 1: Git clone

During the next step, the script will attmept to pull down the relevant git repositories from the [CSHR GitHub](https://github.com/Civil-Service-Human-Resources). This will use terminal commands, so please ensure you are authenticated against the organisation's GitHub with a valid SSH key/username login before running.

### Step 2: Validation (only if using build flag)

The script will first validate that the correct versions of `Node` and `Java` are installed correctly. These are currently versions `16.4` and `1.8`, respectively.

### Step 3: Build (only if using build flag)

The script will then loop through the applications it has cloned and attempt to build them using their respective build commands. This step is required as the Dockerfiles are set up to expect a pre-built application (i.e JAR/compiled TS app) to build correctly.

## Using the dev env

### Initial compose

After all of the repositories have been cloned/built, the initial `docker-compose up` can be executed. **The docker-compose file included in this project is intended for use with the `Dockerfile.dev` Dockerfiles in each app. A different `docker-compose.yaml` is required to make use of the standard `Dockerfile`.**

The `-d` flag can be added to run the up as a daemon command.

#### Java applications

The `idt-feature-LC-XXX-local-development` **must** be used for the initial `docker-compose up` command, as it contains the missing SQL in the migration files for the Java applications. If the regular branches are used first, the springboot applications will fail to apply to migrations (as the files in the regular branches contain invalid SQL). If the springboot apps fail to start for this reason, the migration table will need to be reset as well.

#### NodeJS applications

The main difference between the regular branches and `idt-feature-LC-XXX-local-development` branch for the NodeJS applications are the correction of the endpoints to the `develop.learn.civilservice.gov.uk` domain. **However**, these endpoints are overidden within the environment variables for the dev-env project regardless.

There is also an IntelliJ run configuration in the `idt-feature-LC-XXX-local-development` branch which can be used to conveniently attach to the running Node process in Google Chrome.

### Learning Catalogue

The learning catalogue application will not start correctly unless Elasticsearch is **fully** up. There is a `wait-for-it.sh` but sometimes even this doesn't catch the timing correctly. If learning catalogue fails to start, simply run `docker-compose restart learning-catalogue`

#### Learning Locker

Learning Locker will be set up as normal and should not be changed. It is extremely volatile and should be left alone to work in the background; one small change can cause it to stop working completely.

#### Databases

Redis and MySQL will start up in their own containers as dependencies for all of the other applications in the compose file. Once up, the MySQL container will bind volumes to the local machine to preserve data inbetween starting/stopping the dev-env.

##### Populating the ElasticSearch (learning catalogue) database

Use this command to add test courses to the ES database:

```
curl -XPOST "http://localhost:9200/courses/_doc/_bulk" -H "Content-Type: application/json" --data-binary "@apps/lpg-learning-catalogue/data/data.json"
```

### After up

Once all of the apps have successfully started within Docker, the website can be accessed by visiting `localhost:3001` in a web browser. 

### Development

To develop code for an application, it's easiest to first spin up all of the dependencies in the docker-compose file for that application. The `idt-develop` branch for the application can then be used as a base for the new feature branch to begin development.

**IMPORTANT:** due to the now-mismatched flyway migration files in some of the Java applications, flyway may have to be disabled after switching back to `idt-develop`, as the checksums will mismatch. This can be done with the application.yml property:

```
flyway:
    enabled: false
```

Needless to say, this should not be committed to the codebase.

To run the application, IntelliJ IDEA can be used (for both Java and Node apps) with the supplied `run` files.

### Dependencies

To develop with an application that has dependencies on other applications, the `docker-compose up` command can be used, with a space-seperated list of all the dependencies found in the `depends_on` for that application.

For example, when working on `learning-catalogue`, the command `docker-compose up identity elasticsearch` can be used to spin up the depependencies. Learning-catalogue can then be run as normal, using the localhost address for identity.