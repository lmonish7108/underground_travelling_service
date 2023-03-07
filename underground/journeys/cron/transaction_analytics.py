import json
import os
import requests

from django_cron import CronJobBase, Schedule

from journeys.services import journey


class JourneyUpload(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transaction_analytics.journey_upload'    # a unique code

    def do(self):
        journeys = journey.Journey.all_journey_data(
                columns=['id', 'origin__name', 'destination__name', 
                         'journey_type', 'metro_card_id',
                         'metro_card__userprofile_id', 'metro_card__userprofile__age']
            )
        if journeys:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post(url=os.getenv('LAMBDA_URL'), data=json.dumps(list(journeys)), headers=headers)


class JourneyPaymentUpload(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transaction_analytics.journey_payment_upload'    # a unique code


    def do(self):
        journey_payments = journey.Journey.all_journey_payment_data(
                columns=['id', 'journey_id', 'price']
            )
        if journey_payments:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post(url=os.getenv('LAMBDA_URL'), data=json.dumps(list(journey_payments)), headers=headers)
