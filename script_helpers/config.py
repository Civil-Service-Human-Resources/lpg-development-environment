from script_helpers.classes import AppLanguage, App, Requirement

GIT_REPO_BASE = "https://github.com/Civil-Service-Human-Resources"

APP_DIR = "apps"

LOCAL_DEVELOP_BRANCH = "idt-feature-LC-XXX-local-development"

JAVA_MAVEN = AppLanguage("java", "maven", "mvn clean install -DskipTests", "target")
JAVA_GRADLE = AppLanguage("java", "gradle", "./gradlew build", "build")
LPG_SERVICES = AppLanguage("node", "npm", "npm install && ./bin/setup-dist && npm run compile", "dist/build")
LPG_MANAGEMENT = AppLanguage("node", "npm", "npm install && npm run compile", "dist/build")
TERRAFORM = AppLanguage("terraform")

NODE_16_REQUIREMENT = Requirement("node", "16.4", ["node", "-v"], 'v(\d+\.\d+).*')
JAVA_8_REQUIREMENT = Requirement("java", "1.8", ["java", "-version"], '\"(\d+\.\d+).*\"')
MAVEN_REQUIREMENT = Requirement("maven", "3.8.6", ["mvn", "-v"], '(\d+\.\d+).*')

APPS = [
    App("lpg-services", LPG_SERVICES, [NODE_16_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("lpg-management", LPG_MANAGEMENT, [NODE_16_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("identity-service", JAVA_GRADLE, [JAVA_8_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("lpg-learner-record", JAVA_GRADLE, [JAVA_8_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("lpg-learning-catalogue", JAVA_GRADLE, [JAVA_8_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("civil-servant-registry-service", JAVA_GRADLE, [JAVA_8_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("lpg-report-service", JAVA_GRADLE, [JAVA_8_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("notification-service", JAVA_GRADLE, [JAVA_8_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("identity-management", JAVA_MAVEN, [JAVA_8_REQUIREMENT, MAVEN_REQUIREMENT], LOCAL_DEVELOP_BRANCH),
    App("lpg-terraform-paas", TERRAFORM)
]