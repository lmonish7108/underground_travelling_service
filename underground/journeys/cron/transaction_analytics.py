import os
import requests

from aws_requests_auth.aws_auth import AWSRequestsAuth
from django_cron import CronJobBase, Schedule

from journeys.services import journey


def get_aws_auth():
    return AWSRequestsAuth(aws_access_key=os.getenv('AWS_ACCESS_KEY'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
                           aws_host=os.getenv('AWS_HOST'),
                           aws_region=os.getenv('AWS_REGION'),
                           aws_service='execute-api')


class JourneyUpload(CronJobBase):
    RUN_EVERY_MINS = 60 # every 5 minutes
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transaction_analytics.journey_upload'    # a unique code


    def do(self):
        journeys = journey.Journey.all_journey_data(
                columns=['origin__name', 'destination__name', 'journey_type']
            )

        requests.post(url='https://ar2bnaq6dd.execute-api.eu-west-2.amazonaws.com/prod/upload', json=journeys, auth=get_aws_auth())


class JourneyPaymentUpload(CronJobBase):
    RUN_EVERY_MINS = 60 # every 5 minutes
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transaction_analytics.journey_payment_upload'    # a unique code


    def do(self):
        journeys = journey.Journey.all_journey_data(
                columns=['origin__name', 'destination__name', 'journey_type']
            )
