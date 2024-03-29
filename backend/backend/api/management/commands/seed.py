from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models.admin import Admin
from api.models.developer import Developer
from api.models.organization import Organization
from api.models.requirement import Requirement
from api.models.seniority import Seniority
from api.models.profile import Profile
from api.models.profileseniority import ProfileSeniority
from api.models.profileseniorityrequirement import ProfileSeniorityRequirement
from api.models.pokemon import Pokemon
from api.models.developerprofile import DeveloperProfile
from api.models.developerrequirement import DeveloperRequirement

import random
from faker import Faker


class Command(BaseCommand):
    help = "Seeds the database."

    organizations = [
        "Microsoft Corporation",
        "Oracle Corporation",
        "IBM Corporation",
        "SAP SE",
        "Salesforce.com, Inc.",
        "Hewlett Packard Enterprise Company",
        "Dell Technologies Inc.",
        "Cisco Systems, Inc.",
        "Amazon Web Services, Inc.",
        "Google LLC",
        "Apple Inc.",
        "Intel Corporation",
        "VMware, Inc.",
        "Adobe Inc.",
        "Accenture plc",
        "Fujitsu Limited",
        "NTT Data Corporation",
        "Tata Consultancy Services Limited",
        "Infosys Limited",
        "Wipro Limited"
    ]

    seniorities = [
        "Junior",
        "Middle",
        "Senior",
        "Lead",
        "Principal"
    ]

    requirements = [
        "Python proficiency",
        "Java proficiency",
        "JavaScript proficiency",
        "Web development experience",
        "Mobile app development experience",
        "Database management skills",
        "Git version control experience",
        "Containerization knowledge (e.g., Docker)",
        "Cloud platform experience (e.g., AWS, Azure)",
        "Agile methodology experience",
        "RESTful API knowledge",
        "Microservices architecture knowledge",
        "Machine learning understanding",
        "Test-driven development experience",
        "Continuous integration and delivery",
        "Project management experience",
        "Strong problem-solving skills",
        "Effective communication abilities",
        "Teamwork and collaboration skills",
        "Ability to work under pressure",
        "Willingness to learn new technologies",
        "Attention to detail",
        "Critical thinking capabilities",
        "Creativity in problem-solving",
        "Front-end framework familiarity (e.g., React, Vue)",
        "Back-end framework expertise (e.g., Django, Flask)",
        "Knowledge of SQL databases",
        "NoSQL database experience (e.g., MongoDB)"
    ]

    profiles = [
        "Backend Developer",
        "Frontend Developer",
        "Fullstack Developer",
        "Mobile Developer",
        "Desktop Developer",
        "Quality Assurance Engineer",
        "DevOps Engineer",
        "Cloud Engineer",
        "Data Engineer",
        "Machine Learning Engineer",
        "Technical Lead",
        "Architect",
        "Product Manager",
        "UI/UX Designer",
        "Data Scientist",
        "Security Engineer",
        "Network Engineer",
        "Database Administrator",
        "Embedded Systems Engineer",
        "Game Developer",
        "Blockchain Developer",
        "System Administrator",
        "IT Project Manager",
        "Business Analyst",
        "Network Administrator",
        "Artificial Intelligence Engineer",
        "Computer Vision Engineer",
        "Natural Language Processing Engineer",
        "Software Engineer",
        "IT Consultant"
    ]

    def add_arguments(self, parser):
        parser.add_argument("username", nargs="+", type=str)
        parser.add_argument("password", nargs="+", type=str)

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")

        self.stdout.write("Deleting users...")
        User.objects.all().delete()
        self.stdout.write("Deleting developers...")
        Developer.objects.all().delete()
        self.stdout.write("Deleting admins...")
        Admin.objects.all().delete()
        self.stdout.write("Deleting organizations...")
        Organization.objects.all().delete()
        self.stdout.write("Deleting requirements...")
        Requirement.objects.all().delete()
        self.stdout.write("Deleting seniorities...")
        Seniority.objects.all().delete()
        self.stdout.write("Deleting profiles...")
        Profile.objects.all().delete()

        faker = Faker()
        is_my_organization = False
        usernames = []

        # Create organizations
        for org in random.sample(self.organizations, 4):
            pokemons = []
            self.stdout.write(f"Creating organization {org}...")
            organization = Organization.objects.create(name=org)

            self.stdout.write(f"Creating organization requirements...")

            # Create requirements
            organization_requirements = []
            for req in random.sample(self.requirements, len(self.requirements)):
                requirement = Requirement.objects.create(description=faker.text(
                ), name=req, points=random.randint(50, 1500), organization=organization)
                
                organization_requirements.append(requirement)

            self.stdout.write(f"Creating organization seniorities...")

            # Create seniorities
            organization_seniorities = []
            level = 1
            for sen in self.seniorities:
                seniority = Seniority.objects.create(
                    name=sen, organization=organization, level=level)
                organization_seniorities.append(seniority)
                level += 1

            self.stdout.write(f"Creating organization profiles...")

            # Create profiles
            organization_profiles = []
            for prof in random.sample(self.profiles, random.randint(1, len(self.profiles))):
                profile = Profile.objects.create(
                    name=prof, description=faker.text(), organization=organization)
                organization_profiles.append(profile)

            organization_profileseniorities = []
            for profile in organization_profiles:
                profilerequirements = organization_requirements.copy()
                self.stdout.write(f"Assinging seniorities to profile...")
                for seniority in organization_seniorities:
                    pokemonid = random.randint(1, 151)

                    while pokemonid in pokemons:
                        pokemonid = random.randint(1, 151)

                    pokemons.append(pokemonid)

                    pokemon, _ = Pokemon.objects.get_or_create(pk=pokemonid)
                    profileseniority = ProfileSeniority.objects.create(
                        profile=profile, seniority=seniority, pokemon=pokemon)
                    organization_profileseniorities.append(profileseniority)

                    self.stdout.write(
                        f"Assinging requirements to profilesseniority...")

                    # Adding requirements to profileseniorities
                    for requirement in random.sample(profilerequirements, len(profilerequirements)//len(organization_seniorities)):
                        ProfileSeniorityRequirement.objects.create(
                            profile_seniority=profileseniority, requirement=requirement)
                        profilerequirements.remove(requirement)

            self.stdout.write(f"Creating organization developers...")

            # Create developers
            organization_developers = []
            for i in range(1, random.randint(25, 50)):
                username = faker.user_name()
                while username in usernames:
                    username = faker.user_name()

                usernames.append(username)

                user = User.objects.create_user(
                    username=username, password=faker.password(), email=faker.email())
                developer = Developer.objects.create(
                    user=user,
                    organization=organization,
                    first_name=faker.first_name(),
                    last_name=faker.last_name(),
                    phone_number=faker.phone_number(),
                    birthday="2002-11-25",
                    score=random.randint(500, 100000))
                organization_developers.append(developer)

            self.stdout.write(f"Assinging profiles to developers...")

            organization_developerprofiles = []
            for developer in organization_developers:
                n = len(organization_profiles) if len(
                    organization_profiles) <= 4 else 4
                for profile in random.sample(organization_profiles, random.randint(1, n)):
                    seniority = random.choice(organization_seniorities)

                    # CREATE DEVELOPER PROFILE
                    developer_profile = DeveloperProfile.objects.create(
                        developer=developer, profile=profile, seniority=seniority)
                    organization_developerprofiles.append(developer_profile)

            if not is_my_organization:
                user = User.objects.create_user(
                    username=options["username"][0], password=options["password"][0], email=faker.email())
                admin = Admin.objects.create(
                    user=user, organization=organization)
                is_my_organization = True
                organization_developers.append(developer)
                self.stdout.write(
                    f"Creating your user admin... {options['username'][0]}")
