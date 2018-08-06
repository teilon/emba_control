from django.db import models


class ProductSet(models.Model):

    m1 = models.IntegerField(default=0)
    m2 = models.IntegerField(default=0)
    m3 = models.IntegerField(default=0)
    m4 = models.IntegerField(default=0)
    m5 = models.IntegerField(default=0)
    m6 = models.IntegerField(default=0)
    m7 = models.IntegerField(default=0)
    m8 = models.IntegerField(default=0)
    m9 = models.IntegerField(default=0)
    m10 = models.IntegerField(default=0)
    w1 = models.IntegerField(default=0)
    w2 = models.IntegerField(default=0)
    w3 = models.IntegerField(default=0)
    w4 = models.IntegerField(default=0)
    w5 = models.IntegerField(default=0)
    w6 = models.IntegerField(default=0)
    w7 = models.IntegerField(default=0)
    w8 = models.IntegerField(default=0)
    w9 = models.IntegerField(default=0)
    w10 = models.IntegerField(default=0)

    # shelf
    ms = models.IntegerField(default=0)
    ws = models.IntegerField(default=0)
    ds = models.IntegerField(default=0)

    # tample
    mt = models.IntegerField(default=0)
    wt = models.IntegerField(default=0)


class EventStatusSet(models.Model):

    NO_EVENT = 'NE'
    TO_DILER = 'TD'
    TO_STORAGE = 'TS'
    TO_PERSON = 'TP'
    TO_MARKET = 'TM'
    RETURN_FROM_DILER = 'FD'
    RETURN_FROM_PERSON= 'FP'
    RETURN_FROM_MARKET = 'FM'
    EVENT_STATUS_CHOICES = (
        (NO_EVENT, 'no event'),
        (TO_DILER, 'to diler'),
        (TO_STORAGE, 'to storage'),
        (TO_PERSON, 'to person'),
        (TO_MARKET, 'to_market'),
        (RETURN_FROM_DILER, 'return from diler'),
        (RETURN_FROM_PERSON, 'return from person'),
        (RETURN_FROM_MARKET, 'return from market'),
    )
    event_status = models.CharField(max_length=2,
                                    choices=EVENT_STATUS_CHOICES,
                                    default=NO_EVENT)

    name = models.CharField(max_length=50)


class PartnerStatusSet(models.Model):
    name = models.CharField(max_length=50)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


class Partner(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    status_id = models.ForeignKey(PartnerStatusSet, on_delete=models.CASCADE)


class Request(models.Model):
    product_id = models.ForeignKey(ProductSet, on_delete=models.CASCADE)
    partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
    status_id = models.ForeignKey(EventStatusSet, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)


class Transaction(models.Model):
    date = models.DateTimeField()
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)


class Storage(models.Model):
    product_id = models.ForeignKey(ProductSet, on_delete=models.CASCADE)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)


# class Traider(models.Model):
# partner_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
# coverage_id = models.ForeignKey(CoveragePointSet, on_delete=models.CASCADE)


# class Coverage(models.Model):
# point = models.CharField(max_length=50)
# coverage_name = models.CharField(max_length=50)


# class CoveragePointSet(models.Model):
# coverage_id = models.ForeignKey(Partner, on_delete=models.CASCADE)
# point_id = models.ForeignKey(Point, on_delete=models.CASCADE)


# class Point(models.Model):
# name = models.CharField(max_length=50)
 