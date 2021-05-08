from django.db import models
from django.db.models import Q
from model_utils import Choices
from django.urls import reverse


ORDER_COLUMN_CHOICE_ADDRESS = Choices(
    ('0', 'addressid'),
    ('1', 'aptnumber'),
    ('2', 'city'),
    ('3', 'nearest'),
    ('4', 'state'),
    ('5', 'streetname'),
    ('6', 'streetnumber'),
    ('7', 'zipcode'),
    ('8', 'google_place_id')
)


def query_address_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICE_ADDRESS[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Addresses.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(addressid__icontains=search_value) |
                                        Q(streetname__icontains=search_value) |
                                        Q(streetnumber__icontains=search_value) |
                                        Q(zipcode__icontains=search_value) |
                                        Q(state__icontains=search_value))

    count = queryset.count()

    if length == -1:
        queryset = queryset.order_by(order_column)
    else:
        queryset = queryset.order_by(order_column)[start:start + length]

    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


# Create your models here.
class Addresses(models.Model):
    addressid = models.CharField(db_column='addressID', primary_key=True, max_length=32)  # Field name made lowercase.
    aptnumber = models.CharField(db_column='aptNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=32, blank=True, null=True)
    fromyear = models.CharField(db_column='fromYear', max_length=12, blank=True, null=True)  # Field name made lowercase.
    google_city = models.CharField(max_length=32, blank=True, null=True)
    google_country = models.CharField(max_length=32, blank=True, null=True)
    google_county = models.CharField(max_length=32, blank=True, null=True)
    google_date = models.CharField(max_length=32, blank=True, null=True)
    google_elevation = models.FloatField(blank=True, null=True)
    google_googlesenttoredcap = models.IntegerField(db_column='google_googleSentToREDCap', blank=True, null=True)  # Field name made lowercase.
    google_latitude = models.FloatField(blank=True, null=True)
    google_longitude = models.FloatField(blank=True, null=True)
    google_method = models.CharField(max_length=32, blank=True, null=True)
    google_neighborhood = models.CharField(max_length=64, blank=True, null=True)
    google_place_id = models.CharField(max_length=32, blank=True, null=True)
    google_query = models.CharField(max_length=512, blank=True, null=True)
    google_result = models.CharField(max_length=512, blank=True, null=True)
    google_state = models.CharField(max_length=32, blank=True, null=True)
    google_status = models.CharField(max_length=32, blank=True, null=True)
    google_streetname = models.CharField(db_column='google_streetName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    google_streetnumber = models.CharField(db_column='google_streetNumber', max_length=12, blank=True, null=True)  # Field name made lowercase.
    google_zipcode = models.CharField(db_column='google_zipCode', max_length=12, blank=True, null=True)  # Field name made lowercase.
    google_zipsuffix = models.CharField(db_column='google_zipSuffix', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nearest = models.CharField(max_length=32, blank=True, null=True)
    percentoftime = models.IntegerField(db_column='percentOfTime', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    streetname = models.CharField(db_column='streetName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    streetnumber = models.CharField(db_column='streetNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    toyear = models.CharField(db_column='toYear', max_length=32, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='zipCode', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'addresses'

    def get_absolute_url(self): # new
        return reverse('addressView', args=[str(self.addressid)])

    def __str__(self):
        return self.addressid


class Participants(models.Model):
    ##id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    #id = models.AutoField(primary_key=True)
    pguid = models.CharField(db_column='pGUID', primary_key=True, max_length=32, default='TEST')  # Field name made lowercase.
    enrolledstatus = models.CharField(db_column='enrolledStatus', max_length=12, blank=True, null=True)  # Field name made lowercase.
    expectedvisit = models.CharField(db_column='expectedVisit', max_length=32, blank=True, null=True)  # Field name made lowercase.
    assentdate = models.DateTimeField(db_column='assentDate', blank=True, null=True)  # Field name made lowercase.
    alternateid = models.CharField(db_column='alternateID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nda_guid = models.BigIntegerField(db_column='NDA_GUID', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    legalfirstname = models.CharField(db_column='legalfirstName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    legalmiddlename = models.CharField(db_column='legalmiddleName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    legallastname = models.CharField(db_column='legallastName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='nickName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=12, blank=True, null=True)
    dob = models.CharField(max_length=12, blank=True, null=True)
    placeofbirth = models.CharField(db_column='placeOfBirth', max_length=128, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(max_length=12, blank=True, null=True)
    phone2 = models.CharField(max_length=12, blank=True, null=True)
    phone3 = models.CharField(max_length=12, blank=True, null=True)
    participantnotes = models.CharField(db_column='participantNotes', max_length=512, blank=True, null=True)  # Field name made lowercase.
    informantnotes = models.CharField(db_column='informantNotes', max_length=512, blank=True, null=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='schoolName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    otherschoolid = models.CharField(db_column='otherSchoolID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    otherschoolname = models.CharField(db_column='otherSchoolName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    teachername = models.CharField(db_column='teacherName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    teacheremail = models.EmailField(db_column='teacherEmail', max_length=64, blank=True, null=True)  # Field name made lowercase.
    entrytype = models.CharField(db_column='entryType', max_length=12, blank=True, null=True)  # Field name made lowercase.
    deletemark = models.CharField(db_column='deleteMark', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nopastresidences = models.CharField(db_column='noPastResidences', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cotwin = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    score = models.BigIntegerField(blank=True, null=True)
    contactid = models.CharField(db_column='contactID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    contactid2 = models.CharField(db_column='contactID2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    contactid3 = models.CharField(db_column='contactID3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bpmtvisit = models.CharField(db_column='bpmtVisit', max_length=32, blank=True, null=True)  # Field name made lowercase.
    history = models.CharField(max_length=1024, blank=True, null=True)
    contactmethod = models.CharField(db_column='contactMethod', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recruitmentmethod = models.CharField(db_column='recruitmentMethod', max_length=128, blank=True, null=True)  # Field name made lowercase.
    noyouthcontactcheckbox = models.CharField(db_column='noYouthContactCheckbox', max_length=12, blank=True, null=True)  # Field name made lowercase.
    contact1legalguardiancheckbox = models.CharField(db_column='contact1LegalGuardianCheckbox', max_length=12, blank=True, null=True)  # Field name made lowercase.
    contact2legalguardiancheckbox = models.CharField(db_column='contact2LegalGuardianCheckbox', max_length=12, blank=True, null=True)  # Field name made lowercase.
    altcontact1legalguardiancheckbox = models.CharField(db_column='altContact1LegalGuardianCheckbox', max_length=12, blank=True, null=True)  # Field name made lowercase.
    altcontact2legalguardiancheckbox = models.CharField(db_column='altContact2LegalGuardianCheckbox', max_length=12, blank=True, null=True)  # Field name made lowercase.
    altcontact3legalguardiancheckbox = models.CharField(db_column='altContact3LegalGuardianCheckbox', max_length=12, blank=True, null=True)  # Field name made lowercase.
    locatorparentnotes = models.CharField(db_column='locatorParentNotes', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    email1 = models.EmailField(max_length=128, blank=True, null=True)
    phone1fitbit = models.CharField(db_column='phone1Fitbit', max_length=12, blank=True, null=True)  # Field name made lowercase.
    email1fitbit = models.EmailField(db_column='email1Fitbit', max_length=128, blank=True, null=True)  # Field name made lowercase.
    current_site = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participants'


    def get_absolute_url(self): # new
        return reverse('participantView', args=[str(self.pguid)])

    def __str__(self):
        return self.pguid


class ParticipantsAddresses(models.Model):
    address_id = models.CharField(max_length=64, blank=True, null=True)
    pguid = models.ForeignKey('Participants', models.DO_NOTHING)
    addresstype = models.CharField(db_column='addressType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    from_year = models.IntegerField(blank=True, null=True)
    to_year = models.IntegerField(blank=True, null=True)
    google_place_id = models.CharField(max_length=64, blank=True, null=True)
    percentoftime = models.IntegerField(db_column='percentOfTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participants_addresses'

        unique_together = (('address_id', 'pguid', 'from_year', 'to_year'),)


class SchoolLists(models.Model):
    district_id = models.BigIntegerField(db_column='DISTRICT_ID', blank=True, null=True)
    school_id = models.BigIntegerField(db_column='SCH_ID', blank=True, null=True)
    nces_id = models.BigIntegerField(db_column='NCES_ID', primary_key=True)
    school_name = models.TextField(db_column='SCHOOL_NAME', blank=True, null=True)
    district_name = models.TextField(db_column='DISTRICT_NAME', blank=True, null=True)
    city = models.TextField(db_column='CITY', blank=True, null=True)
    state = models.TextField(db_column='STATE', blank=True, null=True)
    zip = models.BigIntegerField(db_column='ZIP', blank=True, null=True)
    street = models.TextField(db_column='STREET', blank=True, null=True)
    level = models.TextField(db_column='LEVEL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_lists'


class Sites(models.Model):
    name = models.CharField(max_length=128)
    numTargetPart = models.IntegerField()
    state = models.CharField(max_length=12)
    logo = models.CharField(max_length=128, blank=True, null=True)
    emails = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sites'


class TeacherSurvey(models.Model):
    teachersurveyid = models.CharField(db_column='teacherSurveyID', primary_key=True, max_length=32)  # Field name made lowercase.
    actstooyoung = models.IntegerField(db_column='actsTooYoung', blank=True, null=True)  # Field name made lowercase.
    arguesalot = models.IntegerField(db_column='arguesALot', blank=True, null=True)  # Field name made lowercase.
    bpmtdirty = models.CharField(db_column='bpmtDirty', max_length=64, blank=True, null=True)  # Field name made lowercase.
    cantconcentrate = models.CharField(db_column='cantConcentrate', max_length=64, blank=True, null=True)  # Field name made lowercase.
    cantsitstill = models.IntegerField(db_column='cantSitStill', blank=True, null=True)  # Field name made lowercase.
    destroysproperty = models.IntegerField(db_column='destroysProperty', blank=True, null=True)  # Field name made lowercase.
    disobedient = models.IntegerField(blank=True, null=True)
    failstofinish = models.IntegerField(db_column='failsToFinish', blank=True, null=True)  # Field name made lowercase.
    fearful = models.IntegerField(blank=True, null=True)
    feelsworthless = models.IntegerField(db_column='feelsWorthless', blank=True, null=True)  # Field name made lowercase.
    guilty = models.IntegerField(blank=True, null=True)
    impulsive = models.IntegerField(blank=True, null=True)
    inattentive = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=512, blank=True, null=True)
    numdays = models.IntegerField(db_column='numDays', blank=True, null=True)  # Field name made lowercase.
    pguid = models.ForeignKey(Participants, models.DO_NOTHING, db_column='pGUID', blank=True, null=True)  # Field name made lowercase.
    school = models.CharField(max_length=128, blank=True, null=True)
    selfconscious = models.IntegerField(db_column='selfConscious', blank=True, null=True)  # Field name made lowercase.
    serverdate = models.CharField(max_length=32, blank=True, null=True)
    sessionid = models.CharField(db_column='sessionID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    stubborn = models.IntegerField(blank=True, null=True)
    teachername = models.CharField(db_column='teacherName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    teacherrole = models.CharField(db_column='teacherRole', max_length=32, blank=True, null=True)  # Field name made lowercase.
    temper = models.IntegerField(blank=True, null=True)
    threatens = models.IntegerField(blank=True, null=True)
    unhappy = models.IntegerField(blank=True, null=True)
    visit = models.CharField(max_length=32, blank=True, null=True)
    worries = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'teacher_survey'
