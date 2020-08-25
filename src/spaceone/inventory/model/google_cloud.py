from schematics import Model
from schematics.types import ModelType, StringType, BooleanType, ListType, DictType


# class (Model):
#     key = StringType()
#     value = StringType()


class Scheduling(Model):
    on_host_maintenance = StringType(default="MIGRATE")
    automatic_restart = BooleanType(default=True)
    preemptible = BooleanType(default=False)


class GoogleCloud(Model):
    self_link = StringType()
    fingerprint = StringType()
    reservation_affinity = StringType(default="ANY_RESERVATION")
    deletion_protection = BooleanType(default=False)
    scheduling = ModelType(Scheduling)
     = DictType(StringType, default={}, serialize_when_none=False)
