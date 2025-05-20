from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link        = models.URLField(blank=True)

    def __str__(self):
        return self.title

class CV(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=30)
    bio       = models.TextField()
    # many-to-many to normalized tables
    skills   = models.ManyToManyField(Skill, related_name="cvs", blank=True)
    projects = models.ManyToManyField(Project, related_name="cvs", blank=True)
    # contacts as JSON for flexibility
    contacts = models.JSONField(
        help_text="e.g. {'email':'you@me.com','phone':'123-456'}"
    )

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
