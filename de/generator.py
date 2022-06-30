#!/usr/bin/env python3

import json
import os
from copy import deepcopy


buildings = {
    "all": {
        276: {
            "Age ID": 3,
            "Node Type": "BuildingTech",
        },
        70: None,
        199: None,
        621: None,
    },
}

units = {
    "all": {},
    "CHINESE": {36: {"Node Status": "ResearchRequired"}},
    "AZTECS": {359: {"Node Status": "ResearchedCompleted"}},
    "HUNS": {569: {"Node Status": "NotAvailable"}},
    "MAYANS": {567: {"Node Status": "ResearchedCompleted"}},
}

techs = {
    "all": {
        901: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128501,
            "Link ID": -1,
            "Link Node Type": "BuildingTech",
            "Name": "Heaven",
            "Name String ID": 38501,
            "Node ID": 901,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        902: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128502,
            "Link ID": -1,
            "Link Node Type": "BuildingTech",
            "Name": "Richness",
            "Name String ID": 38502,
            "Node ID": 902,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        903: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128503,
            "Link ID": -1,
            "Link Node Type": "BuildingTech",
            "Name": "Training",
            "Name String ID": 38503,
            "Node ID": 903,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        904: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128504,
            "Link ID": -1,
            "Link Node Type": "BuildingTech",
            "Name": "Flower",
            "Name String ID": 38504,
            "Node ID": 904,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        905: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128505,
            "Link ID": -1,
            "Link Node Type": "BuildingTech",
            "Name": "Wing",
            "Name String ID": 38505,
            "Node ID": 905,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        906: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128506,
            "Link ID": -1,
            "Link Node Type": "BuildingTech",
            "Name": "Dragon",
            "Name String ID": 38506,
            "Node ID": 906,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        907: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128507,
            "Link ID": 901,
            "Link Node Type": "Research",
            "Name": "Shadow",
            "Name String ID": 38507,
            "Node ID": 907,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        908: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128508,
            "Link ID": 902,
            "Link Node Type": "Research",
            "Name": "Shalassa",
            "Name String ID": 38508,
            "Node ID": 908,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        909: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128509,
            "Link ID": 903,
            "Link Node Type": "Research",
            "Name": "Machine",
            "Name String ID": 38509,
            "Node ID": 909,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        910: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128510,
            "Link ID": 904,
            "Link Node Type": "Research",
            "Name": "Miracle",
            "Name String ID": 38510,
            "Node ID": 910,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        911: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128511,
            "Link ID": 905,
            "Link Node Type": "Research",
            "Name": "Byzantine",
            "Name String ID": 38511,
            "Node ID": 911,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
        912: {
            "Age ID": 4,
            "Building ID": 276,
            "Draw Node Type": "UnitTech",
            "Help String ID": 128512,
            "Link ID": 906,
            "Link Node Type": "Research",
            "Name": "Griffin",
            "Name String ID": 38512,
            "Node ID": 912,
            "Node Status": "ResearchedCompleted",
            "Node Type": "Research",
            "Picture Index": 107,
            "Prerequisite IDs": [0, 0, 0, 0, 0],
            "Prerequisite Types": ["None", "None", "None", "None", "None"],
            "Trigger Tech ID": -1,
            "Use Type": "Tech",
        },
    },
    "BRITONS": {437: {"Node Status": "ResearchedCompleted"}},
    "BYZANTINES": {
        75: {"Node Status": "ResearchedCompleted"},
        435: {"Node Status": "ResearchedCompleted"},
    },
    "CHINESE": {
        12: {"Node Status": "ResearchedCompleted"},
        377: {"Node Status": "ResearchedCompleted"},
    },
    "FRANKS": {435: {"Node Status": "ResearchedCompleted"}},
    "VIKINGS": {373: {"Node Status": "ResearchedCompleted"}},
}

script_dir = os.path.dirname(__file__)
with open(
    os.path.join(script_dir, "civTechTrees.json"), "r", encoding="utf-8", newline="\r\n"
) as f:
    data = json.load(f)

for civ in data["civs"]:
    buildings_copy = deepcopy(buildings)
    units_copy = deepcopy(units)
    techs_copy = deepcopy(techs)
    for ctb in civ["civ_techs_buildings"]:
        if (
            ctb["Node ID"] in buildings_copy["all"]
            and ctb["Node Type"]
            in [
                "BuildingTech",
                "BuildingNonTech",
            ]
            and buildings_copy["all"][ctb["Node ID"]] is not None
        ):
            ctb.update(buildings_copy["all"][ctb["Node ID"]])
            del buildings_copy["all"][ctb["Node ID"]]
        if civ["civ_id"] in buildings_copy:
            if (
                ctb["Node ID"] in buildings_copy[civ["civ_id"]]
                and ctb["Node Type"]
                in [
                    "BuildingTech",
                    "BuildingNonTech",
                ]
                and buildings_copy[civ["civ_id"]][ctb["Node ID"]] is not None
            ):
                ctb.update(buildings_copy[civ["civ_id"]][ctb["Node ID"]])
                del buildings_copy[civ["civ_id"]][ctb["Node ID"]]
    buildings_to_delete = []
    for id, building in buildings_copy["all"].items():
        if building is not None:
            civ["civ_techs_buildings"].append(building)
        else:
            buildings_to_delete.append(id)
    if civ["civ_id"] in buildings_copy:
        for id, building in buildings_copy[civ["civ_id"]].items():
            if building is not None:
                civ["civ_techs_buildings"].append(building)
            else:
                buildings_to_delete.append(id)
    civ["civ_techs_buildings"] = [
        ctb
        for ctb in civ["civ_techs_buildings"]
        if ctb["Node Type"] in ["BuildingTech", "BuildingNonTech"]
        and ctb["Node ID"] not in buildings_to_delete
    ]
    for ctu in civ["civ_techs_units"]:
        if (
            ctu["Node ID"] in units_copy["all"]
            and ctu["Node Type"]
            in [
                "Unit",
                "UnitUpgrade",
                "UniqueUnit",
            ]
            and units_copy["all"][ctu["Node ID"]] is not None
        ):
            ctu.update(units_copy["all"][ctu["Node ID"]])
            del units_copy["all"][ctu["Node ID"]]
        if (
            ctu["Node ID"] in techs_copy["all"]
            and ctu["Node Type"] in ["Research"]
            and techs_copy["all"][ctu["Node ID"]] is not None
        ):
            ctu.update(techs_copy["all"][ctu["Node ID"]])
            del techs_copy["all"][ctu["Node ID"]]
        if civ["civ_id"] in units_copy:
            if (
                ctu["Node ID"] in units_copy[civ["civ_id"]]
                and ctu["Node Type"]
                in [
                    "Unit",
                    "UnitUpgrade",
                    "UniqueUnit",
                ]
                and units_copy[civ["civ_id"]][ctu["Node ID"]] is not None
            ):
                ctu.update(units_copy[civ["civ_id"]][ctu["Node ID"]])
                del units_copy[civ["civ_id"]][ctu["Node ID"]]
        if civ["civ_id"] in techs_copy:
            if (
                ctu["Node ID"] in techs_copy[civ["civ_id"]]
                and ctu["Node Type"] in ["Research"]
                and techs_copy[civ["civ_id"]][ctu["Node ID"]] is not None
            ):
                ctu.update(techs_copy[civ["civ_id"]][ctu["Node ID"]])
                del techs_copy[civ["civ_id"]][ctu["Node ID"]]
    units_to_delete = []
    techs_to_delete = []
    for id, unit in units_copy["all"].items():
        if unit is not None:
            civ["civ_techs_units"].append(unit)
        else:
            units_to_delete.append(id)
    if civ["civ_id"] in units_copy:
        for id, unit in units_copy[civ["civ_id"]].items():
            if unit is not None:
                civ["civ_techs_units"].append(unit)
            else:
                units_to_delete.append(id)
    for id, tech in techs_copy["all"].items():
        if tech is not None:
            civ["civ_techs_units"].append(tech)
        else:
            techs_to_delete.append(id)
    if civ["civ_id"] in techs_copy:
        for id, tech in techs_copy[civ["civ_id"]].items():
            if tech is not None:
                civ["civ_techs_units"].append(tech)
            else:
                techs_to_delete.append(id)
    civ["civ_techs_units"] = [
        ctu
        for ctu in civ["civ_techs_units"]
        if (
            ctu["Node Type"] in ["Unit", "UnitUpgrade", "UniqueUnit"]
            and ctu["Node ID"] not in units_to_delete
        )
        or (ctu["Node Type"] in ["Research"] and ctu["Node ID"] not in techs_to_delete)
    ]
with open(
    os.path.join(script_dir, "civTechTrees_A.json"),
    "w",
    encoding="utf-8",
    newline="\r\n",
) as f:
    json.dump(data, f, ensure_ascii=False, indent=0, sort_keys=False)

for civ in data["civs"]:
    for ctb in civ["civ_techs_buildings"]:
        if ctb["Node Status"] == "NotAvailable":
            if ctb["Prerequisite IDs"] == [0, 0, 0, 0, 0]:
                ctb["Node Status"] = "ResearchedCompleted"
            else:
                ctb["Node Status"] = "ResearchRequired"
    for ctu in civ["civ_techs_units"]:
        if ctu["Node Status"] == "NotAvailable":
            if ctu["Prerequisite IDs"] == [0, 0, 0, 0, 0]:
                ctu["Node Status"] = "ResearchedCompleted"
            else:
                ctu["Node Status"] = "ResearchRequired"
with open(
    os.path.join(script_dir, "civTechTrees_B.json"),
    "w",
    encoding="utf-8",
    newline="\r\n",
) as f:
    json.dump(data, f, ensure_ascii=False, indent=0, sort_keys=False)
