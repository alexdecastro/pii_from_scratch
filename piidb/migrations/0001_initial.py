# Generated by Django 3.2 on 2021-04-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('pguid', models.CharField(db_column='pGUID', default='TEST', max_length=32, primary_key=True, serialize=False)),
                ('enrolledstatus', models.CharField(blank=True, db_column='enrolledStatus', max_length=12, null=True)),
                ('expectedvisit', models.CharField(blank=True, db_column='expectedVisit', max_length=32, null=True)),
                ('assentdate', models.DateTimeField(blank=True, db_column='assentDate', null=True)),
                ('alternateid', models.CharField(blank=True, db_column='alternateID', max_length=32, null=True)),
                ('nda_guid', models.BigIntegerField(blank=True, db_column='NDA_GUID', null=True)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=64, null=True)),
                ('middlename', models.CharField(blank=True, db_column='middleName', max_length=64, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=64, null=True)),
                ('legalfirstname', models.CharField(blank=True, db_column='legalfirstName', max_length=64, null=True)),
                ('legalmiddlename', models.CharField(blank=True, db_column='legalmiddleName', max_length=64, null=True)),
                ('legallastname', models.CharField(blank=True, db_column='legallastName', max_length=64, null=True)),
                ('nickname', models.CharField(blank=True, db_column='nickName', max_length=64, null=True)),
                ('gender', models.CharField(blank=True, max_length=12, null=True)),
                ('dob', models.CharField(blank=True, max_length=12, null=True)),
                ('placeofbirth', models.CharField(blank=True, db_column='placeOfBirth', max_length=128, null=True)),
                ('phone1', models.CharField(blank=True, max_length=12, null=True)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
                ('phone3', models.CharField(blank=True, max_length=12, null=True)),
                ('participantnotes', models.CharField(blank=True, db_column='participantNotes', max_length=512, null=True)),
                ('informantnotes', models.CharField(blank=True, db_column='informantNotes', max_length=512, null=True)),
                ('schoolname', models.CharField(blank=True, db_column='schoolName', max_length=128, null=True)),
                ('otherschoolid', models.CharField(blank=True, db_column='otherSchoolID', max_length=128, null=True)),
                ('otherschoolname', models.CharField(blank=True, db_column='otherSchoolName', max_length=128, null=True)),
                ('teachername', models.CharField(blank=True, db_column='teacherName', max_length=64, null=True)),
                ('teacheremail', models.EmailField(blank=True, db_column='teacherEmail', max_length=64, null=True)),
                ('entrytype', models.CharField(blank=True, db_column='entryType', max_length=12, null=True)),
                ('deletemark', models.CharField(blank=True, db_column='deleteMark', max_length=12, null=True)),
                ('nopastresidences', models.CharField(blank=True, db_column='noPastResidences', max_length=32, null=True)),
                ('cotwin', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
                ('score', models.BigIntegerField(blank=True, null=True)),
                ('contactid', models.CharField(blank=True, db_column='contactID', max_length=32, null=True)),
                ('contactid2', models.CharField(blank=True, db_column='contactID2', max_length=32, null=True)),
                ('contactid3', models.CharField(blank=True, db_column='contactID3', max_length=32, null=True)),
                ('bpmtvisit', models.CharField(blank=True, db_column='bpmtVisit', max_length=32, null=True)),
                ('history', models.CharField(blank=True, max_length=1024, null=True)),
                ('contactmethod', models.CharField(blank=True, db_column='contactMethod', max_length=128, null=True)),
                ('recruitmentmethod', models.CharField(blank=True, db_column='recruitmentMethod', max_length=128, null=True)),
                ('noyouthcontactcheckbox', models.CharField(blank=True, db_column='noYouthContactCheckbox', max_length=12, null=True)),
                ('contact1legalguardiancheckbox', models.CharField(blank=True, db_column='contact1LegalGuardianCheckbox', max_length=12, null=True)),
                ('contact2legalguardiancheckbox', models.CharField(blank=True, db_column='contact2LegalGuardianCheckbox', max_length=12, null=True)),
                ('altcontact1legalguardiancheckbox', models.CharField(blank=True, db_column='altContact1LegalGuardianCheckbox', max_length=12, null=True)),
                ('altcontact2legalguardiancheckbox', models.CharField(blank=True, db_column='altContact2LegalGuardianCheckbox', max_length=12, null=True)),
                ('altcontact3legalguardiancheckbox', models.CharField(blank=True, db_column='altContact3LegalGuardianCheckbox', max_length=12, null=True)),
                ('locatorparentnotes', models.CharField(blank=True, db_column='locatorParentNotes', max_length=1024, null=True)),
                ('email1', models.EmailField(blank=True, max_length=128, null=True)),
                ('phone1fitbit', models.CharField(blank=True, db_column='phone1Fitbit', max_length=12, null=True)),
                ('email1fitbit', models.EmailField(blank=True, db_column='email1Fitbit', max_length=128, null=True)),
                ('current_site', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'participants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParticipantsAddresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.CharField(blank=True, max_length=64, null=True)),
                ('addresstype', models.CharField(blank=True, db_column='addressType', max_length=32, null=True)),
                ('from_year', models.IntegerField(blank=True, null=True)),
                ('to_year', models.IntegerField(blank=True, null=True)),
                ('google_place_id', models.CharField(blank=True, max_length=64, null=True)),
                ('percentoftime', models.IntegerField(blank=True, db_column='percentOfTime', null=True)),
            ],
            options={
                'db_table': 'participants_addresses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolLists',
            fields=[
                ('district_id', models.BigIntegerField(blank=True, db_column='DISTRICT_ID', null=True)),
                ('school_id', models.BigIntegerField(blank=True, db_column='SCH_ID', null=True)),
                ('nces_id', models.BigIntegerField(db_column='NCES_ID', primary_key=True, serialize=False)),
                ('school_name', models.TextField(blank=True, db_column='SCHOOL_NAME', null=True)),
                ('district_name', models.TextField(blank=True, db_column='DISTRICT_NAME', null=True)),
                ('city', models.TextField(blank=True, db_column='CITY', null=True)),
                ('state', models.TextField(blank=True, db_column='STATE', null=True)),
                ('zip', models.BigIntegerField(blank=True, db_column='ZIP', null=True)),
                ('street', models.TextField(blank=True, db_column='STREET', null=True)),
                ('level', models.TextField(blank=True, db_column='LEVEL', null=True)),
            ],
            options={
                'db_table': 'school_lists',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('numTargetPart', models.IntegerField()),
                ('state', models.CharField(max_length=12)),
                ('logo', models.CharField(blank=True, max_length=128, null=True)),
                ('emails', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('addressid', models.CharField(db_column='addressID', max_length=32, primary_key=True, serialize=False)),
                ('aptnumber', models.CharField(blank=True, db_column='aptNumber', max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('fromyear', models.CharField(blank=True, db_column='fromYear', max_length=12, null=True)),
                ('google_city', models.CharField(blank=True, max_length=32, null=True)),
                ('google_country', models.CharField(blank=True, max_length=32, null=True)),
                ('google_county', models.CharField(blank=True, max_length=32, null=True)),
                ('google_date', models.CharField(blank=True, max_length=32, null=True)),
                ('google_elevation', models.FloatField(blank=True, null=True)),
                ('google_googlesenttoredcap', models.IntegerField(blank=True, db_column='google_googleSentToREDCap', null=True)),
                ('google_latitude', models.FloatField(blank=True, null=True)),
                ('google_longitude', models.FloatField(blank=True, null=True)),
                ('google_method', models.CharField(blank=True, max_length=32, null=True)),
                ('google_neighborhood', models.CharField(blank=True, max_length=64, null=True)),
                ('google_place_id', models.CharField(blank=True, max_length=32, null=True)),
                ('google_query', models.CharField(blank=True, max_length=512, null=True)),
                ('google_result', models.CharField(blank=True, max_length=512, null=True)),
                ('google_state', models.CharField(blank=True, max_length=32, null=True)),
                ('google_status', models.CharField(blank=True, max_length=32, null=True)),
                ('google_streetname', models.CharField(blank=True, db_column='google_streetName', max_length=128, null=True)),
                ('google_streetnumber', models.CharField(blank=True, db_column='google_streetNumber', max_length=12, null=True)),
                ('google_zipcode', models.CharField(blank=True, db_column='google_zipCode', max_length=12, null=True)),
                ('google_zipsuffix', models.CharField(blank=True, db_column='google_zipSuffix', max_length=12, null=True)),
                ('nearest', models.CharField(blank=True, max_length=32, null=True)),
                ('percentoftime', models.IntegerField(blank=True, db_column='percentOfTime', null=True)),
                ('state', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
                ('streetname', models.CharField(blank=True, db_column='streetName', max_length=128, null=True)),
                ('streetnumber', models.CharField(blank=True, db_column='streetNumber', max_length=32, null=True)),
                ('toyear', models.CharField(blank=True, db_column='toYear', max_length=32, null=True)),
                ('zipcode', models.CharField(blank=True, db_column='zipCode', max_length=12, null=True)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
    ]
