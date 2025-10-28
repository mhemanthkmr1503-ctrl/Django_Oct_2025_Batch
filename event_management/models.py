from django.db import models


"""
Name -> CharField 60
EamilID -> CharField 155
Phone Number -> CharField 20
Issues -> Completed, In Progress, Yet to Start
"""

class IssueList(models.Model):
    issue_title = models.CharField(max_length=200)

class User(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=20)
    issue = models.ForeignKey(IssueList, on_delete=models.CASCADE)

