from django import forms
from piidb.models import (Addresses, Participants, TeacherSurvey)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import Tab, TabHolder, InlineRadios


class teacherSurveyForm(forms.ModelForm):

    class Meta:
        model = TeacherSurvey
        fields = "__all__"
        labels = {
            "teachersurveyid" : "Teacher Survey ID",
            "pguid" : "Participant ID",
            "teachername": "Teacher's Name",
            "teacherrole": "Teacher's Role",
        }

    readonly = ('teachersurveyid', 'pguid')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        CHOICES = (('0','Not True'), ('1', 'Somewhat True'), ('2', 'Very True'))
        self.fields['actstooyoung'] = forms.TypedChoiceField(
            label='1. Acts too young for his/her age.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['arguesalot'] = forms.TypedChoiceField(
            label='2. Argues a lot.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['failstofinish'] = forms.TypedChoiceField(
            label='3. Fails to finish things he/she starts.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['cantconcentrate'] = forms.TypedChoiceField(
            label='4. Can’t concentrate, can’t pay attention for long.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['cantsitstill'] = forms.TypedChoiceField(
            label='5. Can’t sit still, restless, or hyperactive.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['destroysproperty'] = forms.TypedChoiceField(
            label='6. Destroys property belonging to others.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['disobedient'] = forms.TypedChoiceField(
            label='7. Disobedient at school.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['feelsworthless'] = forms.TypedChoiceField(
            label='8. Feels worthless or inferior.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['impulsive'] = forms.TypedChoiceField(
            label='9. Impulsive or acts without thinking.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['fearful'] = forms.TypedChoiceField(
            label='10. Too fearful or anxious.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['guilty'] = forms.TypedChoiceField(
            label='11. Feels too guilty.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['selfconscious'] = forms.TypedChoiceField(
            label='12. Self-conscious or easily embarrassed.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['inattentive'] = forms.TypedChoiceField(
            label='13. Inattentive or easily distracted.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['stubborn'] = forms.TypedChoiceField(
            label='14. Stubborn, sullen, or irritable.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['temper'] = forms.TypedChoiceField(
            label='15. Temper tantrums or hot temper.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['threatens'] = forms.TypedChoiceField(
            label='16. Threatens people.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['unhappy'] = forms.TypedChoiceField(
            label='17. Unhappy, sad, or depressed.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )
        self.fields['worries'] = forms.TypedChoiceField(
            label='18. Worries.', widget=forms.RadioSelect(), choices=CHOICES, empty_value=0, coerce=int
        )

        for x in self.readonly:
            self.fields[x].widget.attrs['disabled'] = 'disabled'
            self.fields[x].required = False

        self.helper.layout = Layout(
            Row(
                Column('teachersurveyid', css_class='form-group col-md-4 mb-0'),
                Column('pguid', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('teachername', css_class='form-group col-md-4 mb-0'),
                Column('teacherrole', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('actstooyoung'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('arguesalot'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('failstofinish'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('cantconcentrate'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('cantsitstill'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('destroysproperty'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('disobedient'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('feelsworthless'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('impulsive'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('fearful'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('guilty'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('selfconscious'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('inattentive'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('stubborn'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('temper'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('threatens'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('unhappy'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Row(
                Column(InlineRadios('worries'),  css_class='form-group col-md-8 mb-0 '),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )

    def clean(self):
        data = super(teacherSurveyForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data


class participantForm(forms.ModelForm):

    class Meta:
        model = Participants
        fields = ('pguid', 'firstname', 'lastname', 'middlename','gender','dob','placeofbirth','phone1','email1',
                  'cotwin','nickname', 'legalfirstname', 'legalmiddlename','legallastname','status', 'enrolledstatus',
                  'expectedvisit','assentdate','alternateid','participantnotes', 'informantnotes','history',
                  'schoolname','teachername','bpmtvisit')
        labels = {
            "pguid" : "Participant ID",
            "firstname": "First Name at Birth",
            "middlename": "Middle Name at Birth",
            "lastname": "Last Name at Birth",
            "legalfirstname": "Legal First Name",
            "legalmiddlename": "legal Middle Name",
            "legallastname": "Legal Last Name",
            "gender": "Gender at Birth",
            "dob": "Birth Day",
            "placeofbirth": "Birth Place",
            'status': "Status",
            'enrolledstatus': "Current Status",
            'phone1': "Phone",
            'email1': "Email",
            'expectedvisit': "Expect Next Visit",
            'assentdate': "Baseline Visit Date",
            'alternateid': "Alternate ID",
            'participantnotes': "Participant Notes",
            'informantnotes': "Informant Notes",
            'history': "Visit History",
            'schoolname': "School Name",
            'teachername': "Teacher Name",
            'bpmtvisit': "BPM-T",
            'cotwin': "Co-Twin"
        }

    readonly = ('pguid','dob','gender','firstname','lastname','middlename','assentdate','alternateid','cotwin',
                'expectedvisit')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'


        self.fields['participantnotes'].widget = forms.Textarea()
        self.fields['informantnotes'].widget = forms.Textarea()
        self.fields['history'].widget = forms.Textarea()

        GENDER_AT_BIRTH = (('male','male'), ('female', 'female'))
        CO_TWIN = (('1','Yes'), ('2', 'No'))
        ENROLLEDSTATUS = (('1','Active'), ('2', 'Withdrawn'))

        self.fields['gender'] = forms.TypedChoiceField(
            label='Gender at Birth',
            widget=forms.RadioSelect(),
            choices=GENDER_AT_BIRTH,
            empty_value=0,
            coerce=int,
        )

        self.fields['cotwin'] = forms.TypedChoiceField(
            label='Co-Twin',
            widget=forms.RadioSelect(),
            choices=CO_TWIN,
            empty_value=0,
            coerce=int,
        )

        self.fields['enrolledstatus'] = forms.TypedChoiceField(
            label='Current Status',
            widget=forms.RadioSelect(),
            choices=ENROLLEDSTATUS,
            empty_value=0,
        )

        for x in self.readonly:
            self.fields[x].widget.attrs['disabled'] = 'disabled'
            self.fields[x].required = False

        self.helper.layout = Layout(

            TabHolder(
                Tab('Participant',
                    Row(
                        Column('pguid',  css_class='form-group col-md-6 mb-0'),
                        Column(InlineRadios('enrolledstatus'),  css_class='form-group col-md-6 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('firstname',  css_class='form-group col-md-4 mb-0'),
                        Column('middlename',  css_class='form-group col-md-4 mb-0'),
                        Column('lastname',  css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('dob',  css_class='form-group col-md-4 mb-0 '),
                        Column(InlineRadios('gender'),  css_class='form-group col-md-4 mb-0 '),
                        Column(InlineRadios('cotwin'),  css_class='form-group col-md-4 mb-0 '),
                        css_class='form-row'
                    ),
                    Row(
                        Column('legalfirstname',  css_class='form-group col-md-4 mb-0'),
                        Column('legalmiddlename',  css_class='form-group col-md-4 mb-0'),
                        Column('legallastname',  css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('nickname',   css_class='form-group col-md-4 mb-0'),
                        Column('phone1',  css_class='form-group col-md-4 mb-0'),
                        Column('email1',  css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('alternateid',  css_class='form-group col-md-4 mb-0'),
                        Column('assentdate',  css_class='form-group col-md-4 mb-0'),
                        Column('expectedvisit',  css_class='form-group col-md-4 mb-0'),
                         css_class='form-row'
                    ),
                    Row(
                        Column('participantnotes',   css_class='form-group col-md-12 mb-0'),
                        css_class='form-row'
                    ),
                    Submit('submit', 'Save')
                ),
            )
        )

    def clean(self):
        data = super(participantForm, self).clean()
        for x in self.readonly:
            data[x] = getattr(self.instance, x)
        return data


class participantNewForm(forms.ModelForm):

    class Meta:
        model = Participants
        fields = ('pguid', 'firstname', 'lastname', 'middlename','gender','dob','placeofbirth','phone1','email1',
                  'cotwin','nickname', 'legalfirstname', 'legalmiddlename','legallastname','status', 'enrolledstatus',
                  'expectedvisit','assentdate','alternateid','participantnotes', 'informantnotes','history',
                  'schoolname','teachername', 'bpmtvisit')
        labels = {
            "pguid" : "Participant ID",
            "firstname": "First Name at Birth",
            "middlename": "Middle Name at Birth",
            "lastname": "Last Name at Birth",
            "legalfirstname": "Legal First Name",
            "legalmiddlename": "legal Middle Name",
            "legallastname": "Legal Last Name",
            "gender": "Gender at Birth",
            "dob": "Birth Day",
            "placeofbirth": "Birth Place",
            'status': "Status",
            'enrolledstatus': "Current Status",
            'expectedvisit': "Expect Next Visit",
            'phone1': "Phone",
            'email1': "Email",
            'assentdate': "Baseline Visit Date",
            'alternateid': "Alternate ID",
            'participantnotes': "Participant Note",
            'informantnotes': "Informat Note",
            'history': "Visit History",
            'schoolname': "School Name",
            'teachername': "Teacher Name",
            'bpmtvisit': "BPM-T"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        GENDER_AT_BIRTH = (('1','male'), ('2', 'female'))
        CO_TWIN = (('1','Yes'), ('2', 'No'))
        ENROLLEDSTATUS = (('1','Active'), ('2', 'Withdrawn'))

        self.fields['gender'] = forms.TypedChoiceField(
            label='Gender Select',
            widget=forms.RadioSelect(),
            choices=GENDER_AT_BIRTH,
            empty_value=0,
            coerce=int,
        )

        self.fields['cotwin'] = forms.TypedChoiceField(
                    widget=forms.RadioSelect(),
                    choices=CO_TWIN,
                    empty_value=0,
                    coerce=int,
                )

        self.fields['enrolledstatus'] = forms.TypedChoiceField(
                    widget=forms.RadioSelect(),
                    choices=ENROLLEDSTATUS,
                    empty_value=0,
                    coerce=int,
        )

        #forms.RadioSelect(choices=GENDER_AT_BIRTH)
        self.fields['informantnotes'].widget = forms.Textarea()
        self.fields['history'].widget = forms.Textarea()

        self.helper.layout = Layout(
            TabHolder(
                Tab('Participant Information',
                    Row(
                        Column('pguid',  css_class='form-group col-md-6 mb-0'),
                        Column(InlineRadios('enrolledstatus'),  css_class='form-group col-md-6 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('firstname',  css_class='form-group col-md-4 mb-0'),
                        Column('middlename',  css_class='form-group col-md-4 mb-0'),
                        Column('lastname',  css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('dob',  css_class='form-group col-md-4 mb-0 '),
                        Column(InlineRadios('gender'),  css_class='form-group col-md-4 mb-0 '),
                        Column(InlineRadios('cotwin'),  css_class='form-group col-md-4 mb-0 '),
                        css_class='form-row'
                    ),
                    Row(
                        Column('legalfirstname',  css_class='form-group col-md-4 mb-0'),
                        Column('legalmiddlename',  css_class='form-group col-md-4 mb-0'),
                        Column('legallastname',  css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Row(
                        Column('nickname',   css_class='form-group col-md-4 mb-0'),
                        Column('phone1',  css_class='form-group col-md-4 mb-0'),
                        Column('email1',  css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Submit('submit', 'Save')
                )
            )
        )

    def clean(self):
        data = super(participantNewForm, self).clean()


class addressSelectForm(forms.ModelForm):

    class Meta:
        model = Addresses
        fields = "__all__"


class addressForm(forms.ModelForm):

    # address_search = forms.CharField( label="Search for address", max_length=200, widget=forms.TextInput(),required=False)

    class Meta:
        model = Addresses
        fields = "__all__"
        labels = {
            "addressid" : "Address ID",
            "streetnumber" : "Street Number",
            "streetname" : "Street Name",
            "aptnumber" : "Apt Number",
            "nearest": "Nearest cross street",
            "zipcode" : "ZipCode",
            "google_zipsuffix" : "Suffix",

            "google_neighborhood": "Neighborhood",
            "google_county": "County",
            "google_country": "Country",

            "google_place_id" : "Google Place ID",
            "google_latitude": "Latitude",
            "google_longitude": "Longitude",

            "google_query": "Search for address",
            "google_result": "Goole Maps Result",
        }

    # readonly = ('streetnumber', 'streetname', 'aptnumber', 'nearest', 'city', 'state', 'zipcode', 'google_place_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.fields['address_search'] = forms.CharField(label='Search for address', initial="", disabled=False, required=False)

        #for x in self.readonly:
            #self.fields[x].widget.attrs['disabled'] = 'disabled'
            #self.fields[x].required = False

        self.helper.layout = Layout(
            TabHolder(
                Tab('Address',
                    Row(
                        Column('google_query', css_class='form-group col-md-12 mb-0'),
                    ),
                    Row(
                        Column('addressid',  css_class='form-group col-md-6 mb-0'),
                        Column('google_place_id', css_class='form-group col-md-6 mb-0'),
                    ),
                    Row(
                        Column('streetnumber',  css_class='form-group col-md-3 mb-0'),
                        Column('streetname',  css_class='form-group col-md-6 mb-0'),
                        Column('aptnumber',  css_class='form-group col-md-3 mb-0'),
                    ),
                    Row(
                        Column('city',  css_class='form-group col-md-6 mb-0'),
                        Column('state',  css_class='form-group col-md-2 mb-0'),
                        Column('zipcode',  css_class='form-group col-md-2 mb-0'),
                        Column('google_zipsuffix',  css_class='form-group col-md-2 mb-0'),
                    ),
                    Submit('submit', 'Save')
                ),
                Tab('Details',
                    Row(
                        Column('google_result', css_class='form-group col-md-12 mb-0'),
                    ),
                    Row(
                        Column('nearest', css_class='form-group col-md-12 mb-0'),
                    ),
                    Row(
                        Column('google_neighborhood', css_class='form-group col-md-4 mb-0'),
                        Column('google_county', css_class='form-group col-md-4 mb-0'),
                        Column('google_country', css_class='form-group col-md-4 mb-0'),
                    ),
                    Row(
                        Column('google_latitude', css_class='form-group col-md-4 mb-0'),
                        Column('google_longitude', css_class='form-group col-md-4 mb-0'),
                    ),
                )
            )
        )

    def clean(self):
        data = super(addressForm, self).clean()

