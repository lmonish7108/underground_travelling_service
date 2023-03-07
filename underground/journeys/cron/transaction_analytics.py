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
                         'journey_type', 'metro_card_id', 'timestamp',
                         'metro_card__userprofile_id', 'metro_card__userprofile__age']
            )

        requests.post(url=os.getenv('LAMBDA_URL'), data=json.dumps(journeys))


class JourneyPaymentUpload(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'transaction_analytics.journey_payment_upload'    # a unique code


    def do(self):
        journey_payments = journey.Journey.all_journey_payment_data(
                columns=['id', 'journey_id', 'price']
            )
        requests.post(url=os.getenv('LAMBDA_URL'), data=json.dumps(journey_payments))
