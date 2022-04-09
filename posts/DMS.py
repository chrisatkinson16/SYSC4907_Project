"""
import csv
import json
import os
import time
from datetime import datetime

import pytz
import requests
from neomodel import db

from src.decisions.metric import Metric
from src.decisions.rule import Rule
from src.decisions.rules.SmartGardenRules import get_rules
from src.decisions.rules.enums.ComparisonEnum import ComparisonEnum
from src.decisions.rules.enums.DataTypeEnum import DataTypeEnum
from src.decisions.rules.enums.GardenDataEnum import GardenDataEnum
from src.decisions.rules.enums.WeatherDataEnum import WeatherDataEnum
from api.models import ForecastRecord, PlantRecord, DecisionRecord
from src.server.parser import get_labels_and_keywords

light_rain_threshold = 1
medium_rain_threshold = 10
heavy_rain_threshold = 25
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
NO_CHANGE_NEEDED = "No change needed."


def load_plant_preferences(plant, label):
    f = open('plantpref.json')
    data = json.load(f)
    plant_pref = data["Preferences"][plant][label]
    f.close()
    return plant_pref


def alert_present(alerts):
    if alerts:
        print(alerts)
        dt_start = datetime.fromtimestamp(alerts["start"], pytz.timezone('Canada/Eastern')).ctime()
        dt_end = datetime.fromtimestamp(alerts["end"], pytz.timezone('Canada/Eastern')).ctime()
        alert_msg = "There is an alert from " + str(alerts["sender_name"]) + " regarding a " + str(
            alerts["event"]) + " that will take effect from " + str(dt_start) + " to " + str(dt_end)
        print(alert_msg)


def future_rain_forecast(rainy_days):
    print(rainy_days)
    for key, value in rainy_days.items():
        today = datetime.now(pytz.timezone('Canada/Eastern'))
        type_of_rain = ""
        delta = datetime.fromisoformat(key) - today
        day_difference = delta.days
        if value < 3:
            type_of_rain = "light"
        elif value < 10:
            type_of_rain = "medium"
        elif value < 25:
            type_of_rain = "heavy"
        if day_difference == 1:
            print("There will be " + type_of_rain + " rain tomorrow, for: " + str(
                value) + "mm, make sure to water your plants accordingly.")
        elif day_difference == 2:
            print("There will be " + type_of_rain + " rain day after tomorrow, for: " + str(
                value) + "mm, make sure to water your plants accordingly.")


def convert_factor_to_String(metric):
    if metric.factor == GardenDataEnum.moisture:
        return "Moisture"
    if metric.factor == GardenDataEnum.temp:
        return "Temperature"
    if metric.factor == GardenDataEnum.hum:
        return "Humidity"
    return "ERROR, NOT FOUND"


def pull_current_value(metric):
    if metric.data_type == DataTypeEnum.WEATHER:
        db.set_connection('bolt://neo4j:sysc4907@db:7687')
        all_nodes = ForecastRecord.nodes.all()
        highest = None
        recent_record = None
        if all_nodes[0] is not None:
            highest = all_nodes[0].date
        for node in all_nodes:
            if node.date > highest:
                highest = node.date
                recent_record = node
        print(recent_record)
        if metric.factor == GardenDataEnum.hum:
            return recent_record.humidity, "Tulip"
        elif metric.factor == GardenDataEnum.temp:
            return recent_record.temperature, "Tulip"
        else:
            return 15, "Tulip"
    elif metric.data_type == DataTypeEnum.GARDEN:
        db.set_connection('bolt://neo4j:sysc4907@db:7687')
        all_nodes = PlantRecord.nodes.all()
        highest = None
        recent_record = None
        if all_nodes[0] is not None:
            highest = all_nodes[0].date
        for node in all_nodes:
            if node.date > highest:
                highest = node.date
                recent_record = node
        print(recent_record)

        if metric.factor == GardenDataEnum.hum:
            return recent_record.hum, "Tulip"
        elif metric.factor == GardenDataEnum.temp:
            return recent_record.temp, "Tulip"
        elif metric.factor == GardenDataEnum.moisture:
            return recent_record.moisture, "Tulip"
        else:
            return 15, "Tulip"
    elif metric.data_type == DataTypeEnum.SOCIAL:
        labels, keywords = get_labels_and_keywords()
        for i in range(0, len(labels)):
            if labels[i] == convert_factor_to_String(metric).lower() and labels[i] != "humidity":
                # get plan_id and labels and shit from db
                return int(keywords[i]), "Tulip"
    return -1, "NOT FOUND"


def datatype_to_string(metric):
    str = "unknown"
    if metric.data_type == DataTypeEnum.GARDEN:
        str = "GARDEN"
    elif metric.data_type == DataTypeEnum.WEATHER:
        str = "WEATHER"
    elif metric.data_type == DataTypeEnum.SOCIAL:
        str = "SOCIAL"
    return str


def createDecisionRecord(content, source, metric):
    db.set_connection('bolt://neo4j:sysc4907@db:7687')
    with db.transaction:
        DecisionRecord(content=content, source=source, metric=metric).save()


# Weight table and comparison
def compare_scores(metric, datatypes, decisions):
    for index in range(len(datatypes)):
        if str(decisions[index]).endswith(NO_CHANGE_NEEDED):
            return
        elif metric.factor == GardenDataEnum.hum and datatypes[index] == DataTypeEnum.WEATHER:
            createDecisionRecord(decisions[index], datatype_to_string(metric), convert_factor_to_String(metric))
            print(decisions[index])
        elif metric.factor == GardenDataEnum.temp and datatypes[index] == DataTypeEnum.WEATHER:
            createDecisionRecord(decisions[index], datatype_to_string(metric), convert_factor_to_String(metric))
            print(decisions[index])
        elif metric.factor == GardenDataEnum.moisture and datatypes[index] == DataTypeEnum.GARDEN:
            createDecisionRecord(decisions[index], datatype_to_string(metric), convert_factor_to_String(metric))
            print(decisions[index])


def evaluate_simple_comparison(current_value, preference_val, metric, factor):
    difference = current_value - int(preference_val)
    tolerable_range = 5
    if metric.comparison == ComparisonEnum.GTorLT:
        if abs(difference) > tolerable_range:
            return metric.data_type, datatype_to_string(metric) + ": " + metric.description
    elif metric.comparison == ComparisonEnum.GT:
        if difference > tolerable_range:
            return metric.data_type, datatype_to_string(metric) + ": " + metric.description
    elif metric.comparison == ComparisonEnum.LT:
        if difference < tolerable_range:
            return metric.data_type, datatype_to_string(metric) + ": " + metric.description
    else:
        return -1
    return metric.data_type, datatype_to_string(metric) + ": " + NO_CHANGE_NEEDED


def execute_smituational_awareness_rule(metric):
    current_value, plant_id = pull_current_value(metric)
    # No value returned, value not found.
    if current_value == -1:
        return metric.data_type, "No decision"
    factor = convert_factor_to_String(metric)
    preference_val = load_plant_preferences(plant_id, factor)

    return evaluate_simple_comparison(current_value, preference_val, metric, factor)


def start_dms():
    stored_rules = get_rules()
    modules = [DataTypeEnum.WEATHER, DataTypeEnum.GARDEN, DataTypeEnum.SOCIAL]

    # This is the main execution loop
    while True:

        # This iterates over the rules that exists
        for index in range(len(stored_rules)):

            metric = get_rules()[index].get("metric")
            # This iterates over the modules that will attempt to execute this rule
            decisions = [None] * len(modules)
            datatypes = [None] * len(modules)
            for index2 in range(len(modules)):
                metric.set_Data_Type(modules[index2])
                rule = Rule(0, metric, execute_smituational_awareness_rule, "Description not used")
                datatype, string = rule.execute_outcome()
                datatypes[index2] = datatype
                decisions[index2] = string
            compare_scores(metric, datatypes, decisions)

        time.sleep(60)
"""


def rec(x):
    if x == 1:
        dms = "Turn off lights"
    if x == 2:
        dms = "Turn on lights"
    if x == 3:
        dms = "Turn on AC"
    if x == 4:
        dms = "Turn on Heat"
    if x == 5:
        dms = "Occupancy Limit Reached"
    return dms


"""
start_dms()
"""