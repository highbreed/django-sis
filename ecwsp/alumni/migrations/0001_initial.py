# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'College'
        db.create_table('alumni_college', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
        ))
        db.send_create_signal('alumni', ['College'])

        # Adding model 'CollegeEnrollment'
        db.create_table('alumni_collegeenrollment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('search_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('college', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.College'])),
            ('program_years', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('begin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('graduated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('graduation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('degree_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('alumni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.Alumni'])),
            ('college_sequence', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('alumni', ['CollegeEnrollment'])

        # Adding model 'AlumniStatus'
        db.create_table('alumni_alumnistatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('alumni', ['AlumniStatus'])

        # Adding model 'Withdrawl'
        db.create_table('alumni_withdrawl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('college', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.College'])),
            ('alumni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.Alumni'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('semesters', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True)),
            ('from_enrollment', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('alumni', ['Withdrawl'])

        # Adding model 'AlumniNoteCategory'
        db.create_table('alumni_alumninotecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('alumni', ['AlumniNoteCategory'])

        # Adding model 'AlumniNote'
        db.create_table('alumni_alumninote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.AlumniNoteCategory'], null=True, blank=True)),
            ('note', self.gf('ckeditor.fields.RichTextField')()),
            ('alumni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.Alumni'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal('alumni', ['AlumniNote'])

        # Adding model 'AlumniAction'
        db.create_table('alumni_alumniaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal('alumni', ['AlumniAction'])

        # Adding M2M table for field alumni on 'AlumniAction'
        db.create_table('alumni_alumniaction_alumni', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('alumniaction', models.ForeignKey(orm['alumni.alumniaction'], null=False)),
            ('alumni', models.ForeignKey(orm['alumni.alumni'], null=False))
        ))
        db.create_unique('alumni_alumniaction_alumni', ['alumniaction_id', 'alumni_id'])

        # Adding model 'AlumniEmail'
        db.create_table('alumni_alumniemail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alumni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.Alumni'])),
        ))
        db.send_create_signal('alumni', ['AlumniEmail'])

        # Adding model 'AlumniPhoneNumber'
        db.create_table('alumni_alumniphonenumber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('alumni', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.Alumni'])),
        ))
        db.send_create_signal('alumni', ['AlumniPhoneNumber'])

        # Adding model 'Alumni'
        db.create_table('alumni_alumni', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sis.Student'], unique=True)),
            ('college', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='college_student', null=True, to=orm['alumni.College'])),
            ('graduated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('graduation_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('college_override', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['alumni.AlumniStatus'], null=True, blank=True)),
            ('program_years', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('semesters', self.gf('django.db.models.fields.CharField')(max_length='5', blank=True)),
            ('on_track', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('alumni', ['Alumni'])


    def backwards(self, orm):
        # Deleting model 'College'
        db.delete_table('alumni_college')

        # Deleting model 'CollegeEnrollment'
        db.delete_table('alumni_collegeenrollment')

        # Deleting model 'AlumniStatus'
        db.delete_table('alumni_alumnistatus')

        # Deleting model 'Withdrawl'
        db.delete_table('alumni_withdrawl')

        # Deleting model 'AlumniNoteCategory'
        db.delete_table('alumni_alumninotecategory')

        # Deleting model 'AlumniNote'
        db.delete_table('alumni_alumninote')

        # Deleting model 'AlumniAction'
        db.delete_table('alumni_alumniaction')

        # Removing M2M table for field alumni on 'AlumniAction'
        db.delete_table('alumni_alumniaction_alumni')

        # Deleting model 'AlumniEmail'
        db.delete_table('alumni_alumniemail')

        # Deleting model 'AlumniPhoneNumber'
        db.delete_table('alumni_alumniphonenumber')

        # Deleting model 'Alumni'
        db.delete_table('alumni_alumni')


    models = {
        'alumni.alumni': {
            'Meta': {'object_name': 'Alumni'},
            'college': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'college_student'", 'null': 'True', 'to': "orm['alumni.College']"}),
            'college_override': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'graduated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'graduation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'on_track': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'program_years': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'semesters': ('django.db.models.fields.CharField', [], {'max_length': "'5'", 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.AlumniStatus']", 'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sis.Student']", 'unique': 'True'}),
            'withdrawls': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['alumni.College']", 'through': "orm['alumni.Withdrawl']", 'symmetrical': 'False'})
        },
        'alumni.alumniaction': {
            'Meta': {'object_name': 'AlumniAction'},
            'alumni': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['alumni.Alumni']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        'alumni.alumniemail': {
            'Meta': {'object_name': 'AlumniEmail'},
            'alumni': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.Alumni']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'alumni.alumninote': {
            'Meta': {'object_name': 'AlumniNote'},
            'alumni': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.Alumni']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.AlumniNoteCategory']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('ckeditor.fields.RichTextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        'alumni.alumninotecategory': {
            'Meta': {'object_name': 'AlumniNoteCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'alumni.alumniphonenumber': {
            'Meta': {'object_name': 'AlumniPhoneNumber'},
            'alumni': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.Alumni']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'alumni.alumnistatus': {
            'Meta': {'ordering': "['name']", 'object_name': 'AlumniStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'alumni.college': {
            'Meta': {'ordering': "['name']", 'object_name': 'College'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        'alumni.collegeenrollment': {
            'Meta': {'object_name': 'CollegeEnrollment'},
            'alumni': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.Alumni']"}),
            'begin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.College']"}),
            'college_sequence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'degree_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'graduated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'graduation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'program_years': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'search_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'alumni.withdrawl': {
            'Meta': {'object_name': 'Withdrawl'},
            'alumni': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.Alumni']"}),
            'college': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['alumni.College']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'from_enrollment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semesters': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sis.cohort': {
            'Meta': {'object_name': 'Cohort'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['sis.Student']", 'null': 'True', 'db_table': "'sis_studentcohort'", 'blank': 'True'})
        },
        'sis.emergencycontact': {
            'Meta': {'ordering': "('primary_contact', 'emergency_only', 'lname')", 'object_name': 'EmergencyContact'},
            'city': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'emergency_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'primary_contact': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'relationship_to_student': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'sis.gradelevel': {
            'Meta': {'ordering': "('id',)", 'object_name': 'GradeLevel'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'sis.languagechoice': {
            'Meta': {'object_name': 'LanguageChoice'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'sis.mdluser': {
            'Meta': {'ordering': "('lname', 'fname')", 'object_name': 'MdlUser'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '360', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'sis.reasonleft': {
            'Meta': {'object_name': 'ReasonLeft'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'sis.student': {
            'Meta': {'ordering': "('lname', 'fname')", 'object_name': 'Student', '_ormbases': ['sis.MdlUser']},
            'alert': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'alt_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'bday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cache_cohort': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cache_cohorts'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['sis.Cohort']"}),
            'cache_gpa': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'cohorts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sis.Cohort']", 'symmetrical': 'False', 'through': "orm['sis.StudentCohort']", 'blank': 'True'}),
            'date_dismissed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'emergency_contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sis.EmergencyContact']", 'symmetrical': 'False', 'blank': 'True'}),
            'family_preferred_language': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['sis.LanguageChoice']", 'null': 'True', 'blank': 'True'}),
            'grad_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'individual_education_program': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mdluser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sis.MdlUser']", 'unique': 'True', 'primary_key': 'True'}),
            'mname': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'parent_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'parent_guardian': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'pic': ('ecwsp.sis.thumbs.ImageWithThumbsField', [], {'blank': 'True', 'max_length': '100', 'null': 'True', 'sizes': '((70, 65), (530, 400))'}),
            'reason_left': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sis.ReasonLeft']", 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'siblings': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sis.Student']", 'symmetrical': 'False', 'blank': 'True'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'unique_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sis.GradeLevel']", 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        'sis.studentcohort': {
            'Meta': {'object_name': 'StudentCohort', 'managed': 'False'},
            'cohort': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sis.Cohort']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sis.Student']"})
        }
    }

    complete_apps = ['alumni']